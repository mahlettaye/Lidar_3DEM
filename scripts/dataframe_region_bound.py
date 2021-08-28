import json 
from application_logger import logghandler
import pandas as pd
from itertools import groupby

logger=logghandler('test','Geo_log')
user_logger= logger.get_logger("DEBUG")


class Dataframe_From_Bounds:

    def __init__(self,user_bounds):
        self.user_bounds=user_bounds


    def get_bounds_region(self):
        year=""
        region=""
        Bounds=[] 
        current_bound=[]
        all_year=[]
        all_bounds=[]
        try:
            with open('scripts/all-ept.json') as json_file:
                data = json.load(json_file)
            for user_bound in self.user_bounds:
                for key,value in data.items():
                    current_Year= (key[-5:-1])#to get year from json file 
                    if (current_Year.isdigit()==True):
                        all_year.append(current_Year)
                        #region=key #to specify the region 
                        data_dict=eval(value) #to convert string to Dictionary 
                        URL_Bounds = next(iter(data_dict.items()))[1] 
                        all_bounds.append(URL_Bounds)
                    
                        if URL_Bounds[0] <= user_bound[0] and URL_Bounds[1] <= user_bound[1] and URL_Bounds[3] >= user_bound[3]:
                            current_bound= user_bound
                            year=current_Year
                            region=key
                        else:
                            pass
                
                    else:
                        user_logger.info("The bound you specified doesnot contain year value")
    
                Bounds.append(current_bound)           
                #creating Dictionary
                all_dict= {'year': year, 'bound': Bounds, 'region': region}
                lst=[all_dict]
                for k,v in groupby(lst,key=lambda x:x['year']):
                    agg_dct=list(v)
                year=[]
                bounds=[]
                for index in agg_dct:
                    year.append(index['year'])
                    bounds.append(index['bound'])
            
                year_agg_df= pd.DataFrame(list(zip(year, bounds)),
                    columns =['year', 'bound'])
            
            
            
        except NameError as e:
        #print(e)
            pass
        return year_agg_df

if __name__=="__main__":
    list_bound=[[-17347360, 8065364, -12414, -17321558, 8091166, 13388],
  [-13121128, 3873238, -42479, -13036268, 3958098, 42381],
  [-13119610, 3873810, -42083, -13035300, 3958120, 42227],
  [-13122747, 3874444, -43038, -13036569, 3960622, 43140],
  ]
    Df_year_bound=Dataframe_From_Bounds(list_bound)

    year_df=Df_year_bound.get_bounds_region()
    print(year_df.head())
