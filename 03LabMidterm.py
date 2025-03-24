
ex1 = 3 ** 2 ** 2
# Correct Answer: 81
ex1_1 = 2 ** 2
# output: 4 which means 3 ** 4 would be 81 which is the right answer
ex1_2 = 3 ** 2
# output: 27 which means that 27 ** 2 would give the wrong answer, therefore it is right binded

print(ex1)

ex2 = 10 + 6 - 3
# Correct Answer: 13
ex2_1 = 6 - 3
# output: 3 which adding 10 would get the correct answer
ex2_2= 10 + 6
# output: 16 which subtracting 3 would get the correct answer, same priority, precedence from left to right (left-binded)

print(ex2)

ex3 =  3 * 5 % 30
# Correct Answer: 15
ex3_1 = 5 % 30
# output: 5 which multiplying to 3 would be 15
ex3_2= 3 * 5
# output: 15 which doing the modulo to 30 would be 15 which is the correct answer,
# precedence from left to right (left-binded) same priority
 
print(ex3)

ex4 =  10 * 2 - 8
# Correct Answer: 12
ex4_1 = 10 * 2
# output: 20 which means subtracting 8 would be 12, the correct answer
ex4_2 = 2 - 8
# output: -6 which multiplying to 10 would be - 60 therefore it is left-binded
 
print(ex4)

ex5 =   12 / -6 * -5
# Correct Answer: 10.0
ex4_1 = 12 / -6
# output: -10 which multiplying to  - 5 would be 10, which is correct
ex4_2 = -6 * -5
# output: - 30 which mean dividing to 12 would give the wrong answer.
# same precedence but left to right associotivity therefore this is also left-binded
 
print(ex5)
