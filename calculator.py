# def binary_calculator(bin1, bin2, operator):

# binary_to_decimal
import math
operator = "-"
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

# Operator
if operator == "+":
    thetotal = total + total2
else:
    if operator == "-":
            thetotal = total - total2
    else:
         if operator == "/" and bin2 == ("00000000"):
            print("NaN")
         else:
            if operator == "/":
                thetotal = total / total2
                thetotal = math.floor(thetotal)
            else:
                if operator == "*":
                    thetotal = total * total2

if thetotal > 255:
    print("Overflow")
else:
    if thetotal < 0:
        print("Overflow")
    else:
    #    print(thetotal)

# decimal_to_binary 
        response = "00000000"

        if thetotal == 0:
            print(response)
        else:

            
            # 128 >= 128 - 128 = 0, 0 >= 64? no, move to the next (leave as "0"), 32, 16, 8, 4, 2, 1
            # if thetotal >= 128 then response[0] = "1", thetotal -= 128, 