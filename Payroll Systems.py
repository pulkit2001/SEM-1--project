from tkinter import *
import random
import time
import random
import time
import datetime

payroll= Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management Systems")

def Exit():
    payroll.destroy()

def Reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    CityWeighting.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentsDue.set("")
def PayRef():
    PayDate.set(time.strftime("%d/%m/%Y"))
    #PayDate.set(time.strftime("%x"))
    Refpay = random.randint(20000, 709467)
    Refpaid = ("PR"+str(Refpay))
    Reference .set(Refpaid)

    NIpay = random.randint(4200, 9467)
    NIpaid = ("NI"+str(NIpay))
    NINumber .set(NIpaid)
def PayPeriod():
    i= datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode = random.randint(1200, 4467)
    CodeNI = ("NICode"+str(NCode))
    NICode.set(CodeNI)
    
def MonthlySalary():
    BS = float(BasicSalary.get())
    CW = float(CityWeighting.get())
    OT = float(OverTime.get())

    MTax = ((BS + CW + OT) * 0.3)
    TTax= "Rs.", str('%.2f'%(MTax))
    Tax.set(TTax)


    M_Pension = ((BS + CW + OT) * 0.02)
    MM_Pension= "Rs.", str('%.2f'%(M_Pension))
    Pension.set(MM_Pension)

    M_StudentLoan = ((BS + CW + OT) * 0.12)
    MM_StudentLoan= "Rs.", str('%.2f'%(M_StudentLoan))
    StudentLoan.set(MM_StudentLoan)

    M_NIPayment = ((BS + CW + OT) * 0.11)
    MM_NIPayment= "Rs.", str('%.2f'%(M_NIPayment))
    NIPayment.set(MM_NIPayment)


    Deduct= (MTax +M_Pension +M_StudentLoan + M_NIPayment)
    Deduct_Payment="Rs.", str('%.2f'%(Deduct))
    Deductions.set(Deduct_Payment)
    
    Gross_Pay = "Rs.", str('%.2f' % (BS + CW + OT))
    GrossPay.set(Gross_Pay)

    NetPayAfter=(BS + CW + OT)- Deduct
    NetAfter="Rs.", str('%.2f'%(NetPayAfter))
    NetPay.set(NetAfter)

    TaxablePay.set(TTax)
    PensionablePay.set(MM_Pension)
    OtherPaymentsDue.set("0.00")
        
EmployeeName = StringVar()
Address = StringVar()
Reference=StringVar()
EmployerName = StringVar()
CityWeighting = StringVar()
BasicSalary = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax = StringVar()
Pension = StringVar()
StudentLoan = StringVar()
NIPayment = StringVar()
Deductions = StringVar()
PostCode = StringVar()
Gender = StringVar()
PayDate = StringVar()
TaxPeriod = StringVar()
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionablePay = StringVar()
OtherPaymentsDue = StringVar()


Tops=Frame(payroll, width =1350, height=50, bd=16, relief='raise')
Tops.pack(side=TOP)
LF=Frame(payroll, width =700, height=650, bd=16, relief='raise')
LF.pack(side=LEFT)
RF=Frame(payroll, width=600, height=650, bd=16, relief='raise')
RF.pack(side=RIGHT)

lblInfo = Label(Tops, font=("arial", 50, 'bold' ),
text='Payroll Manangement Systems', fg='Steel Blue', bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

LeftInsideLF=Frame(LF, width=700, height=100,bd=8, relief='raise')
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=325, height=400, bd=8, relief='raise')
LeftInsideLFLF.pack(side=LEFT)
LeftInsideRFRF=Frame(LF, width=325, height=400, bd=8, relief='raise')
LeftInsideRFRF.pack(side=RIGHT)

RightInsideLF=Frame(RF, width=600, height=200, bd=8, relief='raise')
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=300, height=400, bd=8, relief='raise')
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400, bd=8, relief='raise')  
RightInsideRFRF.pack(side=RIGHT)
#========================Left Side============================================
lblEmployeeName = Label(LeftInsideLF, font=('arial', 12, 'bold'),text="Employee Name",
                        fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblEmployeeName.grid(row=0 , column=0)
txtEmployeeName=Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                      bg="powder blue", justify="left", textvariable=EmployeeName)
txtEmployeeName.grid(row=0, column=1)
lblAddress= Label(LeftInsideLF, font=("arial", 12, 'bold' ),text="Address",
                        fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
lblAddress.grid(row=1 , column=0)
txtAddress=Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                      bg="powder blue", justify="left",textvariable=Address)
txtAddress.grid(row=1, column=1)




lblReference = Label(LeftInsideLF, font=('arial', 12, 'bold'),text="Reference",
                     fg='Steel Blue', bd=10, anchor='e')
lblReference.grid(row=2, column=0)
txtReference=Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                      bg="powder blue", justify='left', textvariable=Reference)
txtReference.grid(row=2, column=1)
lblEmployerName= Label(LeftInsideLF, font=("arial", 12, 'bold' ),text="Employer Name",
                        fg="Steel Blue", bd=10, anchor='w', justify=LEFT)
lblEmployerName.grid(row=3, column=0)
txtEmployerName=Entry(LeftInsideLF, font=('arial', 12, 'bold'), bd=20, width=54,
                      bg="powder blue", justify="left",textvariable=EmployerName)
txtEmployerName.grid(row=3, column=1)


#==========================
lblCity = Label(LeftInsideLFLF, font=('arial', 12, 'bold'),text="City Weighting", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblCity.grid(row=0, column=0)
lblCity=Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=CityWeighting)
lblCity.grid(row=0, column=1)

