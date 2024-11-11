import pyfiglet

# ANSI escape codes for colors
RESET = "\033[0m"  # Reset to default
GREEN = "\033[92m"  # Green text
RED = "\033[91m"    # Red text
BLUE = "\033[94m"   # Blue text
YELLOW = "\033[93m" # Yellow text

# Function to display available fonts
def display_fonts():
    fonts = pyfiglet.FigletFont.getFonts()
    print("Available Fonts:\n")
    for i, font in enumerate(fonts):
        print(f"{i}: {font}")
    return fonts

def main():
    # Display fonts and get the list
    fonts = display_fonts()

    # Prompt user for font selection and color
    while True:
        try:
            font_number = int(input("\nEnter the font number you want to use (or -1 to exit): "))
            if font_number == -1:
                print("Exiting the program.")
                break
            if 0 <= font_number < len(fonts):
                word = input("Enter the word you want to display: ")

                # Choose color
                print("\nChoose a color:")
                print("1: Green")
                print("2: Red")
                print("3: Blue")
                print("4: Yellow")
                color_choice = int(input("Enter color number (1-4): "))

                # Map color choice to ANSI code
                color_map = {
                    1: GREEN,
                    2: RED,
                    3: BLUE,
                    4: YELLOW
                }

                if color_choice in color_map:
                    color = color_map[color_choice]
                    fig = pyfiglet.Figlet(font=fonts[font_number])
                    print(color + fig.renderText(word) + RESET)
                else:
                    print("Invalid color choice.")
            else:
                print("Invalid font number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
