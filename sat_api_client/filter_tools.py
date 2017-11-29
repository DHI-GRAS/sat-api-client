from collections import defaultdict
from collections import OrderedDict


def group_results_by_date(results):
    """Group results from SAT-API query by date

    Parameters
    ----------
    list of dict
        results

    Returns
    -------
    OrderedDict date string -> list of dict
        grouped results
        keys: YYYY-MM-DD
        sorted by date
    """
    results_grouped = defaultdict(list)
    for r in results:
        date = r['date']
        results_grouped[date].append(r)
    groups_sorted = OrderedDict()
    for k in sorted(list(results_grouped)):
        groups_sorted[k] = results_grouped[k]
    return groups_sorted
