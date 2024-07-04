import random

def get_numbers_ticket(min, max, quantity):
    if max + 1 - min < quantity or quantity < 1:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    
    return numbers

print(f"Generated numbers are {get_numbers_ticket(1, 50, 10)}")
print(f"Generated numbers for wrong parameters are {get_numbers_ticket(1, 6, 10)}")