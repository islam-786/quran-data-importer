from fireo.fields import IDField, TextField
from fireo.models import Model


class Fstore(Model):
    id = IDField()
    language = TextField()

    class Meta:
        collection_name = "fstore"


# f = Fstore()
# f.id = '123'
# f.language = 'lang 1'
# f.save()

doc = Fstore.collection.get('fstore/123')
print(doc.to_dict())