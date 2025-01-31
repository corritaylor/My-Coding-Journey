'''
The program will read two positive integers from the command-line. The program will then generate a multiplication table with the given width and height. The comlumns of the table must be aligned.
'''

def create_multi_table(width, height):
    output = ""
    num_chars = len(str(width*height)) + 1
    
    for a in range(1, height+1):
        for b in range(1, width+1):
            product = a * b
            
            product_str = str(product)
            product_str = product_str.rjust(num_chars, ' ')
            output += product_str + " "
        output += "\n\n"
    return output

def process_input(raw_input):
    try:
        value = int(raw_input)
    except ValueError:
        raise ValueError("'%s' is not an integer" % raw_input)
    
    if value <= 0:
        raise ValueError("All numbers must be greater than zero (0)")
    return value

def get_user_input():
    values = []
    for prompt in ('Width', 'Height'):
        raw_input = input(prompt + ": ")
        processed_input = process_input(raw_input)
        values. append(processed_input)
        
    return values

def main():
    success = False
    try:
        width, height = get_user_input()
        success = True
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nGoodbye.")
    
    if success:
        output = create_multi_table(width, height)
        print('\n\n' + output)
    
if __name__ == '__main__':
    main()