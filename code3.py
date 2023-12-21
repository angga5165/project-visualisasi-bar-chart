import matplotlib.pyplot as plt
import numpy as np

categories = ['PBI APBN', 'PBI APBD', 'PPU', 'PBPU/MANDIRI', 'BP', 'Jamkesda', 'Asuransi Swasta', 'Asuransi Perusahaan']
jumlah_jiwa_1 = [1211810, 108306, 566047, 368005, 68249, 272, 0, 0]
jumlah_jiwa_2 = [1119615, 546641, 792374, 999677, 58725, 0, 0, 0]
x = np.arange(len(categories))
width = 0.35

plt.figure(figsize=(12, 6), facecolor='grey', dpi=100)
bar1 = plt.bar(x - width/2, jumlah_jiwa_1, width, label='Bandung', color='skyblue')
bar2 = plt.bar(x + width/2, jumlah_jiwa_2, width, label='Bogor', color='orange')
plt.xlabel('Kategori')
plt.ylabel('Jumlah Jiwa')
plt.title('Penerimaan Bantuan Kesehatan di Kabupaten Bandung dan Bogor')
plt.xticks(x, categories, rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=1)

plt.show()