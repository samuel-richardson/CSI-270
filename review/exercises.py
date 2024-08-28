
def exe_1():
    cost = input("Enter cost: ")
    tax = input("Enter tax as decimal: ")
    final_cost = float(cost) * (1 + float(tax))
    print(final_cost)


def exe_2():
    name = input("Enter your name: ")
    year = input("Enter birth year: ")
    current_year = 2024
    age = current_year-int(year)
    print(f"{name} is {age}.")


def exe_3():
    cost = input("Enter cost: ")
    tax = input("Enter tax as decimal: ")
    number_cards = input("Enter the number of cards: ")
    final_cost = (float(cost) * (1 + float(tax))) * int(number_cards)
    print(final_cost)

def exe_4():
    grades = []
    for i in range(5):
        grade = input(f"{i + 1}) Enter the grade: ")
        grades.append(float(grade))
    max_grades =  max(grades)
    min_grades = min(grades)
    for grade in grades:
        print(grade)
    print(f"Highest Grade: {max_grades}")
    print(f"Lowest Grade: {min_grades}")

def exe_5():
    ints = []
    for i in range(4):
        num = input("Enter an integer: ")
        ints.append(int(num))
    ints.sort()
    ints.reverse()
    print(ints)

def exe_6():
    employees = []
    for i in range(3):
        employee = {}
        salary = int(input(f"Enter employee {i + 1} salary: "))
        duration = int(input(f"Enter employee {i + 1} working years: "))
        employee["id"] = i
        if duration > 10:
            increase = salary + (salary * .10)
        elif duration == 10:
            increase = salary + (salary * .07)
        else:
            increase = salary + (salary * 0.03)
        employee["salary"] = salary
        employee["duration"] = duration
        employee["increase"] = increase
        employees.append(employee)
    print(employees)


def exe_7():
    price = float(input("Enter the price of the car: "))
    years = int(input("enter the number of years: "))
    price_list = []
    for i in range(years):
        price = price * 0.95
        price_list.append(int(price))
    print(price_list)

def exe_8():
    start = int(input("Enter beginning year: "))
    end = int(input("Enter the end year: "))
    data = []
    total = 0
    for year in range(start,end+1):
        sales = float(input(f"Enter {year} sales: "))
        data.append((year, sales))
        total += sales
    average = total / (end + 1 - start)
    print("Year \t Sales")
    for d in data:
        print(f"{d[0]} \t {d[1]}")
    print(f"AVG \t {average}")


splash = """
Enter the number of the exercise to run(1,2,3,4,5,6,7,8 or 9 to exit:
"""

while True:
    selection = input(splash)
    if selection in "1":
        exe_1()
    if selection in "2":
        exe_2()
    if selection in "3":
        exe_3()
    if selection in "4":
        exe_4()
    if selection in "5":
        exe_5()
    if selection in "6":
        exe_6()
    if selection in "7":
        exe_7()
    if selection in "8":
        exe_8()
    if selection in "9":
        break
