def getLocation(office):
    longitude = office['longitude']
    latitude = office['latitude']
    loc = {
        'type':'Point',
        'coordinates':[longitude, latitude]
    }
    return loc