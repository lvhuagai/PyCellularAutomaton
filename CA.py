import numpy as np
import random
import matplotlib.pyplot as plt
import copy

length=100
width=100
cell = np.zeros((length,width),int)
cell_process = copy.deepcopy(cell)
num=0

#Init
for i in range(0,length):
    for j in range(0,width):
        cell_process[i][j] = random.randint(0,1)
#Process
while not(cell == cell_process).all():
    cell = copy.deepcopy(cell_process)
    plt.imshow(cell)
    plt.pause(0.1)
    for i in range(0,length):
        for j in range(0,width):

            if ((i>0 and j>0)and(i<length-1 and j<width-1)):
                num=cell[i-1][j]+cell[i+1][j]+cell[i][j-1]+cell[i][j+1]+cell[i-1][j-1]+cell[i+1][j+1]+cell[i+1][j-1]+cell[i-1][j+1]
            if (i==0 and (j>0 and j<width-1)):
                num=cell[i][j-1]+cell[i+1][j]+cell[i][j+1]+cell[i+1][j+1]+cell[i+1][j-1]
            if(i==length-1 and (j>0 and j<width-1)):
                num=cell[i-1][j]+cell[i][j-1]+cell[i][j+1]+cell[i-1][j-1]+cell[i-1][j+1]
            if(j==0 and (i>0 and i<length-1)):
                num=cell[i-1][j]+cell[i-1][j+1]+cell[i][j+1]+cell[i+1][j]+cell[i+1][j+1]
            if(j==width-1 and(i>0 and i<length-1)):
                num=cell[i-1][j-1]+cell[i-1][j]+cell[i][j-1]+cell[i+1][j-1]+cell[i+1][j]
            if(i==0 and j==0):
                num=cell[i][j+1]+cell[i+1][j]+cell[i+1][j+1]
            if(i==0 and j==width-1):
                num=cell[i][j-1]+cell[i+1][j-1]+cell[i+1][j]
            if(i==length-1 and j==0):
                num=cell[i-1][j]+cell[i-1][j+1]+cell[i][j+1]
            if(i==length-1 and j==width-1):
                num=cell[i-1][j]+cell[i][j-1]+cell[i-1][j-1]

            if(cell[i][j]==0 and num !=3):
                continue
            if(cell[i][j]==0 and num ==3):
                cell_process[i][j]=1
                continue
            if(num==2 or num==3):
                continue
            cell_process[i][j]=0
