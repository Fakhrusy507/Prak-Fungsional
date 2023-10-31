def waktu_ke_menit(minggu, hari, jam, menit):
    minggu_menit = minggu * 7 * 24 * 60
    hari_menit = hari * 24 * 60
    jam_menit = jam * 60
    total_menit = minggu_menit + hari_menit + jam_menit + menit
    return total_menit

def ambil_integer(data):
    return list(filter(str.isdigit, data.split()))

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = [waktu_ke_menit(*map(int, ambil_integer(item))) for item in data]

print('OutputData = ', output_data)

output_Int = [ambil_integer(item) for item in data]

for item in output_Int:
    print(item)
