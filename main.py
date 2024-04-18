import time
kelime = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
print("Merhaba! Bu bir bilinmeyen sözler sözlüğü. Bilmedğiniz gündem sözleri sorabilirsiniz.")
time.sleep(2)
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in kelime.keys():
    print(word,"kelmiseinin anlamı:",kelime[word])
else:
    print("Böyle bir kelime küthüpanemizde yok ):")
