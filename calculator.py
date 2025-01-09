# def binary_calculator(bin1, bin2, operator):

# binary_to_decimal
operator = "+"
bin1 = "01000001"
Error = "Error"
total = 0
total2 = 0
length = len(bin1) - 1
for index, digit in enumerate(bin1):
   # print(f"Index: {index}, Digit: {digit}, Power: {length - index}, Value: {2**(length - index)}")
    value = 2**(length - index)
    if digit == "0":
     pass
    else:
        if digit == "1":
          total = total + value
        else:
          print(Error)
          exit()

bin2 = "01000001"
length2 = len(bin2) - 1
for index2, digit2 in enumerate(bin2):
    # print(f"Index: {index2}, Digit: {digit2}, Power: {length2 - index2}, Value: {2**(length2 - index2)}")
    value2 = 2**(length2 - index2)
    if digit2 == "0":
     pass
    else:
        if digit2 == "1":
          total2 = total2 + value2
        else:
          print(Error)
          exit()

print(total, operator, total2)

    # if digit is 1, add "Value ^" to a total, else if 0 do nothing, else return "Error"







    

    # decimal_to_binary = 

    # answer.floor()
    # if bin2 == "00000000" and operator = "/"
    # return "NaN"

    # if answer > 256
    #return "Overflow"

    # if answer < 0
    # return "Overflow"
