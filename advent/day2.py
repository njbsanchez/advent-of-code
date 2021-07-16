"""Advent of Code 2020 - Day 2

Example input:
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
"""


from collections import Counter


def read_file(filepath):

    values = []

    with open(filepath, "r") as raw_file:
        lines = raw_file.readlines()
        for line in lines:
            values.append(line.replace("\n", ""))

    return values


def parse_policy_password(string):
    """
    >>> parse_policy_password("1-3 a: abcde")
    ((1, 3), 'a', 'abcde')
    """

    line_items = string.split(" ")
    nums = line_items[0].split("-")
    rule_tup = (line_items[1].replace(":", ""), int(nums[0]), int(nums[1]))


def count_chars_in_pw(ch, pw):
    """TODO

    >>> count_chars_in_pw('a', 'aaa')
    3
    """

    counter = 0
    for letter in pw:
        if letter == ch:
            counter += 1

    return counter


def range_validator(pw_and_policy):
    """TODO

    >>> range_validator(((1, 3), 'a', 'abcde'))
    True
    """

    nums, char, pw = pw_and_policy

    min_range, max_range = nums
    counter = count_chars_in_pw(char, pw)

    # min_range <= counter <= max_range
    return counter >= min_range and counter <= max_range

# parse password + pol into sane data struct
# create validation fn, take in ^


def pt1_evaluate_password(list):

    pass_counter = 0

    for line in list:

        # pol_nums, pol_char, pw = parse_policy_password(line)
        # num1, num2 = pol_nums

        if range_validator(parse_policy_password(line)):
            pass_counter += 1

    return pass_counter


def pt2_evaluate_password(list):

    pass_counter = 0

    for line in list:
        line_items = line.split(" ")
        nums = line_items[0].split("-")
        rule_tup = (line_items[1].replace(":", ""), int(nums[0]), int(nums[1]))
        counter = 0
        print((line_items[2][rule_tup[1]-1] == rule_tup[0]),
              (line_items[2][rule_tup[2]-1] == rule_tup[0]))
        if (line_items[2][rule_tup[1]-1] == rule_tup[0]) is not (line_items[2][rule_tup[2]-1] == rule_tup[0]):
            pass_counter += 1

    return pass_counter


if __name__ == "__main__":

    password_list = read_file("pass_policies.txt")
    # count_valid_pws(password_list, range_validator)
    # count_valid_pws(password_list, position_validator)

    pt1_valid_passwords = pt1_evaluate_password(password_list)
    print("Part 1 - passwords that are valid:", pt1_valid_passwords)

    pt2_valid_passwords = pt2_evaluate_password(password_list)
    print("Part 2 - passwords that are valid:", pt2_valid_passwords)


"""HI NICOLE"""


def validate_pw1(ch_min: int, ch_max: int, ch: str, pw: str):
    chars = Counter(pw)  # => {'a': 3, 'b': 4}

    return ch_min <= chars[ch] <= ch_max


def validate_pw2(pos1: int, pos2: int, ch: str, pw: str):
    count_found = 0

    if pw[pos1 - 1] == ch:
        count_found += 1

    if pw[pos2 - 1] == ch:
        count_found += 1

    return count_found == 1


def parse_policy_and_pw(policy_and_pw):
    policy_range, policy_char, pw = policy_and_pw.split(" ")

    # ((1, 2), 'a', 'adsfd')
    return tuple(int(n) for n in policy_range.split("-")) + (
        policy_char[0],
        pw,
    )


def count_valid(policies_and_pws, validator):
    valid_pws = 0
    for pol_and_pw in policies_and_pws:
        args = parse_policy_and_pw(pol_and_pw)

        if validator(*args):
            valid_pws += 1

    return valid_pws


if __name__ == "__main__":
    with open("input.txt") as f:
        pols_and_pws = f.readlines()

    print(f"Part 1: {count_valid(pols_and_pws, validate_pw1)}")
    print(f"Part 2: {count_valid(pols_and_pws, validate_pw2)}")
