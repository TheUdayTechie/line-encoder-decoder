import matplotlib.pyplot as plt
import numpy as np
from random import randint


def longestPalindrome(s):
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    max_length = 1
    start = 0
    for l in range(2, len(s) + 1):
        for i in range(len(s) - l + 1):
            end = i + l
            if l == 2:
                if s[i] == s[end - 1]:
                    dp[i][end - 1] = True
                    max_length = l
                    start = i
            else:
                if s[i] == s[end - 1] and dp[i + 1][end - 2]:
                    dp[i][end - 1] = True
                    max_length = l
                    start = i
    return s[start : start + max_length]


# NRZL code

# decoder


def decoder_NRZL(y, n):
    for x in range(n):
        if y[x] == -1:
            y[x] = 0
    print(y)


# encoder
def NRZL(y, n):
    print(y)
    y.insert(0, 0)
    for x in range(1, n + 1):
        if y[x] == 0:
            y[x] = -1
    plt.plot(y, drawstyle="steps-pre", color="red")
    plt.axhline(0, color="black")
    y.pop(0)
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_NRZL(y, n)


# NRZI code

# decoder


def decoder_NRZI(y, n):
    X = 1
    if y[0] == -1:
        y[0] = 0
        X = -1
    elif y[0] == 1:
        y[0] = 1
        X = 1

    for x in range(1, n):
        if y[x] == X:
            X = y[x]
            y[x] = 0
        else:
            X = y[x]
            y[x] = 1

    print(y)


# encoder


def NRZI(y, n):
    print(y)
    y.insert(0, 0)
    X = -1
    y[0] = X
    for x in range(1, n + 1):
        if y[x] == 1:
            if X == -1:
                X = 1
                y[x] = X
            else:
                X = -1
                y[x] = X
        else:
            y[x] = X

    plt.plot(y, drawstyle="steps-pre", color="red")
    plt.axhline(0, color="black")
    y.pop(0)
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_NRZI(y, n)


# AMI CODE

# decoder


def decoder_AMI(y, n):
    for x in range(n):
        if y[x] == -1 or y[x] == 1:
            y[x] = 1
        else:
            y[x] = 0
    print(y)


# encoder


def AMI(y, n):
    print(y)
    y.insert(0, 0)
    X = 1
    for x in range(1, n + 1):
        if y[x] == 1:
            if X == -1:
                y[x] = X
                X = 1
            else:
                y[x] = X
                X = -1
        else:
            y[x] = 0

    plt.plot(y, drawstyle="steps-pre", color="red")
    y.pop(0)
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_AMI(y, n)


# Manchester

# decoder


def decoder_Manchester(y, n):
    ans = []
    for x in range(1, len(y), 2):
        if y[x] == -1:
            ans.append(0)
        else:
            ans.append(1)
    print(ans)


# encoder


def Manchester(y, n):
    print(y)
    Ans = [0]

    for x in range(n):
        if y[x] == 0:
            Ans.append(int(-1))
            Ans.append(int(1))
        else:
            Ans.append(int(1))
            Ans.append(int(-1))

    xaxis = []
    X = []

    Cnt = 0

    for i in range(len(Ans)):
        xaxis.append(float(Cnt))
        X.append(i)
        Cnt = Cnt + 0.5

    plt.plot(Ans, drawstyle="steps-pre", color="red")
    plt.xticks(X, xaxis)
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_Manchester(Ans, n)


# DIFF_Manchester

# decoder


def decoder_DIFF_Manchester(y, n):
    ans = []
    if y[1] == -1:
        ans.append(0)
    else:
        ans.append(1)
    for x in range(3, 2 * n + 1, 2):
        if y[x] == y[x - 2]:
            ans.append(0)
        else:
            ans.append(1)
    print(ans)


# encoder


def DIFFMANCHESTER(y, n):
    print(y)
    A = 1
    B = -1
    if y[0] == 0:
        A = -1
        B = 1

    Ans = [0]
    Ans.append(int(A))
    Ans.append(int(B))
    for x in range(1, n):
        if y[x] == 0:
            Ans.append(int(A))
            Ans.append(int(B))
        else:
            T = A
            A = B
            B = T
            Ans.append(int(A))
            Ans.append(int(B))

    xaxis = []
    X = []

    Cnt = 0

    for i in range(len(Ans)):
        xaxis.append(float(Cnt))
        X.append(i)
        Cnt = Cnt + 0.5

    plt.plot(Ans, drawstyle="steps-pre", color="red")
    plt.xticks(X, xaxis)
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_DIFF_Manchester(Ans, n)


