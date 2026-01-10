"""
Lab5Q2.py - Soru 2:
"Bir string listesinden en kısa string'i bulan ve onu listeden silen bir fonksiyon yazın."

Fonksiyon shortest(ls) olarak adlandırılmalı
En kısa string'i return etmeli
Aynı zamanda o string'i orijinal listeden silmeli
Eğer aynı uzunlukta birden fazla en kısa string varsa, ilkini seçmeli

"""
def shortest(ls):
      
      shortest = ls[0]
      
      for i in range(1, len(ls)) :
            if(len(ls[i]) <= len(shortest)):
                  shortest = ls[i]
                  
      print("shortest is: ", shortest)
      return shortest

def detailed_shortest(ls):
      shortest_words = [ls[0]]
      shortest = ls[0]
      
      for i in range(1, len(ls)) :
            if(len(ls[i]) < len(shortest)):
                  shortest = ls[i]
                  shortest_words.clear()
                  shortest_words.append(ls[i])
                  
            elif(len(ls[i]) == len(shortest)):
                   shortest_words.append(ls[i])
                  
      if(len(shortest_words) > 0 ):   
            print("shortest is: ", shortest_words[0])
            return shortest_words[0]
      
      return
  
ls = ["elma", "armut", "kavun", "erik", "muz", "çilek", "hah", "domates"]
ls.remove(shortest(ls))
ls.remove(detailed_shortest(ls))
