try:
    x = 10/0
except Exception as e:
    print(e)
    
finally:
    print("This will always execute")
    
