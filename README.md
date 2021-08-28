# Lidar_3DEM


Lidar has become the de facto source for elevation data for its accuracy and detailed surface models. Lidar data can be acquired from various platforms, ranging from high-altitude, fixed-wing, manned and unmanned aircraft to moving vehicles and stationary tripods.
The USGS 3DEP programme offers semi-continental coverage of Lidar data for free.

DEMs are files that contain either points (vector) or pixels (raster), with each point or pixel having an elevation value. DEMs: digital elevation models represent the land or "bare earth" (no trees, buildings, etc.)

This project aims to create Lidar_3DEM python package that is used to extract data from Amazon s3 bucket and process it to get elevation and 3D visualization.


### Data


we have use USGS public dataset found here "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"


### Functionality 

- Data_from_url : fetech data from the s3 bucket based on user input bound

- Dataframe_From_Bounds : Accepts list of bounds and returen year agergated points

- Input_dataframe : Accept bounds and return dataframe that contains elevation and Points

- Plots : Accepts dataframe that contains elevation and point will plot 3d projection of input data.


### In progress 


- Calculating TWI


### Package Usage 


......



