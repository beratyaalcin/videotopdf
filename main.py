import cv2
import img2pdf
import os

def video_to_pdf(video_path, output_pdf, frame_interval=30):
    # Videoyu aç
    cam = cv2.VideoCapture(video_path)
    current_frame = 0
    images = []

    print("İşlem başlıyor, lütfen bekleyin...")

    while True:
        ret, frame = cam.read()
        if ret:
            # Belirli aralıklarla kare yakala (Örn: her 30 karede bir)
            if current_frame % frame_interval == 0:
                name = f'frame_{current_frame}.jpg'
                cv2.imwrite(name, frame)
                images.append(name)
            current_frame += 1
        else:
            break

    # Resimleri PDF'e dönüştür
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images))

    # Geçici resim dosyalarını temizle
    for img in images:
        os.remove(img)

    cam.release()
    print(f"Başarılı! {output_pdf} oluşturuldu.")

# Kullanım:
video_to_pdf("ders_videosu.mp4", "ders_notlari.pdf", frame_interval=60)