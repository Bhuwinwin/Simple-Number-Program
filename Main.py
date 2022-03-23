from tkinter import*
try:
    print("*"*20,"โปรแกรมตัวเลข","*"*20)
    print(".")
    print(".")
    print(".")
    print("[ถ้าต้องการหาราคาต่อคน กด1]")
    print("[ถ้าต้องการหาค่าเฉลี่ยของคะแนนสอบ กด2]")
    print("[ถ้าต้องการเข้าเครื่องคิดเลข กด3]")
    print(".")

    try:
        x = int(input("กรุณากรอกตัวเลขที่นี่=>"))
    except ValueError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณากรอกเป็นตัวเลข(INTEGRES)")
        print("Code : Value Error")
        print([A])
        print("="*47)
    except IndexError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Index Error")
        print([A])
        print("="*47)
    except KeyError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Key Error")
        print([A])
        print("="*47)
    except NameError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Name Error")
        print([A])
        print("="*47)
    except TypeError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Type Error")
        print([A])
        print("="*47)
    except ZeroDivisionError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : ZeroDivision Error")
        print([A])
        print("="*47)

        

    if x >= 4:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณากรอกเป็นตัวเลข(INTEGRES)")
        print("Code : Value Error")
        print("คุณกรอก :",x)
        print("="*47)

    if x == 1 :
        try:
            print("="*20)
            p = int(input("กรุณากรอกจำนวนคน =>"))
        except ValueError :
            print("="*20,"ERROR" ,"="*20)
            print("กรุณากรอกเป็นตัวเลข(INTEGRES)")
            print("Code : Value Error")
            print("="*47)
        try:
            print("="*20)
            m = int(input("กรุณากรอกจำนวนราคา =>"))
        except ValueError :
            print("="*20,"ERROR" ,"="*20)
            print("กรุณากรอกเป็นตัวเลข(INTEGRES)")
            print("Code : Value Error")
            print([A])
            print("="*47)

        print("="*10,"จำนวนราคาต่อคนคือ","="*10)
        print(".")
        
        def MainA():
            for count in range(1,(m+1)):
                total = count*p
                print(p, "*", count , "=" , total , "บาท")
                

        print("="*47)

    if x == 2:
        print("="*20,"โปรแกรมคำนวณคะแนนเฉลี่ย","="*20)
        try:
            student = int(input("กรุณากรอกจำนวนนักเรียน =>"))
        except ValueError :
            print("="*20,"ERROR" ,"="*20)
            print("กรุณากรอกเป็นตัวเลข(INTEGRES)")
            print("Code : Value Error")
            print([A])
            print("="*47)

        total = 0
        avg = 0

        for count in range(1,(student+1)):
            
            
            print("== กรุณาใส่คะแนนนักเรียนคนที่"+str(count)+" ==")
            print(".")
            score = float(input("กรุณาใส่คะแนนที่นี่ =>"))
            print("*"*10)
            total+= score

            avg = total/student

        print("="*20)
        print(".")
        print("คะแนนเฉลี่ยเท่ากับ >>",avg,"%")
        print(".")
        print("="*20)

    if x == 3:
        print("="*20,"โปรแรกมเครื่องคิดเลข","="*20)
        print(".")
        print("== เมนูดำเนินการ ==")
        print("1.บวก")
        print("2.ลบ")
        print("3.คูณ")
        print("4.หาร")
        print(".")
        operation = int(input("กดเลือก 1 2 3 4 >>"))
        
        if operation == 1:
            print("="*47)
            num1 = int(input("กรุณากดตัวเลขที่ 1 >>"))
            print(".")
            num2 = int(input("กรุณากดตัวเลขที่ 2 >>"))
            print(".")
            sum = num1 + num2

            print("ผลบวกของ",num1,num2,"คือ",sum) 
        
        if operation == 2:
            print("="*47)
            num1 = int(input("กรุณากดตัวเลขที่ 1 >>"))
            print(".")
            num2 = int(input("กรุณากดตัวเลขที่ 2 >>"))
            print(".")
            sum = num1 - num2

            print("ผลลบของ",num1,num2,"คือ",sum) 
        
        if operation == 3:
            print("="*47)
            num1 = int(input("กรุณากดตัวเลขที่ 1 >>"))
            print(".")
            num2 = int(input("กรุณากดตัวเลขที่ 2 >>"))
            print(".")
            sum = num1 * num2

            print("ผลคูณของ",num1,num2,"คือ",sum) 

        if operation == 4:
            print("="*47)
            num1 = int(input("กรุณากดตัวเลขที่ 1 >>"))
            print(".")
            num2 = int(input("กรุณากดตัวเลขที่ 2 >>"))
            print(".")
            sum = num1 / num2

            print("ผลหารของ",num1,num2,"คือ",sum) 


    print("="*20)
    print(".")
    print("จบโปรแกรม")
    print(".")
    print("="*20)

except ValueError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณากรอกเป็นตัวเลข(INTEGRES)")
        print("Code : Value Error")
        print([A])
        print("="*47)
except IndexError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Index Error")
        print([A])
        print("="*47)
except KeyError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Key Error")
        print([A])
        print("="*47)
except NameError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Name Error")
        print([A])
        print("="*47)
except TypeError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : Type Error")
        print([A])
        print("="*47)
except ZeroDivisionError as A:
        print("="*20,"ERROR" ,"="*20)
        print("กรุณาติดต่อ Admin")
        print("Code : ZeroDivision Error")
        print([A])
        print("="*47)





