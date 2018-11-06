import scipy.io

filename = './OtherFiles/albeck_gene_expression.mat'

mat = scipy.io.loadmat(filename)

print(type(mat))    # <class 'dict'>

# Python dictionary keys      = MATLAB variable names
# Python dictionary values    = MATLAB objects assigned to variables

print(type(mat['rfpCyt']))  # <class 'numpy.ndarray'>