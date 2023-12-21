import matplotlib.pyplot as plt

categories = ['PBI APBN', 'PBI APBD', 'PPU', 'PBPU/MANDIRI', 'BP', 'Jamkesda', 'Asuransi Swasta', 'Asuransi Perusahaan']
jumlah_jiwa = [1211810, 108306, 566047, 368005, 68249, 272, 0, 0]

plt.figure(figsize=(10, 4), facecolor='grey', dpi=100)
plt.bar(categories, jumlah_jiwa, label='Bandung', color='skyblue')
plt.xlabel('Kategori')
plt.ylabel('Jumlah Jiwa')
plt.title('Penerimaan Bantuan Kesehatan di Kabupaten Bandung')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=1)

plt.show()