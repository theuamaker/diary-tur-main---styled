import random
from speech_recog import recognize_speech

puan = 0

# Kullanıcıdan ismi al
oyuncu_isim = input("Lütfen isminizi girin: ")

for i in range(3):
    seviyeler = {

        "kolay": ["huge", "Mouse", "computer"],

        "orta": ["programming", "algorithm", "developer"],
        
        "zor": ["neural network", "machine learning", "artificial intelligence"]       
    }

    secenek = input("Hangi zorluğu istersin? (kolay, orta, zor)")

    if secenek in seviyeler:
        kelime = random.choice(seviyeler[secenek])
        print(kelime, "<------ bunu telaffuz et")
        if recognize_speech() == kelime:
            print("Tebrikler!")
            if secenek == "kolay":
                puan += 1
            elif secenek == "orta":
                puan += 2
            elif secenek == "zor":
                puan += 3
            print("Puanın =", puan)
        else:
            print("Yanlış cevap!")
            print("Puanın =", puan)

# Dosyaya oyuncunun verilerini kaydet
with open("oyuncu_verileri.txt", "a") as file:
    file.write(f"{oyuncu_isim},{puan}\n")

# Liderlik tablosunu oluştur
liderlik_tablosu = []
with open("oyuncu_verileri.txt", "r") as file:
    for line in file:
        isim, puan = line.strip().split(',')
        liderlik_tablosu.append((isim , int(puan)))

# En yüksek puana sahip ilk üç kişiyi seç
liderlik_tablosu.sort(key=lambda x: x[1], reverse=True)
toplam_oyuncu_sayisi = len(liderlik_tablosu)
liderlik_tablosu = liderlik_tablosu[:min(3, toplam_oyuncu_sayisi)]

# Liderlik tablosunu göster
print("Liderlik Tablosu:")
for i, (isim, puan) in enumerate(liderlik_tablosu, 1):
    print(f"{i}. {isim}: {puan}")

print("Toplam Puanınız =", puan)