import webbrowser
from distancemap import distance_on_map


def main():
    TYO_COORDINATES = (35.68944, 139.69167)  # Location of Tokyo
    YOK_COORDINATES = (35.44778, 139.6425)  # Location of Yokohama

    MAPFILE = 'map.html'

    m = distance_on_map(TYO_COORDINATES, YOK_COORDINATES)
    m.save(MAPFILE)
    webbrowser.open(MAPFILE)


if __name__ == '__main__':
    main()
