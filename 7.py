import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('7_1.png')  # 画像のファイル名を指定

# グレースケール変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ガウシアンぼかしを適用してノイズを軽減
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Cannyエッジ検出を実行
edges = cv2.Canny(blurred, threshold1=30, threshold2=100)

# 輪郭を描画するためのコピーを作成
contours_image = image.copy()

# 輪郭の抽出
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を描画
cv2.drawContours(contours_image, contours, -1, (0, 255, 0), 2)

# 結果を表示
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.imshow('Contours', contours_image)

# キー入力待ち
cv2.waitKey(0)
cv2.destroyAllWindows()
