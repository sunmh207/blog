#coding:utf-8

from numpy import *
from numpy import linalg as la

def loadData():    
  return[[5, 3, 0, 2, 2],
         [4, 0, 0, 3, 3],
         [5, 0, 0, 1, 1],
         [1, 1, 1, 2, 0],
         [2, 2, 2, 0, 0],
         [1, 1, 1, 0, 0],
         [5, 5, 5, 0, 0]]

def eSim(A,B):    
  return 1.0/(1.0+la.norm(A-B))

'''
  函数功能：计算在给定相似度计算方法的条件下，用户对物品的估计评分值
input
  ds: 评价矩阵
  userIdx: 用户编号
  simFunc: 相似度计算方法
  courseIdx: 课程编号
output
  编号为courseIdx的课程的估计分值 
'''
def standEst(ds, userIdx, simFunc, courseIdx):
  n = shape(ds)[1] #课程数量
  simTotal = 0.0; ratSimTotal = 0.0
  #遍历所有课程
  for j in range(n):
      userRating = ds[userIdx,j]  #用户对第j个课程的评价
      if userRating == 0: continue  #用户没有对该课程评分，跳过
      #寻找两个用户都评级的课程
      overLap = nonzero(logical_and(ds[:,courseIdx].A>0, ds[:,j].A>0))[0]
      #如果两个课程(courseIdx和j)没有共同评价人，则相似度＝0
      if len(overLap) == 0: similarity = 0
      #否则计算相似度
      else: similarity = simFunc(ds[overLap,courseIdx], ds[overLap,j])
      print 'the %d and %d similarity is: %f' % (courseIdx, j, similarity)
      #总相似度(相似度可以理解为权重)
      simTotal += similarity
      #相似度*评分的合计
      ratSimTotal += similarity * userRating
  if simTotal == 0: return 0
  else: return ratSimTotal/simTotal #预计得分 

'''
推荐引擎
input
  ds: 数据
  userIdx:
  N: 最高推荐N个结果
  simFunc
  estFunc
'''
def recommendCourses(ds, userIdx, N=3, simFunc=eSim, estFunc=standEst):
    unratedCourses = nonzero(ds[userIdx,:].A==0)[1] #当前用户没有打分的课程 
    if len(unratedCourses) == 0: return '你已经学过所有课程'
    courseScores = [] #课程分数列表
    for courseIdx in unratedCourses:
        estimatedScore = estFunc(ds, userIdx, simFunc, courseIdx)
        courseScores.append((courseIdx, estimatedScore))
    return sorted(courseScores, key=lambda jj: jj[1], reverse=True)[:N]

def test():
  dataMat = mat(loadData())
  print recommendCourses(dataMat,2)    
