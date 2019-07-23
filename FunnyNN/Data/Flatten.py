'''
Only for numpy arrays

'''
from numpy import reshape

def FlattenTo1D(data):
    initShape = data.shape
    retShape = 1
    for dim in initShape:
        retShape *= dim

    return reshape(data, retShape)
