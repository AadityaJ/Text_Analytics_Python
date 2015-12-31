import matplotlib.pyplot as plt
import numpy as np  
alphb=np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"])
graph=np.array([3786,3576,2533,2577,1236,2584,1984,6648,3099,348,640,2172,2346,1584,2081,1000,2121,1717,6447,5300,936,490,5465,1667,16])
print len(alphb),len(graph)
plt.plot(graph)
plt.show()