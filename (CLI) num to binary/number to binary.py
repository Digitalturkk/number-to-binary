def reverse(sequence):
    return sequence[::-1] # revercing by creating a new sequence that starts "from the end of the string" and ends "at the beginning of the old string"

num = int(input("Enter a number: ")) # taking input from the user
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