### Algorithm Document

-------------

* **Purpose**: Get a valid input filename from the user.  
* **Name**: get_valid_filename  
* **Parameters**:  
  - None  
* **Return**:  
  - filename (string): The name of the valid input file provided by the user.  
* **Algorithm**:  
  1. Prompt the user for a filename using the message: "Enter the input CSV filename:".  
  2. While the filename does not exist:  
     1. Display the message: "File '<filename>' not found. Please try again.".  
     2. Re-prompt the user for a filename.  
  3. Return the valid filename.  

-------------

* **Purpose**: Read movie data from a CSV file into a list of lists.  
* **Name**: read_data  
* **Parameters**:  
  - filename (string): The name of the input CSV file.  
* **Return**:  
  - data (list): A list of lists containing rows of movie data.  
* **Algorithm**:  
  1. Open the file specified by filename in read mode.  
  2. Read all lines from the file.  
  3. Strip whitespace and split each line by commas to create a list of lists.  
  4. Close the file.  
  5. Return the data.  

-------------

* **Purpose**: Calculate profits, write data to an output file, and determine movies with the highest and lowest profits.  
* **Name**: calculate_and_write_data  
* **Parameters**:  
  - input_data (list): A list of lists containing movie data.  
  - output_filename (string): The name of the output CSV file.  
* **Return**:  
  - highest_profit (list): The row with the highest profit.  
  - lowest_profit (list): The row with the lowest profit.  
* **Algorithm**:  
  1. Initialize output_data as an empty list, and highest_profit and lowest_profit as None.  
  2. For each row in input_data:  
     1. Try to extract title, budget, and worldwide gross.  
     2. Calculate profit as worldwide_gross - budget.  
     3. Append profit to the row.  
     4. Update highest_profit if the current profit is greater than the current highest.  
     5. Update lowest_profit if the current profit is less than the current lowest.  
     6. Add the updated row to output_data.  
     7. Handle exceptions for invalid data with an error message.  
  3. Open the file specified by output_filename in write mode.  
  4. Write all rows from output_data to the file.  
  5. Close the file.  
  6. Return highest_profit and lowest_profit.  

-------------

* **Purpose**: Manage the program flow.  
* **Name**: main  
* **Parameters**:  
  - None  
* **Return**:  
  - None  
* **Algorithm**:  
  1. Print: "Movie Profit Analysis".  
  2. Call get_valid_filename and store the result in input_filename.  
  3. Prompt the user for the output file name and store it in output_filename.  
  4. Call read_data with input_filename and store the result in movie_data.  
  5. Call calculate_and_write_data with movie_data and output_filename.  
  6. Store the returned values in highest_profit and lowest_profit.  
  7. Prompt the user: "Do you want to see the movie with the highest (H) or lowest (L) profit?".  
  8. If the user selects H and highest_profit exists:  
     1. Print the title, profit, and full row of the movie with the highest profit.  
  9. If the user selects L and lowest_profit exists:  
     1. Print the title, profit, and full row of the movie with the lowest profit.  
  10. Otherwise, print: "Invalid choice or no data available.".  

-------------

1. Call the main function.  
