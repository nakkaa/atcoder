# -*- coding: utf-8 -*-
# Page: https://atcoder.jp/contests/exawizards2019
# 2019/3/30(土)
def ex2019a():
    n = raw_input().split(" ")
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])

    if a == b and b == c:
        print "Yes"
    else:
        print "No"

def ex2019b():
    N = int(raw_input())
    S = raw_input()
    s = list(S)

    r = 0
    b = 0

    for i in range(N):
        if s[i] == "R":
            r = r + 1
        elif s[i] == "B":
            b = b + 1
    
    if r > b:
        print "Yes"
    else:
        print "No"

def main():
    ex2019b()
	
if __name__ == '__main__':
    main()