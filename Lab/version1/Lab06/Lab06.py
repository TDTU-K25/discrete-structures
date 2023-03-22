import itertools

# Exercise 1


def ex1_a():
    print("(Q -> P) and (P -> Q)")

# ex1_a()


def ex1_b():
    print("Q and !P")

# ex1_b()


def ex1_c():
    print("Q -> P")

# ex1_c()

# Exercise 2


def ex2_a():
    print("You will get good grade in the midterm exam if, and only if, you understand how to solve all the exercises in the book.")

# ex2_a()


def ex2_b():
    print("If you did not get good grade in the midterm exam, you do not understand how to solve all the exercises in the book.")

# ex2_b()


def ex2_c():
    print("If you understand how to solve all the exercises in the book, you will get good grade in the midterm exam")

# ex2_c()

# Exercise 3


def ex3_a():
    pass


def ex3_b():
    print("Statement: If you did not get good grade in the midterm exam, you do not understand how to solve all the exercises in the book.")
    print("Negation: You did not get good grade in the midterm exam and you understand how to solve all the exercises in the book.")
    print("Converse: If you do not understand how to solve all the exercises in the book, you will not get good grade in the midterm exam.")
    print("Contrapositive: If you understand how to solve all the exercises in the book, you will get good grade in the midterm exam.")


# ex3_b()


def ex3_c():
    print("Statement: If you understand how to solve all the exercises in the book, you will get good grade in the midterm exam")
    print("Negation: You understand how to solve all the exercises and you do not get good grade in the midterm exam.")
    print("Converse: If you get good grade in the midterm exam, you understand how to solve all the exercises in the book.")
    print("Contrapositive: If you do not get good grade in the midterm exam, you do not understand how to solve all the exercises in the book.")

# ex3_c()


# Exercise 4
truths = list(itertools.product([0, 1], repeat=2))


def ex4_a(truths):
    print("Truth table for p and q")
    print("p\t q\t p and q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", a and b)

# ex4_a(truths)


def ex4_b(truths):
    print("Truth table for !p and !q")
    print("p\t q\t !p\t !q\t !p and !q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not a, "\t", not b, "\t", not a and not b)

# ex4_b(truths)


def ex4_c(truths):
    print("Truth table for p -> !q")  # !p v !q
    print("p\t q\t !p\t !q\t p -> !q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not a, "\t", not b, "\t", not a or not b)

# ex4_c(truths)

# Exercise 5


def ex5_a(truths):
    print("p\t q\t p -> q\t q")

    isExistCriticalRowWithConclusionFalse = False

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not a or b, "\t", b)

        if ((not a or b) == True and a == True):
            if b == False:
                isExistCriticalRowWithConclusionFalse = True

    if (isExistCriticalRowWithConclusionFalse):
        print("The argument is invalid")
    else:
        print("The argument is valid")


# ex5_a(truths)

def ex5_b(truths):
    print("p\t q\t !q\t p v q\t p")

    isExistCriticalRowWithConclusionFalse = False

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not b, "\t", a or b, "\t", a)

        if ((a or b) == True and not b == True):
            if a == False:
                isExistCriticalRowWithConclusionFalse = True

    if (isExistCriticalRowWithConclusionFalse):
        print("The argument is invalid")
    else:
        print("The argument is valid")


# ex5_b(truths)

def ex5_c(truths):
    print("p\t q\t p -> q\t p")

    isExistCriticalRowWithConclusionFalse = False

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not a or b, "\t", a)

        if ((not a or b) == True and b == True):
            if a == False:
                isExistCriticalRowWithConclusionFalse = True

    if (isExistCriticalRowWithConclusionFalse):
        print("The argument is invalid")
    else:
        print("The argument is valid")


# ex5_c(truths)

def ex5_d(truths):
    print("p\t q\t !p\t p -> q\t !q")

    isExistCriticalRowWithConclusionFalse = False

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not a, "\t", not a or b, "\t", not b)

        if ((not a or b) == True and not a == True):
            if not b == False:
                isExistCriticalRowWithConclusionFalse = True

    if (isExistCriticalRowWithConclusionFalse):
        print("The argument is invalid")
    else:
        print("The argument is valid")


# ex5_d(truths)
