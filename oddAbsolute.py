def calculateAbsolute():
    # This first line is provided for you
    in_num = int(input("Enter a number: "))
    x = 21
    if in_num > x:
        in_num =abs(int(in_num - x))*2
    else:
        in_num =abs(int(in_num - x))
            
    print("Result:",in_num)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()