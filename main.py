import os

# Function to get a valid filename from the user
def get_valid_filename(prompt):
    while True:
        filename = input(prompt)
        if os.path.exists(filename):
            return filename
        else:
            print(f"File '{filename}' not found. Please try again.")

# Function to read data from a CSV file into a list of lists
def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

# Function to calculate profits and write data to an output file
def calculate_and_write_data(input_data, output_filename):
    output_data = []
    highest_profit = None
    lowest_profit = None

    for row in input_data:
        try:
            # Extracting required fields
            title = row[1]
            budget = int(row[2])
            worldwide_gross = int(row[4])
            # Calculate profit
            profit = worldwide_gross - budget
            row.append(str(profit))

            # Track highest and lowest profit
            if highest_profit is None or profit > highest_profit[-1]:
                highest_profit = row + [profit]
            if lowest_profit is None or profit < lowest_profit[-1]:
                lowest_profit = row + [profit]

            output_data.append(row)
        except (ValueError, IndexError):
            print(f"Error processing row: {row}")

    # Write output to a new CSV file
    with open(output_filename, 'w') as file:
        for row in output_data:
            file.write(','.join(row) + '\n')

    return highest_profit, lowest_profit

# Main function to drive the program
def main():
    print("Movie Profit Analysis")

    # Get filenames from the user
    input_filename = get_valid_filename("Enter the input CSV filename: ")
    output_filename = input("Enter the output CSV filename: ")
    # Read data from input file
    movie_data = read_data(input_filename)
    # Calculate profits and write to output file
    highest_profit, lowest_profit = calculate_and_write_data(movie_data, output_filename)

    # Display the result to the user
    choice = input("Do you want to see the movie with the highest (H) or lowest (L) profit? ").strip().upper()
    if choice == 'H' and highest_profit:
        print("Movie with the highest profit:")
        print(f"Title: {highest_profit[1]}, Profit: {highest_profit[-1]}, Data: {highest_profit}")
    elif choice == 'L' and lowest_profit:
        print("Movie with the lowest profit:")
        print(f"Title: {lowest_profit[1]}, Profit: {lowest_profit[-1]}, Data: {lowest_profit}")
    else:
        print("Invalid choice or no data available.")

# Run the main function
if __name__ == "__main__":
    main()
