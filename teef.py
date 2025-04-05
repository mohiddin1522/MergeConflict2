try:
    num = int(input("Enter a number: "))
    result = 10/num
except ValueError as e:
    print(f"invalid input: {e}")
except ZeroDivisionError as e:
    print(f"cannot divide by zero: {e}") 
except Exception as e: 
    print(f"An unexcepted: {e}")


else:
    print(f"Result: {result}")

finally:
    print("Execution completed")