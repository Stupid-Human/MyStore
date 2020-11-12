#!/usr/bin/env python
# coding: utf-8

# **在Python中，这种一边循环一边计算的机制，称为生成器：generator**

# **第一种方法很简单，只要把一个列表生成式的[]改成()**

# In[19]:


L = [x * x for x in range(10)]
L


# In[36]:


g = (x * x for x in range(10))
g


# **通过next()函数获得generator的下一个返回值**
# 
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误

# In[37]:


next(g)


# **创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误**
# 

# In[39]:


g = (x * x for x in range(10))
for n in g:
    print(n)


# **输出斐波那契数列的前N个数：**

# In[45]:


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

fib(0)


# In[46]:


fib(1)


# In[47]:


fib(2)


# In[49]:


fib(-3)


# In[50]:


fib(6)


# **要把fib函数变成generator，只需要把print(b)改为yield b就可以了:**

# In[51]:


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# In[52]:


fib(6)


# In[ ]:




