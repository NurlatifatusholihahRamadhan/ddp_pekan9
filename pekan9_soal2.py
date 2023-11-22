#soal no 2
def kelulusan(nilai):
    if nilai >= 0 and nilai <= 60:
     return "Gagal"
    elif nilai >= 61 and nilai <= 70:
     return "Baik"
    elif nilai  >= 71 and nilai <= 80:
     return "Sangat Baik"
    elif nilai  >= 81 and nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidah valid"


print(kelulusan(60))