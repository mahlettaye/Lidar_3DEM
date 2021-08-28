import json
import pdal

from application_logger import logghandler
import sys
sys.path.insert(0, '/home/mahlet/10ac/Lidar_3DEM/')

logger=logghandler('test','Geo_log')
user_logger= logger.get_logger("DEBUG")

class DataFromURL:

    def __init__(self, bounds:str, crs:int) -> None:
        
        self.bounds = bounds 
        self.crs = crs   
        self.public_data_path = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"
        
        self.region = "IA_FullState/"
        self.load_pipeline()


    def load_pipeline(self, pipeline_filename='get_data.json'):
        
        """
        The Function loads a templated pipeline 

        Parameters
        ----------
        pipeline_filename : pipeline json file
             (Default value = 'get_data.json')

        Returns
        -------
        None

        """
        
        try:
            with open(pipeline_filename) as json_file:
                the_json = json.load(json_file)

            self.external_pipeline = the_json
            user_logger.info("Pipeline Succefully Loaded")
        except Exception as e:
           
            user_logger.info("Pipeline Could not be Loaded")


    def get_raster_terrain(self, bounds: str) -> None:
        
        """
        The Function 

        Parameters
        ----------
        bounds: str :
            

        Returns
        -------
        None

        """

        user_logger.info(f"Fetching Laz and tiff files for {self.region}")
        PUBLIC_ACCESS_PATH = self.public_data_path + self.region + "ept.json"


        # dynamically update template pipeline
        self.external_pipeline['pipeline'][0]['bounds'] = bounds
        self.external_pipeline['pipeline'][0]['filename'] = PUBLIC_ACCESS_PATH
        self.external_pipeline['pipeline'][3]['filename'] = f"{str(self.region).strip('/')}.laz"
        self.external_pipeline['pipeline'][4]['filename'] = f"{str(self.region).strip('/')}.tif"

        # create pdal pipeline
        pipeline = pdal.Pipeline(json.dumps(self.external_pipeline))
        user_logger.info("Pipeline Dumped and Read for use")
    

        # execute pipeline
        try:
            pipe_exec = pipeline.execute()
            metadata = pipeline.metadata
            log = pipeline.log
            user_logger.info("Execution completed for Pipeline succefully ")


        except RuntimeError as e:
            print(e)
            user_logger.info(" Pipeline execution Process Could not be completed")
        
        return self.region

 

if __name__ == "__main__":
    BOUNDS = "([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"

    data_obj = DataFromURL(bounds=BOUNDS, crs=32618)
    region = data_obj.get_raster_terrain(bounds=BOUNDS)
    print(region)
    