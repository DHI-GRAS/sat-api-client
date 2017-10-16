import datetime

from sat_api_client import search


def test_search_latlon():
    res = search.search(
            satellite='S2',
            start_date=datetime.datetime(2017, 1, 1),
            end_date=datetime.datetime(2017, 3, 1),
            lon=13,
            lat=55)
    assert isinstance(res, dict)
    assert 'results' in res
