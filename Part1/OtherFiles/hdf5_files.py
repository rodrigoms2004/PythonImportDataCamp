import h5py

filename = './OtherFiles/LIGO_data.hdf5'

data = h5py.File(filename, 'r')

print(type(data))
# <class 'h5py._hl.files.File'>

# The structure of HDF5 files
for key in data.keys():
    print(key)
# meta      Meta-data for the file, such as GPTS times covered, which instrument, etc
# quality   Data quality
# strain    Strain data from the interferometer

print(type(data['meta']))
# <class 'h5py._hl.group.Group'>

for key in data['meta'].keys():
    print(key)
# Description
# DescriptionURL
# Detector
# Duration
# GPSstart
# Observatory
# Type
# UTCstart

print(data['meta']['Description'].value)    # b'Strain data time series from LIGO'
print(data['meta']['Detector'].value)       # b'L1'






