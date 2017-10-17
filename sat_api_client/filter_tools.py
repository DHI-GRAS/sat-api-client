from collections import defaultdict


def group_results_by_date(results):
    """Group results from SAT-API query by date

    Parameters
    ----------
    list of dict
        results

    Returns
    -------
    dict date string -> list of dict
        grouped results
        keys: YYYY-MM-DD
    """
    results_grouped = defaultdict(list)
    for r in results:
        date = r['date']
        results_grouped[date].append(r)
    return results_grouped
