# define the main function to execute the program
def main():
    # prompt the user for a variable name in camelCase
    camelCase = input("camelCase: ")
    # convert the variable name to snake_case
    snake_case = convert_to_snake_case(camelCase)
    # print the converted variable name
    print(f"snake_case: {snake_case}")

# define a function to convert camelCase to snake_case
def convert_to_snake_case(text):
    # create an empty variable to store every character
    result = ""
    # iterate through each character in the input text
    for char in text:
        # check if the character is uppercase
        if char.isupper():
            # append an underscore followed by the lowercase version of char to result
            result += "_" + char.lower()
        # if character is not uppercase
        else:
            # return the char as it is
            result += char
        # return the modified text
    return result

# call the main function to execute the program
if __name__ == "__main__":
    main()


