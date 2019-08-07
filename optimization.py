import json
from pathlib import Path
from typing import Tuple
from geopy.distance import distance


def pairwise_distance(point_1:Tuple[float, float], point_2:Tuple[float, float]) -> int:
	return distance(points_1, points_2)

path2data = Path("data") / "bilbao_restaurants.json"

with open(path2data) as json_file:
	data = json.load(json_file)


# with open(path2data) as json_file:
# 	data = json.load(json_file)


lat = "latitude"
lng = "longitude"

points = []
for i, point in enumerate(data):
	points.append(tuple(point[info] for info in [lat, lng]))
