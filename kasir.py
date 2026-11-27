# Input
nama_barang = input("Nama barang: ")
harga_satuan = int(input("Harga satuan: "))
jumlah_beli = int(input("Jumlah beli: "))
diskon_persen = float(input("Diskon (%): "))

# Proses
total = harga_satuan * jumlah_beli
diskon = total * diskon_persen / 100
bayar = total - diskon

# Output
print(f"{nama_barang} x{jumlah_beli}")
print(f"Total : Rp{total:,.0f}")
print(f"Diskon: Rp{diskon:,.0f}")
print(f"Bayar : Rp{bayar:,.0f}")
