import os
import uuid

def create_node(node_id, value, style, x, y, w, h):
    return f"""            <mxCell id="{node_id}" value="{value}" style="{style}" vertex="1" parent="1">
                <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>
            </mxCell>"""

def create_edge(edge_id, source, target, value=""):
    return f"""            <mxCell id="{edge_id}" value="{value}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="{source}" target="{target}">
                <mxGeometry relative="1" as="geometry"/>
            </mxCell>"""

def create_decision_edge(edge_id, source, target, value, exit_point="1"):
    # exit_point: 1=bottom, 0.5=right (approx)
    exit_attr = "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" if value == "T" else "exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;"
    if value == "T" and exit_point == "right":
        exit_attr = "exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;"

    return f"""            <mxCell id="{edge_id}" value="{value}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;{exit_attr}" edge="1" parent="1" source="{source}" target="{target}">
                <mxGeometry relative="1" as="geometry">
                    <mxPoint as="offset"/>
                </mxGeometry>
            </mxCell>"""

def wrap_drawio(name, content):
    return f"""<mxfile host="65bd71144e">
    <diagram id="{uuid.uuid4()}" name="{name}">
        <mxGraphModel dx="1000" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
{content}
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>"""

# Styles
ST_START = "ellipse;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;"
ST_PROCESS = "whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;"
ST_DECISION = "rhombus;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;"
ST_IO = "shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fixedSize=1;fillColor=none;strokeColor=#000000;"

def generate_manual_system():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Pelanggan datang / Hubungi via Telepon", ST_IO, 290, 120, 200, 60))
    nodes.append(create_node("n3", "Tanya ketersediaan jadwal", ST_PROCESS, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Cek buku jadwal manual", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Jadwal Tersedia?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Informasikan jadwal penuh", ST_IO, 520, 430, 140, 60))
    nodes.append(create_node("n7", "Catat booking di buku besar", ST_PROCESS, 320, 540, 140, 60))
    nodes.append(create_node("n8", "Pembayaran (DP/Cash)", ST_IO, 320, 640, 140, 60))
    nodes.append(create_node("n9", "Selesai", ST_START, 350, 740, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n7", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n6", "T"))
    edges.append(create_edge("e7", "n7", "n8"))
    edges.append(create_edge("e8", "n8", "n9"))
    edges.append(create_edge("e9", "n6", "n9"))

    return wrap_drawio("Sistem Manual", "\n".join(nodes + edges))

