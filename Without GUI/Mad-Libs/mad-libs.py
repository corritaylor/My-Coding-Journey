# Mad Libs Welcome message
print("Welcome to the Mad Libs game!")
print("In this game, you will fill in the blanks to create a funny story.")
print("Just follow the prompts and have fun!")
print("----------------------------------------------------------")

# Ask the user for input to fill in the blanks in a mad lib story

noun = input("Choose a noun: ")
p_noun = input("Choose a plural noun: ")
noun2 = input("Choose another noun: ")
place = input("Name a place: ")
adjective = input("Choose an adjective (a describing word): ")
noun3 = input("Choose another noun: ")

#Print the mad lib story using the user's input

print("\nHere's your mad lib story:")
print("\n----------------------------------------------------------")
print(f"Once upon a time, there was a {noun} who loved to play with {p_noun}.")
print(f"One day, they found a {noun2} in the {place}.")
print(f"They were so {adjective} that they decided to take it home.")
print(f"From that day on, the {noun} and the {noun2} were the best of friends.")
print(f"They went on many adventures together, exploring the {place} and making new {p_noun}.")
print(f"And they lived happily ever after with their {noun3}.")
print("The end.")
print("----------------------------------------------------------")
print("\nThanks for playing!")
print("We hope you enjoyed creating your own mad lib story.")
print("Feel free to play again and create a new story with different words.")

while True:
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        print("\nGreat! Let's create another mad lib story.")
        # You can call the function or repeat the input process here
        # For now, we will just break the loop to end the program
        break
    elif play_again == 'no':
        print("Thank you for playing! HAve a great Day!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

