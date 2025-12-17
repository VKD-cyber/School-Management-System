import mysql.connector as a
con=a.connect(host='localhost', user='root', database='cs_project', passwd='vijay40@')
def ast():
    n=input('Student name:')
    c=input('Class:')
    q=input('Admission no.:')
    r=input('Roll no:')
    a=input('Address:')
    p=input('Phone:')
    data=(n,c,q,r,a,p,)
    sql='insert into student values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Entered Successfully')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def rst():
    c=input('Class:')
    r=input('admission_no:')
    data=(c,r)
    sql='delete from student where class=%s and admission_no=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Updated')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def addt():
    x=input('Teacher Name:')
    y=input('Post:')
    z=input('Salary:')
    v=input('Address:')
    p=input('Phone:')
    a=input('Account:')
    data=(x,y,z,v,p,a)
    sql='insert into teacher values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Enter Successfully')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def remt():
    n=input('Teacher Name:')
    ac=input('Account No.:')
    data=(n,ac)
    sql='delete from teacher where teacher_name=%s and account=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Updated')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def abclass():
    d=input('date:')
    cl=input('Class:')
    ab=input('Name Of Absent Student')
    data=(d,cl,ab)
    sql='insert into cattendance values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Updated')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def abteacher():
    d=input('Date:')
    ab=input('Names Of Absent Teacher:')
    data = (d,ab)
    sql = 'insert into tattendance values(%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Updated')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def submitfee():
    n=input('Student name :')
    c=input('Class :')
    r=input('Roll No.:')
    m=input('Quater & Year (Q/Y):')
    f=input('Fees :')
    d=input('Date :')
    data=(n,c,r,m,f,d)
    sql='insert into fees values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Entered Successfully')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def pays():
    n=input('Teacher Name:')
    m=input('Month:')
    p=input('Yes/No:')
    data=(n,m,p)
    sql='insert into pay_salary values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Entered Successfully')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def dclass():
    cl=input('Class:')
    data=(cl,)
    sql='select * from student where class=%s'
    c=con.cursor()
    c.execute(sql,data)
    d=c.fetchall()
    for i in d:
        print('Name:',i[0])
        print('Class:',i[1])
        print('Roll:',i[2])
        print('Address:',i[3])
        print('Phone:',i[4])
        print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def dteacher():
    sql='select * from teacher'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print('Name:',i[0])
        print('Post:',i[1])
        print('Salary',i[2])
        print('Address:',i[3])
        print('Phone:',i[4])
        print('Acno:',i[5])
        print('>-----------------------------------------------------------------------------------------------------------------------<')
    main()

def main():
    print("""                                                   KENDRIYA VIDYALAYA NARANGI


                                    TASK NO.                                       TASK
                                    
                                       1                   <---->               ADD STUDENT
                                       2                   <---->               REMOVE STUDENT
                                       3                   <---->               ADD TEACHER
                                       4                   <---->               REMOVE TEACHER
                                       5                   <---->               CLASS ATTENDANCE
                                       6                   <---->               TEACHER ATTENDANCE
                                       7                   <---->               SUBMIT FEES
                                       8                   <---->               PAY SALARY
                                       9                   <---->               DISPLAY CLASS
                                       10                  <---->               TEACHER LIST
""")
    choice=input('Enter Task No. :')
    print('>-----------------------------------------------------------------------------------------------------------------------<')
    if(choice=='1'):
        ast()
    elif(choice=='2'):
        rst()
    elif(choice=='3'):
        addt()
    elif(choice=='4'):
        remt()
    elif(choice=='5'):
        abclass()
    elif(choice=='6'):
        abteacher()
    elif(choice=='7'):
        submitf()
    elif(choice=='8'):
        pays()
    elif(choice=='9'):
        dclass()
    elif(choice=='10'):
        dteacher()
    else:
        print('WRONG CHOICE...')
        main()

def pswd():
    p=input('PASSWORD:')
    if p=='uhlala':
        main()
    else:
        print('WRONG PASSWORD')
        pswd()
pswd()
