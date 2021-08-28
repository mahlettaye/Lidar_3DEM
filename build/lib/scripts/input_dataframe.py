
from application_logger import logghandler
import pandas as pd 
import geopandas as gpd
import georasters as gr
import sys
sys.path.insert(0, '/home/mahlet/10ac/Lidar_3DEM/')


logger=logghandler('test','Geo_log')
user_logger= logger.get_logger("DEBUG")


class Dataframe_Generator:
    def __init__(self,file_name,crs):
        self.file_name = file_name
        self.crs = crs
    
    def generate_point_dataframe(self):
        """
        Computes the Elevations in a raster tif file
      
        Parameters
        ---------
      
        tif_file: str : filename/location of a tif image
        CRS: str : crs value for the given tif image
        
        Returns
        -------
        DataFrame
        """
        grid_raster = self.file_name
        try:
            grid = gr.from_file(grid_raster)

        except Exception as e:
        
            user_logger.info("Error in reading fiele"+e)
        
        #Convert to Pandas DataFrame
        single_df = grid.to_pandas()
      
        #Drop row and column columns
        columns =['row','col' ]
        single_df = pd.DataFrame(single_df.drop(columns=columns))
        single_df.rename(columns = {'value':'elevation'}, inplace = True) 
        single_df=single_df[['x','y','elevation']] # organize column
    
        single_df_point = gpd.GeoDataFrame(
            single_df, geometry=gpd.points_from_xy(single_df.x,single_df.y))
   
        # specify user inputed crs
        epsg='epsg:'+str(self.crs)
        single_df_point.crs = {'init' :epsg}
    
        #return dataframe that contains points and elevation 
        return single_df_point
if __name__=="__main__":
    dataframe_obj= Dataframe_Generator("data/IA_FullState.tif",32618)
    point_df= dataframe_obj.generate_point_dataframe()
    print(point_df.head())