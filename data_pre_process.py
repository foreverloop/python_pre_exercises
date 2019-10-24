import numpy as np
import matplotlib.pyplot as plt

#emacs ctrl + e for end of line
#emacs ctrl + x , ctrl + s
#linux evince normalised.pdf, for opening pdf files form the command line
#alt + tab to move between windows in linux

dataRaw = []
DataFile = open("ClimateData.csv","r")

while True:
    theline = DataFile.readline()
    if len(theline) == 0:
        break
    readData = theline.split(",")
    for pos in range(len(readData)):
        readData[pos] = float(readData[pos]);
    dataRaw.append(readData)
DataFile.close()

data = np.array(dataRaw)

print(dataRaw)

def standard(data):
    standardData = data.copy()

    rows = data.shape[0]
    cols = data.shape[1]

    for j in range(cols):
        sigma = np.std(data[:,j])
        mu = np.mean(data[:,j])

        for i in range(rows):
            standardData[i,j] = (data[i,j] - mu) / sigma
    return standardData

def plot(data,fileName):
    fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(nrows=2,ncols=2)

    fig.set_size_inches(9.0,6.0)
    ax1.plot(data[:,0],data[:,1],".")
    ax2.plot(data[:,0],data[:,2],".")
    ax3.plot(data[:,0],data[:,3],".")
    ax4.plot(data[:,0],data[:,4],".")

    ax1.set_ylabel("Wind Speed")
    ax2.set_ylabel("Wind Direction")
    ax3.set_ylabel("Precipitation")
    ax4.set_ylabel("Humidity")
    plt.savefig(fileName,bbox_inches='tight')

plot(data,"/home/vagrant/Documents/output/nonStandardised.pdf")
plot(standard(data),"/home/vagrant/Documents/output/standardised.pdf")

#moving on to normalisation
def normalise(data):
    normalisedData = data.copy()

    rows = data.shape[0]
    cols = data.shape[1]

    for j in range(cols):
        maxElement = np.amax(data[:,j])
        minElement = np.amin(data[:,j])
        for i in range(rows):
            normalisedData[i,j]=(data[i,j]-minElement)/(maxElement-minElement)
    return normalisedData

norm_data  = normalise(data)
plot(norm_data,"/home/vagrant/Documents/output/normalised.pdf")


def normalise_neg(data):
    normalisedData = data.copy()

    rows = data.shape[0]
    cols = data.shape[1]

    for j in range(cols):
        maxElement = np.amax(data[:,j])
        minElement = np.amin(data[:,j])

        for i in range(rows):
            normalisedData[i,j]=2*(data[i,j]-minElement)/(maxElement-minElement) - 1

    return normalisedData
    
norm_neg_data = normalise_neg(data)
plot(norm_neg_data,"/home/vagrant/Documents/output/normalised_neg.pdf")

print("finished normalisation and standardisation of the data")

#each individual item has the feature mean subtracted from it
#this produces the feature mean 
def centralize(data):
    centralizedData = data.copy()
    rows = data.shape[0]
    cols = data.shape[1]

    for j in range(cols):
        mu = np.mean(data[:,j])

        for i in range(rows):
            centralizedData[i,j] = (data[i,j] - mu)
    return centralizedData

centralizedData = centralize(data)
plot(centralizedData,"/home/vagrant/Documents/output/centralised_data.pdf")
print(np.corrcoef(centralizedData,rowvar=False))



