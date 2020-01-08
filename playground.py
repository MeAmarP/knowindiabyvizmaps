import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt




def KnowIndiaOneByOneMap(map_shape_dframe,
                         data_dframe,
                         parameter_to_map=None,
                         fig_title=None,
                         cmap='RdYlGn',
                         cb_label=None,
                         save_fig=None):
    var_df = pd.read_csv(path_to_dset)
    map_df = gpd.read_file(path_to_shpfile)
    mappedf= map_df.set_index('NAME_1').join(var_df.set_index('State/UT'))
    fig, ax = plt.subplots(1, 1,figsize=(10,10))    
    mappedf.plot(column=parameter_to_map,
                ax=ax,
                cmap=cmap,
                legend=True,
                legend_kwds={'label':cb_label},
                edgecolor='k')
    plt.title(fig_title)
    if save_fig == True:
        plt.savefig('/home/amarp/Documents/pyproj/ML/forFolio/india_voz/plots/'+fig_title+'.png', dpi=400)
    return



path_to_shpfile = 'India_Shapefiles/India.shp'
path_to_dset = 'data/Road_Accidents_NatioanlHWay_2017-Annuxure_Tables_9.csv'
var_df = pd.read_csv(path_to_dset)
map_df = gpd.read_file(path_to_shpfile)

KnowIndiaOneByOneMap(map_df,
                     var_df,
                     parameter_to_map='Total Number of Road Accidents on National Highways -  2017',
                     fig_title='State-UT wise National Highway Road Accidents-2017',
                     cb_label='Number of Road Accidents',
                     cmap='Reds',
                     save_fig=True)


#
#
#fig, ax = plt.subplots(1, 1,figsize=(14,14))
#map_df.plot(column=var_df['pcent forest area'],
#            ax=ax,
#            cmap='RdYlGn',
#            legend=True,
#            legend_kwds={'label':'Total Forest Area(%)'},
#            edgecolor='w')
#plt.text(81,6,"Tree cover comprises of tree patches\noutside the recorded forest area\nexclusive of forest cover and less\nthan the minimum mappabe area.",size=10)
#plt.text(68.0,6.0,"Data Source: data.gov.in")
#plt.title('State/UT-wise % of Forest Cover 2017')
#plt.savefig('plots/ForestCover2017.png', dpi=400)

