# Import package
import scipy.io

filename = './OtherFiles/albeck_gene_expression.mat'

# Load MATLAB file: mat
mat = scipy.io.loadmat(filename)

# Print the datatype type of mat
print(type(mat))    # <class 'dict'>