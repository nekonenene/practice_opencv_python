import numpy as np
import cv2

# 黒画像の作成
img = np.zeros((512, 512, 3), np.uint8)

# 斜めに線を引く
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 正方形
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 正円
img = cv2.circle(img, (400, 80), 63, (0, 0, 255), -1)

# 楕円
img = cv2.ellipse(img, (120, 400), (100, 50), 0, 0, 270, 255, -1)

# 多角形
pts = np.array([[20, 10], [100, 300], [380, 20], [90, 100]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

# テキスト追加
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 450), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
