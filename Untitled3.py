#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
image = cv2.imread('https://miro.medium.com/max/875/1*lSvFUirQRKEI1TKN_BBVFA.jpeg')
image.shape


# 
# 

# ![sasa.jpeg](attachment:sasa.jpeg)

# In[9]:





# In[39]:


import PIL
import numpy as np
from numpy.linalg import norm
from PIL import Image
image = Image.open('C:\\Users\\Partenaire_Inform\\Desktop\\sasa.jpeg')
data = np.array(image)
data.shape
mat=data[1,0:3]
print(mat)
mat_transpose = mat.T
print(mat_transpose)


# In[ ]:





# In[ ]:





# In[ ]:




