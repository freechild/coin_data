from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .websocket import *
import websocket
import json
import sys
from bson.json_util import dumps,loads,ObjectId

client = mongo_connect('localhost',27017,'btc-database','test.ok_sub_spot_btc_usd_ticker')

def index(request):
    data = findAll(client,'polls')
    print('getIn')
    dump = dumps(data)
    return HttpResponse(dump,content_type='application/json')


