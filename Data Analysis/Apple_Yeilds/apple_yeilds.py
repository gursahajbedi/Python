import numpy as np
import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')
    
climatedata=np.genfromtxt('./climate.txt',delimiter=",",skip_header=1)

weights=np.array([0.3,0.2,0.5])

yeilds=np.matmul(climatedata,weights)
yeilds=yeilds.reshape(10000,1)

climatedata=np.concatenate((climatedata,yeilds),axis=1)

np.savetxt('./climate_results.txt',climatedata,fmt="%.2f",delimiter=',',header="temprature,rainfall,humidity,yeild",comments="")