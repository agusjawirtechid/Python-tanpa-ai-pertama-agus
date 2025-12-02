import random
import base64


while True:
  print("========================================")
  print("pilih menu")
  print("========================================")
  menu = input("1) mengubah teks ke base64 atau sebaliknya \n2) mesin perhitungan \n3) tebak angka")
  if not menu.isdigit():
    print("==============================")
    print("masukan angka bang")
    print("==============================")
    continue
    
  
  
  if menu != "1" and menu != "2" and menu != "3":
    print("==============================")
    print("tidak ada pilihan seprti itu")
    print("==============================")
    continue
  
  #MENU NOMOR 1
  if menu == "1":
    menu1 = input("pilih \n1) di ubah ke base6\n2) base64 di ubah ke teks biasa")
    if not menu1.isdigit():
      print("==============================")
      print("masukan angka bang")
      print("==============================")
      continue
    
    if menu1 != "1" and menu1 != "2" and menu1 != "3":
      print("==============================")
      print("tidak ada pilihan seperti itu")
      print("==============================")
      continue
    
    if menu1 == "1":
      teks1 = input("masukan teks: ")
      hasil = base64.b64encode(teks1.encode()).decode()
      print("=====================================")
      print("hasilnya: ")
      print(hasil)
      print("=====================================")
    if menu1 == "2":
      
      teks = input("masukan teks base64: ")
      hasil = base64.b64decode(teks.encode()).decode()
      print("=====================================")
      print("hasilnya: ")
      print(hasil)
      print("=====================================")
  
  #MENU NOMOR 2
  if menu == "2":
      angka1 = int(input("masukan angka 1: "))
      
      angka2 = int(input("masukan angka 2: "))
      
      perhitungan = input("mau di kali/bagi/kurang/tambah").lower()
      if perhitungan != "kali" and         perhitungan != "bagi" and         perhitungan != "kurang" and       perhitungan != "tambah":
        print("gk ada pilihan itu, Ketik kali atau yang lainnya")
      if perhitungan == "kali":
        print("=====================================")
        print(f"hasilnya : {angka1 * angka2}")
        print("=====================================")
      if perhitungan == "bagi":
        print("=====================================")
        print(f"hasilnya : {angka1 / angka2}")
        print("=====================================")
      if perhitungan == "tambah":
        print("=====================================")
        print(f"hasilnya : {angka1 + angka2}")
        print("=====================================")
      if perhitungan == "kurang":
        print("=====================================")
        print(f"hasilnya : {angka1 - angka2}")
        print("=====================================")
        
  while True:
    if menu == "3":
      tebak = random.randint(1, 10)
    
      tebakan = int(input("masukan angka 1 - 10: "))
      if tebakan > tebak:
        print("kebesaran")
      if tebakan < tebak:
        print("kekecilan")
      if tebakan == tebak:
        print("anda benar")
