import mysql.connector as my

# Untuk Koneksi Database
db_conn = {
    'host': 'localhost',
    'username': 'root',
    'password': '',
    'database': 'toko'
}

#Memeriksa apakah database berhasil tersambung atau tidak
try:
    connection = my.connect(**db_conn)
    if connection.is_connected():
        print('Berhasil')
except my.Error as e:
    print(f'Gagal: {e}')

# Fungsi Menambahkan Data
def tambah_data():
    cursor = connection.cursor()

    #Query SQL Menambahkan Data
    insert_query = 'INSERT INTO barang (id, kode_barang, nama_barang, harga, satuan) VALUES (%s, %s, %s, %s, %s)'

    id = input('Masukkan id barang: ')
    kode_barang = input('Masukkan kode barang: ')
    nama_barang = input('Masukan nama barang: ')
    harga = input('Masukan Harga Barang: ')
    satuan = input('Masukan Satuan Barang: ')
    values = (id, kode_barang, nama_barang, harga, satuan)

    try:
        cursor.execute(insert_query, values)
        connection.commit()
        print('Data berhasil ditambahkan')
    except my.Error as e:
        print(f'Error: {e}')

    cursor.close()

#Fungsi Mengambil Data
def ambil_data():
    cursor = connection.cursor()

    #Query SQL Select Data
    select_query = 'SELECT * FROM barang'
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()

#Fungsi Update Data
def update_data():
    cursor = connection.cursor()

    #Query SQL Update Data
    update_query = 'UPDATE barang SET kode_barang = %s, nama_barang = %s, harga = %s, satuan = %s WHERE id = %s'

    id = input('Masukkan id barang yang ingin diubah: ')
    kode_barang = input('Masukkan kode barang baru: ')
    nama_barang = input('Masukan nama barang baru: ')
    harga = input('Masukan Harga Barang baru: ')
    satuan = input('Masukan Satuan Barang baru: ')
    values = (kode_barang, nama_barang, harga, satuan, id)

    try:
        cursor.execute(update_query, values)
        connection.commit()
        print(f'Data berhasil diupdate untuk id: {id}')
    except my.Error as e:
        print(f'Error: {e}')

    cursor.close()

#Fungsi Delete Data
def hapus_data():
    cursor = connection.cursor()
    
    #Query SQL Delete Data
    delete_query = 'DELETE FROM barang WHERE id = %s'
    hapus = input('Masukkan id yang ingin dihapus: ')
    values = (hapus,)

    try:
        cursor.execute(delete_query, values)
        connection.commit()
        print(f'Data berhasil dihapus untuk id: {hapus}')
    except my.Error as e:
        print(f'Error: {e}')

    cursor.close()

#Menu untuk fungsi fungsi
while True:
    user = input('Masukkan fungsi = ')
    if user == 'create':
        tambah_data()
    elif user == 'read':
        ambil_data()
    elif user == 'update':
        update_data()
    elif user == 'delete':
        hapus_data()
    elif user == 'exit':
        break