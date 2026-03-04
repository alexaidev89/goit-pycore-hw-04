import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


print(get_numbers_ticket(1, 49, 6))