#---------------------------------

lblBasicSalary = Label(LeftInsideLFLF, font=('arial', 12, 'bold'),text="Basic Salary", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblBasicSalary.grid(row=1, column=0)
lblBasicSalary=Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=BasicSalary)
lblBasicSalary.grid(row=1, column=1)

#--------------------------------
lblOverTime = Label(LeftInsideLFLF, font=('arial', 12, 'bold'),text="Over Time", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblOverTime.grid(row=2, column=0)
lblOverTime=Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=OverTime)
lblOverTime.grid(row=2, column=1)
#--------------------------------
lblGrossPay = Label(LeftInsideLFLF, font=('arial', 12, 'bold'),text="Gross Pay", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblGrossPay.grid(row=3, column=0)
lblGrossPay=Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left", textvariable=GrossPay)
lblGrossPay.grid(row=3, column=1)


lblNetPay = Label(LeftInsideLFLF, font=('arial', 12, 'bold'),text="Net Pay",
                  fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblNetPay.grid(row=4, column=0)
lblNetPay=Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=NetPay)
lblNetPay.grid(row=4, column=1)


#==================================================================================
#===================================

lblTax = Label(LeftInsideRFRF, font=('arial', 12, 'bold'),text="Tax", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblTax.grid(row=0, column=0)
lblTax=Entry(LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=Tax)
lblTax.grid(row=0, column=1)

#---------------------------------

lblPension = Label(LeftInsideRFRF, font=('arial', 12, 'bold'),text="Pension", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblPension.grid(row=1, column=0)
lblPension=Entry(LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=Pension)
lblPension.grid(row=1, column=1)

#--------------------------------
lblStudentLoan= Label(LeftInsideRFRF, font=('arial', 12, 'bold'),text="Student Loan", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblStudentLoan.grid(row=2, column=0)
lblStudentLoan=Entry(LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=StudentLoan)
lblStudentLoan.grid(row=2, column=1)
#--------------------------------
lblPayment = Label(LeftInsideRFRF, font=('arial', 12, 'bold'),text="NI Paymet", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblPayment.grid(row=3, column=0)
lblPayment=Entry(LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=NIPayment)
lblPayment.grid(row=3, column=1)


lblDeductions = Label(LeftInsideRFRF, font=('arial', 12, 'bold'),text="Deductions", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblDeductions.grid(row=4, column=0)
lblDeductions=Entry(LeftInsideRFRF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=Deductions)
lblDeductions.grid(row=4, column=1)

#==============================Right side=====================================
lblPostCode = Label(RightInsideLF, font=('arial', 12, 'bold'),text="Post Code", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblPostCode.grid(row=0 , column=0)
txtlblPostCode=Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=48,
                      bg="powder blue", justify="left",textvariable=PostCode)
txtlblPostCode.grid(row=0, column=1)
lblGender= Label(RightInsideLF, font=("arial", 12, 'bold' ),text="Gender",
                        fg="Steel Blue", bd=10, anchor='w',justify=LEFT)
lblGender.grid(row=1 , column=0)
txtGende=Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=48,
                      bg="powder blue", justify="left",textvariable=Gender)
txtGende.grid(row=1, column=1)


#========================Right inner Side============================================
lblPayDate = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="Pay Date", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblPayDate.grid(row=0 , column=0)
lblPayDate=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=PayDate)
lblPayDate.grid(row=0, column=1)

lblTaxPeriod = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="Tax Period", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblTaxPeriod.grid(row=1 , column=0)
lblTaxPeriod=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=TaxPeriod)
lblTaxPeriod.grid(row=1, column=1)
#=========================================
lblNINumber = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="NI Number", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblNINumber.grid(row=2 , column=0)
lblNINumber=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=NINumber)
lblNINumber.grid(row=2, column=1)
#=================================================
lblNICode = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="NI Code", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblNICode.grid(row=3 , column=0)
lblNICode=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=NICode)
lblNICode.grid(row=3, column=1)
#===========================================
lblTaxablePay = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="Taxable Pay", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblTaxablePay.grid(row=4 , column=0)
lblTaxablePay=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=TaxablePay)
lblTaxablePay.grid(row=4, column=1)
#=============================================
lblPensionablePay = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="Pensionable Pay", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblPensionablePay.grid(row=5 , column=0)
lblPensionablePay=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=PensionablePay)
lblPensionablePay.grid(row=5, column=1)


lblOtherPaymentsDue = Label(RightInsideLFLF, font=('arial', 12, 'bold'),text="Other Payments Due", fg='Steel Blue', bd=10, anchor='w', justify=LEFT)
lblOtherPaymentsDue.grid(row=6 , column=0)
lblOtherPaymentsDue=Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=10, width=18,
                      bg="powder blue", justify="left",textvariable=OtherPaymentsDue )
lblOtherPaymentsDue.grid(row=6, column=1)


btnWagePayment=Button(RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                      width=14, text="Wage Payment", bg="sky blue",command=MonthlySalary).grid(row=0, column=0)
btnReset=Button(RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                      width=14, text="Reset System", bg="sky blue",command=Reset).grid(row=1, column=0)
btnPayRef=Button(RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                      width=14, text="Pay Refernece", bg="sky blue",command=PayRef).grid(row=2, column=0)
btnPayCode=Button(RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                      width=14, text="Pay Code", bg="sky blue",command=PayPeriod).grid(row=3, column=0)
btnExit=Button(RightInsideRFRF, pady=8, bd=8 ,fg='black', font=('arial', 12, 'bold'),
                      width=14, text="Exit", bg="sky blue", command=Exit).grid(row=4, column=0)




payroll.mainloop()
