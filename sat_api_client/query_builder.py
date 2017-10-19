import datetime

import dateutil.parser
import geojson.mapping

SATELLITE_NAMES = {
    'S2': 'sentinel-2',
    'L8': 'landsat-8'}


def _format_date_from(start_date):
    return 'date_from={:%Y-%m-%d}'.format(start_date)


def _format_date_to(end_date):
    return 'date_from={:%Y-%m-%d}'.format(end_date)


def _format_cloud_from(pct):
    return 'cloud_from={:.0f}'.format(pct)


def _format_cloud_to(pct):
    return 'cloud_to={:.0f}'.format(pct)


def _format_contains(lat, lon):
    return 'contains={lon},{lat}'.format(lon=lon, lat=lat)


def _format_intersects(geom):
    if isinstance(geom, dict):
        gjdict = geom
    else:
        gjdict = geojson.mapping.to_mapping(geom)
    gjstr = geojson.dumps(gjdict)
    return 'intersects=' + gjstr


def _format_satellite_name(satellite):
    satellite_name = SATELLITE_NAMES[satellite]
    return 'satellite_name=' + satellite_name


def _format_limit(limit):
    return 'limit={:d}'.format(limit)


def _parse_date(date):
    if date is None:
        return None
    if isinstance(date, (datetime.datetime, datetime.date)):
        return date
    return dateutil.parser.parse(date)


def build_query_string(
        satellite,
        start_date=None, end_date=None,
        lat=None, lon=None, aoi_geom=None,
        cloud_min=None, cloud_max=None, limit=1000):
    """Build SAT-API query string

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
        AOI geometry
    cloud_min, cloud_max : int
        cloud range in percent
    limit : int
        maximum number of query results

    Returns
    -------
    str
        query string
    """
    start_date = _parse_date(start_date)
    end_date = _parse_date(end_date)
    query = []
    query.append(_format_limit(limit))
    query.append(_format_satellite_name(satellite))
    if start_date is not None:
        query.append(_format_date_from(start_date))
    if end_date is not None:
        query.append(_format_date_to(end_date))
    if cloud_min is not None:
        query.append(_format_cloud_from(cloud_min))
    if cloud_max is not None:
        query.append(_format_cloud_to(cloud_max))
    if aoi_geom is not None:
        query.append(_format_intersects(aoi_geom))
    if lat and lon:
        query.append(_format_contains(lat, lon))
    and_string = '&'.join(map(str, query))
    return and_string
