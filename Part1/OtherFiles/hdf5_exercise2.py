# https://www.gw-openscience.org/events/GW150914/
# https://www.gw-openscience.org/s/events/GW150914/GW150914_tutorial.html

# Import packages
import numpy as np
import h5py
import matplotlib.pyplot as plt

# Assign filename: file
file = './OtherFiles/LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()