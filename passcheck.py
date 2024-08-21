import re

def display_banner():
    banner = r"""
 ________  ________  ________   ________                 ________  ___  ___  _______   ________  ___  __       
|\   __  \|\   __  \|\   ____\ |\   ____\               |\   ____\|\  \|\  \|\  ___ \ |\   ____\|\  \|\  \     
\ \  \|\  \ \  \|\  \ \  \___|_\ \  \___|_  ____________\ \  \___|\ \  \\\  \ \   __/|\ \  \___|\ \  \/  /|_   
 \ \   ____\ \   __  \ \_____  \\ \_____  \|\____________\ \  \    \ \   __  \ \  \_|/_\ \  \    \ \   ___  \  
  \ \  \___|\ \  \ \  \|____|\  \\|____|\  \|____________|\ \  \____\ \  \ \  \ \  \_|\ \ \  \____\ \  \\ \  \ 
   \ \__\    \ \__\ \__\____\_\  \ ____\_\  \              \ \_______\ \__\ \__\ \_______\ \_______\ \__\\ \__\
    \|__|     \|__|\|__|\_________\\_________\              \|_______|\|__|\|__|\|_______|\|_______|\|__| \|__|
                       \|_________\|_________|                                                                 
                                                                                                              
    """
    print(banner)

def check_password_complexity(password):
    complexity_score = 0
    criteria = [
        (r'[a-z]', "lowercase letter"),
        (r'[A-Z]', "uppercase letter"),
        (r'[0-9]', "digit"),
        (r'[!@#$%^&*(),.?":{}|<>]', "special character")
    ]
    
    # Check length
    if len(password) >= 8:
        complexity_score += 1
    
    # Check each criteria
    for pattern, description in criteria:
        if re.search(pattern, password):
            complexity_score += 1
    
    # Determine complexity level
    if complexity_score <= 2:
        complexity = "WEAK"
    elif complexity_score == 3:
        complexity = "MODERATE"
    else:
        complexity = "STRONG"
    
    return complexity

# Example usage
if __name__ == "__main__":
    display_banner()
    password = input("Enter a password to check its complexity: ")
    complexity = check_password_complexity(password)
    print(f"The password complexity is: {complexity}")
