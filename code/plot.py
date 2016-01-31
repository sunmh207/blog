#coding:utf-8
from numpy import *

def loadDataSet():
  return [[1,2],
    [1,3],
    [4,7]]


def plot(dataSet,clr='green'):
  import matplotlib.pyplot as plt
  fig=plt.figure()
  ax=fig.add_subplot(111)
  x=[];y=[]
  for i in range(len(dataSet)):
     x.append(dataSet[i][0])
     y.append(dataSet[i][1])
  ax.scatter(x,y,s=30,c=clr)

  ax.annotate('A(1,2)', xy=(1, 2), xytext=(0.6, 2),)
  ax.annotate('B(1,3)', xy=(1, 3), xytext=(0.6, 3),)
  ax.annotate('C(4,7)', xy=(4, 7), xytext=(4.1, 7),)

  ax.plot(mat(dataSet)[:,0].A,mat(dataSet)[:,1].A)
  plt.show() 

def test():
  dataSet = loadDataSet()
  plot(dataSet)