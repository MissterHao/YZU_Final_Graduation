import pymongo
from pymongo import MongoClient
import os, json
import logging
from datetime import datetime, timedelta

from collections import Counter
from collections import defaultdict
from itertools import groupby

from App.METACLASS import Singleton

logging.basicConfig(
    handlers = [logging.FileHandler("./execute.log", 'a+', 'utf-8'),], 
    level=logging.DEBUG,
    format="[%(filename)15s:%(lineno)3s - %(funcName)20s() ] %(levelno)s%(asctime)15s %(threadName)5s %(message)s",
    datefmt='%Y/%m/%d %I:%M:%S %p'
)

# print(os.getcwd())
class DataBase(metaclass=Singleton):
    
    def __init__(self):
        # Load in Config file
        self.config = None
        with open("./App/DB_Connector/config") as f:
            self.config = json.load(f)

        # Start connect the Mongo DB
        uri = self.config["uri"]  # "mongodb://localhost:27017" 
        self.client = MongoClient(uri)

        self.db = self.client[self.config["dbname"]]
        self.collect = self.db[self.config["collection"]]

    def db_status(self):
        """Return Status of MongoDB(Year count)"""

        # Return Value Init
        year_count = []
        detail_of_year = {}
        Role_of_year = {}
        
        # ================================================================================
        # 利用 Year 來分割
        # ================================================================================
        # MongoDB Aggregate Pipeline
        pipeline = [
            {
                "$match":{"date":{"$ne":""}}
            },
            {
                "$project":{
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
                    "month" : {"$month" : "$date"},
                    "year" : {"$year" :  "$date"},
                }
            },
            {
                "$group" : {
                    "_id" : {"year" : "$year" },
                    "count":{"$sum":1}
                }
            }
        ]
        # Aggregate
        cursor = list(self.collect.aggregate(pipeline))
        
        for item in cursor:
            year_count.append({
                "y": item["count"],
                "label": item["_id"]["year"]
            })

        # get year_count with groupby year in cursor
        # for k,v in groupby(cursor, key=lambda x:x["_id"]["year"]):
        #     print(k,list(v))
        #     year_count.append({
        #         "label":k,
        #         "y":list(v)[0]["count"]
        #     })

        # ================================================================================
        # MongoDB Aggregate Pipeline
        pipeline = [
            {
                "$match":{"date":{"$ne":""}}
            },
            {
                "$project":{
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
                    "month" : {"$month" : "$date"},
                    "year" : {"$year" :  "$date"},
                }
            },
            {
                "$group" : {
                    "_id" : {"month":"$month","year" : "$year" },
                    "count":{"$sum":1}
                }
            }
        ]
        # Aggregate
        cursor = list(self.collect.aggregate(pipeline))
        for item in cursor:
            key_year = item["_id"]["year"]
            key_month = item["_id"]["month"]
            count = item["count"]
            if detail_of_year.get(key_year, None) is None:
                detail_of_year[key_year] = [{"label":key_month, "y":count}]
            else:
                detail_of_year[key_year].append({"label":key_month, "y":count})


        # ================================================================================
        # 利用 Year 來分割
        # ================================================================================
        # MongoDB Aggregate Pipeline
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

        # Aggregate
        cursor = list(self.collect.aggregate(pipeline))
        from pprint import pprint
        # pprint(cursor, indent=4)
        Role_of_year
        for item in cursor:
            key_year = item["_id"]["year"]
            key_Role = item["_id"]["Role"]
            count = item["count"]
            if Role_of_year.get(key_year, None) is None:
                Role_of_year[key_year] = [{"name":key_Role, "y":count}]
            else:
                Role_of_year[key_year].append({"name":key_Role, "y":count})

        pprint(Role_of_year, indent=4)




        return {
            "year_count":year_count,
            "detail_of_year":detail_of_year,
            "role_of_year":Role_of_year
        }

    def _db_status(self):
        """Return Status of MongoDB(Indon num, Tailand num....etc)"""
        
        ll = []
        for i in self.collect.find({}, {"date":1}):
            ll.append(i["date"])

        year_c = Counter([x.year for x in ll])
        print(year_c)

        return {
            "year_count": [ {"y":v, "label":k} for k,v in year_c.items()],
        }





# Start connect the Mongo DB
# uri = config["uri"]  # "mongodb://localhost:27017" 
# client = MongoClient(uri)

# db = client[config["dbname"]]
# collect = db[config["collection"]]







# def toMongoDB(list_to_write, role=None):
#     if role == None:
#         raise Exception("Role didn't define!")
#     if role not in ["Tai", "Indon"]:
#         raise Exception("Role can't recognize!")

#     num = 0


#     for root_retreives in list_to_write:
#         for rootdir, dirs, files in os.walk(root_retreives):
#             if len(files) != 0:
#                 for fi in files:
#                     if fi.endswith(".json"):
                        
#                         with open(os.path.join(rootdir, fi), "r") as f:
#                             a = json.load(f)
#                             a["Role"] = role
                            
#                             try:
#                                 collect.insert_one(a)
#                                 num = num + 1
#                             except pymongo.errors.DuplicateKeyError as de:
#                                 # print(de.details, a["title"])
#                                 # logging.error("{} error 發生在{}".format(de, a["title"]))
#                                 pass

#                             except Exception as e:
#                                 print(e)
#                                 logging.error("{} ,  {}".format(str(e), a["title"]))
#     logging.info("這次傳入資料庫 {} 筆資料  Role:{}".format(str(num), role))


# if __name__ == '__main__':
#     INDON_LIST = ["./Indon/19/", "./Indon/5/", "./Indon/8/"]
#     TAI_LIST = ["./Tai/4", "./Tai/5", "./Tai/6", "./Tai/7", "./Tai/10", "./Tai/11", "./Tai/12", "./Tai/14"]
    
#     toMongoDB(INDON_LIST, "Indon")
#     toMongoDB(TAI_LIST, "Tai")
    
