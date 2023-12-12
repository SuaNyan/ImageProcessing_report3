from PIL import Image
import numpy as np

def gamma_correction(image_path, output_path, gamma):
    # 画像を開く
    image = Image.open(image_path)
    
    # NumPy配列に変換
    img_array = np.array(image)
    
    # トーンカーブ変換を適用
    corrected_array = ((img_array / 255.0) ** gamma) * 255.0
    
    # NumPy配列をPIL画像に変換
    corrected_image = Image.fromarray(corrected_array.astype('uint8'))
    
    # 画像を保存
    corrected_image.save(output_path)

# トーンカーブ変換を適用したい画像と出力先ファイルを指定
input_image_path = 'neko.jpeg'  # ファイル名を 'neko.jpeg' に変更
output_image_path = 'output_image.jpg'
gamma_value = 3  # ここでγの値を調整

# トーンカーブ変換を実行
gamma_correction(input_image_path, output_image_path, gamma_value)

# 出力された画像を確認
Image.open(output_image_path).show()
