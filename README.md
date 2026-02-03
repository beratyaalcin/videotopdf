## Video to PDF Converter

Video dosyalarını kare bazlı analiz ederek belirlenen aralıklarla görüntü ayıklar ve bu görüntüleri tek bir PDF dokümanında birleştirir.

### **Özellikle slayt şeklinde yüklenen ders videoları için.



### İşlem adımları

Görüntü İşleme: OpenCV kütüphanesi kullanılarak video akışı kare kare okunur.

Kare Ayıklama: Kullanıcı tarafından belirlenen *frame_interval* parametresine göre, gereksiz veri tekrarını önlemek amacıyla sadece belirli aralıktaki kareler yakalanır.

Yakalanan görüntüleri tek bir PDF dosyasında birleştirir.

İşlem bittikten sonra geçici görsel dosyalarını otomatik temizler.


### Kurulum

1\. Repoyu klonlayın: `git clone https://github.com/beratyaalcin/video-to-pdf.git`

2\. Kütüphaneleri kurun: `pip install -r requirements.txt`

3\. Çalıştırın: `python main.py`



---

\*Bu proje, üniversite ders içeriklerini daha verimli çalışabilmek adına geliştirilmiştir.\*




