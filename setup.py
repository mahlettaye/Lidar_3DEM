from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Education',
  
    'Programming Language :: Python :: 3'
]

setup(
    author='Mahlet Taye',
    author_email='formahlet@gmail.com',
    name='LIDAR_3DEM',
    version='0.1.0',
    description='A python package used to featch and visuaize raster data',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='',
    classifiers=classifiers,
    keywords='LIDAR',
    packages=find_packages(),
    install_requires=['georasters','gdal','pdal','geopandas', 'matplotlib'])