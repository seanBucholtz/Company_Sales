# Sean Bucholtz
# CSC 110
# Section 3
# 5/31/13
# Assinment #7


def numbers():
    print("Please enter all of the monthly sales amounts for each" +\
          " of the divisions. Enter a negative number to finish.")
    number_list = []
    number = float(input("\nDivision sales amount: "))
    while number >= 0:
        
        number_list.append(number)
        number = float(input("\nDivision sales amount: "))

    return number_list

def numbers_string(numbers):
    
    string = ""

    for num in range(len(numbers)):
        
        string += (str(numbers[num]) + " ")

    return string
        
def max2(numbers):
    
    largest = [numbers[0]]
    
    for num in range(1,len(numbers)):
                
        if numbers[num] > largest[0]:
            
            largest = [numbers[num]]
            
    return largest

def min2(numbers):
    
    lowest = [numbers[0]]
    
    for num in range(1,len(numbers)):
                
        if numbers[num] < lowest[0]:
            
            lowest = [numbers[num]]
            
    return lowest
    
def sum2(numbers):
    
    num_total = 0
    
    for num in range(len(numbers)):
        
        num_total += numbers[num]
        
    return num_total

def award(numbers, threshold):
    
    win = []
    
    for num in range(len(numbers)):

        if numbers[num] >= threshold:

            win.append(numbers[num])

    return win

def main():
    x = numbers() # receives intial list values

    print("\n" + str(x))
    string_nums = (numbers_string(x)) # float-to-string converter
                                      # function definition
    print("\n" + string_nums + "is " + str(type(string_nums)))

    print("\nThe heighest number in the list is: " + str(max(x)))
    large = max2(x) # max function definition
    print("\nAgain, the largest number in the list is: " + str(large[0]))
     

    print("\nThe lowest number in the list is: " + str(min(x)))
    minim = min2(x) # min function
    print("\nAgain, the lowest number in the list is: " + str(minim[0]))
    

    print("\nThe total sales for the company in one month is: " + str(sum(x)))
    total = sum2(x) # sum function
    print("\nAgain, the total sales for the company in one month is: " + \
          str(total))

    print("\nThe average sales for the month is: " + str((sum(x)/len(x))))
    print("\nAgain, the average sales for the month is: " + \
          str((total/len(x)))) # average using function

    min_sale = float(input("\n\nWhat would you like the top sales" + \
                               "threshold to?: ")) # threshold
    winners = award(x, min_sale)
    print("\nThe top sales amounts are: " + str(winners))
    print("\n\nGoodbye")


main()

"""
- TESTING -

All function definitions appear to be working properly.

Inputs: [1,2,3,4,5,6,7,8,9,10]

Results:

- Float to string function definition matches that of the print output.
    type() validates this
- Max2 function matches the print output using native max() function.
    10.0:10.0
- Min2 function matches the print output using native min() function.
    1.0:1.0
- Sum2 function matches the print output using native sum() function.
    55.0:55.0
  and corresponds to externally verified calculations
- Sale averages match externally verified calculations.
    5.5:5.5
- Sale volume validation function returns as expected.
    threshold = 5
    return = [4.0,5.0,6.0,7.0,8.0,9.0,10.0]

END of TESTING.

"""
        
        
        
