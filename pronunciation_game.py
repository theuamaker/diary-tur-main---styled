import random
from speech_recog import recognize_speech
#from speech_recog import r
puan=0

for i in range(3):
    seviyeler = {

        "kolay": ["huge", "Mouse", "computer"],

        "orta": ["programming", "algorithm", "developer"],

        "zor": ["neural network", "machine learning", "artificial intelligence"] 
        }

    secenek = input("hangi zorluğu istersin?(kolay, orta, zor)")

    if secenek == "kolay":
        kelime=random.choice(seviyeler["kolay"])
        print(kelime, "<------ bunu telaffuz et")    
        if recognize_speech() == kelime:
            print("Tebrikler")
            puan+=1
            print("puanın =", puan)
        
        else:
            print("yanlış cevap!")
            print(puan)


    elif secenek == "orta":
        kelime=random.choice(seviyeler["orta"])
        print(kelime, "<------ bunu telaffuz et")   
        if recognize_speech() == kelime:
            print("Tebrikler")
            puan+=2
            print("puanın =", puan)
        
        else:
            print("yanlış cevap!")
            print(puan)

    elif secenek == "zor":
        kelime=random.choice(seviyeler["zor"])
        print(kelime, "<------ bunu telaffuz et")   
        if recognize_speech() == kelime:
            print("Tebrikler")
            puan+=3
            print("puanın =", puan)
        
        else:
            print("yanlış cevap!")
            print(puan)

print("toplam puan =",puan)