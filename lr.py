import numpy as np
import pandas as pd
import sys
import math
import statistics
import matplotlib.pyplot as plt
#from sklearn.preprocessing import StandardScaler



def linear(data):
    age = np.array((data[0]))
    weight = np.array(data[1])
    height = np.array(data[2])
    #normData = np.insert(data0, 0, 1, axis = 1)

    # preprocessing
    A = []
    W = []

    sd_a = np.mean(age)
    m_a = np.mean(age)

    sd_w = np.mean(weight)
    m_w = np.mean(weight)

    
    for each in age:
        A.append((each - m_a) / sd_a)

    for each in weight:
        W.append((each - m_w) / sd_w)

    mat = np.ones((len(A), 4))
    mat[:,2] = W
    mat[:,1] = A
    mat[:,3] = height

    alphas = [0.001,0.005,0.01,0.05,0.1,0.5,1,5,10, .0001]
    i = 0
    betas = []
    BETA = []
    for alpha in alphas:
        R = []
        betas = gradient(A,W, alpha, mat)
        i +=1

        for i in range(100):
            x = (risk(betas, mat, i))
            R.append(x)


        result = (choose(betas,R))
        BETA.append(result)
    return BETA
        

    


    #pred = np.dot(R,A) + B

    #plt.scatter(A, W, height) 
    #plt.plot([min(A), max(A)], [min(pred), max(pred)], color='red')  # regression line
    #plt.show()   
        
    
def choose(beta, R):

    r = np.argmin(R)
    final = np.argmax(beta[r])

    return beta[r]



    
def gradient(A,W, alpha, mat):
    betas = [np.zeros(3)]
    b = np.zeros(3)
    
    for i in range(100):
        summ = []
        i = 0
        while i < 3:
            tots = np.sum((b[0] + (b[1]*A[0] \
            + b[2]* W[0]- mat[:,i])*mat[:,3]))
            summ.append(tots)
            i+=1
        
        j = 0
        while j < 3:
            b[j] -= (summ[j] * alpha)/len(A)
            betas.append(b)
            j+=1

    return np.array(betas)

def risk(betas, mat, i):
    t = sum((betas[i, 0] + betas[i,1]*mat[:,1] + betas[i,2] *mat[:,2] - mat[:,3])**2)
    R = t/(2*len(mat))
    return R
    
        
        

if __name__ == "__main__":

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    data = pd.read_csv(in_file, header=None)
    result = linear(data)
    b = []
    a = []
    w = []
    for i in result:
        b.append(i[0])
        a.append(i[1])
        w.append(i[2])

    alphas = [0.001,0.005,0.01,0.05,0.1,0.5,1,5,10, .0001]
    it = [100,100,100,100,100,100,100,100,100,100]
    df = pd.DataFrame({'alpha': alphas,'iteration': it, '[b_0]': b,'[b_age]': a,\
                       '[b_weight]': w})

    df.to_csv(out_file)

    print("Done, check " + str(out_file) + " for results")    



