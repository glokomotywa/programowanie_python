def most_frequent_element(data: list):
    freq = {}
    for element in data:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    max_frequency = max(freq)

    for i in freq:
        if freq[i] == max_frequency:
            return i


data = [1,1,1,2,2,3]

print(most_frequent_element(data))