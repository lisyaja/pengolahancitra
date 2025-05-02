import cv2
import numpy as np

def konversi_biner_manual(grayscale_path, output_path='biner_manual.jpg', threshold=128):
    gray_img = cv2.imread(grayscale_path)
    height, width, _ = gray_img.shape

    binary_img = gray_img.copy()

    for i in range(height):
        for j in range(width):
            gray = gray_img[i, j][0]
            binary = 255 if gray >= threshold else 0
            binary_img[i, j] = [binary, binary, binary]

    cv2.imwrite(output_path, binary_img)

    # Gabungkan grayscale dan biner untuk ditampilkan
    combined = np.hstack((gray_img, binary_img))
    cv2.imshow("Grayscale dan Biner Manual", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# === Jalankan Program ===
konversi_biner_manual('grayscale_manual.jpg')
