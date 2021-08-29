# TripleX Python
Triplex is a Terminal game created by [Eslam Shukri](https://github.com/DEVEslamisHere)

Concept taken form the [Udemy Course](https://www.udemy.com/course/unrealcourse)

In the course, the game was created in [C++](https://github.com/DEVEslamisHere/TripleX-Cpp) and I did all the steps and created it myself. Then, I created it again in [Python](https://github.com/DEVEslamisHere/TripleX-Python). The story is as follows: You are a secret agent " your task is to break into a secure server and get some files. you need to guess 3 numbers that their sum and product are equal to the values displayed to pass the current level. solve these mathematical problems until you reach the final level which is level 5 by default.

## C++ vs Python
There is some differences between the C++ version and Python version.

### Python
In Python, when you get an input from the player by calling `input()`, it will always return a string even if the player entered just numbers. So you have to split input into a list. Then check if the list length is 3 as there are just 3 numbers needed to be guessed. Then check if it's just numbers, and finally calculate the sum and product.

### C++
This is not quite like C++ as the following code `std::cin.clear()` clear the error flag on cin. For example, if the value that will be stored as an input is an integer, and the player entered a character, the code will not raise an error, and `std::cin.ignore()` skips to next line to ignore anything else on the previous line. So, it won't cause any other parse failure.

### Pros of the Python Version
The Python version is more optimized as it will alert you on an invalid format, Telling you to type in the form of `X X X`, or if you entered characters rather than numbers, it will alert you too.
