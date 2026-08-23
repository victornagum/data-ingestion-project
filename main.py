import pandas as pd, glob

# Find CSV files
files = glob.glob("data/*.csv") #Put file paths inside "files"

# Check if there are CSV files
if not files:
    print("No CSV files found.")
    exit()

# Display available files
print("\nAvailable CSV files:") # \n means new line

for i, file in enumerate(files, start=1):
    print(f"{i}. {file}") # f string {} - placeholder

try:
    choice = int(input("Choose a file: "))

    if choice >= 1 and choice <= len(files):
        selected_file = files[choice - 1]
        data = pd.read_csv(selected_file)
        df = pd.DataFrame(data)

        # Display information
        print("\n--- SELECTED FILE ---")
        print(selected_file)

        print("\n--- FIRST 5 ROWS ---")
        print(df.head())

        print("\n--- DATA SIZE ---")
        rows, columns = df.shape
        print("Rows:", rows)
        print("Columns:", columns)

        print("\n--- COLUMNS ---")
        print(df.columns.tolist())

        print("\n--- DATA TYPES ---")
        print(df.dtypes)

        print("\n--- STATISTICS ---")
        print(df.describe())
    else:
        print("Invalid choice.")

except ValueError:
    print("Please enter a number.")






