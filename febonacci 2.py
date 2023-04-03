from tkinter import *
root=Tk()

root.title("Fibonacci Series 2")
root.geometry("400x600")
result=Label(root)
sum=Label(root)

def febonacci():
    num=10
    num1=0
    num2=1
    sum1=0
    sum2=0
    counter=1
    while counter<num:
        result["text"]+=str(sum1)+" "
        counter=counter+1
        num1=num2
        num2=sum1
        sum1=num1+num2
        sum2=sum2+sum1
    sum["text"]=sum2

btn=Button(root,text="febonacci",command=febonacci) 
btn.pack()
result.pack()
sum.pack()   
        
        

root.mainloop()

