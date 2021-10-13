import math

a = int(input("Enter a numerator (Value must be greater than 0): "))
while True:
    if a < 0:
        a = int(input("Please re-enter the numerator (Value must be greater than 0): "))
        continue
    else:
        break

b = int(input("Enter a denominator (Value must be greater than 0): "))
while True:
    if b < 0:
        b = int(input("Please re-enter the denominator (Value must be greater than 0): "))
        continue
    else:
        if b > a:
            print(f"{a}/{b} is a proper fraction.")
            x = math.gcd(a,b)
            int(x)
            if x != 1:     
                m = a / x
                n = b / x
                m = int(m)
                n = int(n)
                print(f"This proper fraction can be reduced to: {m}/{n}")
                break
            else:
                print("This proper fraction cannot be reduced any further.")
                break
        else:
            print(f"{a}/{b} is an improper fraction.")
            x = math.gcd(a,b)
            int(x)
            if x != 1:     
                m = a / x
                n = b / x
                m = int(m)
                n = int(n)
                print(f"This improper fraction can be reduced to: {m}/{n}")
                p = m // n
                o = m % n
                print(f"The mixed number is {p} and {o}/{n}")
                break
            else:
                print("This improper fraction cannot be reduced any further.")
                p = a // b
                o = a % b
                print(o)
                if o != 0:
                    print(f"The mixed number is {p} and {o}/{b}")
                    break
                else:
                    print(f"The whole number is {p}")
                    break