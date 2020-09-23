# ex7_7.py

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)

if __name__ == "__main__":
    print(f(0))
    print(f(1))
    print(f(3))
    print(f(5))
