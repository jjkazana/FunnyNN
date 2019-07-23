from NN.Model import new_model
from Data.DataConfig import Config
from Data.Flatten import FlattenTo1D
from Data.Loader import DataFrom

from numpy import zeros,abs,sum, divide

def Run():
    cfg = Config()
    rawData, _ = DataFrom(cfg.path, cfg.electrodes, cfg)

    data = zeros((len(rawData), len(rawData[0])*len(rawData[0][0])))
    ann = zeros((len(rawData), len(rawData[0])*len(rawData[0][0])))
    
    print(data.shape)

    for i in range(0,len(rawData)):
        tmp = FlattenTo1D(rawData[i])
        data[i] = tmp
        ann[i] = tmp    

    model = new_model(len(data[0]))

    resume = []
    for i in range(200,300):
        model.fit(data, ann, epochs = 100)
        prediction = model.predict(data[i:i+1])[0]
        resume.append(sum(abs(prediction-ann[i])/len(prediction)))
        print(resume[-1])

    print("\n\n")
    for r in resume:
        print("Średni błąd bezwzględny: ", r)

Run()
