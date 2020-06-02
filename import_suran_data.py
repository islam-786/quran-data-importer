import requests
import fireo
from models.ayah import Ayah
from models.surah import Surah

surah_batch = fireo.batch()
surah_count = 0
init_surah_number = 0

resp = requests.get('http://api.alquran.cloud/v1/surah')

if resp.status_code == 200:

    data = resp.json()['data']

    for s in data:
        
        surah = Surah()
        surah.id = str(s["number"])
        surah.number = s["number"]
        surah.name = s["name"]
        surah.english_name = s["englishName"]
        surah.english_name_translation = s["englishNameTranslation"]
        surah.number_of_ayahs = s["numberOfAyahs"]
        surah.revelation_type = s["revelationType"]

        surah.save(batch=surah_batch)
        surah_count += 1

        print('Surah complete ', surah_count)

    if(surah_count >= 400):
        surah_batch.commit()
        surah_count = 0

else:
    print("unable to get data")

print('============Complete=============================')
surah_batch.commit()