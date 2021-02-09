# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

"""
Refactoring plan:
Split the function into smaller functions.
- one function for performing calculations
- one function for receiving userinput
- one function for displaying output
"""

def get_userinput():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    
    return grade_list

def find_mean(grade_list):
    # Calculate the mean of the grades
    sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum = sum + grade
    mean = sum / len(grade_list)
    return mean

def find_sd(grade_list, mean):
    # Calculate the standard deviation of the grades
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd
    # print out the mean and standard deviation in a nice format.
    
def display_calculations(grade_list):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", find_mean(grade_list))
    print('The population standard deviation of grades is: ', round(find_sd(grade_list, find_mean(grade_list)), 3))
    print('****** END ******')

gradelist = get_userinput()
mean = find_mean(gradelist)
sd = find_sd(gradelist, mean)
display_calculations(gradelist)

