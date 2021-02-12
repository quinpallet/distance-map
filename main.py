import webbrowser
from distancemap import distance_on_map


def main():
    TYO_COORDINATES = (35.68944, 139.69167)  # Location of 東京都庁
    YOK_COORDINATES = (35.4503658, 139.6336805)  # Location of 横浜市市庁舎

    MAPFILE = 'map.html'

    m = distance_on_map(TYO_COORDINATES, YOK_COORDINATES)
    m.save(MAPFILE)
    webbrowser.open(MAPFILE)


if __name__ == '__main__':
    main()
