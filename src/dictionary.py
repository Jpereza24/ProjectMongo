from src import clean_jsonAPI as ca
from src import API as ap

def dicti(query,lista):
    dicts = []
    result = []
    for lst in lista:
        for coords in lst:
            res = ca.getLocationAPI(ap.searchPlaces(query,coords))
            result.append(res)
    for lista in result:
        for i in range(len(lista)):
            if lista[i] not in dicts:
                dicts.append(lista[i])
    return dicts