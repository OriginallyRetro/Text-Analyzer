import os
import sys

def clear_screen():
    """
    Clears the terminal screen based on the operating system.
    Uses 'cls' for Windows and 'clear' for Linux/macOS.
    """
    os.system("cls" if os.name == "nt" else "clear")

class GlobalVariables:
    """
    Class to manage global variables for the program.
    
    Attributes:
        first_time (int): Indicates whether the program is running for the first time.
    """
    def __init__(self, first_time):
        """
        Initializes the GlobalVariables class with the given first_time value.
        
        Parameters:
            first_time (int): Initial value for the first_time attribute.
        """
        self.first_time = first_time

# Instantiate global variables
global_vars = GlobalVariables(first_time=0)

def display_results(text):
    """
    Displays the results of the text analysis.
    
    Parameters:
        text (str): The text to analyze.
    """
    print("=======================================================")
    print("\nResults:")
    print(f"Number of characters: {len(text)}")
    print(f"Number of words: {len(text.split())}")
    print(f"Number of spaces: {text.count(' ')}")
    print("=======================================================")

def entry_point():
    """
    Displays the main menu and handles user choices to continue or exit the program.
    """
    clear_screen()
    print("Welcome to Text Analyzer!")
    print("[1] Continue to the program")
    print("[2] Exit the program")
    
    choice = input("Choose: ")
    match choice:
        case '1':
            active_analyzer()
        case '2':
            clear_screen()
            print("Goodbye!")
            sys.exit()
        case _:
            input("Invalid choice. Please try again.")
            entry_point()  # Restart the main menu if the choice is invalid

def active_analyzer():
    """
    Handles text analysis. Provides an introduction and performs word, character, and space count on user input.
    """
    if global_vars.first_time == 0:
        clear_screen()
        print("This program counts characters, spaces, and words in your input.")
        input("Press Enter to continue...")
        global_vars.first_time += 1
        active_analyzer()  # Re-enter the function to start text analysis
    else:
        clear_screen()
        user_input = input("Enter your text:\n\n")
        display_results(user_input)
        
        action = input("Press 'ENTER' to analyze more text or type 'exit' to quit: ")
        match action:
            case 'exit':
                clear_screen()
                print("Goodbye!")
                sys.exit()
            case _:
                active_analyzer()  # Re-enter the function to analyze more text

# Run the main menu
entry_point()
