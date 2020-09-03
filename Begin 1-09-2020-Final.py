import pymysql


def Display():
    #display all order list
    try:
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        select1 = "SELECT * FROM ITEM;"
        
        cursor.execute(select1)
        rows = cursor.fetchall()
        for row in rows:
           print(row)
        connection.commit()
        connection.close()
    except:
        print(" open xamp ")
def AmountUpdate():
    try:
        #display the order list which has amount =0
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()

        mark='y'
        while(mark=='y'):
            select1 = "SELECT * FROM ITEM WHERE AMOUNT =0;"
            cursor.execute(select1)
            rows = cursor.fetchall()
            check=[]
            if(rows!=()):
                for row in rows:
                   print(row)
                   check.append(row[0])

                try:
                    #asking the user that which order you want to update
                    OrderNo=int(input("mention the order number you want to update: "))
                    UpdatedAmount=int(input("please enter final amount:" ))
                except:
                    print("WRONG INPUT !")

                if OrderNo in check:
                    
                    #updating the amount
                    
                
                    Update1="UPDATE ITEM SET AMOUNT = %s WHERE ID = %s;"
                    Update2 = (UpdatedAmount, OrderNo)
                    cursor.execute(Update1,Update2)
                else:
                    print("INVALID ORDER NUMBER ")
                mark=input("Press y to CONTINUE and any key to EXIT")
            else:
                print( "No Order To Display ")
                mark='n'

            
        
        connection.commit()
        connection.close()
        print("AMOUNT UPDATED SUCCESSFULLY")
    except:
         print(" open xamp")
def DeliveryStatus():
    #display the order list which has delivery status ='NO'
    
    
    
    Mark='y'
    while(Mark=='y'):
        try:
            connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
            cursor = connection.cursor()
            select1 = "SELECT * FROM ITEM WHERE DELIVERY ='NO' AND NOT AMOUNT=0;"
        
            cursor.execute(select1)
            rows = cursor.fetchall()
            Check=[]
            if rows!=():
                for row in rows:
                   print(row)
                   Check.append(row[0])


                #asking the user that which order you want to update
                try:
                    OrderNo=int(input("mention the order number you want to update: "))
                except:
                    print("incorrect value error")


                if OrderNo in Check:
                    DeliveryStatus=input("press 1 to confirm:" )
                    if(DeliveryStatus=='1'):
                        #updating the delivery
                        Update1="UPDATE ITEM SET DELIVERY ='YES'  WHERE ID = %s;"
                        Update2 = (OrderNo)
                        cursor.execute(Update1,Update2)
                    else:
                        print("confirmation not provided")
                
                   
                else:
                    print(" Order Not Found")
                Mark=input("press y to continu and any key to exit")
                    
            else:
                print("NO ORDER TO DISPIAY ")
                Mark='n'
            

        
       
            ##database work as what to do then where to do so in execution line first we put query of doing then which query to do 
            connection.commit()
            connection.close()
            print("DELIVERY UPDATED SUCCESSFULLY")##giving message of update status
        except:
            print("open xamp")
       

## work of businesman starts form this function 
def Business():
    Business1=input("press 1 for Display\npress 2 for Amount Update\npress 3 for Delivery Status")
    if(Business1=="1"):
        Display()# display all order
    elif(Business1=="2"):
        AmountUpdate()## display only those order which has amount=0
    elif(Business1=="3"):
        DeliveryStatus()#display only those order which has delivery status ='NO'
    else:
        print("Invalid Input")
        
                   
                   
                   
##choice=1 then this function will help the Customer in Ordering with her/his Detailed Record

def PlaceOrder():
    #Asking Customer Detail
    Name=input("Enter Name: ")
    Address=input("Enter Address: ")
    PhoneNumber=input("Enter Phone Number: ")
    ItemList=input("Enter Itemlist:  ")
    #Default Value
    Amount=0
    Delivery="No"
    #databasework
    try:
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="mydb")
        cursor = connection.cursor()
        #insert query
        insert1 = "INSERT INTO ITEM (NAME, PHONE, ADDRESS, ITEMS, AMOUNT, DELIVERY) VALUES (%s,%s,%s,%s,%s,%s);"
        
        insert2= (Name, PhoneNumber, Address, ItemList, Amount, Delivery)
        cursor.execute(insert1,insert2)
        ##Executing The Query
        connection.commit()
        connection.close()
        ##Closing Database Work
        print("order place successfully")
        ##Giving Confirmation Message Off Order Placed
    except:                                 ##for error detection
        print(" open xamp")
#If Choice=2 then for Businessman
def Login():
    Password=input("please enter your password:")
    if(Password=="pravash123"):
        print("WELCOME")
        Business()
    else:
        print("UNAUTHORIZED")


#program body        

print("-"*20," SHOP MANAGEMENT","-"*20)
      
Choice=input("Press 1 if you are Customer\nPress 2 if you are a Businessman: ")

if(Choice=="1"):
    PlaceOrder()
elif(Choice=="2"):
    Login()
else:
    print("Invalid Order")
