
import sys

def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    n = int(sys.argv [1])
    print("Even or odd:", even_odd(n))

