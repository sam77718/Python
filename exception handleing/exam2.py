# 🟡 Exception Handling Q2

# Use Pandas to read:

# sales.csv

# Requirements:

# If the file exists → display the rows.
# If the file doesn't exist → print:
# Sales file missing!

# Use try-except.




try:
    import pandas as pd

    df = pd.read_csv("C:\\Users\\Samarth\\.vscode\\Python\\sales.csv",encoding="latin1")
    print(df)

except Exception as e:
    print("Error:", e)

finally:
    print("Execution completed.")