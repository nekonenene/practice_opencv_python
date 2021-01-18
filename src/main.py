# 参考:
# https://blog.mudatobunka.org/entry/2016/10/03/014520
# https://qiita.com/hitomatagi/items/04b1b26c1bc2e8081427
import cv2
import time

start_time = time.time()

# 画像の読み込み
image = cv2.imread('images/sample.jpg')

# 処理速度を高めるために画像をグレースケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 評価器を読み込み
face_cascade = cv2.CascadeClassifier(
    'data/haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# 顔検出
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=3,
    minSize=(50, 50),
)

for (x, y, w, h) in faces:
    # 検知した顔を矩形で囲む
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 3)
    # 顔画像（グレースケール）
    roi_gray = gray[y: y + int(h * 2 / 3), x: x + w]
    # 顔画像（カラースケール）
    roi_color = image[y: y + int(h * 2 / 3), x: x + w]
    # 顔の中から目を検知
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        # 検知した目を矩形で囲む
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv2.imshow('image', image)

elapsed_time = time.time() - start_time
print("処理時間: {0} sec".format(elapsed_time))

key = cv2.waitKey(0)
if key == ord('s'):  # s を押したら画像保存
    cv2.imwrite('dist/sample.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])
    cv2.destroyAllWindows()
else:  # 他のキーならウィンドウを閉じるだけ
    cv2.destroyAllWindows()
