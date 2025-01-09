def binary_calculator(bin1, bin2, operator):
    import math
    Error = "Error"
    total = 0
    total2 = 0
    length = len(bin1) - 1
    for index, digit in enumerate(bin1):
        value = 2**(length - index)
        if digit == "0":
            pass
        else:
            if digit == "1":
                total = total + value
            else:
                return Error
                exit()
    length2 = len(bin2) - 1
    for index2, digit2 in enumerate(bin2):
        value2 = 2**(length2 - index2)
        if digit2 == "0":
            pass
        else:
            if digit2 == "1":
                total2 = total2 + value2
            else:
                return Error
                exit()
    if operator == "+":
        thetotal = total + total2
    else:
        if operator == "-":
                thetotal = total - total2
        else:
            if operator == "/" and bin2 == ("00000000"):
                return "NaN"
            else:
                if operator == "/":
                    thetotal = total / total2
                    thetotal = math.floor(thetotal)
                else:
                    if operator == "*":
                        thetotal = total * total2
    if thetotal > 255:
        return "Overflow"
    else:
        if thetotal < 0:
            return "Overflow"
        else:
            response = "00000000"
            response_list = list(response)
            if thetotal == 0:
                return response
            else:
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
    response = ''.join(response_list)
    return response