def generate_new_system():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Akses Website Boking Rias", ST_IO, 300, 120, 180, 60))
    nodes.append(create_node("n3", "Cari & Pilih Layanan Rias", ST_PROCESS, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Cek Jadwal Otomatis", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Isi Form Booking & Checkout", ST_IO, 320, 420, 140, 60))
    nodes.append(create_node("n6", "Lakukan Pembayaran DP", ST_PROCESS, 320, 520, 140, 60))
    nodes.append(create_node("n7", "Upload Bukti Pembayaran", ST_IO, 320, 620, 140, 60))
    nodes.append(create_node("n8", "Verifikasi oleh Admin", ST_DECISION, 330, 720, 120, 80))
    nodes.append(create_node("n9", "Konfirmasi Booking Berhasil", ST_IO, 320, 840, 140, 60))
    nodes.append(create_node("n10", "Selesai", ST_START, 350, 940, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_edge("e5", "n5", "n6"))
    edges.append(create_edge("e6", "n6", "n7"))
    edges.append(create_edge("e7", "n7", "n8"))
    edges.append(create_decision_edge("e8", "n8", "n9", "Y"))
    edges.append(create_edge("e9", "n9", "n10"))

    return wrap_drawio("Sistem Baru", "\n".join(nodes + edges))

def generate_login():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Halaman Login", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Masukkan Username & Password", ST_IO, 290, 220, 200, 60))
    nodes.append(create_node("n4", "Login", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Validasi?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Tampil Pesan Kesalahan", ST_IO, 150, 520, 160, 60))
    nodes.append(create_node("n7", "Beranda", ST_IO, 450, 520, 140, 60))
    nodes.append(create_node("n8", "Menu", ST_PROCESS, 450, 620, 140, 60))
    nodes.append(create_node("n9", "Login Gagal", ST_DECISION, 170, 620, 120, 80))
    nodes.append(create_node("n10", "Selesai", ST_START, 350, 750, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n7", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n6", "T"))
    edges.append(create_edge("e7", "n7", "n8"))
    edges.append(create_edge("e8", "n8", "n10"))
    edges.append(create_edge("e9", "n6", "n9"))
    edges.append(create_decision_edge("e10", "n9", "n10", "Y"))

    # Custom edge for T back to login
    edges.append(f"""            <mxCell id="e11" value="T" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n2">
                <mxGeometry relative="1" as="geometry">
                    <mxPoint x="100" y="300" as="targetPoint"/>
                </mxGeometry>
            </mxCell>""")

    return wrap_drawio("Login", "\n".join(nodes + edges))

def generate_registrasi():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Halaman Registrasi", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Input Nama, Email, No HP, Password", ST_IO, 280, 220, 220, 60))
    nodes.append(create_node("n4", "Klik Daftar", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Data Valid?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Simpan User Baru ke DB", ST_PROCESS, 320, 540, 140, 60))
    nodes.append(create_node("n7", "Tampil Pesan Error", ST_IO, 520, 430, 140, 60))
    nodes.append(create_node("n8", "Registrasi Berhasil", ST_IO, 320, 640, 140, 60))
    nodes.append(create_node("n9", "Selesai", ST_START, 350, 740, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n6", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n7", "T"))
    edges.append(create_edge("e7", "n6", "n8"))
    edges.append(create_edge("e8", "n8", "n9"))
    edges.append(create_edge("e9", "n7", "n2"))

    return wrap_drawio("Registrasi", "\n".join(nodes + edges))

def generate_pencarian():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Halaman Katalog / Cari", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Input Kata Kunci / Pilih Kategori", ST_IO, 290, 220, 200, 60))
    nodes.append(create_node("n4", "Sistem Mencari Data Layanan", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Data Ditemukan?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Tampilkan Daftar Layanan", ST_IO, 320, 540, 140, 60))
    nodes.append(create_node("n7", "Tampil Pesan 'Tidak Ditemukan'", ST_IO, 520, 430, 160, 60))
    nodes.append(create_node("n8", "Pilih Layanan", ST_PROCESS, 320, 640, 140, 60))
    nodes.append(create_node("n9", "Tampil Detail Layanan", ST_IO, 320, 740, 140, 60))
    nodes.append(create_node("n10", "Selesai", ST_START, 350, 840, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n6", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n7", "T"))
    edges.append(create_edge("e7", "n6", "n8"))
    edges.append(create_edge("e8", "n8", "n9"))
    edges.append(create_edge("e9", "n9", "n10"))
    edges.append(create_edge("e10", "n7", "n3"))

    return wrap_drawio("Pencarian", "\n".join(nodes + edges))

def generate_booking():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Halaman Detail Produk", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Klik Tombol Booking", ST_PROCESS, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Pilih Tanggal & Jam", ST_IO, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Jadwal Tersedia?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Isi Form Data Pemesan", ST_IO, 320, 540, 140, 60))
    nodes.append(create_node("n7", "Tampil Notifikasi Jadwal Penuh", ST_IO, 520, 430, 180, 60))
    nodes.append(create_node("n8", "Klik Pesan Sekarang", ST_PROCESS, 320, 640, 140, 60))
    nodes.append(create_node("n9", "Data Booking Tersimpan", ST_PROCESS, 320, 740, 140, 60))
    nodes.append(create_node("n10", "Ke Halaman Pembayaran", ST_IO, 320, 840, 140, 60))
    nodes.append(create_node("n11", "Selesai", ST_START, 350, 940, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n6", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n7", "T"))
    edges.append(create_edge("e7", "n6", "n8"))
    edges.append(create_edge("e8", "n8", "n9"))
    edges.append(create_edge("e9", "n9", "n10"))
    edges.append(create_edge("e10", "n10", "n11"))
    edges.append(create_edge("e11", "n7", "n4"))

    return wrap_drawio("Booking", "\n".join(nodes + edges))

