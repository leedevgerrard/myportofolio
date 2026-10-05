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

## Progress Mingguan

### Minggu 1 - Individual Assignment 1: Static Web with HTML5 and CSS3
- Membuat section About Me dan Achievements menggunakan HTML5 dan CSS3
- Membuat desain responsif yang tetap rapi di tampilan desktop maupun mobile

### Minggu 2 - Individual Assignment 2: Implementasi Model-View-Template (MVT) pada Django
- Membuat section Experience dan Projects menggunakan HTML5 dan CSS3
- Mengimplementasikan MVT pada pengembangan
- Menggunakan unit test untuk pengujian fitur

### Minggu 3 - Individual Assignment 3: Form & Data Delivery
- Membuat form untuk create dan update data
- Membuat fungsi-fungsi pada view untuk mengimplementasikan CRUD pada Experience dan Project
- Menggunakan JSON sebagai format data delivery

### Minggu 4 - Individual Assignment 4: Authentication, Session and Cookies Implementation
- Manajemen authorization dan menambah Editor
- Menambah fitur pemberian star
- Memastikan kemananan API dan data
- Menambahkan halaman project detail dan menambah field Project (fitur tambahan)

### Minggu 5 - Individual Assignment 5: Web Interactivity with JavaScript
- Menampilkan dan menambahkan data dengan AJAX
- Pencarian dengan debouncing
- Menambahkan notifikasi toast
- Mengimplementasikan mitigasi XSS

## Setup & Instalasi

1. Clone repository project ini
```bash
git clone https://github.com/leedevgerrard/myportofolio.git
cd myportofolio
```
2. Buat Python virtual environment
- Windows:
```bash
python -m venv env
```
- Unix (macOS, Linux):
```bash
python3 -m venv env
```
3. Aktifkan Python virtual environment
- Windows:
```bash
env\Scripts\activate
```
- Unix (macOS, Linux):
```bash
source env/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Migrasi database
```bash
python manage.py migrate
```
6. Jalankan server development
```bash
python manage.py runserver
```
Website dapat diakses pada `http://127.0.0.1:8000/`

### Tugas 1

1. Ya, saya menggunakan elemen semantik HTML5. Elemen-elemen semantik memberikan konteks pada suatu konten tertentu pada web, berbeda dengan div yang lebih umum dan tidak memberikan konteks apapun. Penggunaan elemen semantik dapat memudahkan developer dalam membaca dan memahami kode. Selain itu, elemen semantik juga bermanfaat untuk SEO optimization.
2. Membuat halaman web yang tetap responsif menjadi tantangan tersendiri dalam pengembangan proyek ini. Hal ini dikarenakan saya harus memerhatikan tampilan web pada ukuran-ukuran layar yang berbeda, guna menyesuaikan penataan elemen-elemen agar tetap responsif, khususnya pada breakpoint-breakpoint tertentu (media query). Hingga saat ini, ketika transisi dari tampilan desktop ke mobile, saat tata letak mulai terasa janggal, saya akan melakukan penyesuaian-penyesuaian. Hal-hal yang saya perhatikan dan prioritaskan adalah ukuran font (ukuran font biasanya saya buat lebih kecil pada tampilan mobile) dan juga flex-direction (biasanya row saat di tampilan desktop dan column saat di tampilan mobile).
3. Saya merasakan bahwa static web hanya bisa menampilkan data statis saja sesuai dengan apa yang kita tuliskan di HTML, sehingga untuk beberapa hal, seperti penyajian achievements, seluruh data achievements harus dituliskan satu per satu secara manual. Untuk iterasi berikutnya, saya ingin menerapkan konsep MVT agar pembuatan web lebih efisien dan rapi.

### Tugas 2

