# Student Name: Vincess Jane B. Corbilla
# Course & Section: BIT41

import os

RESET = "\033[0m"
BOLD = "\033[1m"
ORANGE = "\033[38;2;255;149;0m"
BG_ORANGE = "\033[48;2;255;149;0m\033[38;2;255;255;255m"
DARK_GRAY = "\033[38;2;142;142;147m"
LIGHT_GRAY = "\033[38;2;212;212;210m"
WHITE = "\033[38;2;255;255;255m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add (a,b):
    return a + b

def render_header():
    print(f"\n  {ORANGE}  iOS CALCULATOR MASTER{RESET}")
    print(f"  {DARK_GRAY}──────────────────────────────────────────{RESET}")

def render_screen(status_msg="Ready", display_value=None):
    clear_screen()
    render_header()
    print(f"  {LIGHT_GRAY}╭────────────────────────────────────────╮{RESET}")
    if display_value is not None:
        val_str = f"{display_value:g}" if isinstance(display_value, (int, float)) else str(display_value)
        print(f"  {LIGHT_GRAY}│{RESET} {WHITE}{BOLD}{val_str:>38}{RESET} {LIGHT_GRAY}│{RESET}")
    else:
        print(f"  {LIGHT_GRAY}│{RESET} {DARK_GRAY}{'0':>38}{RESET} {LIGHT_GRAY}│{RESET}")
    print(f"  {LIGHT_GRAY}╰────────────────────────────────────────╯{RESET}")
    print(f"   {ORANGE}▶ Status:{RESET} {WHITE}{status_msg}{RESET}\n")

def display_menu():
    print(f"  {BOLD}{WHITE}SELECT OPERATION{RESET}")
    print(f"   {BG_ORANGE}  1  {RESET}  {WHITE} +   Addition{RESET}")
    print(f"   {BG_ORANGE}  2  {RESET}  {WHITE} −   Subtraction{RESET}")
    print(f"   {BG_ORANGE}  3  {RESET}  {WHITE} ×   Multiplication{RESET}")
    print(f"   {BG_ORANGE}  4  {RESET}  {WHITE} ÷   Division{RESET}")
    print(f"   {DARK_GRAY}[ 5 ]  ✕   Exit Calculator{RESET}")
    print(f"  {DARK_GRAY}──────────────────────────────────────────{RESET}")

def get_numbers(operation_label):
    print(f"  {ORANGE}━━ {operation_label.upper()} INPUT ━━{RESET}")
    a = float(input(f"   {LIGHT_GRAY}Enter First Number  :{RESET} "))
    b = float(input(f"   {LIGHT_GRAY}Enter Second Number :{RESET} "))
    return a, b

def main():
    status = "Ready"
    last_result = None

    while True:
        render_screen(status, last_result)
        display_menu()
        choice = input(f"  {BOLD}{WHITE}Choose Option (1-5):{RESET} ").strip()

        if choice == '5':
            render_screen("Goodbye! Exiting iOS Calculator.", last_result)
            break
        elif choice == '1':
            try:
                a, b = get_numbers("Addition")
                last_result = add(a, b)
                status = f"Added {a:g} + {b:g}"
            except ValueError:
                last_result = "Error: Invalid Input"
                status = "Failed: Please enter numeric values only."
        elif choice in ['2', '3', '4']:
            status = "Feature coming soon in feature branches!"
        else:
            status = "Invalid option! Choose between 1 and 5."

if __name__ == "__main__":
    main()