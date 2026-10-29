#!/usr/bin/env python3
# Kedi Miyav Selamlaşma Protokolü v1.0
# Bu program, insanların kedilerle resmi diplomatik selamlaşmasını sağlar.
# Uyarı: Kediler bu protokolü ciddiye almayabilir.

import time
import random
import base64

def kediye_selam_ver(insan_selami):
    print("\n=== KEDİ DİPLOMASİ PROTOKOLÜ BAŞLATILIYOR ===")
    print("Protokol seviyesi: ULUSLARARASI MİYAV STANDARDI (UMS-2026)")
    time.sleep(1.5)
    
    miyav_listesi = ["Miyav", "Miiyav", "Miyavvv", "Mırr", "Purr", "Hıss", "Miyau"]
    miyav_sayisi = (len(insan_selami) % 7) + 3  # En az 3 miyav
    
    print(f"\nGirdi analiz ediliyor: '{insan_selami}'")
    print("Kedinin ruh hali hesaplanıyor... (bu biraz sürer, kediler acele etmez)")
    time.sleep(2)
    
    print("\n--- MİYAV ÇEVİRİSİ ---")
    for i in range(miyav_sayisi):
        miyav = random.choice(miyav_listesi)
        print(f"  {miyav}!", end=" ")
        time.sleep(0.8)
    print("\n")
    
    # Gizli diplomatik not (base64 ile saklı)
    gizli = base64.b64decode("S2F5eXVtIGF0YW1hc8SxIGdpcmVsaSBiaXIgZGlwbG9tYXRp").decode('utf-8')
    # print(gizli)  # Açmak isterseniz yorumu kaldırın, ama kediler bilmesin
    
    print("Protokol tamamlandı. Kedi memnuniyet derecesi: %" + str(random.randint(42, 99)))
    print("Not: Eğer kedi kuyruğunu sallarsa, diplomasi başarılıdır.")
    print("Eğer kedi sizi tırmalarsa, protokol revizyonu gerekir.")

if __name__ == "__main__":
    print("Hoş geldiniz, Sayın Diplomat!")
    selam = input("Lütfen kedinize söylemek istediğiniz selamı girin: ")
    if not selam.strip():
        selam = "Merhaba kedi"
    kediye_selam_ver(selam)
    print("\nProtokol sona erdi. İyi miyavlar!")
