import itertools

# Exercise 1

truths = list(itertools.product([0, 1], repeat=3))


def ex1_a(truths):
    print("Truth table for p and q and r")
    print("p\t q\t r\t p and q and r")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", a and b and c)


# ex1_a(truths)


def ex1_b(truths):
    print("Truth table for not p or (q or r)")
    print("p\t q\t r\t !p\t q v r\t !p v (q v r)")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", not (a),
              "\t", b or c, "\t", not (a) or (b or c))

# ex1_b(truths)


def ex1_c(truths):
    print("Truth table for p and not (r or not q)")
    print("p\t q\t r\t !q\t r v !q\t !(r v !q)\t p and !(r v !q)")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", not (b), "\t", c or not (b),
              "\t", not (c or not (b)), "\t\t", a and not (c or not (b)))


# ex1_c(truths)


def ex1_d(truths):
    print("Truth table for (p or q) and not q and r")
    print("p\t q\t r\t !q\t p or q\t (p or q) and !q and r")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", not (b), "\t",
              a or b, "\t", (a or b) and not (b) and c)


# ex1_d(truths)

# Exercise 2

# a
# p and q => r equivalent to !(p and q) or r
# !p or !q or r (De Morgan's law)


def implication(a, b):
    if (a == True and b == False):
        return False
    return True


def ex2_a(truths):
    print("Truth table for p and q => r")
    print("p\t q\t r\t p and q\t p and q => q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", a and b,
              "\t\t", implication(a and b, c))
        # print(a, "\t", b, "\t", c, "\t", a and b, "\t\t", not(a) or not(b) or c)


# ex2_a(truths)

# b
# !p or q => r equivalent to !(!p or q) or r
# p and !q or r (De Morgan's law)

def ex2_b(truths):
    print("Truth table for !p or q => r")
    print("p\t q\t r\t !p\t !p or q\t !p or q => r")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", not (a), "\t", not (
            a) or b, "\t\t",  implication(not (a) or b, c))
        # print(a, "\t", b, "\t", c, "\t\t\t\t", a and not(b) or c)

# ex2_b(truths)

# c
# p => !q or r equivalent to !p or (!q or r)


def ex2_c(truths):
    print("Truth table for p => !q or r")
    print("p\t q\t r\t !q\t !q or r\t p => !q or r")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", not (b), "\t", not (
            b) or c, "\t\t", implication(a, not (b) or c))
        # print(a, "\t", b, "\t", c, "\t\t\t\t", not(a) or (not(b) or c))


# ex2_c(truths)

# d
# p <-> r and q

def biConditional(a, b):
    if (a == b):
        return True
    return False


def ex2_d(truths):
    print("Truth table for p <-> r and q")
    print("p\t q\t r\t r and q\t p <-> r and q")

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        print(a, "\t", b, "\t", c, "\t", c and b,
              "\t\t", biConditional(a, c and b))

# ex2_d(truths)

# Exercise 3

# a
# p => q v r equivalent to !p v (q v r)
# !q => !p v r equivalent to q v (!p v r)
# => p => q v r equivalent to !q => !p v r


def ex3_a(truths):
    truth_table_p_implies_q_or_r = []
    truth_table_notQ_implies_notP_or_r = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        truth_table_p_implies_q_or_r.append(implication(a, b or c))
        truth_table_notQ_implies_notP_or_r.append(
            implication(not (b), not (a) or c))

    isEquivalent = True
    for i in range(len(truth_table_p_implies_q_or_r)):
        if (truth_table_notQ_implies_notP_or_r[i] != truth_table_p_implies_q_or_r[i]):
            isEquivalent = False
            break

    return isEquivalent


# print("Is p => q v r equivalent to !q => !p v r:", ex3_a(truths))


# b
# p or q not equivalent to p or q or r


def ex3_b(truths):
    truth_table_p_or_q = []
    truth_table_p_or_r_or_q = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        truth_table_p_or_q.append(a or b)
        truth_table_p_or_r_or_q.append(a or c or b)

    isEquivalent = True
    for i in range(len(truth_table_p_or_q)):
        if (truth_table_p_or_q[i] != truth_table_p_or_r_or_q[i]):
            isEquivalent = False
            break

    return isEquivalent

# print("Is p or q equivalent to p or r or q:", ex3_b(truths))

# c
# !(!p v !q) and r equivalent to p and q and r
# p and q and !r not equivalent to !(!p v !q) and r


def ex3_c(truths):
    truth_table_p_and_q_and_notR = []
    truth_table_not_notP_or_notQ_and_r = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        truth_table_p_and_q_and_notR.append(a and b and not (c))
        truth_table_not_notP_or_notQ_and_r.append(
            not (not (a) or not (b)) and c)

    isEquivalent = True
    for i in range(len(truth_table_p_and_q_and_notR)):
        if (truth_table_p_and_q_and_notR[i] != truth_table_not_notP_or_notQ_and_r[i]):
            isEquivalent = False
            break

    return isEquivalent

# print("Is p and q and !r equivalent to !(!p or !q) and r:", ex3_c(truths))

# d
# !p => q v t not equivalent to !(p => p) and r


def ex3_d(truths):
    truth_table_notP_implies_q_or_r = []
    truth_table_not_p_implies_p_and_r = []

    for item in truths:
        if item[0] == 1:
            a = True
        else:
            a = False

        if item[1] == 1:
            b = True
        else:
            b = False

        if item[2] == 1:
            c = True
        else:
            c = False

        truth_table_notP_implies_q_or_r.append(implication(not (a), b or c))
        truth_table_not_p_implies_p_and_r.append(not (implication(a, a)) and c)

    isEquivalent = True
    for i in range(len(truth_table_notP_implies_q_or_r)):
        if (truth_table_notP_implies_q_or_r[i] != truth_table_not_p_implies_p_and_r[i]):
            isEquivalent = False
            break

    return isEquivalent


# print("Is !p => q v r equivalent to !(p => p) and r:", ex3_d(truths))
