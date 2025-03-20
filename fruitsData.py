def main():
    # Initialize an empty dictionary to store fruit data
    
    fruitsDictionary = {}

    # Get the number of fruits to input (input statement). This will be the 
    # number of sets of data you need to collect.
    
    fruits_number = int(input("Please request the desired amount of fruits you'd like to see: "))

    

    # Collect data for the number of fruits above from the user. Should include name, color, 
    # weight in lbs, and price. Once each set of data points is collected
    # Think about what kind of control structure to create to complete this process
    for x in range (fruits_number):
        name = input(f"Enter the fruits name: ").strip()
        color = input(f"Enter the color of {name}: ").strip()
        weight = float(input(f"Enter the average weight of {name} (in lbs): ")) 
        price = float(input(f"Enter in the average price per pound of {name} ($): "))

        # Data storage...wowza.............
        fruit[name] = {
            'Color': color, 
            'Average Weight': weight,
            'Price Per Pound': price
        }

    # Output the fruit data 
        # After each set of input statements, store the data in the dictionary
    print("\n Fruit Data Overview:\n")   

    print(fruitsBasket['Fruits'])

    for fruit, details in fruits.item():
        print(f"Fruit: {fruit}")
        print(f"Color: {details['Color']}")
        print(f"Average Weight: {details['Average Weight']}")
        print(f"Price Per Pound: $ {details['Price Per Pound']}")
        print("-" * 20)


    

    # Output each of the fruit's data as a vertical list. This happens one time
    # for each of the fruits in the dictionary. 
    

if __name__ == "__main__":
    main()

