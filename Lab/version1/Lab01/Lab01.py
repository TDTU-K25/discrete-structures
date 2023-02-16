import math

# Câu 1
a = 3 * 3 + 4 * 4
b = 2 - 5 * 2 + 4
c = 6 ** 2 - 4 * 2
d = (1 / 2) + 3 * 6
e = ((1 / 2) + (4 / 5)) / ((2 / 5) - 1)
f = (3 - (2 / 3)) / (4 - (6 / 7))
g = ((7 / 2) * (2 / 6)) / ((5 / 3) + (6 / 7))

# Câu 2
print("3 * 3 + 4 * 4 =", a)
print("2 - 5 * 2 + 4 =", b)
print("6 ** 2 - 4 * 2 =", c)
print("(1 / 2) + 3 * 6 =", d)
print("((1 / 2) + (4 / 5)) / ((2 / 5) - 1) =", e)
print("(3 - (2 / 3)) / (4 - (6 / 7)) =", f)
print("((7 / 2) * (2 / 6)) / ((5 / 3) + (6 / 7)) =", g)

# Câu 3


def calculateCircleArea(r):
    return math.pi * r ** 2

# Câu 4


def calculateSquareArea(a):
    return a ** 2


# Câu 5
color_list = ["Red", "Green", "White", "Black"]
for color in color_list:
    print(color)

# Câu 6


def countNumberFour(nums):
    count = 0
    for num in nums:
        if (num == 4):
            count += 1
    return count


print(countNumberFour([4, 5, 1, 3, 4]))


# Câu 7


def signOfNumber(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# Câu 8


def printEvenAndOddNumbers(nums):
    evenNums = []
    oddNums = []
    for num in nums:
        if (num % 2 == 0):
            evenNums.append(num)
        else:
            oddNums.append(num)
    print("Tất cả các số lẻ:", oddNums)
    print("Tất cả các số chẵn:", evenNums)


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527]

printEvenAndOddNumbers(numbers)

# Câu 9


def calculateSum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Câu 10


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
