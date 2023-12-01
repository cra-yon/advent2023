import re

def find_calibration_values_from_file(file_path):
    with open(file_path, 'r') as file:
        input_text = file.read()
    
    return find_calibration_values(input_text)

def find_calibration_values(input_text):
    lines = input_text.split('\n')
    total_sum = 0

    for line in lines:
        digits = re.findall(r'\b(?:one|two|three|four|five|six|seven|eight|nine|\d)\b', line)
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]

            # Convert words to digits if necessary
            digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                             'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
            first_digit = digit_mapping.get(first_digit, first_digit)
            last_digit = digit_mapping.get(last_digit, last_digit)

            # Combine and add to the total sum
            value = int(first_digit + last_digit)
            total_sum += value

    return total_sum

# Example usage with a file
file_path = 'path/to/your/input/file.txt'
result = find_calibration_values_from_file(file_path)
print(result)
