# Exercise 1

truths = [[0, 0], [0, 1], [1, 0], [1, 1]]


def ex1_a(truths):
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

# ex1_a(truths)


def ex1_b(truths):
    print("Truth table for not p or q")
    print("p\t q\t !p\t !p or q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not (a), "\t", not (a) or b)

# ex1_b(truths)


def ex1_c(truths):
    print("Truth table for p or not q")
    print("p\t q\t !q\t p or !q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not (b), "\t", a or not (b))

# ex1_c(truths)


def ex1_d(truths):
    print("Truth table for (p or q) and not q")
    print("p\t q\t !q\t p or q\t (p or q) and !q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not (b), "\t",
              a or b, "\t", (a or b) and not (b))

# ex1_d(truths)


def ex1_e(truths):
    print("Truth table for p or not q")
    print("p\t q\t !q\t p or !q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not (b), "\t", a or not (b))

# ex1_e(truths)


def ex1_f(truths):
    print("Truth table for (p and q) and q")
    print("p\t q\t p and q\t (p and q) and q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", a and b, "\t\t", (a and b) and b)

# ex1_f(truths)

# Exercise 2

# a
# p => q equivalent to !p or q


def implication(a, b):
    if (a == True and b == False):
        return False
    return True


def ex2_a(truths):
    print("Truth table for p => q")
    print("p\t q\t p => q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", implication(a, b))
        # print(a, "\t", b, "\t", not(a) or b)


# ex2_a(truths)

# b
# !p => q equivalent to p or q

def ex2_b(truths):
    print("Truth table for not p => q")
    print("p\t q\t !p\t !p => q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not (a), "\t", implication(not (a), b))
        # print(a, "\t", b, "\t", not(a), "\t", a or b)

# ex2_b(truths)

# c
# p => !q equivalent to not p or not q


def ex2_c(truths):
    print("Truth table for p => not q")
    print("p\t q\t !q\t p => !q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        print(a, "\t", b, "\t", not (b), "\t", implication(a, not (b)))
        # print(a, "\t", b, "\t", not(b), "\t", not(a) or not(b))

# ex2_c(truths)

# Exercise 3

# a
# p => q equivalent to !q => !p


def ex3_a(truths):
    truth_table_p_implies_q = []
    truth_table_notQ_implies_notP = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        truth_table_p_implies_q.append(implication(a, b))
        truth_table_notQ_implies_notP.append(implication(not (b), not (a)))

    isEquivalent = True
    for i in range(len(truth_table_notQ_implies_notP)):
        if (truth_table_p_implies_q[i] != truth_table_notQ_implies_notP[i]):
            isEquivalent = False
            break

    return isEquivalent

# print("Is p => q equivalent to !q => !p:", ex3_a(truths))

# b
# p or q not equivalent to p


def ex3_b(truths):
    truth_table_p_or_q = []
    truth_table_p = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        truth_table_p_or_q.append(a or b)
        truth_table_p.append(a)

    isEquivalent = True
    for i in range(len(truth_table_p_or_q)):
        if (truth_table_p_or_q[i] != truth_table_p[i]):
            isEquivalent = False
            break

    return isEquivalent

# print("Is p or q equivalent to p:", ex3_b(truths))

# c
# p and q equivalent to !(!p or !q) (De morgan's law)


def ex3_c(truths):
    truth_table_p_and_q = []
    truth_table_not_notP_or_notQ = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        truth_table_p_and_q.append(a and b)
        truth_table_not_notP_or_notQ.append(not (not (a) or not (b)))

    isEquivalent = True
    for i in range(len(truth_table_p_and_q)):
        if (truth_table_p_and_q[i] != truth_table_not_notP_or_notQ[i]):
            isEquivalent = False
            break

    return isEquivalent

# print("Is p and q equivalent to !(!p or !q):", ex3_c(truths))

# d
# !p => q not equivalent to !(p => p)


def ex3_d(truths):
    truth_table_notP_implies_q = []
    truth_table_not_p_implies_p = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        truth_table_notP_implies_q.append(implication(not (a), b))
        truth_table_not_p_implies_p.append(not (implication(a, a)))

    isEquivalent = True
    for i in range(len(truth_table_notP_implies_q)):
        if (truth_table_notP_implies_q[i] != truth_table_not_p_implies_p[i]):
            isEquivalent = False
            break

    return isEquivalent


# print("Is !p => q equivalent to !(p => p):", ex3_d(truths))
