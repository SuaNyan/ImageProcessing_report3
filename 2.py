import cv2
import numpy as np

# 2つの画像を読み込む
image1 = cv2.imread('2_1neko.png')
image2 = cv2.imread('2_2neko.png')

# アルファブレンディングのためのアルファチャンネル（透明度）を作成
alpha = 0.5  # アルファ値（0.0から1.0の間で調整）

# 2つの画像をアルファブレンディング
blended = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)

# 結果を表示または保存
cv2.imshow('Blended Image', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画像を "neko2.png" として保存
cv2.imwrite('neko2.png', blended)
