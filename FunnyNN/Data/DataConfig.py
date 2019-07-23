class EpochObject(object):
    pass

def Config():
    epoch = EpochObject()
    epoch.size = 128
    epoch.start = 12000
    epoch.stop = 48000
    epoch.gap = 32
    epoch.sampling_freq = 200
    
    epoch.path = './Data/'
    epoch.electrodes = range(21,41)
    
    return epoch
