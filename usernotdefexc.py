class NotEligible(Exception):
    pass
def checkage(age):
    if age < 18:
        raise NotEligible("not eligible")
    else:
        print("eligible")
try:
    age = int(input("Enter your age: "))
    checkage(age)
except NotEligible as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")    