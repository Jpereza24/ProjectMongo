from pymongo import MongoClient

def geoQuery(collection,coordinates,maxdistance,mindistance):
    lista = collection.find(
        {"location":
         {"$near":
          {"$geometry":
           {"type":"Point",
            "coordinates":coordinates
           },
           "$maxDistance":maxdistance,
            "$minDistance":mindistance
          }
         }
        }
    )
    return len(list(lista))