#!/usr/bin/env python
# coding: utf-8

# **参考莫烦Python的简要教程**

# # **Numpy的属性**
# 

# **ndim：维度**
# 
# **shape：行数和列数**
# 
# **size：元素个数** 

# In[1]:


import numpy as np


# In[207]:


array = np.array([[1,2,3],[2,3,4]]) 

print(array.shape) #行数和列数
print(array.size) #元素个数
print(array.ndim) #维数


# # **array：创建数组**

# ## **关键字**
# 
# **array：创建数组**
# 
# **dtype：指定数据类型**
# 
# **zeros：创建数据全为0**
# 
# **ones：创建数据全为1**
# 
# **empty：创建数据接近0**
# 
# **arrange：按指定范围创建数据**
# 
# **linspace：创建线段**

# In[13]:


a = np.array([2, 23, 4])
print(a)
#没有逗号分隔


# **dtype int float**

# In[17]:


a = np.array([2, 23, 4], dtype = np.int64)
print(a.dtype)


# In[18]:


a = np.array([2, 23, 4], dtype = np.int)
print(a.dtype)


# In[19]:


a = np.array([2, 23, 4], dtype = np.int32)
print(a.dtype)


# In[21]:


a = np.array([2, 23, 4], dtype = np.float)
print(a.dtype)


# In[23]:


a = np.array([2, 23, 4], dtype = np.float32)
print(a.dtype)


# **指定行列数**

# In[24]:


array = np.array([[1, 2, 3],
                 [5, 6, 7]])
print(array)


# **全0**

# In[26]:


a = np.zeros((3, 4))
print(a)


# **全1**

# In[28]:


a = np.ones((5, 8), dtype = np.int16)
print(a)


# In[49]:


xArry = np.ones((3, 4))
xArry


# **全空**

# In[30]:


a = np.empty((5, 6))
print(a)


# **arange**

# In[50]:


a = np.arange(10, 101, 7)
print(a)
#类似于Python中的arange 7为步长


# **reshape**

# In[43]:


a = np.arange(12).reshape(3, 4)
print(a)


# **linspace**

# In[47]:


a = np.linspace(1, 100, 20)
print(a)


# In[48]:


a = np.linspace(1, 100, 20).reshape(10, 2)
print(a)


# # **Numpy基础运算**

# **+ - * / 幂次 sin... < ==等**

# In[66]:


a = np.array([10, 20, 30, 40])
b = np.arange(4)
print('a:', a)
print('b:', b)
print('a,b:', a, b)
c = a + b
d = a - b
e = a * b #逐个相乘 必须结构一样
f = b / a
g = a**2
h = b**3
print('a+b:',c)
print('a-b:',d)
print('a*b:',e)
print('b/a:',f)
print('a^2:', g)
print('b^3:', h)

c = 10*np.sin(a)
print('10*sin(a):', c)
#cos tan...

print('b:', b)
print(b<3)

print('b:', b)
print(b==3)


# **矩阵相乘**

# In[82]:


a = np.array([[9, 1, 8],
              [2, 1, 0]])
b = np.arange(12).reshape((3, 4))
print('a:')
print(a)
print('b:')
print(b) 

c_dot = np.dot(a, b) 
c_dot_2 = a.dot(b)    #另一种表示
print('a和b的矩阵相乘:')
print(c_dot)
print(c_dot_2)


# **求和 求最小值 求最大值**

# In[96]:


a = np.random.random((2, 4))
print(a)
#随机生成0到1的数字

print(np.sum(a))
print(np.min(a))
print(np.max(a))
      


# **在行数、列数中求和**

# In[108]:


print(np.sum(a, axis=1))    #在列数求和
print(np.sum(a, axis=0))    #在行数种求和
print(np.min(a, axis=1))
print(np.min(a, axis=0))
print(np.max(a, axis=1))
print(np.max(a, axis=0))


# **argmin() argmax(),求矩阵中最小元素和最大元素的索引**

# In[113]:


A = np.arange(2, 14).reshape((3, 4))
print(A)
print(np.argmin(A))
print(np.argmax(A))


# **求均值、中位数**

# In[149]:


print(np.mean(A))
print(np.average(A)) #两种表达方式

print(np.median(A)) #求中位数


# **累加的效果**

# In[145]:


print(A)
print(np.cumsum(A))


# **差的效果**

