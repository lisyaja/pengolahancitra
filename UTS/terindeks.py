import cv2
import numpy as np
from tkinter import Tk, filedialog, Button, Label, Entry
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

class IndexedImageApp:
    def __init__(self, master):
        self.master = master
        master.title("Konversi Citra Terindeks")

        self.label = Label(master, text="Unggah gambar:")
        self.label.pack()

        self.upload_button = Button(master, text="Pilih Gambar", command=self.upload_image)
        self.upload_button.pack()

        self.color_label = Label(master, text="Jumlah warna (indeks):")
        self.color_label.pack()

        self.color_entry = Entry(master)
        self.color_entry.insert(0, "16")  # default 16 warna
        self.color_entry.pack()

        self.convert_button = Button(master, text="Konversi", command=self.convert)
        self.convert_button.pack()

        self.original_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = cv2.imread(file_path)
            print("Gambar berhasil dimuat.")

    def convert(self):
        if self.original_image is None:
            print("Silakan unggah gambar terlebih dahulu.")
            return

        try:
            k = int(self.color_entry.get())
            self.convert_to_indexed(self.original_image, k)
        except ValueError:
            print("Jumlah warna harus berupa angka.")

    def convert_to_indexed(self, image, k=16):
        # Konversi BGR ke RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pixels = image_rgb.reshape((-1, 3))

        # KMeans clustering untuk mendapatkan palet warna
        kmeans = KMeans(n_clusters=k, random_state=0).fit(pixels)
        indexed_pixels = kmeans.labels_
        palette = kmeans.cluster_centers_.astype("uint8")

        # Buat citra terindeks
        indexed_image = palette[indexed_pixels].reshape(image_rgb.shape)

        # Tampilkan hasil
        plt.figure(figsize=(12, 6))

        # Gambar asli
        plt.subplot(1, 3, 1)
        plt.title("Gambar Asli")
        plt.imshow(image_rgb)
        plt.axis('off')

        # Gambar terindeks
        plt.subplot(1, 3, 2)
        plt.title(f"Citra Terindeks ({k} warna)")
        plt.imshow(indexed_image)
        plt.axis('off')

        # Tabel warna vertikal
        plt.subplot(1, 3, 3)
        plt.title("Palette")

        block_height = 40
        palette_img = np.zeros((k * block_height, 50, 3), dtype=np.uint8)

        for i, color in enumerate(palette):
            palette_img[i * block_height:(i + 1) * block_height, :] = color

        plt.imshow(palette_img)
        plt.axis('off')

        # Tambahkan label indeks di samping kanan blok
        for i in range(k):
            plt.text(55, i * block_height + block_height // 2, str(i),
                     va='center', fontsize=8, color='black')

        plt.tight_layout()
        plt.show()

# Jalankan aplikasi
root = Tk()
app = IndexedImageApp(root)
root.mainloop()
