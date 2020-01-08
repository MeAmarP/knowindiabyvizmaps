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
                edgecolor='w')
    plt.title(fig_title)
    if save_fig == True:
        plt.savefig('plots/'+fig_title+'.png', dpi=400)
    return


#==============================================================================
path_to_shpfile = 'India_Shapefiles/India.shp'
path_to_dset = 'data/obesity_india.csv'
var_df = pd.read_csv(path_to_dset)
map_df = gpd.read_file(path_to_shpfile)


KnowIndiaOneByOneMap(map_df,
                     var_df,
                     parameter_to_map='Female(%)',
                     fig_title='State-UT wise Female(%) Obesity-NFHS2007',
                     cb_label='Percentage of Female who are overweight or obese',
                     cmap='YlOrRd',
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

