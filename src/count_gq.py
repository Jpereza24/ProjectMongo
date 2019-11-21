from src import geoqueries as gq
def count(collection, lista):
    list250 = []
    list500 = []
    for e in lista:
        list250.append(len(gq.geoQuery(collection,e,250,0)))
        list500.append(len((gq.geoQuery(collection,e,500,250)))/2)
    return list250, list500