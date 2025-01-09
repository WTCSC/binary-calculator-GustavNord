# Binary Calculator
This code is a calculator that works with two 8-bit binary numbers using the four basic arithmetic operations, (addition, subtraction, division, and multiplication.)

## Features 
Returns `"Error"` for invalid binary inputs (containing characters other than `0` and `1`).

Returns `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).

Handles division by zero by returning `"NaN"`.

Handles decimal numbers by rounding down to the nearest whole number (flooring).

Outputs are returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Implemented own binary-to-decimal and decimal-to-binary conversion logic.

## How it Works
























[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17649999)