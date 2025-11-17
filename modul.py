def penjumlahan(x, y):
   """Menambahkan dua angka"""
   return x + y

def pengurangan(x, y):
   """Mengurangi dua angka"""
   return x - y

def perkalian(x, y):
   """Mengalikan dua angka"""
   return x * y

def pembagian(x, y):
   """Membagi dua angka. Menangani pembagian oleh nol."""
   if y == 0:
       return "Tidak bisa dibagi dengan nol"
   return x / y

# Menu kalkulator
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari pengguna
while True:
   pilihan = input("Masukkan pilihan(1/2/3/4): ")

   # Memeriksa apakah pilihan valid
   if pilihan in ('1', '2', '3', '4'):
       try:
           angka1 = float(input("Masukkan angka pertama: "))
           angka2 = float(input("Masukkan angka kedua: "))
       except ValueError:
           print("Input tidak valid. Masukkan angka.")
           continue

       if pilihan == '1':
           print(angka1, "+", angka2, "=", penjumlahan(angka1, angka2))

       elif pilihan == '2':
           print(angka1, "-", angka2, "=", pengurangan(angka1, angka2))

       elif pilihan == '3':
           print(angka1, "×", angka2, "=", perkalian(angka1, angka2))

       elif pilihan == '4':
           print(angka1, "÷", angka2, "=", pembagian(angka1, angka2))
       
       lanjut = input("Lanjutkan perhitungan? (ya/tidak): ")
       if lanjut == "tidak":
          break
   else:
       print("Input tidak valid")
       