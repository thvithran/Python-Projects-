# STRING MANIPULATION

string = "Thvithran is the Best in the world "

cap = string.capitalize()  # capitalize the string
low = string.lower()       # lowercase the string
up = string.upper()        # uppercase the string
swap = string.swapcase()   # swap cases in the string
tit = string.title()       # titlecase the string

if __name__ == "__main__":
    print(f"Original String :    {string}")
    print(f"Capitalized String : {cap}")
    print(f"Lowercased String : {low}")
    print(f"Uppercased String : {up}")
    print(f"Swapcase String : {swap}")
    print(f"Titlecase String : {tit}")