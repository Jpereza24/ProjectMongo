import folium
def mapFolium(mapp,query,icon,color):  
    for company in query:
        folium.Marker(company['location']['coordinates'][::-1],
                        radius=2,
                        icon=folium.Icon(icon=icon,color=color), 
                       ).add_to(mapp)
    return mapp