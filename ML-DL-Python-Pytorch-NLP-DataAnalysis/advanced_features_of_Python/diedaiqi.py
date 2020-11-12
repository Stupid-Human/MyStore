#!/usr/bin/env python
# coding: utf-8

# **可以直接作用于for循环的对象统称为可迭代对象：Iterable**
# 
# 可以使用isinstance()判断一个对象是否是Iterable对象：

# In[13]:


from collections import Iterable


# In[16]:


print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))


# In[23]:


isinstance((x for x in range(10)), Iterable) 


# **生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。**
# 
# **把list、dict、str等Iterable变成Iterator可以使用iter()函数：**

# In[24]:


isinstance(iter([]), Iterable)


# In[25]:


isinstance(iter('abc'), Iterable)

