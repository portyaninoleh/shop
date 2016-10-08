from __future__ import unicode_literals
import httplib, json

from celery.schedules import crontab
from celery.task import periodic_task

from django.conf import settings

from products.models import WareHouse

@periodic_task(run_every=crontab(hour=0, minute=0))
# @periodic_task(run_every=crontab(minute='*/1'))
def updateWareHouses():
    warehouses = list()
    npUrl = "/v2.0/json/AddressGeneral/getWarehouses/"
    headers = {
        'Content-Type': 'application/json'
    }
    params = json.dumps({
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "apiKey": settings.NOVA_POSHTA_KEY
    })
    try:
        conn = httplib.HTTPConnection('testapi.novaposhta.ua')
        conn.request('POST', npUrl, params, headers)
        response = conn.getresponse()
        data = response.read()
        dictData = json.loads(data)
        if 'success' in dictData.keys() and dictData['success']:
            WareHouse.objects.all().delete()
            for warehouse_data in dictData['data']:
                warehouses.append(WareHouse(
                    description=warehouse_data['DescriptionRu'],
                    phone=warehouse_data['Phone'],
                    number=warehouse_data['Number'],
                    site_key=warehouse_data['SiteKey'],
                    city=warehouse_data['CityDescriptionRu']
                ))
            WareHouse.objects.bulk_create(warehouses)
        conn.close()
    except Exception as e:
        print(e)