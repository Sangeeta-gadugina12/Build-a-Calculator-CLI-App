def add (a , b):
    print("addition of two numbers")
    return a + b
def sub(a,b):
    print("subtraction of two numbers")
    return a - b
def mul(a,b):
    print("multiple of two numbers")
    return a * b
def div(a,b):
    print("division of 2 numbers")
    if b == 0:
        return "error :division by zero"
    return a / b

def calculator():
    while True:
        print("\n select an operation:")
        print("1.addtion")
        print("2.subtraction")
        print("3.multiply")
        print("4.division")
        print("5.exit")
        choice = input("\n enter choice(1/2/3/4/5):")

        if choice == 5:
            print("thank you for using the calculator goodbye!")
            break

        if choice not in('1','2','3','4'):
            print("invalid input please enter a valid input(1-5)")
            continue
        try:
            num1 = float(input("enter a first number:"))
            num2 = float(input("enter a second number:"))
        except ValueError:
            print("invalid number please enter a  numeric values")
            continue

        if choice == '1':
            result = add(num1,num2)
            operation = '+'
        elif choice == '2':
            result = sub(num1,num2)
            operation = '-'
        elif choice == '3':
            result = mul(num1,num2)
            operation = '*'
        elif choice == '4':
            result = div(num1,num2)
            operation = '/'

        print(f"\n result:{num1,num2}={result}")

if __name__ == "__main__":
    calculator()