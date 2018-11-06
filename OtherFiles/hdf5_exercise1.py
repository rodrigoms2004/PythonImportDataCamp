# https://www.gw-openscience.org/events/GW150914/
# https://www.gw-openscience.org/s/events/GW150914/GW150914_tutorial.html

# Import packages
import numpy as np
import h5py

# Assign filename: file
file = './OtherFiles/LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
