import pymongo
from pymongo import MongoClient
import os, json
import logging
from datetime import datetime, timedelta

from itertools import groupby



with open("./App/DB_Connector/config") as f:
    config = json.load(f)

uri = config["uri"];client = MongoClient(uri)
db = client[config["dbname"]]
collect = db[config["collection"]]

# pipeline = [
# {
#           "$match":{"date":{"$ne":""}}
#         },
# {
#             "$project":{
#                 "Role":"$Role",
                
#                 "date": {
#                      "$dateFromString": {
#                         "dateString": "$date",
#                         "format": "%Y/%m/%d"
#                      }
#                   }
#             }
#         },
# {
#             "$project" : {
#                 "month" : {"$month" : "$date"},
#                 "year" : {"$year" :  "$date"},
#             }
#         },
# {
#             "$group" : {
#                 "_id" : {"year" : "$year","Role":"$Role" },
#                 "count":{"$sum":1}
#         }}
# ]

pipeline = [
        {
          "$match":{"date":{"$ne":""}}
        },
        {
            "$project":{
                "Role":"$Role",
                
                "date": {
                     "$dateFromString": {
                        "dateString": "$date",
                        "format": "%Y/%m/%d"
                     }
                  }
            }
        },
        {
            "$project" : {
                "Role": "$Role",
                "month" : {"$month" : "$date"},
                "year" : {"$year" :  "$date"},
            }
        },
        {
            "$group":{
                "_id" : {"year" : "$year","Role":"$Role" },
                "count":{"$sum":1}
                }
        }
]





year_count = []
cursor = list(collect.aggregate(pipeline))
for k,v in groupby(cursor, key=lambda x:x["_id"]["year"]):
    print(k,list(v))
    year_count.append({
        "label":k,
        "y":sum(item["count"] for item in list(v))
    })

