import datetime

from sat_api_client import query_builder


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
