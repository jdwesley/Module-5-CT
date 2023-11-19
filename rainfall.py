#create a function to select the years to be iterated over
def get_valid_years():
#create while loop to define valid integers for input
    while True:
        try:
            #ask for value to assign to variable years
            years = int(input('Enter the number of years you wish to record, up to but no more than 10: '))
            #clarify what integers satify true
            if 1 <= years <= 10:
                return years
            else: 
                print('The number is not not valid! Please enter a number between 1 and.')
        except ValueError:
            print('Incorrect figure! Please enter a number.')

def main():
#initialize variables 
    total_rainfall = 0
    total_months = 0
    #call get_valid_years function and set equal to years in main function
    years = get_valid_years()
    # loop iterates years from 0 to value of varible year +1(python starts at zero)
    for year in range(1, years + 1):
        #nested loop iterates months 1 through 12
        for month in range(1, 13):
            #while itertation is true enter rainfall total for specify year and month combo assinged to rainfall total
            while True:
                try: 
                    rainfall_totals = float(input(f'Enter the amount of rainfall in inches for the Year {year} and Month {month}: '))
                    break
                    
                except ValueError:
                    print('You entered a invalid figure. Please enter a number.')
                
            #set total rainfall equal to sum of rainfall_totals
            total_rainfall += rainfall_totals
            #add 1 to total months and assign to total months
            total_months += 1
            #create avaerage rainfall by division
            average_rainfall = total_rainfall/total_months
            #print a space and calculated variables
            print('\n')
            print(f'Total months: {total_months}')
            print(f'Total rainfall : {total_rainfall:.3f}')
            print(f'Average rainfall per month: {average_rainfall:.3f}')


if __name__ == "__main__":
    main()
