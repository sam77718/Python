    # 🟢 Next Level — Exception Handling Q1

    # Write a function:

    # safe_sqrt(x)

    # Requirements:

    # If x >= 0 → print the square root.
    # If x < 0 → print:
    # Cannot find square root of negative number
    # If the input is not a number, handle the error and print:



def safe_sqrt(x):
    try:
        if int(x) >= 0:
            print(f"The square root of {x} is {int(x) ** 0.5}")
        else:
            print("Cannot find square root of negative number")

    # except ValueError:
    #     print("Error: Input is not a number")

    except Exception as e:
        print(f"Error: Input is not a number : {e}")

    finally:
        print("Execution completed.")    


num=safe_sqrt(99)
print(num)        



        