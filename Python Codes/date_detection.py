"""Date Detection """

import re
from typing import List


def detect_date(date_samples: List[str]) -> str:
    """Returns valid date from a list of date inputs"""
    date_regex = r"^([0-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/([1-2][0-9]{3})$"
    detected_dates = []
    for date in date_samples:
        match = re.fullmatch(date_regex, date)
        if match:
            detected_dates.append(date)
    return ", ".join(detected_dates)


if __name__ == "__main__":
    print(
        detect_date(
            ["01/08/2005", "32/06/1990", "18/15/2007", "19/26/929", "18/02/2002"]
        )
    )