1. Ketika user, melalui browser, mengakses halaman portofolio baru, yakni halaman projects, request HTTP akan diteruskan oleh portofolio/urls.py (level proyek) ke aplikasi yang tepat, yakni main/urls.py (level aplikasi), karena endpoint yang diakses memiliki awalan "" dan bukan "admin/". Pada routing yang terdapat di main/urls.py, karena endpoint berupa "project/", maka view show_project dipanggil. Views show_project() (yang didefinisikan pada main/views.py) menerima request. Kemudian, views mengambil data seluruh project dari database sesuai dengan model Project (yang didefinisikan pada main/models.py dan berperan sebagai blueprint data) dan menyimpannya di context. Setelah itu, views me-render template project.html dan mengganti seluruh template variable dengan data dari context yang sesuai, kemudian mengirimnya ke browser.
2. Karena dengan adanya prinsip separation of concern pada MVT Django, masing-masing dari model, view, dan template sudah memiliki tanggung jawab dan perannya masing-masing. Model berperan untuk mengatur data, sedangkan template berperan untuk menampilkan data melalui tampilan HTML. Jika hal tersebut dicampurkan, misal data langsung dituliskan pada template, maka akan menjadi tidak efisien dan juga sulit untuk pengembangan berkelanjutannya. Hal ini dikarenakan jika terdapat data yang ingin diubah, maka kode template harus diubah juga. Berbeda jika menggunakan model, bila ingin mengganti data tertentu, cukup mengubah data di database, kemudian template akan dengan otomatis menampilkan data secara dinamis.
3. Fungsi makemigrations membuat file migrasi yang berisi perubahan model, namun belum diaplikasikan ke database. Sedangkan fungsi migrate mengaplikasikan perubahan model yang tercantum dalam file migrasi ke database sehingga database sinkron dengan model terbaru. Setiap terdapat perubahan pada model, maka harus dilakukan migrasi dengan menjalankan kedua fungsi tersebut. Contohnya adalah ketika mengubah atau menambah atribut pada model, seperti ketika saya menambahkan atribut start_date dan end_date pada class Experience di main/models.py.

### Tugas 3

1. Penggunaan Modelform dikarenakan ModelForm jelas memudahkan kita dalam membuat mekanisme form dibanding harus membuatnya secara manual. Dengan ModelForm, form kita akan langsung terintegrasi dengan model dan database, sehingga kita tidak perlu mendefinisikan ulang field-field yang diinginkan secara manual dan juga melakukan validasi dasar secara manual, tetapi kita tetap bisa memodifikasinya melalui class Meta. Kemudian, kita diwajibkan menambahkan {% csrf_token %} untuk meningkatkan keamanan web khususnya untuk memitigasi Cross-Site Request Forgery. Singkatnya CSRF Token tersebut digunakan sebagai fitur keamanan tambahan untuk memastikan request yang dikirimkan merupakan request sah yang memang berasal dari aplikasi kita berdasarkan intensi kita secara sadar.
2. Karena JSON lebih relevan dengan kebutuhan aplikasi web modern dan JSON memberikan kemudahan. Beberapa keunggulan JSON dibanding XML antara lain formatnya yang lebih sederhana, sangat cocok dengan JavaScript (karena sangat mirip dengan object di JavaScript), dan dapat digunakan oleh banyak bahasa pemrograman. Sedangkan XML lebih banyak digunakan untuk sistem enterprise dan legacy karena bersifat lebih kompleks.
3. Ketika view menerima HTTP request, view akan mengambil data dari database. Data yang dikirimkan dari database tersebut secara default berbentuk QuerySet yang berisi Django Model Instance. Untuk memudahkan transmisi data dan agar sesuai dengan format standar, maka dilakukanlah serialization terhadap data tersebut menjadi format JSON. Kemudian, JSON tersebut oleh fungsi lain pada view akan di-deserialize agar kemudian dapat digunakan datanya di template dengan mudah.

### Tugas 5

