import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('6_1.jpeg')  # 画像のファイル名を指定

# ガウシアンぼかしフィルタの適用
blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=1.5)

# 鮮鋭化フィルタの強度を変更しながら適用
sharpened_1 = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
sharpened_2 = cv2.addWeighted(image, 2.0, blurred, -1.0, 0)
sharpened_3 = cv2.addWeighted(image, 2.5, blurred, -1.5, 0)

# 結果を表示
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened (Strength 1.5)', sharpened_1)
cv2.imshow('Sharpened (Strength 2.0)', sharpened_2)
cv2.imshow('Sharpened (Strength 2.5)', sharpened_3)

# キー入力待ち
cv2.waitKey(0)
cv2.destroyAllWindows()
