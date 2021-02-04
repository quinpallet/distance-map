import folium
from geopy.distance import great_circle as distance


def distance_on_map(location1: tuple, location2: tuple) -> folium.Map:
    FONTSIZE = 16
    min_lat = min(location1[0], location2[0])
    max_lat = max(location1[0], location2[0])
    center_lat = (max_lat - min_lat) / 2 + min_lat

    min_lng = min(location1[1], location2[1])
    max_lng = max(location1[1], location2[1])
    center_lng = (max_lng - min_lng) / 2 + min_lng

    map = folium.Map(location=(center_lng, center_lat))
    map.fit_bounds([location1, location2])
    folium.PolyLine(locations=[location1, location2], color='blue').add_to(map)
    folium.CircleMarker(location=location1, color='red', radius=5, fill='red').add_to(map)
    folium.CircleMarker(location=location2, color='red', radius=5, fill='red').add_to(map)
    folium.map.Marker(location=(center_lat, center_lng), icon=folium.DivIcon(icon_size=(FONTSIZE * 11, FONTSIZE * 2.5), icon_anchor=(0, 0), html='<div style="font-size: {}px; color: red; background-color: rgba(255, 255, 255, .7); text-align: center">直線距離: {:.3f}Km</div>'.format(FONTSIZE, distance(location1, location2).kilometers))).add_to(map)

    return map
