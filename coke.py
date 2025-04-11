def main():
    cost = 50
    # list of valid coins
    valid_input = [50, 25, 10, 5]
    # loop until the user has inserted enough coins
    while cost > 0:
        # print the balance amount due
        print(f"Amount Due: {cost}")
        # prompt the user to insert coin
        coin = int(input("Insert Coin: "))
        # check if the coin is valid
        if coin in valid_input:
            # subtract the the value of the coin from the cost
            cost -= coin
        # otherwise, if the coin is not valid
        else:
            # prompt the user to insert a valid coin
            print("Invalid coin. Please insert a valid coin such as 50, 25, 10 and 5.")
            # go back to the beginning of the loop
            continue
   
    # calculate the change owed
    change_owed = abs(cost)
    print(f"Changed Owed: {change_owed}")

# call the main function
if __name__ == "__main__":
    main()
    

