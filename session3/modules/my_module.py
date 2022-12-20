def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    if len(numbers) % 2 == 0:
        middle_index = len(numbers) // 2
        return (numbers[middle_index - 1] + numbers[middle_index]) / 2
    else:
        return numbers[len(numbers) // 2]
