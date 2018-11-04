import pymongo
from pymongo import MongoClient
import os, json
import logging

logging.basicConfig(
    handlers = [logging.FileHandler("./execute.log", 'a+', 'utf-8'),], 
    level=logging.DEBUG,
    format="[%(filename)15s:%(lineno)3s - %(funcName)20s() ] %(levelno)s%(asctime)15s %(threadName)5s %(message)s",
    datefmt='%Y/%m/%d %I:%M:%S %p'
)

uri = "mongodb://localhost:27017" 
client = MongoClient(uri)

db = client['TAI_INDON']
collect = db['Essay']

def toMongoDB(list_to_write, role=None):
    if role == None:
        raise Exception("Role didn't define!")
    if role not in ["Tai", "Indon"]:
        raise Exception("Role can't recognize!")

    num = 0


    for root_retreives in list_to_write:
        for rootdir, dirs, files in os.walk(root_retreives):
            if len(files) != 0:
                for fi in files:
                    if fi.endswith(".json"):
                        
                        with open(os.path.join(rootdir, fi), "r") as f:
                            a = json.load(f)
                            a["Role"] = role
                            
                            try:
                                collect.insert_one(a)
                                num = num + 1
                            except pymongo.errors.DuplicateKeyError as de:
                                # print(de.details, a["title"])
                                # logging.error("{} error 發生在{}".format(de, a["title"]))
                                pass

                            except Exception as e:
                                print(e)
                                logging.error("{} ,  {}".format(str(e), a["title"]))
    logging.info("這次傳入資料庫 {} 筆資料  Role:{}".format(str(num), role))


if __name__ == '__main__':
    INDON_LIST = ["./Indon/19/", "./Indon/5/", "./Indon/8/"]
    TAI_LIST = ["./Tai/4", "./Tai/5", "./Tai/6", "./Tai/7", "./Tai/10", "./Tai/11", "./Tai/12", "./Tai/14"]
    
    toMongoDB(INDON_LIST, "Indon")
    toMongoDB(TAI_LIST, "Tai")
    
