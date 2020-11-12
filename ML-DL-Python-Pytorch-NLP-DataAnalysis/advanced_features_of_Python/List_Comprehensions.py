#!/usr/bin/env python
# coding: utf-8

# In[1]:


list(range(1, 10))


# **写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来：**

# In[2]:


[x * x for x in range(1, 11)]


# **for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：**

# In[39]:


[x * x for x in range (1, 11) if x % 2 == 0 ]


# **还可以使用两层循环，可以生成全排列：**

# In[4]:


[m+n for m in 'ABC' for n in 'XYZ']


# In[5]:


[m + n for m in (1, 2, 3) for n in (9, 20, 22)]


# In[6]:


import os 
[d for d in os.listdir('.')]


# **for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：**

# In[7]:


d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.items():
    print(k, '=', v)


# **列表生成式也可以使用两个变量来生成list：**

# In[8]:


d = {'x':'A', 'y':'B', 'z':'C'}
[k + '=' + v for k, v, in d.items()]


# **把一个list中所有的字符串变成小写：**
# 
# lower() 方法转换字符串中所有大写字符为小写，方法：str.lower()

# In[9]:


L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]


# **isinstance函数可以判断一个变量是不是字符串**

# In[10]:


x = 'ABC'
y = 123
print(isinstance(x, str))
isinstance(y, str)


# **练习：请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：**

# In[57]:


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# # 欢迎学习Markdown
#  
# 
# 添加重点的方法
# 
# **粗体**
# 
# *斜体这样操作？*
#  
#  
# 几个链接：
# 
# [马克飞象](https://maxiang.io/)
# 
# [给初学者的 Jupyter Notebook 教程][1]
# 
# [1]:https://juejin.im/post/5af8d3776fb9a07ab7744dd0
