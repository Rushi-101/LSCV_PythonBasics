import numpy as np
import random
import matplotlib.pyplot as plt

def main():
    with open("data.txt", 'r') as inp:
        data = inp.readlines()
    matrix= [[0 for i in range(len(data[0]))] for j in range(len(data))]
    for i in range(len(data)):
        matrix[i]=(np.array(data[i].split(",")).astype(float)).tolist()

    data = np.array(matrix)
    std = np.std(data, axis=0)
    mean = np.mean(data, axis=0)
    data = (data - mean)/std
    cov = np.cov(data.T)
    value, vector = np.linalg.eig(cov)
    a = np.random.randint(3, size=2)
    eigen_vecs = [vector[a[0]],vector[a[1]]]
    eigen_vecs = np.array(eigen_vecs )
    output = np.dot(data, eigen_vecs.T)
    plt.figure(figsize = (10,10))
    plt.scatter(output[:,0], output[:,1])
    plt.show()
    plt.savefig('out.png')

main()