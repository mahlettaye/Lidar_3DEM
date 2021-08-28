import geopandas as gpd
import rasterio as rio
from shapely.geometry import box
import matplotlib.pyplot as plt
from descartes import PolygonPatch

from application_logger import logghandler


logger=logghandler('test','Geo_log')
user_logger= logger.get_logger("DEBUG")



class Plotter:
    def __init__(self, tif_file_path,shp_file_path):
        self.tif_file_path=tif_file_path
        self.shp_file_path=shp_file_path

    def get_shp_from_tif(self) -> None:
        
        
        print(self.shp_file_path)
        raster = rio.open(self.tif_file_path)
        bounds = raster.bounds
        
        df = gpd.GeoDataFrame({"id":1,"geometry":[box(*bounds)]})
        # save to file
        df.to_file(self.shp_file_path)
        print('Shape file is saved')
    
    def plot_geometry(self):
        shapefile = gpd.read_file(self.shp_file_path)
        shapefile.set_index('id', inplace=True)
        BLUE = '#6699cc'
        poly= shapefile['geometry'][1]
        fig = plt.figure() 
        ax = fig.gca() 
        ax.add_patch(PolygonPatch(poly, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2 ))
        ax.axis('scaled')
        plt.show()


if __name__=="__main__":
    plotter_obj= Plotter("IA_FullState.tif","IA_FullState.shp")
    #plotter_obj.get_shp_from_tif()
    plotter_obj.plot_geometry()



