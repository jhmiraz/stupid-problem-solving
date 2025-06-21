def reverse(x):

    INT_min, int_max = -2**31 , 2**31-1
    sign=0


    if x<0:
        sign= -1
    else:
        sign= 1
    x= abs(x)

    reverse_x= int(str(x)[::-1]) * sign

    if reverse_x < INT_min or reverse_x> int_max:
        return 0
    return reverse_x



print(reverse(-125))