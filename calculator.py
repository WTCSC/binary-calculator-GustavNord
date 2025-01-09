# def binary_calculator(bin1, bin2, operator):

# binary_to_decimal
bin1 = "00000001"
Error = "Error"
length = len(bin1) - 1
for index, digit in enumerate(bin1):
    print(f"Index: {index}, Digit: {digit}, Power: {length - index}, Value: {2**(length - index)}")

    value = {2**(length - index)}
    if digit == "0":
     pass
    else:
        if digit == "1":
          digit = value
        else:
          print(Error)
          exit()

print(digit)


    # if digit is 1, add "Value ^" to a total, else if 0 do nothing, else return "Error"







    

    # decimal_to_binary = 

    # answer.floor()
    # if bin2 == "00000000" and operator = "/"
    # return "NaN"

    # if answer > 256
    #return "Overflow"

    # if answer < 0
    # return "Overflow"
