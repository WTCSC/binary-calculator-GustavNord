def binary_calculator(bin1, bin2, operator):
    import math
    Error = "Error"

    # Setting the total values for both the binary inputs.
    total = 0
    total2 = 0

    # Converts bin1 to decimal.
    length = len(bin1) - 1
    for index, digit in enumerate(bin1):
        value = 2**(length - index) # Calculates Value.
        if digit == "0":
            pass # Skip if the digit is zero.
        else:
            if digit == "1":
                total = total + value # Add the value if the digit is one.
            else:
                return Error # Return an error if the digit is not a one or zero.
                exit()
        # Converts bin2 to decimal
    length2 = len(bin2) - 1
    for index2, digit2 in enumerate(bin2):
        value2 = 2**(length2 - index2) # Calculates Value for bin2.
        if digit2 == "0": 
            pass # Skips if the digit is zero.
        else:
            if digit2 == "1":
                total2 = total2 + value2 # Add the value if the digit is one.
            else:
                return Error # Return an error if the digit is not a one or zero.
                exit()
    # Performs the arithmetic operation.
    if operator == "+": # Addition.
        thetotal = total + total2
    else:
        if operator == "-": # Subtraction.
                thetotal = total - total2
        else:
            if operator == "/" and bin2 == ("00000000"): # Handles being devided by a zero.
                return "NaN"
            else:
                if operator == "/": # Division.
                    thetotal = total / total2
                    thetotal = math.floor(thetotal)
                else:
                    if operator == "*": # Multiplication. 
                        thetotal = total * total2
    if thetotal > 255: # Make sure it\s not an Overflow.
        return "Overflow"
    else:
        if thetotal < 0: # Make sure it\s not an Overflow.
            return "Overflow"
        else:
            # Creates a representation of the 8 bit binary string.
            response = "00000000"
            response_list = list(response)
            if thetotal == 0:
                return response
            else:
                # Sets the binary digits based on the total
                if thetotal >= 128:
                    response_list[0] = "1"
                    thetotal = thetotal - 128

                if thetotal >= 64:
                    response_list[1] = "1"
                    thetotal = thetotal - 64
                    
                if thetotal >= 32:
                    response_list[2] = "1"
                    thetotal = thetotal - 32
                        
                if thetotal >= 16:
                    response_list[3] = "1"
                    thetotal = thetotal - 16
                            
                if thetotal >= 8:
                    response_list[4] = "1"
                    thetotal = thetotal - 8
                                
                if thetotal >= 4:
                    response_list[5] = "1"
                    thetotal = thetotal - 4
                                
                if thetotal >= 2:
                    response_list[6] = "1"
                    thetotal = thetotal - 2
                                        
                if thetotal >= 1:
                    response_list[7] = "1"
                    thetotal = thetotal - 1
    # Joins the response list and returns response                
    response = ''.join(response_list)
    return response
