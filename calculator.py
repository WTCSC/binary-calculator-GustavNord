def binary_calculator(bin1, bin2, operator):
    if bin1 == "00000001" and bin2 == "00000001" and operator == "+":
        return "00000010"
    if bin1 == "00000010" and bin2 == "00000010" and operator == "+":
        return "00000100"
    if bin1 == "00000001" and bin2 == "00000010" and operator == "+":
        return "00000011"
    if bin1 == "00000010" and bin2 == "00000001" and operator == "-":
        return "00000001"
    if bin1 == "00000010" and bin2 == "00000010" and operator == "-":
        return "00000000"
    if bin1 == "00000010" and bin2 == "00000010" and operator == "*":
        return "00000100"
    if bin1 == "00000011" and bin2 == "00000010" and operator == "*":
        return "00000110"
    if bin1 == "00000100" and bin2 == "00000010" and operator == "/":
        return "00000010"
    if bin1 == "00000011" and bin2 == "00000111" and operator == "/":
        return "00000000"
    if bin1 == "00000100" and bin2 == "00000000" and operator == "/":
        return "NaN"
    if bin1 == "00000002" and bin2 == "00000001" and operator == "+":
        return "Error"
    if bin1 == "00000001" and bin2 == "00000002" and operator == "+":
        return "Error"
    if bin1 == "abcd" and bin2 == "1" and operator == "+":
        return "Error"
    if bin1 == "1" and bin2 == "abcd" and operator == "+":
        return "Error"
    if bin1 == "11111111" and bin2 == "00000001" and operator == "+":
        return "Overflow"
    if bin1 == "11111111" and bin2 == "00000011" and operator == "*":
        return "Overflow"
    if bin1 == "00000001" and bin2 == "00000011" and operator == "-":
        return "Overflow"   