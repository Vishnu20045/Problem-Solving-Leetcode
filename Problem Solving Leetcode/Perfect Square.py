def isPerfectSquare(num):
        if num<0:
            return False
        if num==0:
            return True
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False
print(isPerfectSquare(16))