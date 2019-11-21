def getLocationAPI(result):
    location = []
    for i in range(len(result)):
        latitude = result[i]['geometry']['location']['lat']
        longitude = result[i]['geometry']['location']['lng']
        name = result[i]['name']
        address = result[i]['formatted_address']
        loc = {
            'name': name,
            'address': address,
            'location':{
                'type':'Point',
                'coordinates':[longitude,latitude]
            }
        }
        location.append(loc)
    return location  