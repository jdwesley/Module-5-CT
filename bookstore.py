#create main function
def main():
#create a variable, prompt and assign a integer input
    num_books = int(input("Enter the number of books purchased this month: "))
 
#create logical statements to define the number of points awarded for the variable value and print the associatd points
    if (num_books < 2):
            print("Points = 0")
    elif (num_books >= 2 and num_books < 4):
            print("Points = 5")
    elif (num_books >= 4 and num_books < 6):
            print("Points = 15")
    elif (num_books >= 6 and num_books < 8):
            print("Points = 30")
    elif (num_books >= 8):
            print("Points = 60")


#create while loop to call main() and repeat the function    
while True:
    main()
    if input("Repeat the program? (Y/N)") != 'Y':
        break
        



    

            

     
        

    

        



