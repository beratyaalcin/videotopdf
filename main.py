import cv2
import img2pdf
import os

def video_to_pdf(video_path, output_pdf, frame_interval=30):
    cam = cv2.VideoCapture(video_path)
    current_frame = 0
    images = []

    print("İşlem başlıyor, lütfen bekleyin...")

    while True:
        ret, frame = cam.read()
        if ret:
            #belirli aralıklarla kare yakala (her 30 karede bir)
            if current_frame % frame_interval == 0:
                name = f'frame_{current_frame}.jpg'
                cv2.imwrite(name, frame)
                images.append(name)
            current_frame += 1
        else:
            break

    #resimleri pdf'e donustur
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(images))

    #toplanilan resimleri sil
    for img in images:
        os.remove(img)

    cam.release()
    print(f"Başarılı! {output_pdf} oluşturuldu.")

#kullanimi
video_to_pdf("ders_videosu.mp4", "ders_notlari.pdf", frame_interval=60)
