from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "id": 1,
        "title": "Web Portofolio Pribadi",
        "description": "Website portofolio interaktif dengan desain modern dan responsif untuk memperkenalkan diri sebagai mahasiswa Informatika.",
        "tech": ["HTML", "CSS", "Flask", "Python"],
        "category": "Web Dev"
    },
    {
        "id": 2,
        "title": "Analisis UI/UX Aplikasi Kampus",
        "description": "Studi kasus dan analisis antarmuka aplikasi akademik kampus, dilengkapi dengan rekomendasi perbaikan desain menggunakan prinsip UX.",
        "tech": ["Figma", "UX Research", "Data Analysis"],
        "category": "Analysis"
    },
    {
        "id": 3,
        "title": "Sistem Informasi Data Mahasiswa",
        "description": "Aplikasi CRUD sederhana untuk mengelola data mahasiswa baru, dilengkapi fitur pencarian dan validasi input.",
        "tech": ["Flask", "SQLite", "Python", "Bootstrap"],
        "category": "Database"
    },
    {
        "id": 4,
        "title": "Laporan Data Statistik Publik",
        "description": "Proyek analisis data sederhana menggunakan Python untuk mengolah dan memvisualisasikan data statistik ke dalam bentuk grafik yang mudah dipahami.",
        "tech": ["Python", "Pandas", "Matplotlib"],
        "category": "Data Science"
    },
    {
        "id": 5,
        "title": "Dokumentasi Proyek Organisasi",
        "description": "Penyusunan dokumentasi teknis dan panduan pengguna (user guide) untuk proyek web organisasi mahasiswa kampus menggunakan Markdown.",
        "tech": ["Markdown", "Technical Writing", "Git"],
        "category": "Documentation"
    },
    {
        "id": 6,
        "title": "Landing Page Event Kampus",
        "description": "Halaman promosi dan pendaftaran untuk acara seminar kampus, dirancang dengan desain yang menarik dan ramah pengguna.",
        "tech": ["HTML", "CSS", "JavaScript", "Figma"],
        "category": "Web Design"
    }
]

SKILLS_DATA = [
    {"name": "HTML & CSS", "level": 85},
    {"name": "Analisis & Pemecahan Masalah", "level": 80},
    {"name": "Python & Flask", "level": 75},
    {"name": "UI/UX & Desain (Figma)", "level": 70},
    {"name": "Git & Dokumentasi", "level": 65},
    {"name": "Data Analysis (Pandas)", "level": 50}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html", skills=SKILLS_DATA)

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
