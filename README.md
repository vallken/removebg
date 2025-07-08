
▶️ Menjalankan API

```
python app.py

Akses akan tersedia di:

http://localhost:5000
```


📤 Penggunaan API

Endpoint: /remove

Metode: POST
Form field: image (file)

Contoh dengan curl:
```
curl -X POST -F "image=@foto.jpg" http://localhost:5000/remove --output hasil.png
```

Hasil akan berupa gambar PNG transparan (hasil.png).
