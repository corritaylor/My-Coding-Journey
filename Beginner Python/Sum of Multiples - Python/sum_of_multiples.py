'''
This program will ask the user for a coma-serperated list of positive integers. The program will outpput the sum of all multiples of those numbers up to 1000.
'''
def sum_of_multiples(numbers, max):
    total = 0
    
    for i in range(1, max+1):
        for number in numbers:
            if i % number == 0:
                total += i
                break
    
    return total

def validate_single_number(raw_string):
    try:
        value = int(raw_string)
    except ValueError:
        raise ValueError("'%s' is not an integer." % raw_string)
    
    if value <= 0:
        raise ValueError("All numbers muse be greater than zero (0)")
    return value

def process_input(raw_input):
    "1, 2, 3, 4"
    numbers = []
    for raw_string in raw_input.split(","):
        value = validate_single_number(raw_string)
        if value not in numbers:
             numbers.append(value)
    return numbers

def get_user_input():
    raw_input = input("Enter a coma-seperated list of positive integers: ")
    processed_input = process_input(raw_input)
    return processed_input

def main():
    success = False
    try:
        numbers = get_user_input()
        success = True
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nGoodbye")
        
    if success:
        max = 1000
        result = sum_of_multiples(numbers, max)
        print("The sum of the multiple of %s to %d is %d." \
            % (numbers, max, result) )
        
if __name__ == "__main__":
    main()