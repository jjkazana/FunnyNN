'''
Take:
    path to catalog which contains 2 files: "data.csv" and "annotations.csv"
    tuple containing indices under which desired chanels are located
    epoch object, containing attributes:
        start - first signal index
        stop - last signal index
        gap - distance between epochs beginings
		size - size of epoch

Return 2 tuples of: 3D numpy array containing data in epoch, and 1D array 
containing annotations 

(data, annotations), (test_data, test_annotations)

'''

from numpy import loadtxt, zeros, arange

def DataFrom(path, electrodes, epoch):
    #should be 2D array [index][data_point]
    all_records = loadtxt(path+"data.csv", delimiter=",")
    #should be 2D array [index][annotation(0)/ occurence_time(1)]
    annotations = loadtxt(path+"annotations.csv", delimiter=',')
    
    epochs = arange(start=epoch.start, stop=epoch.stop, step=epoch.gap)
    ann_data = zeros(len(epochs))

    for ann in annotations:
        low = ann[1]*epoch.sampling_freq - 0.7*epoch.size - epoch.start
        high = ann[1]*epoch.sampling_freq + 0.3*epoch.size - epoch.start
        low = int(low/epoch.gap)
        high = int(high/epoch.gap)
        if low > 0:
            ann_data[low:high] = ann[0]
        elif high > 0:
            ann_data[0:high] = ann[0]

    cut_records = zeros( ( len(electrodes), len(all_records) ) )

    e_index = 0
    for electrode in electrodes:
        cut_records[e_index] = all_records[0:,electrode]
        e_index += 1
    
    ret_data = zeros( (len(epochs), len(electrodes), epoch.size) )

    e_index = 0
    for ep in epochs:
        print("Slicing epoch:", e_index)
        ret_data[e_index] = cut_records[0:, int(ep):int(ep+epoch.size)]
        e_index += 1

    return (ret_data, ann_data)


