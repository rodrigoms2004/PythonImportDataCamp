# https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm

# Import package
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

filename = './OtherFiles/albeck_gene_expression.mat'

# Load MATLAB file: mat
mat = scipy.io.loadmat(filename)

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))    # <class 'numpy.ndarray'>

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))  # (200, 137) dimensions of the array

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
