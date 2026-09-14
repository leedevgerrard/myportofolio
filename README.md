Nama : Lee Devin Gerrard

NPM : 2506548452

Kelas : PBP E

# Website Portofolio Pribadi

Website ini merupakan website portofolio pribadi yang dibuat untuk memenuhi tugas mata kuliah PBP. Website ini berisi informasi mengenai profil, pencapaian, pengalaman, dan proyek saya pribadi.

## Fitur

- Profile / About Me
- Achievement section
- Experience page
- Projects page
- Responsive design

## Tech Stack

### Backend
- Django
- Python

### Frontend
- HTML
- CSS

### Database
- SQLite / PostgreSQL

## Setup Mingguan

### Minggu 1 - Individual Assignment 1: Static Web with HTML5 and CSS3
- Membuat section About Me dan Achievements menggunakan HTML5 dan CSS3
- Membuat desain responsif yang tetap rapi di tampilan desktop maupun mobile

### Minggu 2 - Individual Assignment 2: Implementasi Model-View-Template (MVT) pada Django
- Membuat section Experience dan Projects menggunakan HTML5 dan CSS3
- Mengimplementasikan MVT pada pengembangan
- Menggunakan unit test untuk pengujian fitur

### Tugas 1

1. Ya, saya menggunakan elemen semantik HTML5. Elemen-elemen semantik memberikan konteks pada suatu konten tertentu pada web, berbeda dengan div yang lebih umum dan tidak memberikan konteks apapun. Penggunaan elemen semantik dapat memudahkan developer dalam membaca dan memahami kode. Selain itu, elemen semantik juga bermanfaat untuk SEO optimization.
2. Membuat halaman web yang tetap responsif menjadi tantangan tersendiri dalam pengembangan proyek ini. Hal ini dikarenakan saya harus memerhatikan tampilan web pada ukuran-ukuran layar yang berbeda, guna menyesuaikan penataan elemen-elemen agar tetap responsif, khususnya pada breakpoint-breakpoint tertentu (media query). Hingga saat ini, ketika transisi dari tampilan desktop ke mobile, saat tata letak mulai terasa janggal, saya akan melakukan penyesuaian-penyesuaian. Hal-hal yang saya perhatikan dan prioritaskan adalah ukuran font (ukuran font biasanya saya buat lebih kecil pada tampilan mobile) dan juga flex-direction (biasanya row saat di tampilan desktop dan column saat di tampilan mobile).
3. Saya merasakan bahwa static web hanya bisa menampilkan data statis saja sesuai dengan apa yang kita tuliskan di HTML, sehingga untuk beberapa hal, seperti penyajian achievements, seluruh data achievements harus dituliskan satu per satu secara manual. Untuk iterasi berikutnya, saya ingin menerapkan konsep MVT agar pembuatan web lebih efisien dan rapi.

### Tugas 2

1. Ketika user, melalui browser, mengakses halaman portofolio baru, yakni halaman projects, request HTTP akan diteruskan oleh portofolio/urls.py (level proyek) ke aplikasi yang tepat, yakni main/urls.py (level aplikasi), karena endpoint yang diakses memiliki awalan "" dan bukan "admin/". Pada routing yang terdapat di main/urls.py, karena endpoint berupa "project/", maka view show_project dipanggil. Views show_project() (yang didefinisikan pada main/views.py) menerima request. Kemudian, views mengambil data seluruh project dari database sesuai dengan model Project (yang didefinisikan pada main/models.py dan berperan sebagai blueprint data) dan menyimpannya di context. Setelah itu, views me-render template project.html dan mengganti seluruh template variable dengan data dari context yang sesuai, kemudian mengirimnya ke browser.
2. Karena dengan adanya prinsip separation of concern pada MVT Django, masing-masing dari model, view, dan template sudah memiliki tanggung jawab dan perannya masing-masing. Model berperan untuk mengatur data, sedangkan template berperan untuk menampilkan data melalui tampilan HTML. Jika hal tersebut dicampurkan, misal data langsung dituliskan pada template, maka akan menjadi tidak efisien dan juga sulit untuk pengembangan berkelanjutannya. Hal ini dikarenakan jika terdapat data yang ingin diubah, maka kode template harus diubah juga. Berbeda jika menggunakan model, bila ingin mengganti data tertentu, cukup mengubah data di database, kemudian template akan dengan otomatis menampilkan data secara dinamis.
3. Fungsi makemigrations membuat file migrasi yang berisi perubahan model, namun belum diaplikasikan ke database. Sedangkan fungsi migrate mengaplikasikan perubahan model yang tercantum dalam file migrasi ke database sehingga database sinkron dengan model terbaru. Setiap terdapat perubahan pada model, maka harus dilakukan migrasi dengan menjalankan kedua fungsi tersebut. Contohnya adalah ketika mengubah atau menambah atribut pada model, seperti ketika saya menambahkan atribut start_date dan end_date pada class Experience di main/models.py.

## AI Disclosure

AI, berupa chatbot, hanya saya gunakan murni sebagai asisten yang bisa diajak berdiskusi. AI chatbot (ChatGPT) saya gunakan untuk menanyakan hal-hal terkait properti CSS, best practices, dan troubleshooting. Saya tidak melakukan copy paste dari AI dan selalu mengevaluasi jawaban dari AI.

### AI Tools
- ChatGPT

### Strategi Prompting
- Properti CSS: Saya menjelaskan konsep dan ide desain saya, kemudian menanyakan properti CSS apa yang cocok untuk implementasinya. Jawaban dari AI biasanya berupa penjelasan mengenai properti tertentu yang kemudian saya jadikan pembelajaran.
- Best practice: Saya menjelaskan mengenai konsep dan ide yang ingin saya implementasikan, kemudian menanyakan bagaimana best practice untuk implementasinya. AI akan menjelaskan best practice nya dan kemudian saya terapkan secara mandiri.
- Troubleshooting: Jika terdapat error atau permasalahan terkait Django, biasanya saya menjelaskan kejadiannya serta berdiskusi mengenai jalan keluarnya dengan AI.