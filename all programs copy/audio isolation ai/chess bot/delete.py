import cv2
import numpy as np


img = cv2.imread('sprite_sheet.png', cv2.IMREAD_UNCHANGED)

q = img[213:426, 0:213,:]
print(q.shape)

cv2.imwrite('sprites\\KING_B.png', q)