def karatsuba(m,n):
    """Simple and Quick Implementation of Karatsuba Algorithm """
    if(m<10 or n<10):
        return m*n
    else:
        mstring = str(m)
        nstring = str(n)

        k = max(len(mstring), len(nstring))
        mid=int(k/2)
        
        #finding the higher bits for each number(a and c)
        a = int(mstring[:-mid])
        c = int(nstring[:-mid])

        #finding the lower bits for each number(b and d)
        b = int(mstring[-mid:])
        d = int(nstring[-mid:])

        #finding ac, bd and ad_plus_bc
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        return ac*10**(2 * mid) + ad_plus_bc*10**(mid) + bd

if __name__ == "__main__":
    print("Answer is:")
    print(karatsuba(1970,2023))