A = [10, 20, 30, 40, 50]

print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terkahir:", A[-1])

A[3] = 100
print("Setelah mengubah elemen ke-4:", A)

A[3:] = [200, 300]
print("Setelah mengubah elemen ke-4 sampai terakhir:", A)

B = A[:2]
print("List B setelah mengambil 2 elemen dari A", B)

B.append("Python")
print("List B setelah menambahkan nilai string:", B)

B.extend([60, 70, 80])
print("List B setelah menambahkan 3", B)

C = B + A
print("Gabungan list B dan A:", C)