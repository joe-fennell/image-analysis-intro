from getsentinel import gs_io, gs_downloader, gs_localmanager
import datetime as dt
import os
# important for linux NFS use
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'
#
vpath = '../geo_files/cali_sugarcane.shp'
vpath2 = '../geo_files/cali_validation.shp'

query = gs_downloader.Query('S2', dt.datetime(2016,5,1).date(), dt.datetime.now().date(), vpath)
query.product_details(proclevel='L1C', cloudcoverlimit=30)

pipe = gs_downloader.CopernicusPipeline()
nprods, prods = pipe.submit_query(query)

#
pipe.download_and_process(prods)
gs_localmanager.add_tilelist()

inventory = gs_localmanager.get_product_inventory()
filtered = {uuid:prod for (uuid,prod) in inventory.items() if prod['platformname']=='Sentinel-2'}

training = gs_io.geofile_to_xarray(vpath,product_inventory=filtered)
training.to_netcdf(path='cali_training.nc',mode='w')

validation = gs_io.geofile_to_xarray(vpath2, product_inventory=filtered)
validation.to_netcdf(path='cali_validation.nc',mode='w')

print('Files Generated!')