# In[128]:


print(A)
print(np.diff(A)) #后一个减前一个数的差


# **找出非0的数**

# In[130]:


print(np.nonzero(A))

#结果解释：第0行第0列，第0行第1列


# **逐行排序**

# In[133]:


A = np.arange(14, 2, -1).reshape(3, 4)
print(A)

print(np.sort(A))


# **矩阵转置**

# In[139]:


A = np.arange(14, 2, -1).reshape(3, 4)
print(A)

print(np.transpose(A))
print(A.T)    #另一种表示

print((A.T).dot(A))


# **clip函数**

# In[143]:


#clip(Array,Array_min,Array_max)
#让大于max的数变为max,让小于min的数变为min

print(A)
print(np.clip(A, 3, 8))


# **补充一下按列按行**

# In[152]:


print(A)
print(np.median(A, axis = 0)) #按行计算
print(np.median(A, axis = 1)) #按列计算


# # **Numpy索引**

# **一维索引**

# In[255]:


A = np.arange(3, 15)
print(A)
print(A[3])

A = np.arange(3, 15).reshape(3, 4)
print(A)
print(A[2])    #行数
 


# **二维索引**

# In[256]:


print(A[1][1])
print(A[1, 1])

print(A[1, :])
print(A[:, 1])
print(A[:, :])

print(A[1, 1:2])  #第一行 第1~2这个数
print(A[1, 1:3])

for row in A:
    print(row)    #按行迭代

for column in A.T:
    print(column)     #实现按列迭代的效果

print(A.flatten())    
    
for item in A.flat:
    print(item)


# ## **Numpy array 合并**

# **vstack 上下合并**
# 
# **hstack 左右合并**

# In[269]:


A = np.array([1, 1, 1])
B = np.array([2, 2, 2])


c = np.vstack((A, B))
print(c)
print(A.shape)
print(c.shape)
print(c)

c = np.hstack((A, B))
print(c.shape)
print(c)


# In[270]:


print('A:')
print(A)
print('B:')
print(B)

print('A.T:')
print(A.T)    #翻转不过来

print('newA1:')
print(A[np.newaxis,:])    #行上加一个维度 

print('newA2:')    
print(A[:,np.newaxis])    #纵向加维度 

print('添加新维度后：')
A = np.array([1, 1, 1])[:,np.newaxis]
B = np.array([2, 2, 2])[:,np.newaxis]
c = np.hstack((A, B))
print('A:')
print(A)
print('B:')
print(B)
print(A.shape, c.shape)
print(c)


# **再探newaxis**

# In[265]:


HH = np.arange(2, 8).reshape(2, 3)
print(HH)
print(HH.shape)

JJ = HH[np.newaxis,:]
print(JJ)
print(JJ.shape)

KK = HH[:,np.newaxis]
print(KK)
print(KK.shape)


# 插曲：验证属性输出

# In[208]:


MM = np.array([1, 2, 3, 4, 5, 6])
print(np.shape(MM))


# **concatenate**

# In[268]:


print('A:')
print(A)
print('B:')
print(B)

print('C:')
C = np.concatenate((A,B,B,A),axis=0)    #上下这个方向合并
print(C)

print('C:')
C = np.concatenate((A,B,B,A),axis=1)    #左右这个方向合并
print(C)


# ## **Numpy array 分割**

# In[272]:


A = np.arange(12).reshape(3, 4)
print(A)


# **split**

# In[280]:


print(np.split(A, 2, axis = 1))
print(np.split(A, 3, axis = 0))


# **array_split**

# In[282]:


print(np.array_split(A, 3, axis = 1))    #不等项分割


# **vsplit**
# 
# **hsplit**

# In[284]:


print(np.vsplit(A, 3))
print(np.hsplit(A, 2))


# # **Numpy copy & deep copy**

# **关于赋值, = 的赋值方式会带有关联性**

# In[291]:


a = np.arange(4)
print(a)

b = a
c = a
d = b

a[0] = 23
print(a)
print(b)
print(d)

b is a


# In[292]:


c is a


# In[293]:


d is a


# In[294]:


d[1:3] = [55, 66]

print(a)


# **copy() 的赋值方式没有关联性 **

# In[298]:


mm = a.copy()

print(a)
print(mm)

a[3] = 100
print(a)
print(mm)

mm is a


# In[ ]:




