def cek_kelayakan(pendapatan, jumlah_pinjaman, riwayat_kredit):
    if riwayat_kredit.lower() != 'baik':
        return "Ditolak (Riwayat Kredit Buruk)"
    if pendapatan < 3000:
        return "Ditolak (Pendapatan di bawah $3,000)"
    if jumlah_pinjaman > (pendapatan * 5):
        return "Ditolak (Pinjaman melebihi 5x pendapatan)"
    return "Disetujui (Nasabah Layak)"

if __name__ == "__main__":
    print("========================================")
    print("   SISTEM PENILAIAN KELAYAKAN PINJAMAN  ")
    print("========================================\n")
    
    nasabah = [
        {"nama": "Budi", "pendapatan": 5000, "pinjaman": 15000, "kredit": "Baik"},
        {"nama": "Siti", "pendapatan": 2500, "pinjaman": 5000, "kredit": "Baik"},
        {"nama": "Andi", "pendapatan": 8000, "pinjaman": 20000, "kredit": "Buruk"}
    ]

    for n in nasabah:
        hasil = cek_kelayakan(n["pendapatan"], n["pinjaman"], n["kredit"])
        print(f"Nama Nasabah    : {n['nama']}")
        print(f"Pendapatan      : ${n['pendapatan']}")
        print(f"Jumlah Pinjaman : ${n['pinjaman']}")
        print(f"Riwayat Kredit  : {n['kredit']}")
        print(f"Status          : {hasil}")
        print("-" * 40)
