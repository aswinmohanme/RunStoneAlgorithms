
def find_min_n2(numbers):
    min_number = 0
    for n in numbers:
        for m in numbers:
            if min_number > m:
                min_number = m
    return min_number

def find_min(numbers):
    min_number = numbers[0]
    for n in numbers:
        if min_number > n:
            min_number = n
    return min_number

