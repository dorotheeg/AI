import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from matplotlib import cm
import matplotlib.lines as mlines
from mpl_toolkits.mplot3d import Axes3D

       
                
w1 = 0
w2 = 0
b = 0

def perceptron(file):
    #print(file)
    weights = np.zeros(len(file)+1)

    global w1 
    global w2 
    global b 
    
    f1 = file[0]
    f2 = file[1]
    labels = file[2]
    
    #n_w1, n_w2, n_b = train(f1,f2, labels, w1,w2,b)
    weight_1 = []
    weight_2 = []
    bias = []


    #for i in range(200):
    old = w1
    new = -1
    weight = []
    while(old - new != 0):
        old = w1
        w1, w2, b = train(f1,f2, labels, w1,w2,b)
        new = w1
        #print( w1, w2, b)
        weight_1.append(w1)
        weight_2.append(w2)
        bias.append(b)
        

    return weight_1, weight_2, bias


    # (w1 * X1) + (w2 * X2) + bias

def predict( f1, f2, w1,w2,b):
        act = (f1 * w1) + (f2 * w2) + b
        if act > 0:
          outy = 1
          
        else:
          outy = -1
          
        return outy


def train(f1, f2, labels, w1,w2,b):
        
        for label,x,y in  zip(labels,f1,f2):
                prediction = predict(x, y, w1,w2,b)
                w1 += .01 * (label - prediction) * (x)
                w2 += .01 * (label - prediction) * (y)
                b += (label - prediction) 

        return w1, w2, b



if __name__ == "__main__":

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    data = pd.read_csv(in_file, header=None)
    weight_1, weight_2, bias = perceptron(data)

    w1 = [int(element * 100)/10 for element in weight_1]    
    w2 = [int(element * 100)/10 for element in weight_2]
    b = [int(element * 100)/10 for element in bias]

    
    df = pd.DataFrame({'weight_1': w1,'weight_2': w2,'bias': b})

    df.to_csv(out_file)

    print("Done, check " + str(out_file) + " for results")
    

