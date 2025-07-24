# Tugas 
# Buat program baru, toko.py
# Buat list of dictionary, bernama items
    # key items : nama,stok,harga


# 1.) Isi list of dictionary tersebut sebanyak min  5 item 
barang1={"nama":"pulpen","stok":"40","harga":"8000"}
barang2={"nama":"pensil","stok":"20","harga":"4000"}
barang3={"nama":"buku tulis","stok":"20","harga":"50000"}
barang4={"nama":"penghapus","stok":"16","harga":"3000"}
barang5={"nama":"penggaris","stok":"5","harga":"10000"}

namaBarang = [barang1,barang2,barang3,barang4,barang5]

# 2.) Tampilakan isi dari list of dictionary menggunakan perulangan for atau while 

for i in range (len(namaBarang)):
    print("Nama Barang, No-",i,":",namaBarang[i]["nama"])

# 3.) Buat Function untuk menambahkan item ke list of dictionary 

def creat():
    nama = str(input())
    stok = int(input())
    harga = int(input())
    barang6 = {"nama":nama, "stok":stok,"harga":harga}
    namaBarang.append(barang6)
    
    
creat()
print(namaBarang)

print("Nama\tstok\tharga")
for n in namaBarang:
    print(n["nama"], "\t",n["stok"], "\t",n["harga"])

