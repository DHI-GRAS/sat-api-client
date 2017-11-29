import datetime

import geojson

from sat_api_client import query_builder

AOI_GEOJSON = """{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              11.589202880859375,
              54.59832341427045
            ],
            [
              12.17559814453125,
              54.59832341427045
            ],
            [
              12.17559814453125,
              54.94923107905585
            ],
            [
              11.589202880859375,
              54.94923107905585
            ],
            [
              11.589202880859375,
              54.59832341427045
            ]
          ]
        ]
      }
    }
  ]
}"""


def test_build_query_string_latlon():
    querystr = query_builder.build_query_string(
        satellite='S2',
        start_date=datetime.datetime(2017, 1, 1),
        end_date=datetime.datetime(2017, 3, 1),
        cloud_min=22,
        cloud_max=99,
        lon=180,
        lat=90)
    assert 'contains=180,90' in querystr
    assert 'date_from=2017-01-01' in querystr
    assert 'cloud_from=22' in querystr


def test_build_query_string_intersects():
    aoi_gj = geojson.loads(AOI_GEOJSON)
    querystr = query_builder.build_query_string(
        satellite='S2',
        start_date=datetime.datetime(2017, 1, 1),
        end_date=datetime.datetime(2017, 3, 1),
        cloud_min=22,
        cloud_max=99,
        aoigeom=aoi_gj)
    assert 'intersects' in querystr
