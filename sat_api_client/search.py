import json

import requests

from sat_api_client import SAT_API_URL
from sat_api_client import query_builder


def _query_sat_api(query_string, sat_api_url):
    """Call SAT-API URL with query string"""
    query_url = sat_api_url + '?' + query_string
    r = requests.get(query_url)
    results_dict = json.loads(r.text)
    return results_dict


def search(
        satellite,
        start_date=None, end_date=None,
        lat=None, lon=None, aoi_geom=None,
        cloud_min=None, cloud_max=None,
        limit=1000, sat_api_url=SAT_API_URL):
    """Search for results on SAT-API

    Parameters
    ----------
    satellite : str in ['S2', 'L8']
        satellite to query
    start_date, end_date : str or datetime.datetime, optional
        date range
        empty means full range
    lat, lon : float, optional
        point to query for
    aoi_geom : GeoJSON dict or something with a __geo_interface__, optional
        AOI geometry in WGS84
    cloud_min, cloud_max : int
        cloud range in percent
    limit : int
        maximum number of query results

    Returns
    -------
    dict
        parsed JSON response of SAT-API
        see http://docs.sat-utils.org/
    """
    query_string = query_builder.build_query_string(
            satellite=satellite,
            start_date=start_date,
            end_date=end_date,
            lat=lat,
            lon=lon,
            aoi_geom=aoi_geom,
            cloud_min=cloud_min,
            cloud_max=cloud_max,
            limit=limit)
    results_dict = _query_sat_api(query_string, sat_api_url)
    return results_dict
