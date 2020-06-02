import fireo
from models.ayah import Ayah
from models.translation import Translation


ayah = Ayah.collection.get('quran_ayahs/2-1')
print(ayah.to_dict())

trans = Translation.collection.get('quran_translations/en.sahih_2-1')
print(trans.to_dict())