import re
import statistics


#Define a function that allows the user to enter the name of a file and access it for reading.
def read_file():
    while True:
        try:
            filenames = input("Please enter a class file to grade or press 'e' to exit: ")
            #if the user enter 'e', the function will return None for both filenames and lines
            if filenames == "e":
                return None, None
            file = filenames.lower() + ".txt"
            #User has to enter correct file name without .txt extension
            #Prompt the user re-enter the name of file again, if failing.
            #Use try-except for error handling
            if re.match("^class[1-8]", file):
                try:
                    with open(file, "r") as f:
                        lines = f.readlines()
                        print(f"\nsuccessfully opened {file}!! \n")
                        print(f"**** ANALYZING **** \n")
                        return filenames, lines
                except FileNotFoundError as e:  
                    print(e)
            else:
                print(f"\nFile {file} can not found")
        # Add "except exception" (not just filenotfounderror) that might occur during file processing.
        except Exception as e:
            print(f"\nAn Error occurred", e)


    #Returning None, None in this case helps maintain consistency in the return value.
        return None, None

# Define a function to check the valid data contained
def is_valid_line(line):
    value_ = line.strip().split(",")

    for i in range(len(value_)):
        #Replace blank value by NA to avoid missing them when checking
        if value_[i] == "":
            value_[i] = "NA"

    student_id = value_[0]

    #A valid line contains a comma-separated list of 26 values.
    if len(value_) == 26:
        #N for a student is the first item on the line. It must contain the character “N” followed by 8 numeric characters.
        if re.match('^N\d{8}', student_id):
            return True
        else:
            print(f"Invalid line of data: N# is invalid: \n")
            print(f"{line.strip()} \n")     
    else:
        print(f"Invalid line of data: does not contain exactly 26 values: \n")
        print(f"{line.strip()} \n")

# Define a function to calculate a score for each valid line. 
def calculate_grade(answer_key, student_answer):
    #initialize a variable score to 0 to keep track of the scores
    score = 0
    #iterate through the answer_key list
    for i, answer1 in enumerate(answer_key):
        #if the answer is blank, the score remains unchanged (+0)
        if student_answer[i] == "":
            score += 0
        #if the answer matches the correct answer key, the score is increased by 4 
        elif student_answer[i] == answer1:
            score += 4
        #if the answer does not match the correct answer key, the score is decreased by 1
        else:
            score -= 1

    return score

# Define a function to write result to file:
def write_file(filenames, valid_lines_, value_, scores_):
    #create new output file with '_grade.txt' extension if it does not exist already.
    output_filename = filenames + '_grade.txt'
    with open(output_filename, "w") as output_file:
        output_file.write("Student_id, score\n")
        for m in range(len(valid_lines_)):
            output_file.write(f"{value_[0]}, {scores_[m]}\n")


def main():

    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key_lis = answer_key.split(",")

    #Infinite loop until exiting the program
    while True:
        #Inside the loop, calling read_file() function, which is defined earlier.
        filenames, lines = read_file()
        #Checking for exit condition, if both filenames and lines are None, it returns None
        if filenames == None and lines == None:
            print("Exiting the program. Goodbye!")
            return None, None

        #Processing the file
        #Initialize the following variables:

        valid_lines = 0                     #count the number of valid lines
        valid_lines_ = []                   #create an empty list to store the valid line numbers
        scores_ = []                        #Create an empty list to store the scores for each valid line
        #a list of 25 zeros to count the number of skipped questions for each question
        skipped_ques = [0]*25
        #a list of 25 zeros to count the number of incorrect answers for each question
        incorrect_ques = [0]*25

        for line in lines:
            #For each line, it checks if the line is valid using the is_valid_line function.
            if is_valid_line(line):
                #if it is valid line:
                # increase 1 incrementally for each valid line
                valid_lines += 1
                # append the current valid_lines value to the valid_lines_ list.
                valid_lines_.append(valid_lines)
                value_ = line.strip().split(",")
                student_answer = value_[1:]
                #calculates the score for this line using the calculate_grade function, the score is stored in new_score.
                new_score = calculate_grade(answer_key_lis, student_answer)
                #append the new_score to the scores_ list.
                scores_.append(new_score)
                #loop through each answer in student_answer
                for j, answer2 in enumerate(student_answer):
                    if answer2 == "":
                        #if the answer is blank, it is increased by 1 for the corresponding element in skipped_ques.
                        skipped_ques[j] += 1
                    elif answer2 != answer_key_lis[j]:
                        ##if the answer is incorrect, it is increased by 1 for the corresponding element in incorrect_ques.
                        incorrect_ques[j] += 1

        #Calculating Statistics after processing the file
        total_lines = len(lines)
        invalid_lines = total_lines - valid_lines
        if invalid_lines == 0:
           print("No errors found! \n")
               
        print(f"**** REPORT ****\n")
        print(f"Total valid lines of data: {valid_lines}\n")
        print(f"Total invalid lines of data: {invalid_lines}\n")
    
        #calculate the following statistics for each class:
        no_of_std_highest_score = sum(1 for new_score in scores_ if new_score > 80)
        medium_score = round(statistics.mean(scores_),3)
        highest_score = max(scores_)
        lowest_score = min(scores_)
        range_score_value = round(highest_score - lowest_score, 3)
        median_score = statistics.median(scores_)
        most_skipped_ques = max(skipped_ques)
        most_incorrect_count = max(incorrect_ques)
        
        print(f"Number of students with highest score(>80): {no_of_std_highest_score}\n")
        print(f"Average score: {medium_score}\n")
        print(f"highest score: {highest_score}\n")
        print(f"lowest score: {lowest_score}\n")
        print(f"Range of score values(highest minus lowest): {range_score_value}\n")
        print(f"median value: {median_score}\n")

        #return the questions most skipped by students in order:
        print(f"\nThe questions most skipped by students:\n")
        for k, skipped_ques_ in enumerate(skipped_ques, start = 1):
            if skipped_ques_ == most_skipped_ques:
                print(f"{k} - {skipped_ques_} - {round(skipped_ques_/len(lines),3)}")
        #return the questions most incorrect by students in order:
        print("\nThe questions most incorrect by students: \n")
        for l, incorrect_ques_ in enumerate(incorrect_ques, start = 1):
            if incorrect_ques_ == most_incorrect_count:
                print(f"{l} - {incorrect_ques_} - {round(incorrect_ques_/ len(lines), 3)}")

        #Write result (write_file function)
        write_file(filenames, valid_lines_, value_, scores_)


if __name__ == "__main__":
    main()