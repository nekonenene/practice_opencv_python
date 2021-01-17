import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('sample.jpg', 0)

cv2.imshow('image', img)
key = cv2.waitKey(0)
if key == ord('s'):  # s を押したら画像保存
    cv2.imwrite('dist/sample.png', img)
    cv2.destroyAllWindows()
else: # 他のキーならウィンドウを閉じるだけ
    cv2.destroyAllWindows()
