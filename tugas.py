import pandas as pd

# Data teman
data = {
    'nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'],
    'tinggi_badan': [170, 165, 160, 158, 172],
    'umur': [20, 21, 19, 22, 20],
    'berat_badan': [65, 60, 55, 50, 70]
}

df = pd.DataFrame(data)

df.to_csv('teman_data.csv', index=False)

# Baca file csv
df = pd.read_csv('teman_data.csv')

# Manipulasi 1: Tambahkan kolom BMI (Indeks Massa Tubuh)
df['BMI'] = df['berat_badan'] / ((df['tinggi_badan'] / 100) ** 2)

# Manipulasi 2: Filter teman dengan umur di atas 20
umur_di_atas_20 = df[df['umur'] > 20]

# Manipulasi 3: Urutkan berdasarkan berat_badan
df_sorted = df.sort_values(by='berat_badan', ascending=False)

# Manipulasi 4: Ambil hanya kolom nama dan BMI
nama_bmi = df[['nama', 'BMI']]

# Cetak hasil
print("Teman dengan umur di atas 20:")
print(umur_di_atas_20)
print("\nData diurutkan berdasarkan berat badan:")
print(df_sorted)
print("\nDaftar nama dan BMI:")
print(nama_bmi)
