
def round_numbers(numbers: list[int], threshold: int):
    rounded_list = []
    for num in numbers:
        if num < threshold:
            num = num - (num % 10)
            rounded_list.append(num)
        elif num % 10 == 0:
            rounded_list.append(num)
        else:
            num = num + (10 - (num % 10))
            rounded_list.append(num)

    return rounded_list

numbers = [23, 45, 12, 38, 60, 9]
threshold = 30

result = round_numbers(numbers, threshold)

print(result)