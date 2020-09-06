print('Enter 10 integers:')
int_list = []

# while loop that accepts integer input from user and stops after 10
# sends error if not integer and prompts to try again

counter = 0
while len(int_list) < 9:
    try:
        while True:
            int_list.append(int(input()))
            counter += 1
            if counter >= 10:
                break

    except ValueError:
        print("This is not an integer. Please enter a valid number")

def min_op(x):    # function to find min value 
    min_value = x[0]
    for i in x[0:]:
        if i < min_value:
          min_value = i
    return min_value
	
def max_op(x):    # function to find max value
    max_value = x[0]
    for i in x[0:]:
        if i > max_value:
          max_value = i
    return max_value
	
# loop to add all elements in list and divide by number of elements
# finds average
	
sum = 0
for i in int_list:
  sum += i
mean = sum / len(int_list)

# loop to find variance
# subtracts the mean from each value in int_list. Squares it. Adds all results together and divides by # of elements in int_list

plus = 0
for i in int_list:
  plus += ((i - mean) ** 2)
variance = plus / len(int_list) 

deviation = variance ** 0.5    # finds standard deviation

minimum = min_op(int_list)    # stores result of function min_op in a variable
maximum = max_op(int_list)    # stores result of function max_op in a variable

# prints all stored variables

print('Integer List:', int_list)
print('Minimum:', minimum)
print('Maximum:', maximum)
print('Range:', minimum, "-", maximum)
print('Mean:', mean)
print('Variance:', variance)
print('Standard Deviation:', deviation)














