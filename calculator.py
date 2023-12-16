from tkinter import * 
def btnClick(item): 
    global expression 
    expression = expression + str(item)  
    text_input.set(expression) 
 
def btnClearDisplay():     
    global expression 
    expression = ''          
    text_input.set('')         
 
def btnEqualsInput():     
    global expression 
    try: 
        result=str(eval(expression)) 
        text_input.set(result) 
        expression = '' 
    except ZeroDivisionError: 
        text_input.set('Zero Division Error') 
    except: 
        text_input.set('Invalid Input') 
 
#main 
cal = Tk() 
cal.title("Calculator") 
expression = '' 
text_input = StringVar() 
fnt = ('arial', 20, 'bold') 
screen = Entry(cal, font=fnt, textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4) 

btn7 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='7', bg='powder blue', 
command=lambda:btnClick(7)).grid(row=1,column=0) 
btn8 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='8', bg='powder blue', 
command=lambda:btnClick(8)).grid(row=1,column=1) 
btn9 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='9', bg='powder blue', 
command=lambda:btnClick(9)).grid(row=1,column=2) 
Addition = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='+', bg='powder blue', 
command=lambda:btnClick('+')).grid(row=1,column=3) 

btn4 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='4', bg='powder blue', 
command=lambda:btnClick(4)).grid(row=2,column=0) 
btn5 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='5', bg='powder blue', 
command=lambda:btnClick(5)).grid(row=2,column=1) 
btn6 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='6', bg='powder blue', 
command=lambda:btnClick(6)).grid(row=2,column=2) 
Subtraction = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='-', bg='powder blue', 
command=lambda:btnClick('-')).grid(row=2,column=3) 

btn1 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='1', bg='powder blue', 
command=lambda:btnClick(1)).grid(row=3,column=0) 
btn2 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='2', bg='powder blue', 
command=lambda:btnClick(2)).grid(row=3,column=1) 
btn3 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='3', bg='powder blue', 
command=lambda:btnClick(3)).grid(row=3,column=2) 
Multiply = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='*', bg='powder blue', 
command=lambda:btnClick('*')).grid(row=3,column=3) 

btn0 = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='0', bg='powder blue', 
command=lambda:btnClick(0)).grid(row=4,column=0) 
btnClear = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='C', bg='powder blue', 
command=lambda:btnClearDisplay()).grid(row=4,column=1) 
Moddiv = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='%', bg='powder blue', 
command=lambda:btnClick('%')).grid(row=4,column=2) 
Division = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='/', bg='powder blue', 
command=lambda:btnClick('/')).grid(row=4,column=3) 
btnEquals = Button(cal,padx=16,bd=8, fg="black",font=fnt,text='=', bg='powder blue', 
command=btnEqualsInput).grid(columnspan=4,sticky=EW)

cal.mainloop()