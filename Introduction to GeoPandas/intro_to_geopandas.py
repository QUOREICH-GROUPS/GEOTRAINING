# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:01:06 2024

@author: Abdouramane SAWADOGO
"""

import geopandas  as gpd
import matplotlib.pyplot as plt



#Importing an ESRI shapefile and plotting it using Geoapndas

districts=gpd.read_file(r'F:\GEOAI\GEOPANDAS\Introduction to GeoPandas-20240803T233901Z-001\Introduction to GeoPandas\Shapefiles\districts.shp')
districts.plot(cmap='hsv', color='red',edgecolor='black', column='districts')


area_of_interest = gpd.read_file(r'F:\GEOAI\GEOPANDAS\Introduction to GeoPandas-20240803T233901Z-001\Introduction to GeoPandas\Shapefiles\area_of_interest.shp')
area_of_interest.plot()

atms =  gpd.read_file(r'F:\GEOAI\GEOPANDAS\Introduction to GeoPandas-20240803T233901Z-001\Introduction to GeoPandas\Shapefiles\atms.shp')


#Plot the figures side by side

#fig, (ax1, ax2)= plt.subplots(ncols=2, figsize=(10 ,8))

#districts.plot(ax= ax1,cmap='hsv', color='red',edgecolor='black', column='districts')
#area_of_interest.plot(ax=ax2, color='green')

# =============================================================================
# #Plotting multiple Layers
# fig, ax=plt.subplots(figsize=(10 ,8))
# districts.plot(ax= ax,cmap='hsv', color='red',edgecolor='black', column='districts')
# area_of_interest.plot(ax=ax, color='none', edgecolor='black')
# atms.plot(ax=ax, color='black', markersize=14)
# =============================================================================

#Reprojecting GeoPandas GeoDataFrames
fig, ax=plt.subplots(figsize=(10 ,8))

districts= districts.to_crs(epsg=32629 )
districts.plot(ax = ax ,figsize=(10 ,8), cmap='hsv', color='red',edgecolor='black', column='districts')

area_of_interest =area_of_interest.to_crs(epsg=32629)
area_of_interest.plot( ax = ax ,figsize=(10 ,8), color='none', edgecolor='black')

#Intersecting Layers

districts_in_aoi= gpd.overlay(districts, area_of_interest, how='intersection')
districts_in_aoi.plot(edgecolor='red')

# Afficher les premières lignes du GeoDataFrame résultant
print(districts_in_aoi.head())

# Afficher des informations sur le GeoDataFrame résultant
print(districts_in_aoi.info())

#Calculating the areas of intersected layer
districts_in_aoi['area'] = districts_in_aoi.area/1000000


#Exporting Geopandas GeoDataFrames into an ESRI ShapeFiles
districts_in_aoi.to_file('districts_within_aoi.shp', driver="ESRI Shapefile")




