expenses = []

def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')

def add_expense(month):
    print()
    expense_amount = int(input("Podaj kwotę [zł]: "))
    expense_type = input("Podaj rodzaj wydatku (jedzenie, rozrywka, dom, inny): ")

    expense = (expense_amount, expense_type, month)                                        # nawias () a więc jest to krotka (tuple) - raz dodana wielkość nie będzie mogła być w przyszłości modyfikowana
    expenses.append(expense)

def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)  
    average_expense_this_month = total_amount_this_month / number_of_expenses_this_month
    average_expense_all = total_amount_all / len(expenses)

    print()
    print("Statystyki")
    print("Wszystkie wydatki w tym miesiącu [zł]:", total_amount_this_month)
    print("Średni wydatek w tym miesiącu [zł]:", average_expense_this_month)
    print("Wszystkie wydatki w roku [zł]:", total_amount_all) 
    print("Średni wydatek w skali roku [zł]:", average_expense_all)

def save_file():
    file = open("wydatki.txt", "w")
    file.write("Testowy tekst" "\n")
  
    for expense in expenses:
         file.write(expense+"\n")
    file.close()                       
    print("Plik został poprawnie zapisany!")  

# def save_file():
#     file = open("wydatki.txt", "w")
#     for expense in expenses:
#         file.write(expense+"\n")
#     file.close()                       
#     print("Plik został poprawnie zapisany!")  

def open_file():
    try:
        file = open("wydatki.txt")
        for line in file.readlines():
            expenses.append(line.strip())
        file.close()
        print("Plik został poprawnie uruchomiony!")
    except FileNotFoundError:
        return

# open_file()

while True:
    print()
    month = str(input("Wybierz miesiąc [1-12]: "))

    if month == "1":
        print("Wybrano: styczeń")
    elif month == "2":
        print("Wybrano: luty")
    elif month == "3":
        print("Wybrano: marzec")
    elif month == "4":
        print("Wybrano: kwiecień")
    elif month == "5":
        print("Wybrano: maj")
    elif month == "6":
        print("Wybrano: czerwiec")
    elif month == "7":
        print("Wybrano: liepic")
    elif month == "8":
        print("Wybrano: sierpień")
    elif month == "9":
        print("Wybrano: wrzesień")
    elif month == "10":
        print("Wybrano: październik")
    elif month == "11":
        print("Wybrano: listopad")
    elif month == "12":
        print("Wybrano: grudzień")
    else:
        print("Wpisano nieprawidłową wartość. Wpisz ponownie: ")
        continue

    while True:
        print()
        print("0. Powrót do wyboru miesiąca.")
        print("1. Wyświetl wszystkie wydatki.")
        print("2. Dodaj wydatek.")
        print("3. Statystyki.")
        print("4. Zapisz plik.")
        print("5. Otwórz plik.")
        choice = input("Wybierz opcję: ")

        if choice == "0":
            break

        if choice == "1":
            show_expenses(month)

        if choice == "2":
            add_expense(month)

        if choice == "3":
            show_stats(month)
        
        if choice == "4":
            save_file()

        if choice == "5":
            open_file()

        else:
            print("Wpisano nieprawidłową wartość. Spróbuj ponownie.")
            continue
    

    # DO USTODKONALENIA:
    # done 1. walidacja danych
    # 2. rozbudowanie statystyk - sortowanie wydatków
    # done 3. przypisać miesiącom ich nazwy
    # 4. zapis danych do pliku i jego import 
    # 5. Zakrąglanie liczb do 2 miejsc po przecinku








       
    # if month is not int:
    #    print("Wpisano nieprawidłową wartość. Wpisz ponownie: ")
    #    continue

    # if month != range (1, 12, 1): 
    #     print("Wpisano nieprawidłową wartość. Wpisz ponownie: ")
    #     continue

    # if month != 1 or month != 2 or month != 3 or month != 4 or month != 5 or month != 6 or month != 7 or month != 8 or month !=9 or month != 10 or month != 11 or month != 12:
    #    print("Wpisano nieprawidłową wartość. Wpisz ponownie: ")
    #    continue

    # if month == "1" or month == "2" or month == "3" or month == "4" or month == "5" or month == "6" or month == "7" or month == "8" or month == "9" or month == "10" or month == "11" or month == "12":
    #    break

    # if month != "1" or month != "2" or month != "3" or month != "4" or month != "5" or month != "6" or month != "7" or month != "8" or month !="9" or month != "10" or month != "11" or month != "12":
    #    print("Wpisano nieprawidłową wartość. Wpisz ponownie: ")
    #    continue
