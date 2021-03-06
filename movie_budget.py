from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = 'stream', 'rent'


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
       cheaper than streaming movies by months.

       Determine this PER MONTH for the movies in renting_history.

       Return a dict of:
       keys = months (YYYY-MM)
       values = 'rent' or 'stream' based on what is cheaper

       Check out the tests for examples.
    """
    considered_months = {date.strftime(timeformat.date, '%Y-%m') for timeformat in renting_history}
    
    rentprice_dict = {key: 0 for key in considered_months}
    result_dict = {key: "stream" for key in considered_months}
    
    for month in considered_months:
        for movie in renting_history:
            if date.strftime(movie.date, '%Y-%m') == month:
                rentprice_dict[month] += movie.price
    
    for month in result_dict:
        if rentprice_dict[month] <= streaming_cost_per_month:
            result_dict[month] = 'rent'
    
    return result_dict
    pass