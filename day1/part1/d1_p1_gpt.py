def extract_calibration_value(line):
    # Function to extract the calibration value from a line
    digits = [char for char in line if char.isdigit()]  # Extract digits from the line
    # if len(digits) >= 2:  # Ensure there are at least two digits in the line
    return int(digits[0] + digits[-1])  # Form a two-digit number from the first and last digits
      # Return 0 if there aren't enough digits in the line
def sum_calibration_values(document):
    # Function to sum all calibration values in the document
    total = 0
    for line in document:
        calibration_value = extract_calibration_value(line)
        total += calibration_value
    return total

# Example calibration document
calibration_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# Calculate the sum of calibration values in the provided document
result = sum_calibration_values(calibration_document)
print("The sum of calibration values is:", result)