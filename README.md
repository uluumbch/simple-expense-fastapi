# simple-expense-fastapi

simple-expense-fastapi adalah REST API berbasis FastAPI yang digunakan untuk mengelola pemasukan dan pengeluaran dalam mata uang Rupiah (IDR). API ini memungkinkan pengguna untuk mencatat, membaca, memperbarui, dan menghapus transaksi keuangan mereka.

## 🚀 Fitur
- **Tambah transaksi** (pemasukan & pengeluaran)
- **Lihat daftar transaksi**
- **Edit transaksi berdasarkan ID**
- **Hapus transaksi berdasarkan ID**
- **Validasi data dengan Pydantic**
- **Dokumentasi otomatis dengan Swagger UI & ReDoc**

## 🛠️ Teknologi yang Digunakan
- **FastAPI** - Framework Python untuk membangun API
- **Firebase Firestore** - Database NoSQL untuk menyimpan transaksi
- **Pydantic** - Validasi data
- **Poetry** - Manajemen dependensi Python

---

## 📌 Cara Menjalankan Proyek

### **1. Clone Repository**
```sh
git clone https://github.com/uluumbch/simple-expense-fastapi.git
cd simple-expense-fastapi
```

### **2. Instal Poetry**
Jika belum menginstal **Poetry**, jalankan:
```sh
pip install poetry
```

### **3. Instal Dependensi**
```sh
poetry install
```

### **4. Konfigurasi Firebase**
- Buat akun di [Firebase](https://firebase.google.com/)
- Buat proyek Firestore
- Unduh file **serviceAccountKey.json** dan simpan di root folder proyek

### **5. Jalankan Server FastAPI**
```sh
poetry run uvicorn main:app --reload
```

Server akan berjalan di `http://127.0.0.1:8000`

Alternatif lain adalah menggunakan Docker dengan bantuan `devcontainer`:
1. Buka project dengan VSCode
2. Install ekstensi `Remote - Containers`
3. Klik ikon `><` di pojok kiri bawah dan pilih `Reopen in Container` atau `Rebuild and Reopen in Container`
4. Tunggu proses build selesai
5. Jalankan perintah untuk menginstall dependensi dan menjalankan server:
   ```sh
   poetry install
   poetry run uvicorn main:app --reload
   ```
6. Server akan berjalan di `http://127.0.0.1:8000`


---

## 🔄 Alur Penggunaan API
1. **Menambahkan Transaksi**
   - Endpoint: `POST /transactions`
   - Contoh Request:
     ```json
     {
       "amount": 10000,
       "category": "Makan",
       "type": "income",
       "description": "Gaji bulan Maret",
       "date": "2025-03-13T14:15:22Z"
     }
     ```
   - Respon:
     ```json
     {
       "message": "Transaction added successfully",
       "transaction_id": "abc123"
     }
     ```

2. **Melihat Semua Transaksi**
   - Endpoint: `GET /transactions`
   - Respon:
     ```json
     [
       {
         "transaction_id": "abc123",
         "amount": 10000,
         "category": "Makan",
         "type": "income",
         "description": "Gaji bulan Maret",
         "date": "2025-03-13T14:15:22Z"
       }
     ]
     ```

3. **Melihat Transaksi Berdasarkan ID**
   - Endpoint: `GET /transactions/{transaction_id}`

4. **Mengedit Transaksi**
   - Endpoint: `PUT /transactions/{transaction_id}`
   - Contoh Request:
     ```json
     {
       "amount": -5000,
       "category": "Makan",
       "type": "expense",
       "description": "Makan malam di restoran",
       "date": "2025-03-13T14:15:22Z"
     }
     ```

5. **Menghapus Transaksi**
   - Endpoint: `DELETE /transactions/{transaction_id}`

6. **Melihat Jumlah Saldo**
   - Endpoint: `GET /balance`
   - Respon:
     ```json
     {
       "balance": 5000
     }
     ```
---

## 📖 Dokumentasi API
Setelah menjalankan server, dokumentasi API tersedia di:
- **Swagger UI** → [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
- **ReDoc** → [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)

---

## 📌 Lisensi
Proyek ini menggunakan lisensi **MIT**.

---

💡 **Dibuat dengan ❤️ menggunakan FastAPI dan Firebase Firestore!** 🚀

