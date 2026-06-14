try:
    x =int(input("Enter x : "))
    y =int(input("Enter y : "))

    z=x/y
    print(f"Result : {z}")

except ValueError:
    print("Invaild input..")


except ZeroDivisionError:
    print("Division by zero error...")


except Exception as e:
    print(f"Someting unexpected happened {e}")

finally:
    print("Execution complete...")