def longest_increasing_subsequence(sequence: list[int]):
    counter = 1
    longest_sub = 0
    for i in range(0, len(sequence)-1):
        if sequence[i] < sequence[i+1]:
             counter += 1
        else:
            counter = 1
        if counter > longest_sub:
            longest_sub = counter
    return longest_sub


numbers = [1, 2, 3, 1, 0, 1, 2, 3, 4, 5]

longest = longest_increasing_subsequence(numbers)

print(longest)