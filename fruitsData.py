def main():
    # Initialize an empty dictionary to store fruit data
    
    fruitsDictionary = []

    # Get the number of fruits to input (input statement). This will be the 
    # number of sets of data you need to collect.
    
    fruits_number = int(input("Please request the desired amount of fruits you'd like to see: "))

    

    # Collect data for the number of fruits above from the user. Should include name, color, 
    # weight in lbs, and price. Once each set of data points is collected
    # Think about what kind of control structure to create to complete this process
    fruitsBasket = {'Fruits': "Apple: 70-100 grams, often coming in shades of red, green or sometimes yellow." }
    
        # After each set of input statements, store the data in the dictionary
        

    print(fruitsBasket['Fruits'])

    

    # Output each of the fruit's data as a vertical list. This happens one time
    # for each of the fruits in the dictionary. 
    

if __name__ == "__main__":
    main()

