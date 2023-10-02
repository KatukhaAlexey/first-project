import datetime

def convert_date(date: str) -> str:

    if len(date) != 10:

        return "Error: Invalid date."

    else:

        pass

    d, m, y = date.split('/')

    new_format_of_date = y + '-' + m + '-' + d

    try:

        datetime.date.fromisoformat(new_format_of_date)

    except ValueError:

        return "Error: Invalid date."

    return new_format_of_date

date = "25/12/2021"

print(convert_date(date))