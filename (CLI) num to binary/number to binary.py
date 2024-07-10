def reverse(sequence):
    return sequence[::-1] # revercing by creating a new sequence that starts "from the end of the string" and ends "at the beginning of the old string"

def binary(num):
    answer = "" # creating an empty string to store the binary number
    # creating a loop to convert the number to binary
    while num != 0: 
        if num % 2 == 0:
            i="0"
        elif num % 2 == 1:
            i="1"
        num = num // 2
        answer += i
    answer = reverse(answer) # reversing the string to get the correct binary number
    answer = int(answer) # converting string data type to integer data type
    print("Your number in binary is: ", answer)

# same logic as binary function
def octal(num):
    answer = "" 
    while num != 0:
        i = str(num % 8)
        num = num // 8
        answer += i
    answer = reverse(answer) 
    answer = int(answer) 
    print("Your number in octal is: ", answer)

# same logic as binary and octal function
def hexadecimal(num):
    hex_values = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    answer = ""
    while num != 0:
        if num % 16 < 10:
            i = str(num % 16)
        else:
            i = hex_values[num % 16]
        num = num // 16
        answer += i
    answer = reverse(answer)
    answer = int(answer)
    print("Your number in hexadecimal is: ", answer)

system = input("Enter the number system you want to convert to binary(2), hexadecimal(16) or octal(8): ")
system = system.lower()

num = int(input("Enter a number: "))

if system == "hexadecimal" or system == "16":
    hexadecimal(num)
elif system == "binary" or system == "2":
    binary(num) 
elif system == "octal" or system == "8":
    octal(num)
