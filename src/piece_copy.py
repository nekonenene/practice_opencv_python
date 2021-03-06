import cv2

# Load an color image in grayscale
img = cv2.imread('images/sample.jpg', 0)

print(img.shape)  # (縦のpx数, 横のpx数)

print(img.size)  # 合計画素数

print(img.dtype)  # 画像のデータ型 : 例えば uint8 なら 0-255 で表現される

piece = img[200:1000, 1000:1500]
img[800:1600, 1300:1800] = piece

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
