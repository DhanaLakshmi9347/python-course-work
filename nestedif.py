act = eval(input("Link Active: : "))

if act:
    per = eval(input("Permission Granted: : "))
    if per:
        print("File Opened Sucessesfuly")
    else:
            print("Access Denied")
else:
        print("Invalid file Link")
                 
    

