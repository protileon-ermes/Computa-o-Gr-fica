import cv2
from matplotlib import pyplot as plt
import numpy as np
import math

path ='/'
img1 = cv2.imread(path + 'quote2.png')
img2 = cv2.imread(path + 'praia.jpg')
plt.figure(figsize=(12,12))
plt.subplot(121)
plt.imshow(cv2.cvtColor(img1, cv2. COLOR_BGR2RGB))

plt.subplot(122)
plt.imshow(cv2.cvtColor(img2, cv2. COLOR_BGR2RGB))