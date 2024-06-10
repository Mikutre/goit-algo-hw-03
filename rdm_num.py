

def get_numbers_ticket(min, max, quantity):

    import random

    if min < 1 or max> 1000 or quantity > max:
        
        return "Wrong number"
    else:
        pass

    numbers = set()

    while len(numbers) != quantity:
        k = 0
        numbers = set()

        while k <= quantity:
            k = k + 1
            numbers.add(random.randint(min, max))

        if len(numbers) == quantity:
            break
    

    sorted_numbers = sorted(numbers)
    
    return sorted_numbers

print(get_numbers_ticket(1, 10, 10))