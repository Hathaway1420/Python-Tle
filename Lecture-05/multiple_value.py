def calculate_stats(number):
    total_sum = sum(number)
    aversge = total_sum / len(number)
    maximum = max (number)
    minimum = min(number)
    return total_sum, aversge, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, avg, max_num, min_num, = calculate_stats(numbers)

print(f"Total Sum: {total}")
print(f"Average:{avg}")
print(f"Maximum:{max_num}")
print(f"Minimum: {min_num}")