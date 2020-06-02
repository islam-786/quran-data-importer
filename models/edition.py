from fireo.fields import IDField, TextField
from fireo.models import Model


class Edition(Model):
    id = IDField()
    language = TextField()
    name = TextField()
    translator = TextField()

    class Meta:
        to_lowercase = True
        collection_name = "quran_editions"
