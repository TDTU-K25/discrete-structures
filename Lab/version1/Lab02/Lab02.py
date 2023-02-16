# Exercise 1

def exercise1():

    a = True
    b = False

    # a
    print(a and b)  # False

    # b
    print(b and a)  # False

    # c
    print(not a and b)  # False

    # d
    print(not a and not b)  # False

    # e
    print(a or b)  # True

    # f
    print(not a or not b)  # True

    # g
    print(a or not b)  # True


exercise1()

# Exercise 2


def exercise2():
    A = True
    B = False
    C = True

    # a
    print((A and B) or C)  # True

    # b
    print((A or C) and B)  # False

    # c
    print((not A and B) or not C)  # False

    # d
    print((A and not B) and not C)  # False

    # e
    print(A or B or C)  # True

    # f
    print(A and (B or not C))  # False

    # g
    print((B and C) or not A)  # False

    # h
    print((B or not C) and A)  # False


exercise2()

# Exercise 3


def exercise3():
    p = True
    q = False

    # a) p -> q is equivalent to !p v q
    print(not p or q)  # False

    # b) !p -> q is equivalent to p v q
    print(p or q)  # True

    # c) !p -> !q is equivalent to p v !q
    print(p or not q)  # True

    # d) p -> !q is equivalent to !p v !q
    print(not p or not q)  # True


exercise3()

# Exercise 4


def exercise4():
    over_18 = True
    over_21 = False

    # a
    print(over_18 and over_21)  # False

    # b
    print(over_18 or over_21)  # True

    # c
    print(not over_18)  # False

    # d
    print(not over_21 or (over_21 or over_18))  # True


exercise4()

# Exercise 5


def exercise5():
    age = 20

    # a
    print("Age is less than 13:", age < 13)  # False

    # b
    print("Age is greater than or equal to 20 and less than 21:",
          (age >= 20) and age < 21)  # True

    # c
    print("Age is equal to 21:", age == 21)  # False


exercise5()

# Exercise 6


def implication(p, q):
    if p == True and q == False:
        return False
    return True


print(implication(False, False))
print(implication(False, True))
print(implication(True, False))
print(implication(True, True))

# Exercise 7


def biConditional(p, q):
    if (p == q):
        return True
    return False


print(biConditional(False, False))
print(biConditional(False, True))
print(biConditional(True, False))
print(biConditional(True, True))
