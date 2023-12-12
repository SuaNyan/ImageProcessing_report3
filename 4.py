import cv2
import numpy as np
import time
import random

# 画像を読み込む
image = cv2.imread('4_1.jpeg')

# 画像を3x3のモザイクタイルに分割
tile_size = (image.shape[1] // 3, image.shape[0] // 3)

# シャッフルするためのタイルのリストを作成
tiles = []
for y in range(3):
    for x in range(3):
        tile = image[y * tile_size[1]: (y + 1) * tile_size[1], x * tile_size[0]: (x + 1) * tile_size[0]]
        tiles.append(tile)

# シャッフルしてから反転
random.shuffle(tiles)

for tile in tiles:
    # タイルを左右反転
    flipped_tile = cv2.flip(tile, 1)  # 第2引数を1に設定して左右反転

    # 反転したタイルを表示
    cv2.imshow('Flipped Tile', flipped_tile)
    cv2.waitKey(5000)  # 5秒待つ

# 全てのウィンドウを閉じる
cv2.destroyAllWindows()
