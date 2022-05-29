import os

from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using curl and ip"""
    latitude, longitude = os.popen("curl ipinfo.io/loc").read().replace("\n", "").split(",")
    return Coordinates(latitude=latitude, longitude=longitude)
