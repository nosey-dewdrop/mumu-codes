"""
Lab5Q3.py - Soru 3:
"Bir string'deki her karakterin kaç kez geçtiğini sayan ve sonucu bir dosyaya yazan program yazın."

Fonksiyon countLetters(s) olarak adlandırılmalı
Her karakter için bir dictionary oluşturmalı (karakter: tekrar sayısı)
Kullanıcıdan string almalı
Sonuçları 'outfile.txt' dosyasına yazmalı (karakter ve sayısını tab ile ayırarak)

"""

      
def countLetters(str):
      counts = {}  
      for i in str:
            if i in counts:
                  counts[i] += 1
            else:
                  counts[i] = 1

      with open("outfile.txt", "w", encoding="utf-8") as f:
            for i, count in counts.items():
                  f.write(f"{i}\t{count}\n")

text = input("input a word: ")
countLetters(text)
      
      