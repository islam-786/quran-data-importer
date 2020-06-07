from os import listdir
from os.path import isfile, join

import fireo
from models.ayah import Ayah

file_location = './quran-simple.txt'
f = open(file_location, "r", encoding="utf8")

line_count = 0

for line in f:

    if not line.strip():
        print('file end')
        break

    surah_number, ayat_number, line_text = line.strip().split('|')
    line_count += 1

    print(line_text)

    if line_count == 3:
        break;


print('============Complete=============================')
#ayah_batch.commit()