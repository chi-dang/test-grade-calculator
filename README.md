# Test Grade Calculator
![Calculator](https://mypercentcalculator.com/images/grade-calculator.png)
<br>**Overview**:
<br>This project, named "Test Grade Calculator", is designed to calculate and analyze test scores for Many classes. The purpose of this program is to help the grading process and save time.
***
## Project Requirements
Python version 3.9 is required.
## Installation Libraries 
```bash
import re
import statistics
```
**Note**: 
>`re` module provides functions, which can be used to work with Regular Expressions.
`statistic` module provides functions to calculate mathematical statistics of numeric data.
## Usage
- Save the script as lastname_firstname_grade_the_exams.py, and make sure that this source code file is in the same directory as the data files.
- Run the script by executing python lastname_firstname_grade_the_exams.py (i.e: in visual studio code)
- Enter the name of the file (without the .txt extension) Or enter e to exist the program.
- The script will generate a brief report with statistics (such as median, mean, highest point, lowest point,,,) and then the program will Write the results to a new file with the same name as the corresponding input file but with a _grade.txt extension.
### Function
**The following functions are defined to use in the main program**:

- read_file(): Reads a text file and checks for validity.
- is_valid_line(): Checks if a line of data is valid.
- calculate_grade(): Calculates a score for each valid line.
- write_file(): Writes the results to a new file.
- main(): The main function.
