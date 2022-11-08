import mysql.connector as a
con=a.connect(host='localhost',user='root',password='Mysql@99',database='bank',auth_plugin='mysql_native_password')
def openAcc():
    n=input("enter name:")
    ac=input("enter account no :")
    db=input("enter d.o.b:")
    p=input("enter phone :")
    ad=input("enter address:")
    opba=int(input("enter opening balance:"))
    data1=(n,ac,db,p,ad,opba)
    data2=(n,ac,opba)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print('data entered successfully')
    main()

def depoamo():
    am=int(input("enter amount:"))
    ac=input('enter account no:')
    a='select balance from amount where acno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    main()

def witham():
    am=int(input('input amount:'))
    ac=input('enter account no:')
    a='select balance from amount where acno=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql='update amount set balance=%s where acno=%s'
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    main()

def balance():
    ac=input('enter account no :')
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("balance for account:",ac,"is",myresult[0])
    main()

def dispacc():
    ac=input("enter account no:")
    a="select * from account where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=' ')
    main()

def closeac():
    ac=input("enter accoun no:")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()

def main():
    print('''
          1. OPEN NEW ACCOUNT
          2. DEPOSIT AMOUNT
          3. WITHDRAW AMOUNT
          4. BALANCE ENQUIRY
          5. DISPLAY CUSTOMERS DETAILS
          6. CLOSE AN ACCOUNT''')

    choice =input("enter task number")
    while True:
        if (choice=='1'):
            openAcc()
        elif(choice=='2'):
            depoamo()
        elif(choice=='3'):
            witham()
        elif(choice=='4'):
            balance()
        elif (choice == '5'):
            dispacc()
        elif (choice == '6'):
            closeac()
        else :
            print("wrong choice")
            main()
main()

