from numpy import savetxt, reshape

def SaveResults(path, input, output, shape):
    savetxt(path+"input.csv", reshape(input, shape), delimiter = ',')
    savetxt(path+"output.csv", reshape(output, shape), delimiter = ',')
