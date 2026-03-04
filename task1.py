from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        delta = today - given_date
        return delta.days
    
    except ValueError:
        return "Invalid date format"


if __name__ == "__main__":
    print(get_days_from_today("2020-10-09"))

