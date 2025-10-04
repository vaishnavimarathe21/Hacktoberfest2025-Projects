library = {"Python": True, "C++": True, "ML": True}
def display_books():
    for book, available in library.items():
        print(f"{book} - {'Available' if available else 'Borrowed'}")
def borrow_book():
    name = input("Book to borrow: ")
    if name in library and library[name]:
        library[name] = False
    else:
        print("Not available")
def return_book():
    name = input("Book to return: ")
    if name in library:
        library[name] = True
while True:
    print("1.Display 2.Borrow 3.Return 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        display_books()
    elif ch == "2":
        borrow_book()
    elif ch == "3":
        return_book()
    elif ch == "4":
        break
