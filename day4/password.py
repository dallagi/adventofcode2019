RANGE = (147981, 691423)

def two_equal_adjacent_digits(password):
    previous_digit = "10"
    for digit in str(password):
        if digit == previous_digit:
            return True
        previous_digit = digit
    return False

def exactly_two_equal_adjacent_digits(password):
    sequences_len = []
    for prev_digit, current_digit in zip(str(password) + "x", "x" + str(password)):
        if current_digit != prev_digit:
            sequences_len.append(0)
        sequences_len[-1] += 1
    return 2 in sequences_len

def non_decreasing_digits(password):
    previous_digit = "-1"
    for digit in str(password):
        if int(digit) < int(previous_digit):
            return False
        previous_digit = digit
    return True

def meets_restrictions(password):
    return two_equal_adjacent_digits(password) and non_decreasing_digits(password)

def meets_stricter_restrictions(password):
    return exactly_two_equal_adjacent_digits(password) and non_decreasing_digits(password)

def brute_force_password():
    base_candidates = 0
    stricter_restrictions_candidates = 0
    for password_candidate in range(RANGE[0], RANGE[1]+1):
        if meets_restrictions(password_candidate):
            base_candidates += 1
        if meets_stricter_restrictions(password_candidate):
            stricter_restrictions_candidates += 1

    print(base_candidates)
    print(stricter_restrictions_candidates)

if __name__ == '__main__':
    brute_force_password()
