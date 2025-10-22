# Example: [1, 1, 2, 2, 2, 3, 4, 5] → 10
def sum_evens(numbers_list: list) -> int:
    evens=[]
    for number in numbers_list:
        if number%2==0:
            evens.append(number)
    return  sum(evens)

print(sum_evens([1, 1, 2, 2, 2, 3, 4, 5]))