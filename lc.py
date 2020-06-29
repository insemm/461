def commonChars(A):
        check = list(A[0])
        print(check)
        for word in A:
            newCheck = []
            for c in word:
                if c in check:
                    print(newCheck)
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
            print(check)
        
        return check
            
print(commonChars(["bella","label","roller"]))