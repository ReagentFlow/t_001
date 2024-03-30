#from scanner.scanner import barcode_scanner
from scales.scales_main import getting_weight
# from fire_db import action
from fire_db.fire_db import FireDataBase

from model import StatusExperation, Container, ContainerData

COLLECTION = 'reagents'

if __name__ == "__main__":
    #key = barcode_scanner()
    key = 14
    print(key)
    if key:
        #weight = getting_weight()
        fire_db = FireDataBase('/Users/voron/Desktop/RF/script/private.json')
        weight = 120120
        data = ContainerData(name='malina', weight=weight, value=weight * 10, status=StatusExperation.FEW)
        containter = Container(key=key, data=data)

        doc = fire_db.get(str(key), COLLECTION)
        if doc:
            print(fire_db.update(COLLECTION, containter))
        else:
            fire_db.create(COLLECTION, containter)

        # fire_db.create('reagents', containter)
        # docs = fire_db.get(collection='reagents')
        # for doc in docs:
        #     print(doc.id, doc.get('name'), doc.to_dict())
    else:
        raise Exception("Error with scanning bar code")
