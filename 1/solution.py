f = open("input.txt", "r")
numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

inputs = f.readlines()
sum = 0
for input in inputs:
    first = 0
    last = 0
    #print("analyzing input: " + input)
    while(len(input) > 0):
        char = input[0]
        #print("analyzing char: " + char)
        if(char.isdigit()):
            digit = ord(char) - ord('0')
            if(last == 0):
                first = last = digit
            else:
                last = digit
            input = input[1:]
        else:
            for index, num in enumerate(numbers):
                if(input.startswith(num)):
                    digit = index + 1
                    if(last == 0):
                        first = last = digit
                    else:
                        last = digit
                    input = input[len(num)-1:]
                    break
            input = input[1:]
                    
            
    #print("first: " + str(first) + ", last: " + str(last) + ", sum:" + str(sum))
    sum += (first * 10) + last


print("solution: " + str(sum))