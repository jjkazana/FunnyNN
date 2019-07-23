from NN.Model import new_model
from Data.DataConfig import Config
from Data.Flatten import FlattenTo1D
from Data.Loader import DataFrom
from Data.SaveResults import SaveResults

from numpy import zeros,abs,sum, divide
import os

def Run():
    savePath = './Results/'
    cfg = Config()
    rawData, _ = DataFrom(cfg.path, cfg.electrodes, cfg)

    data = zeros((len(rawData), len(rawData[0])*len(rawData[0][0])))
    ann = zeros((len(rawData), len(rawData[0])*len(rawData[0][0])))

    for i in range(0,len(rawData)):
        tmp = FlattenTo1D(rawData[i])
        data[i] = tmp
        ann[i] = tmp    

    model = new_model(len(data[0]))

    resume = []
    shape = rawData[0].shape
    for i in range(0,1000):
        model.fit(data, ann, epochs = 100)
        prediction = model.predict(data[i:i+1])[0]
        if not os.path.isdir(savePath+str(i)):
            os.mkdir(savePath+str(i))
        SaveResults(savePath+str(i)+'/', data[i:i+1], prediction, shape)

    

Run()
