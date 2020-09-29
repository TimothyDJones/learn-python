# hamming_numbers.py
# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python

def hamming(n):
    pass
    
def nthuglynumber(n):
    p2, p3, p5=0, 0, 0
    uglynumber=[1]
    while len(uglynumber)<n:
        ugly2, ugly3, ugly5= uglynumber[p2]*2, uglynumber[p3]*3, uglynumber[p5]*5
        next=min(ugly2, ugly3, ugly5)
        if next==ugly2: p2+=1
        if next==ugly3: p3+=1
        if next==ugly5: p5+=1
        uglynumber+=[next]
    return uglynumber[-1]

if __name__ == "__main__":
    print(nthuglynumber(5))
    print(nthuglynumber(10))
