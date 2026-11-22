from flask import Flask, render_template, request, redirect, url_for, session
import json, os

app = Flask(__name__)
app.secret_key = "tania-secret-123"

DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    return {
        "nama": "Tania",
        "tentang": "Ga banyak yang tau tentang aku, bahkan aku sendiri kadang bingung sama diriku sendiri. Tapi yang pasti, aku suka hal-hal kecil yang bikin bahagia.",
        "skills": ["Python", "HTML", "Canva"],
        "projects": [{"judul": "Website Portofolio", "deskripsi": "Website portofolio pribadi"}],
        "experience": [{"judul": "Asisten Praktikum", "deskripsi": "Membantu praktikum kampus"}],
        "education": [{"judul": "Universitas", "deskripsi": "Mahasiswa"}]
    }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', nama=data['nama'], skills=data['skills'], projects=[p['judul'] for p in data['projects']], data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['login'] = True
            return redirect(url_for('dashboard'))
        else:
            return "Username / Password Salah! <a href='/login'>Coba lagi</a>"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('login'):
        return redirect(url_for('login'))
    data = load_data()
    return render_template('dashboard.html', data=data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# CRUD - Tambah
@app.route('/tambah/<kategori>', methods=['POST'])
def tambah(kategori):
    if not session.get('login'):
        return redirect(url_for('login'))
    data = load_data()
    judul = request.form.get('judul', '').strip()
    deskripsi = request.form.get('deskripsi', '').strip()
    # Validasi - tidak boleh kosong
    if not judul or not deskripsi:
        return "Gagal! Judul dan Deskripsi tidak boleh kosong! <a href='/dashboard'>Kembali</a>"
    if kategori == 'skills':
        if not judul:
            return "Skill tidak boleh kosong! <a href='/dashboard'>Kembali</a>"
        data['skills'].append(judul)
    else:
        data[kategori].append({"judul": judul, "deskripsi": deskripsi})
    save_data(data)
    return redirect(url_for('dashboard'))

# CRUD - Hapus
@app.route('/hapus/<kategori>/<int:index>')
def hapus(kategori, index):
    if not session.get('login'):
        return redirect(url_for('login'))
    data = load_data()
    try:
        del data[kategori][index]
        save_data(data)
    except:
        pass
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)