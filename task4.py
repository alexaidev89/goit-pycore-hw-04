from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # день народження в поточному році
        bday_this_year = birthday.replace(year=today.year)

        # якщо вже минув — беремо наступний рік
        if bday_this_year < today:
            bday_this_year = bday_this_year.replace(year=today.year + 1)

        # потрапляє в проміжок [today; today+7]
        if today <= bday_this_year <= end_date:
            congratulation_date = bday_this_year

            # перенос з вихідних на понеділок
            if congratulation_date.weekday() == 5:      # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # Sunday
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    print(get_upcoming_birthdays(users))