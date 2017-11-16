#!/usr/bin/python3

def main():
    num1 = 42 / 9                  # result as a float
    num2 = 42 // 9                 # result as an integer, remainder dropped
    num3 = round(42 / 9)           # result is rounded to the nearest whole number
    num4 = round(42 / 9, 2)        # result is rounded off to 2 decimal places
    num5 = 42 % 9                  # remainder of the result
    num6 = int(12.2)               # casting to int, the decimal point will be dropped
    num7 = float(12)               # casting to float
    print(type(num1), num1)
    print(type(num2), num2)
    print(type(num3), num3)
    print(type(num4), num4)
    print(type(num5), num5)
    
if __name__ == "__main__": main()