def generate_pembayaran():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Lihat Instruksi Pembayaran", ST_IO, 300, 120, 180, 60))
    nodes.append(create_node("n3", "Transfer ke Rekening Bank", ST_PROCESS, 310, 220, 160, 60))
    nodes.append(create_node("n4", "Buka Halaman Konfirmasi", ST_PROCESS, 310, 320, 160, 60))
    nodes.append(create_node("n5", "Upload Foto Bukti Bayar", ST_IO, 320, 420, 140, 60))
    nodes.append(create_node("n6", "Klik Kirim", ST_PROCESS, 350, 520, 80, 40))
    nodes.append(create_node("n7", "Status Booking: Menunggu Verifikasi", ST_IO, 280, 600, 220, 60))
    nodes.append(create_node("n8", "Selesai", ST_START, 350, 700, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_edge("e5", "n5", "n6"))
    edges.append(create_edge("e6", "n6", "n7"))
    edges.append(create_edge("e7", "n7", "n8"))

    return wrap_drawio("Pembayaran", "\n".join(nodes + edges))

def generate_verifikasi_admin():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Admin Login & Buka Dashboard", ST_PROCESS, 290, 120, 200, 60))
    nodes.append(create_node("n3", "Buka Menu Pemesanan", ST_PROCESS, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Cek Detail & Bukti Pembayaran", ST_IO, 290, 320, 200, 60))
    nodes.append(create_node("n5", "Bukti Valid?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Setuju & Verifikasi", ST_PROCESS, 320, 540, 140, 60))
    nodes.append(create_node("n7", "Tolak & Minta Upload Ulang", ST_PROCESS, 520, 430, 160, 60))
    nodes.append(create_node("n8", "Update Status Jadi 'Lunas/DP'", ST_PROCESS, 300, 640, 180, 60))
    nodes.append(create_node("n9", "Kirim Notifikasi ke Pelanggan", ST_IO, 310, 740, 160, 60))
    nodes.append(create_node("n10", "Selesai", ST_START, 350, 840, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n6", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n7", "T"))
    edges.append(create_edge("e7", "n6", "n8"))
    edges.append(create_edge("e8", "n8", "n9"))
    edges.append(create_edge("e9", "n9", "n10"))
    edges.append(create_edge("e10", "n7", "n10"))

    return wrap_drawio("Verifikasi Admin", "\n".join(nodes + edges))

def generate_kelola_produk():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Menu Produk", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Klik Tambah Produk", ST_PROCESS, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Input Nama, Harga, Deskripsi", ST_IO, 290, 320, 200, 60))
    nodes.append(create_node("n5", "Upload Foto Produk", ST_IO, 320, 420, 140, 60))
    nodes.append(create_node("n6", "Simpan", ST_PROCESS, 350, 520, 80, 40))
    nodes.append(create_node("n7", "Tampil di Katalog Website", ST_IO, 310, 600, 160, 60))
    nodes.append(create_node("n8", "Selesai", ST_START, 350, 700, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_edge("e5", "n5", "n6"))
    edges.append(create_edge("e6", "n6", "n7"))
    edges.append(create_edge("e7", "n7", "n8"))

    return wrap_drawio("Kelola Produk", "\n".join(nodes + edges))

def generate_laporan():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Menu Laporan", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Pilih Periode Laporan", ST_IO, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Klik Filter/Cari", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Sistem Mengambil Data Transaksi", ST_PROCESS, 290, 420, 200, 60))
    nodes.append(create_node("n6", "Tampilkan Rekap Laporan", ST_IO, 310, 520, 160, 60))
    nodes.append(create_node("n7", "Cetak / Export PDF", ST_PROCESS, 320, 620, 140, 60))
    nodes.append(create_node("n8", "Selesai", ST_START, 350, 720, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_edge("e5", "n5", "n6"))
    edges.append(create_edge("e6", "n6", "n7"))
    edges.append(create_edge("e7", "n7", "n8"))

    return wrap_drawio("Laporan", "\n".join(nodes + edges))

def generate_pembatalan():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Buka Riwayat Booking", ST_PROCESS, 310, 120, 160, 60))
    nodes.append(create_node("n3", "Pilih Booking Aktif", ST_IO, 320, 220, 140, 60))
    nodes.append(create_node("n4", "Klik Batalkan Pesanan", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Konfirmasi Pembatalan?", ST_DECISION, 330, 420, 120, 80))
    nodes.append(create_node("n6", "Update Status: Dibatalkan", ST_PROCESS, 310, 540, 160, 60))
    nodes.append(create_node("n7", "Batal Dibatalkan", ST_IO, 520, 430, 140, 60))
    nodes.append(create_node("n8", "Selesai", ST_START, 350, 650, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_decision_edge("e5", "n5", "n6", "Y"))
    edges.append(create_decision_edge("e6", "n5", "n7", "T"))
    edges.append(create_edge("e7", "n6", "n8"))
    edges.append(create_edge("e8", "n7", "n8"))

    return wrap_drawio("Pembatalan", "\n".join(nodes + edges))

def generate_ulasan():
    nodes = []
    nodes.append(create_node("n1", "Mulai", ST_START, 350, 40, 80, 40))
    nodes.append(create_node("n2", "Acara Rias Selesai", ST_PROCESS, 320, 120, 140, 60))
    nodes.append(create_node("n3", "Buka Riwayat Pemesanan", ST_PROCESS, 310, 220, 160, 60))
    nodes.append(create_node("n4", "Klik Beri Ulasan", ST_PROCESS, 320, 320, 140, 60))
    nodes.append(create_node("n5", "Input Rating (1-5 Bintang)", ST_IO, 310, 420, 160, 60))
    nodes.append(create_node("n6", "Tulis Komentar Ulasan", ST_IO, 310, 520, 160, 60))
    nodes.append(create_node("n7", "Klik Simpan", ST_PROCESS, 350, 620, 80, 40))
    nodes.append(create_node("n8", "Ulasan Tampil di Halaman Produk", ST_IO, 280, 700, 220, 60))
    nodes.append(create_node("n9", "Selesai", ST_START, 350, 800, 80, 40))

    edges = []
    edges.append(create_edge("e1", "n1", "n2"))
    edges.append(create_edge("e2", "n2", "n3"))
    edges.append(create_edge("e3", "n3", "n4"))
    edges.append(create_edge("e4", "n4", "n5"))
    edges.append(create_edge("e5", "n5", "n6"))
    edges.append(create_edge("e6", "n6", "n7"))
    edges.append(create_edge("e7", "n7", "n8"))
    edges.append(create_edge("e8", "n8", "n9"))

    return wrap_drawio("Ulasan", "\n".join(nodes + edges))

def main():
    output_dir = "diagram/flowchart"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    flowcharts = {
        "flowchart_sistem_manual.drawio": generate_manual_system(),
        "flowchart_sistem_baru.drawio": generate_new_system(),
        "flowchart_login.drawio": generate_login(),
        "flowchart_registrasi.drawio": generate_registrasi(),
        "flowchart_pencarian_produk.drawio": generate_pencarian(),
        "flowchart_booking.drawio": generate_booking(),
        "flowchart_pembayaran.drawio": generate_pembayaran(),
        "flowchart_verifikasi_admin.drawio": generate_verifikasi_admin(),
        "flowchart_kelola_produk.drawio": generate_kelola_produk(),
        "flowchart_laporan.drawio": generate_laporan(),
        "flowchart_pembatalan.drawio": generate_pembatalan(),
        "flowchart_ulasan.drawio": generate_ulasan()
    }

    for filename, xml in flowcharts.items():
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            f.write(xml)
        print(f"Generated: {filepath}")

if __name__ == "__main__":
    main()
