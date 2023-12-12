import cv2

# 画像を読み込む
image = cv2.imread('3_1.jpeg')

# 画像を中心軸に関して左右反転する
flipped_image = cv2.flip(image, 1)  # 第2引数を1に設定して左右反転

# 反転した画像を表示する
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画像を "3_output_image.jpg" として保存
cv2.imwrite('3_output_image.jpeg', flipped_image)
