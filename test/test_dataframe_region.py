import unittest
import sys, os


sys.path.append(os.path.abspath(os.path.join('../')))

from scripts.dataframe_region_bound import DataFromURL

class TestDataFromURL(unittest.TestCase):
    """
	A class for unit-testing function in the dataframe_region_bound.py file

	Args:
        -----
	unittest.TestCase this allows the new class to inherit
	from the unittest module
	"""

    def setUp(self):
        BOUNDS = "([-10425171.940, -10423171.940], [5164494.710, 5166494.710])"
        self.raster_obj = DataFromURL(BOUNDS,crs=32618)
        self.region = self.raster_obj.extract_raster(BOUNDS)
    
    def test_extract_raster(self):
        actual_region = "IA_FullState"
        self.assertEqual(self.region, actual_region)
    

