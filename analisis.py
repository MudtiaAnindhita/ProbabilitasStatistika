import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# Tabel Data
path = r"D:\probstat_pertemuan4\mudtia.xlsx"
dataraw = pd.read_excel(path)

print("DATA MAHASISWA:")
print(dataraw)

# Tabel Frekuensi
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")

print("\nTabel Frekuensi:")
print(datafrq)

# Data warna untuk setiap Grade
warna = [
    "#FFD54F",   # A
    "#52D4E6",   # AB
    "#81C784",   # B
    "#BA68C8",   # BC
    "#E57373",   # C
    "#707B81"    # D
]

# Grafik Garis
plt.figure(figsize=(9, 5))
# Garis utama
plt.plot(
    datafrq.index,
    datafrq["Frekuensi"],
    linewidth=2.5,
    color="#4682B4"
)
# Titik mengikuti warna setiap Grade
for i in range(len(datafrq)):
    plt.scatter(
        datafrq.index[i],
        datafrq["Frekuensi"].iloc[i],
        color=warna[i],
        s=100,
        edgecolor="white",
        linewidth=1.5,
        zorder=3
    )
plt.title(
    "Distribusi Frekuensi Grade Mahasiswa",
    fontname="Arial",
    fontweight="black",
    fontsize=16
)
plt.xlabel(
    "Grade",
    fontname="Arial",
    fontweight="black",
    fontsize=12
)
plt.ylabel(
    "Jumlah Mahasiswa",
    fontname="Arial",
    fontweight="black",
    fontsize=12
)
plt.xticks(
    fontname="Arial",
    fontweight="black"
)
plt.yticks(
    fontname="Arial",
    fontweight="black"
)
plt.grid(
    True,
    linestyle="--",
    alpha=0.4
)
plt.tight_layout()
plt.show()

# Grafik Batang
plt.figure(figsize=(9, 5))
bars = plt.bar(
    datafrq.index,
    datafrq["Frekuensi"],
    color=warna
)
plt.title(
    "Jumlah Mahasiswa Berdasarkan Grade",
    fontname="Arial",
    fontweight="black",
    fontsize=16
)
plt.xlabel(
    "Grade",
    fontname="Arial",
    fontweight="black",
    fontsize=12
)
plt.ylabel(
    "Jumlah Mahasiswa",
    fontname="Arial",
    fontweight="black",
    fontsize=12
)
plt.xticks(
    fontname="Arial",
    fontweight="black"
)
plt.yticks(
    fontname="Arial",
    fontweight="black"
)
# Menampilkan angka di atas batang
for bar in bars:
    tinggi = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        tinggi + 0.2,
        str(int(tinggi)),
        ha="center",
        fontname="Arial",
        fontweight="black",
        fontsize=11
    )
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)
plt.tight_layout()
plt.show()

# Pie Chart
fig, ax = plt.subplots(figsize=(8, 8))
nilai = datafrq["Frekuensi"].values
label = datafrq.index
total = nilai.sum()
sudut = np.cumsum([0] + list(nilai)) / total * 360

# Bagian bawah
for y in np.linspace(-0.12, 0, 8):
    for i in range(len(nilai)):
        bagian = Wedge(
            (0, y),
            1,
            sudut[i],
            sudut[i + 1],
            facecolor=warna[i],
            edgecolor="white"
        )
        ax.add_patch(bagian)
# Bagian atas
for i in range(len(nilai)):
    bagian = Wedge(
        (0, 0),
        1,
        sudut[i],
        sudut[i + 1],
        facecolor=warna[i],
        edgecolor="white"
    )
    ax.add_patch(bagian)
# Label di tengah pie
for i in range(len(nilai)):
    tengah = (sudut[i] + sudut[i + 1]) / 2
    x = 0.58 * np.cos(np.radians(tengah))
    y = 0.58 * np.sin(np.radians(tengah))
    persen = nilai[i] / total * 100
    ax.text(
        x, y,
        f"{label[i]}\n{persen:.1f}%",
        ha="center",
        va="center",
        fontsize=12,
        fontname="Arial Black",
        fontweight="normal"
    )
ax.set_title(
    "Persentase Grade Mahasiswa",
    fontsize=18,
    fontname="Arial Black",
    fontweight="normal",
    pad=20
)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect("equal")
ax.axis("off")
plt.tight_layout()
plt.show()

# Statistika Deskriptif
dataraw["Nilai"] = pd.to_numeric(dataraw["Nilai"], errors="coerce")

dt = dataraw["Nilai"]

stats = dt.describe()

stats["Standard Error"] = dt.sem()
stats["Median"] = dt.median()
stats["Mode"] = dt.mode().iloc[0]
stats["Variance"] = dt.var()
stats["range"] = dt.max() - dt.min()
stats["skewness"] = dt.skew()
stats["kurtosis"] = dt.kurtosis()

print("\nStatistika Deskriptif:")
print(stats)