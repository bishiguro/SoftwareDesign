# Bonnie Ishiguro
# 02/01/2014

def check_fermat(a,b,c,n):
    if (n > 2) and (a**n + b**n == c**n):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def prompt_CF():
    a = raw_input("a: ")
    b = raw_input("b: ")
    c = raw_input("c: ")
    n = raw_input("n: ")
    check_fermat(int(a),int(b),int(c),int(n))
