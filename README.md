# distance-map
Display the direct distance between the two locations into the map.

## Requirements

- [folium](https://github.com/python-visualization/folium)
- [geopy](https://github.com/geopy/geopy)
- [reverse-geocode](https://github.com/quinpallet/reverse-geocode) *see blow

## Prerequisites

- Python >= 3.7

## Setup

```sh
$ pip install git+https://github.com/quinpallet/reverse-geocode.git
$ 
```

## Usage

- Sample

``` python
import webbrowser
from distancemap import distance_on_map


def main():
    TYO_COORDINATES = (35.68944, 139.69167)  # Location of Tokyo
    YOK_COORDINATES = (35.44778, 139.6425)  # Location of Yokohama

    MAPFILE = 'map.html'

    m = distance_on_map(TYO_COORDINATES, YOK_COORDINATES)
    m.save(MAPFILE)
    webbrowser.open(MAPFILE)

```
![map html](https://user-images.githubusercontent.com/77138234/107734288-6254ef00-6d40-11eb-80fe-4724fe2b1eff.png)

## License

&copy; 2021 [Ken Kurosaki](https://github.com/quinpallet).<br>
This project is [MIT](https://github.com/quinpallet/distance-map/blob/master/LICENSE) licensed.
