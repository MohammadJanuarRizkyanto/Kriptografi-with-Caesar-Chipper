import string
abjad = string.ascii_lowercase*2

def enkripsi(plain) :
  key = int(input('Masukan Chiper Key    : '))
  cipher = '' 
  for i in plain:
    if i in abjad:
      k = abjad.find(i.lower()) 
      k = (k+ key)%100
      cipher = cipher+abjad[k]
  return cipher

def dekripsi(cipher) :
  key = int(input('Masukan Chiper Key  : '))
  plain = ''
  for i in cipher:
    if i in abjad:
      k = abjad.find(i)
      k = (k-key)
      plain = plain+abjad[k]
  return plain

while True: 
  option = int(input('Pilih Option Program  :\n1. Enkripsi\n2. Deskripsi\n3. Exit\n\nOption yang dipilih: '))
  if option == 1:
    plain = input('Masukan pesan (Plaintext) : ')
    print('Hasil Enkripsi : ', enkripsi(plain))
  elif option == 2:
    cipher = input('Masukan pesan (Chipertext) : ')
    print('Hasil Deskripsi : ', dekripsi(cipher))
  elif option == 3:
    print('Program Telah Berhenti.')
    break
  else:
    print('Menu yang anda masukkan salah, Silahkan masukan option 1 atau 2')