1. Debouncing adalah sebuah teknik untuk menunda eksekusi suatu fungsi hingga beberapa saat setelah event terakhir terjadi. Dalam hal fitur pencarian yang menggunakan AJAX, mekanismenya adalah setiap kali user mengetikkan suatu karakter baru tanpa jeda, timer akan selalu di-reset. Fungsi yang mengirim request baru akan dijalankan saat user berhenti mengetik dan terdapat jeda waktu yang berlalu sesuai dengan yang sudah di-set. Teknik ini penting untuk diterapkan pada pencarian yang menggunakan AJAX karena akan mencegah request dikirimkan setiap user mengetik satu karakter. Teknik ini juga membantu untuk meringankan beban server dan database serta menghindari race condition.
2. Saat menggunakan fetch(), await dibutuhkan karena fetch() merupakan fungsi asynchronous, yang mana fetch() tidak langsung mengembalikan Response, melainkan mengembalikan Promise, yakni objek yang merepresentasikan hasil dari operasi asynchronous yang belum selesai. Dalam hal ini, await memiliki fungsi untuk menunggu Promise dari fetch() selesai, kemudian memberikan Response yang diminta. Jika kita tidak menggunakan await pada fetch(), maka jika kita menampung hasil dari fetch() pada sebuah variable, variable tersebut akan berisi Promise, bukan Response. Hal tersebut tentu dapat menimbulkan error di kode-kode berikutnya dan membuat kode tidak berjalan sebagaimana mestinya.
3. XSS (Cross-Site Scripting) sederhananya adalah sebuah serangan di mana attacker menyusupkan script JavaScript berbahaya ke suatu web dan script tersebut dijalankan oleh browser korban ketika mengakses web tersebut. XSS memiliki tiga jenis utama, yakni reflected XSS, stored XSS, dan DOM-based XSS. Data yang ditampilkan melalui template Django akan relatif aman dari serangan ini karena template Django akan secara default melakukan HTML escaping. Sedangkan ketika kita menggunakan AJAX/JavaScript, upaya pencegahan XSS harus dilakukan secara manual, sehingga jika kita lalai dalam mengimplementasikan fitur keamanannya, data yang ditampilkan melalui AJAX/JavaScript ini akan lebih rentan terhadap serangan XSS. Upaya untuk mencegah XSS jika kita menggunakan AJAX/JavaScript antara lain melakukan escaping manual dan membersihkan input di server.

## AI Disclosure

AI, berupa chatbot, hanya saya gunakan murni sebagai asisten yang bisa diajak berdiskusi. AI chatbot (ChatGPT) saya gunakan untuk menanyakan hal-hal terkait properti CSS, best practices, troubleshooting, dan mempelajari suatu hal baru. Saya tidak melakukan copy paste dari AI dan selalu mengevaluasi jawaban dari AI.

### AI Tools
- ChatGPT

### Strategi Prompting
- Properti CSS: Saya menjelaskan konsep dan ide desain saya, kemudian menanyakan properti CSS apa yang cocok untuk implementasinya. Jawaban dari AI biasanya berupa penjelasan mengenai properti tertentu yang kemudian saya jadikan pembelajaran.
- Best practice: Saya menjelaskan mengenai konsep dan ide yang ingin saya implementasikan, kemudian menanyakan bagaimana best practice untuk implementasinya. AI akan menjelaskan best practice nya dan kemudian saya terapkan secara mandiri.
- Troubleshooting: Jika terdapat error atau permasalahan terkait Django, biasanya saya menjelaskan kejadiannya serta berdiskusi mengenai jalan keluarnya dengan AI.

### Disclosure

Format:
`id` / `index tugas/tutorial` - `deskripsi singkat` : `tautan ke chat`
#### 001 / 3 - Widget ModelForm & best practice HTTP method : [tautan ke chat](https://chatgpt.com/share/6ab15a5a-5430-83ec-9907-7e3152ab390f)
#### 002 / 3 - Penjelasan properti CSS flex-wrap : [tautan ke chat](https://chatgpt.com/share/6ab15be9-e360-83ec-947f-de3f18c15e11)
#### 003 / 3 - Format data default dari database pada Django : [tautan ke chat](https://chatgpt.com/share/6ab15b31-c574-83ec-b0e2-7741938130c1)
#### 004 / 4 - Django group dan permission : [tautan ke chat](https://chatgpt.com/share/6aba8509-7510-83ec-9fbd-1cbcf37588a4)
#### 005 / 4 - Troubleshooting ModelForm : [tautan ke chat](https://chatgpt.com/share/6aba8590-ae68-83ec-afe8-77d077e3aea8)
#### 006 / 5 - Date Formatting JavaScript : [tautan ke chat](https://chatgpt.com/share/6ac36ae1-73dc-83ec-8a4b-fcbdc752e223)