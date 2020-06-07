from os import listdir
from os.path import isfile, join

import fireo
from models.ayah import Ayah

file_location = './quran-simple.txt'
f = open(file_location, "r", encoding="utf8")

ayah_batch = fireo.batch()
count = 0
line_count = 0
ayahNumber = 0;

for line in f:

    if not line.strip():
        print('file end')
        break

    surah_number, ayat_number, line_text = line.strip().split('|')
    print(' writing line...' + str(line_count))
    line_count += 1

    if int(ayat_number) != 0:
        ayahNumber += 1

    ayah = Ayah()
    ayah.id = str(surah_number) + '-' + str(ayat_number)
    ayah.surah_id = str(surah_number)
    ayah.number = ayahNumber
    ayah.number_in_surah = int(ayat_number)
    ayah.arabic = line_text
    ayah.save(batch=ayah_batch)

    count += 1

    if(count >= 400):
        ayah_batch.commit()
        count = 0

print('============Complete=============================')
ayah_batch.commit()