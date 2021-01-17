def fizzbuzz(n) :
    result = []
    for x in range(1,n+1):
        if x % 3 == 0 and x % 5 == 0 :
            result.append("fizz buzz")
        elif x % 3 == 0 : 
            result.append("fizz")
        elif x % 5 == 0 : 
            result.append("buzz")
        else : 
            result.append(str(x))
    return result

def main() : 
    print(','.join(fizzbuzz(100)))
    
main()