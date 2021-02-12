import folium
import unicodedata
from geopy.distance import great_circle as distance
from q_geocode import ReverseGeocode


def get_tooltip(location: tuple) -> str:
    return f'緯度:{location[0]}, 経度:{location[1]}'

def get_marker_icon(label: str) -> folium.DivIcon:
    # マーカ文字サイズ
    font_size = 16
    # 文字数取得（半角1、全角2）
    n_chars = sum([2 if unicodedata.east_asian_width(c) in 'FWA' else 1 for c in label]) + 2
    # マーカアイコンの表示サイズ
    icon_size = (font_size * n_chars / 2, font_size * 2.5)
    # マーカHTMLスタイル
    marker_dom_style = f'font-size: {font_size}px; color: red; background-color: rgba(255, 255, 255, .7); text-align: center'

    return folium.DivIcon(icon_size=icon_size, icon_anchor=(-10, font_size * 0.75), html=f'<div style="{marker_dom_style}">{label}</div>')

def distance_on_map(location1: tuple, location2: tuple) -> folium.Map:
    # 2点間座標の緯度中間座標を取得
    min_lat = min(location1[0], location2[0])
    max_lat = max(location1[0], location2[0])
    center_lat = (max_lat - min_lat) / 2 + min_lat
    # 2点間座標の経度中間座標を取得
    min_lng = min(location1[1], location2[1])
    max_lng = max(location1[1], location2[1])
    center_lng = (max_lng - min_lng) / 2 + min_lng

    map = folium.Map(location=(center_lng, center_lat))
    map.fit_bounds([location1, location2])
    folium.PolyLine(locations=[location1, location2], color='blue').add_to(map)
    folium.CircleMarker(location=location1, tooltip=get_tooltip(location1), color='red', radius=5, fill='red').add_to(map)
    folium.CircleMarker(location=location2, tooltip=get_tooltip(location2), color='red', radius=5, fill='red').add_to(map)
    # 始点座標住所表示
    folium.map.Marker(location=location1, icon=get_marker_icon(ReverseGeocode(location1).get_address())).add_to(map)
    # 終点座標住所表示
    folium.map.Marker(location=location2, icon=get_marker_icon(ReverseGeocode(location2).get_address())).add_to(map)
    # 直線距離表示
    folium.map.Marker(location=(center_lat, center_lng), icon=get_marker_icon(f'直線距離: {distance(location1, location2).kilometers:.3f}Km')).add_to(map)

    return map
