# subsequence_product_sum.py
# https://www.codewars.com/kata/5d653190d94b3b0021ec8f2b

def prod(a):
    product = 1
    for x in a:
        product *= x
    
    return product
    
def product_sum(a, m):
    #result = sum([prod(a[i:j+1]) for i in range(len(a)) for j in range(i+1, i+m+1)])
    result = 0
    for i in range(len(a)-m+1):
        print(i, a[i:i+m+1], prod(a[i:i+m+1]))
        result += prod(a[i:i+m+1])
    return result

if __name__ == "__main__":
    print(product_sum([1,2,3], 2))
    print(product_sum([2,3, 4, 5], 3))


