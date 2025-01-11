# Binary Calculator
This code is a calculator that works with two 8-bit binary numbers using the four basic arithmetic operations, (addition, subtraction, division, and multiplication).

## Features 
Returns `"Error"` for invalid binary inputs (containing characters other than `0` and `1`).

Returns `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).

Handles division by zero by returning `"NaN"`.

Handles decimal numbers by rounding down to the nearest whole number (flooring).

Outputs are returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Implemented own binary-to-decimal and decimal-to-binary conversion logic.

## How it Works 
Each string (`bin1` and `bin2`) is converted to its decimal value by adding up the values of `2^n` for every `1` bit at position `n`. 

The function performs the operation on the two decimal numbers.

Handles the Special Cases like attempt at dividing by zero or overflowing.

If the results are within the range (0-255), this function converts the number to an 8-bit binary string.

## Requirements
Python 3

The `math` module, (should come with Python by default).


## End of README
This `README.md` is a detailed guide on the features, behavior, and requirements for the `calculator.py`. 