# B80SScrambler


# decoder
def decoder_B80SScrambler(y, n):
    ans = []
    p = -1
    x = 0
    while x in range(len(y)):
        if y[x] == 0:
            ans.append(0)
        elif y[x] == -p:
            ans.append(1)
            p = -p
        else:
            for i in range(5):
                ans.append(0)
            x = x + 4
        x = x + 1
    print(ans)

    # encoder


def B80SScrambler(y, n):
    print(y)
    X = 1
    for x in range(n):
        if y[x] == 1:
            if X == -1:
                y[x] = X
                X = 1
            else:
                y[x] = X
                X = -1
        else:
            y[x] = 0

    i = 0
    j = 0
    Cnt = 0

    p = -1
    while i < n and j < n:
        if y[j] == 0:
            Cnt = Cnt + 1
            if Cnt == 8:
                Cnt = 0
                y[i + 3] = p
                if p == -1:
                    p = 1
                else:
                    p = -1
                y[i + 4] = p
                y[j - 1] = p
                if p == -1:
                    p = 1
                else:
                    p = -1
                y[j] = p
                i = j + 1
            j = j + 1
        else:
            p = y[j]
            i = j + 1
            j = i
            Cnt = 0

    y.insert(0, 0)
    plt.plot(y, drawstyle="steps-pre", color="red")
    y.pop(0)
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_B80SScrambler(y, n)

    # HDB3

    # decoder


def decoder_HDB3(y, n):
    ans = []
    p = 1
    x = 1
    while x <= n:
        if y[x] == 0:
            ans.append(0)
        elif y[x] == p:
            ans.append(1)
            p = -p
        else:
            ans.append(0)
            ans[x - 4] = 0
        x = x + 1
    print(ans)


# encoder


def HDB3(y, n):
    print(y)
    p = -1
    count = 0
    f = 0
    i = 1
    j = 1
    ans = [0]

    while i <= n and j <= n:
        if y[j - 1] == 0:
            ans.append(0)
            count = count + 1
            if count == 4:
                if f == 0:
                    ans[i] = -p
                    ans[j] = -p
                    p = -p
                    count = 0
                    i = j + 1
                else:
                    ans[j] = p
                    f = 0
                count = 0
                i = j + 1

        else:
            p = -p
            if f == 0:
                f = 1
            else:
                f = 0
            ans.append(p)
            i = j + 1
            count = 0
        j = j + 1

    plt.plot(ans, drawstyle="steps-pre", color="red")
    plt.show()
    print("Do You Want To Decode This Graph Yes(1)/No(0):-")
    decoderst = int(input())
    if decoderst == 1:
        decoder_HDB3(ans, n)


print("Enter Number Of Bits:-")

i = input()
n = int(i)
y = []
print("What Type Of Sequence You Want Random(1)/Manual(2)")

Scheme = int(input())
if Scheme == 1:
    for x in range(n):
        y.append(randint(0, 1))
elif Scheme == 2:
    for x in range(n):
        y.append(int(input()))

S = ""
for x in y:
    S += str(x)

print(S)
print("The Largest Palindrome is:-")
print(longestPalindrome(S))

print("Use Following Schemes:-")
print("For NRZ-L Press 1")
print("For NRZ-I Press 2")
print("For Manchester Press 3")
print("For DIFFMANCHESTER Press 4")
print("For AMI Press 5")


print()
print("Enter Scheme Type:-")
num = int(input())


if num == 1:
    NRZL(y, n)
elif num == 2:
    NRZI(y, n)
elif num == 3:
    Manchester(y, n)
elif num == 4:
    DIFFMANCHESTER(y, n)
elif num == 5:
    print("Do You Want Scrambling Or Not Yes(1)/No(2)")
    Scramble = int(input())
    if Scramble == 2:
        AMI(y, n)
    else:
        print("Which Type Of Scrambling B8ZS(1)/HDB3(2)")
        sctype = int(input())
        if sctype == 2:
            HDB3(y, n)
        elif sctype == 1:
            B80SScrambler(y, n)
