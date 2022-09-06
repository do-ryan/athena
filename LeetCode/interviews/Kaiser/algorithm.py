"""
receives series of characters
what is the highest consecutive repeats and on what character

input:
    'aabbbccaadd'
output:
    print b, 3
"""

def highest_consec_repeat (input_str: str):
    current_char = input_str[0]
    current_count = 1
    max_count = 1
    max_count_char = input_str[0]

    for char in input_str[1::]:
        if char == current_char:
            current_count += 1
        else:
            current_char = char
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_count_char = current_char

    print(max_count, max_count_char)

