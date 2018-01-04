import datetime

from sat_api_client import filter_tools
from sat_api_client import search

from .my_vcr import my_vcr


@my_vcr.use_cassette
def test_group_results_by_date():
    res = search.search(
            satellite='S2',
            start_date=datetime.datetime(2017, 1, 1),
            end_date=datetime.datetime(2017, 3, 1),
            lon=13,
            lat=55)
    results = res['results']
    groups = filter_tools.group_results_by_date(results)

    assert len(groups) > 2
    assert len(groups) < len(results)
    assert sorted(list(groups)) == list(groups)

    firstgroup = next(iter(groups.values()))
    assert isinstance(firstgroup, list)
    firstgroupname = next(iter(groups.keys()))
    assert isinstance(firstgroupname, str)
