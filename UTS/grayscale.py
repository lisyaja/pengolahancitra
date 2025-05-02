import cv2
import numpy as np

def konversi_grayscale_manual(image_path, output_path='grayscale_manual.jpg'):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    gray_img = img.copy()

    for i in range(height):
        for j in range(width):
            B, G, R = img[i, j]
            gray = int(0.114 * B + 0.587 * G + 0.299 * R)
            gray_img[i, j] = [gray, gray, gray]

    cv2.imwrite(output_path, gray_img)

    # Gabungkan input dan output untuk ditampilkan
    combined = np.hstack((img, gray_img))
    cv2.imshow("Gambar Asli dan Grayscale Manual", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# === Jalankan Program ===
konversi_grayscale_manual('1.jpg')
