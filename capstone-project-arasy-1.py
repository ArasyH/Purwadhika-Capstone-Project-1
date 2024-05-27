rental_f1 = [{
        "model": "Ferrari SF-24 EVO",
        "available": True,
        "stock" : 2,
        "price_per_day": 1000
        },
    {
        "model": "Mclaren MCL38",
        "available": True,
        "stock" : 2,
        "price_per_day": 800
    },
    {
        "model": "Red Bull RB20",
        "available": True,
        "stock" : 2,
        "price_per_day": 1250
    },
    {
        "model": "Mercedes W15",
        "available": True,
        "stock" : 2,
        "price_per_day": 700
    },
    {
        "model": "Aston Martin AMR24",
        "available": True,
        "stock" : 2,
        "price_per_day": 700
    }, 
    {
        "model": "RedBull2 VCARB 01",
        "available": True,
        "stock" : 2,
        "price_per_day": 550
    },
    {
        "model": "Alpine A524",
        "available": True,
        "stock" : 2,
        "price_per_day": 500
    },
    {
        "model": "SAUBER Stake C44",
        "available": True,
        "stock" : 2,
        "price_per_day": 350
    },
    {
        "model": "Williams FW46",
        "available": True,
        "stock" : 2,
        "price_per_day": 450
    },
    {
        "model": "HAAS VF-24",
        "available": True,
        "stock" : 2,
        "price_per_day": 400
    }]

#menampung pembelian yang akan digunakan di function return_f1()
cartF1 = [] 

#menampilkan daftar mobil f1 
def daftar_mobilf1(): 
    print("Daftar Rental Mobil F1 Season 2024 \n")
    print('Index\t| Model\t\t\t\t\t| Available\t| Stock\t| Price_per_day')
    print('-' * 88)
    for index in range(len(rental_f1)):
        print('{}\t| {}\t\t\t| {}\t\t| {}\t| {}'.format(index,rental_f1[index]["model"].ljust(14),rental_f1[index]["available"],rental_f1[index]["stock"],rental_f1[index]["price_per_day"]))

#menambah data dict rental_f1
def tambahf1():
    namaF1 = input("Masukkan Nama Model Mobil: ")
    isAvailable = input("Masukkan Ketersediaan (True/False): ").capitalize()
    stockF1 = int(input("Masukkan stock mobil F1: "))
    hargaRental = int(input("Masukkan harga rental perhari: "))
    rental_f1.append({
        'model': namaF1,
        'available': isAvailable,
        'stock': stockF1,
        'price_per_day': hargaRental
    })
    daftar_mobilf1()

#menghapus data mobil f1 berdasarkan index    
def delete_f1():
    daftar_mobilf1()
    indexRentalF1 = int(input("Masukkan index F1 yang ingin dihapus: "))
    del rental_f1[indexRentalF1]
    daftar_mobilf1()


# function proses rental mobil
def rentalmobil_f1():
    daftar_mobilf1()

    listHari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum\'at", "Sabtu", "Minggu"]
    while True:
        indexRentalF1 = int(input("Masukkan index mobil F1 yang ingin dirental: "))
        jmlrentalF1 = int(input("Masukkan jumlah mobil yang ingin di rental: "))
        if (jmlrentalF1 <= rental_f1[indexRentalF1]['stock']) and (jmlrentalF1 > 0):
            hariRental = input("Masukkan hari perentalan :").capitalize()
            lamaRental = int(input("Masukkan lama periode peminjaman (hari): "))
            
            hariRental_indeks = listHari.index(hariRental)
            lamaRental_indeks = (hariRental_indeks + lamaRental) % 7
            hariPengembalian = listHari[lamaRental_indeks]
            cartF1.append({
                'index' : indexRentalF1,
                'model' : rental_f1[indexRentalF1]['model'],
                'available' : rental_f1[indexRentalF1]['available'],
                'stock' : jmlrentalF1,
                'price_per_day' : rental_f1[indexRentalF1]['price_per_day'],
                'duration' : lamaRental,
                'return_day' : hariPengembalian
                
            })
            
        else:
            print("Stock Tidak Cukup, stock {} tersedia {}".format(rental_f1[indexRentalF1]['model'],rental_f1[indexRentalF1]['stock']))
       
        print('Isi Cart :')
        print('Model\t\t\t\t\t| Available\t| Stock\t| Price_per_day')
        print('-' * 80)
        for item in cartF1 :
            print('{}\t\t\t\t| {}\t\t| {}\t| {}'.format(item['model'].ljust(14), item['available'], item['stock'], item['price_per_day']))
        
        checker = input('Mau rental yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Daftar Detail Rental  :')
    print('Model\t\t\t\t\t| Stock\t| Price per Day\t| Durasi Peminjaman \t| Hari Pengembalian')
    totalBiaya = 0
    for item in cartF1 :
        print('{}\t\t\t\t| {}\t| {}\t| {}\t| {}'.format(item['model'].ljust(14), item['stock'], item['price_per_day'], item['duration'], item['return_day']))
        totalBiaya += item['stock'] * item['price_per_day'] * item['duration']    
    
    #konfirmasi pembayaran
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalBiaya))
        jmlUang = int(input('Masukkan jumlah uang : '))
        if(jmlUang > totalBiaya) :
            kembalian = jmlUang - totalBiaya
            print('Terima kasih \n\nUang kembalian Anda : {}'.format(kembalian))
            for item in cartF1 :
                rental_f1[item['index']]['stock'] -= item['stock']
            break
        elif(jmlUang == totalBiaya) :
            print('Terima kasih')
            for item in cartF1 :
                rental_f1[item['index']]['stock'] -= item['stock']
            break
        else :
            kekurangan = totalBiaya - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))

#proses pengembalian mobil yang di rental
def return_F1():
    print('Daftar Mobil yang Sedang Dirental:')
    print('Index\t| Model\t\t\t\t\t| Stock\t| Price_per_day\t| Durasi (hari)\t| Hari Pengembalian')
    print('-' * 110)
    for index, item in enumerate(cartF1):
        print('{}\t| {}\t\t\t\t| {}\t| {}\t\t| {} Hari\t| {}'.format(index, item['model'].ljust(14), item['stock'], item['price_per_day'], item['duration'], item['return_day']))
    indexReturn = int(input('Masukkan index rental yang ingin dikembalikan: '))
    rental_f1[cartF1[indexReturn]['index']]['stock'] += cartF1[indexReturn]['stock']
    del cartF1[indexReturn]
    print('Mobil berhasil dikembalikan.')



def main():
    while True:
        pilihmenu = input('''
        Selamat Datang di Rental Mobil F1 Season 2024

        List Menu:
        1. Menampilkan Daftar Mobil F1
        2. Menambah Mobil F1
        3. Menghapus Mobil F1
        4. Rental F1
        5. Mengembalikan Mobil Rental F1
        6. Exit Program
        
        
        Masukkan menu yang ingin dipilih: ''')
        if (pilihmenu == '1'):
            daftar_mobilf1()
        elif pilihmenu == '2':
            tambahf1()
        elif pilihmenu == '3':
            delete_f1()
        elif pilihmenu == '4':
            rentalmobil_f1()
        elif pilihmenu == '5':
            return_F1()
        elif pilihmenu == '6':
            print("Terima Kasih Sudah Rental di Tempat Kami!")
            break
        else:
            print("PILIHAN TIDAK TEPAT")


main()
