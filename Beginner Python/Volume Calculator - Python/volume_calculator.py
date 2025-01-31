'''
The program will ask the user for the length, width and height of a rectangular box. The program will calculate the volume of the box and display the result.The program will display meaningful error messages and exit gracefully in all situations.
'''

def process_input(raw_input):
    '''
    (1) Converts user input into a positive float.(2) Raises ValueError if the input is non-numeric. (3) Raises ValueError if the input is a negative number.
    '''
    try:
        value = float(raw_input)
    except ValueError:
        raise ValueError("%s is not a number"  % raw_input)
    
    if value <= 0:
        raise ValueError("All demensions must be greater than zero (0)")
    
    return value

def get_dimensions_from_user(*names):
    output_values =[]
    
    for name in names:
        raw_input = input(name + ": ")
        processed_input = process_input(raw_input)
        output_values.append(processed_input)
        
    return output_values

def main():
    print("This program will calculate the volume of a rectanguler box given its length, width, and height.\n")
    
    success = False
    
    try:
        length, width, height = get_dimensions_from_user('Length', 'Width', 'Height')
        success = True
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        '''
        Exits the program all together
        '''
        print("\nGoodbye")
    
    if success:
        volume = length * width * height
        print("\nThe volume of the box is %.2f." % volume)
    
if __name__ == "__main__":
    main()