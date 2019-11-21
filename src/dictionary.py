from src import clean_jsonAPI as ca
from src import API as ap

def dicti(query):
    dicts = []
    dict1 = ca.getLocationAPI(ap.searchPlaces(query,'47.6024156,-122.3326145'))
    dict2 = ca.getLocationAPI(ap.searchPlaces(query,'47.6103008,-122.3399782'))
    dict3 = ca.getLocationAPI(ap.searchPlaces(query,'47.603364,-122.333359'))
    dict4 = ca.getLocationAPI(ap.searchPlaces(query,'47.676762,-122.2049192'))
    dict5 = ca.getLocationAPI(ap.searchPlaces(query,'47.627368,-122.34229'))
    dict6 = ca.getLocationAPI(ap.searchPlaces(query,'47.693994,-122.349701'))
    dict7 = ca.getLocationAPI(ap.searchPlaces(query,'47.715013,-122.320283'))
    result = [dict1,dict2,dict3,dict4,dict5,dict6,dict7]
    for lista in result:
        for i in range(len(lista)):
            if lista[i] not in dicts:
                dicts.append(lista[i])
    return dicts