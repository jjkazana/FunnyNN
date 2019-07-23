'''
Take data for all epochs and apply Welch window for each channel in
each epoch

Takes 3D array-like object
Returns data in exact same format as input
'''
def Window(data):
    N = len(data[0][0]) - 1
    window = [1-((x-N/2)/(N/2))**2 for x in range(0,N+1)]
    
    for epoch in data:
        for chanel in epoch:
            chanel *= window

    return data
