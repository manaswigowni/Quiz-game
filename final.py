from tkinter import*
from tkinter import ttk
import time
import matplotlib.pyplot as plt

window=ttk.Notebook(height=2000,width=2500)

front=ttk.Frame(window)
frame1=ttk.Frame(window)
frame2=ttk.Frame(window)
frame3=ttk.Frame(window)
frame4=ttk.Frame(window)
frame5=ttk.Frame(window)
frame6=ttk.Frame(window)
frame7=ttk.Frame(window)
frame8=ttk.Frame(window)
frame9=ttk.Frame(window)
frame10=ttk.Frame(window)

global correct
correct=0
global incorrect
incorrect=0
global ans
ans={1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',10:''}
global subj
subj={'space':0,'sports':0,'gk':0}
global time_arr
time_arr={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10}


def quiz(window):
    global front
    window.add(front,text='Welcome')
    Label(front,text="THE MIND FIZZ",font=('Toffee',60,'bold'),bg='pale green').place(x=450,y=100)
    Label(front,text="User Name",font=('Times New Roman',30,'bold'),bg='lavender').place(x=400,y=400)
    global t1
    t1=Entry(front,font=('Times New Roman',30,'bold'))
    t1.place(x=650,y=400)
    Button(front,text="Start",font=('Times New Roman',30,'bold'),bg='pink',command=lambda:[starttime(),sample()]).place(x=1000,y=550)

    window.add(frame1,text='Question1')

    Label(frame1, text='1. Which among the following state produces maximum raw silk in India?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame1, text='a.Bihar',font=('Arial',25,'bold'),bg='violet',command=lambda:window_incorrect(1)).place(x=160,y=150)
    Button(frame1, text='b.Assam',font=('Arial',25,'bold'),bg='violet',command=lambda:window_incorrect(1)).place(x=160,y=250)
    Button(frame1, text='c.karnataka',font=('Arial',25,'bold'),bg='violet',command=lambda:window_correct(1,'gk')).place(x=160,y=350)
    Button(frame1, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame1.destroy(),starttime()]).place(x=1000,y=500)

    
    
    window.add(frame2, text='Question2')

    Label(frame2, text='2. Who among the following was known as Flying Sikh?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame2, text='a.Milkha Singh',font=('Arial',25,'bold'),bg='pink',command=lambda:window_correct(2,'sports')).place(x=160,y=150)
    Button(frame2, text='b.Harbhajan Singh',font=('Arial',25,'bold'),bg='pink',command=lambda:window_incorrect(2)).place(x=160,y=250)
    Button(frame2, text='c.Yuvaraj Singh',font=('Arial',25,'bold'),bg='pink',command=lambda:window_incorrect(2)).place(x=160,y=350)
    Button(frame2, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame2.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame3, text='Question3')

    Label(frame3, text='3. Which of the following is indicated by the colour of a star?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame3, text='a.Weight',font=('Arial',25,'bold'),bg='light blue',command=lambda:window_incorrect(3)).place(x=160,y=150)
    Button(frame3, text='b.Distance',font=('Arial',25,'bold'),bg='light blue',command=lambda:window_incorrect(3)).place(x=160,y=250)
    Button(frame3, text='c.Temperature',font=('Arial',25,'bold'),bg='light blue',command=lambda:window_correct(3,'space')).place(x=160,y=350)
    Button(frame3, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame3.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame4, text='Question4')

    Label(frame4, text='4. Patanjali is well known for the compilation of ',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame4, text='a.Yoga Sutra',font=('Arial',25,'bold'),bg='light green',command=lambda:window_correct(4,'gk')).place(x=160,y=150)
    Button(frame4, text='b.Panchatantra',font=('Arial',25,'bold'),bg='light green',command=lambda:window_incorrect(4)).place(x=160,y=250)
    Button(frame4, text='c.Brahma Sutra',font=('Arial',25,'bold'),bg='light green',command=lambda:window_incorrect(4)).place(x=160,y=350)
    Button(frame4, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame4.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame5, text='Question5')

    Label(frame5, text='5. The hottest planet in the solar system?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame5, text='a.Mercury',font=('Arial',25,'bold'),bg='orange',command=lambda:window_incorrect(5)).place(x=160,y=150)
    Button(frame5, text='b.Venus',font=('Arial',25,'bold'),bg='orange',command=lambda:window_correct(5,'space')).place(x=160,y=250)
    Button(frame5, text='c.Mars',font=('Arial',25,'bold'),bg='orange',command=lambda:window_incorrect(5)).place(x=160,y=350)
    Button(frame5, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame5.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame6, text='Question6')

    Label(frame6, text='6. Which is the governing body Chess in the world?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame6, text='a.World Chess Federation ',font=('Arial',25,'bold'),bg='plum',command=lambda:window_correct(6,'sports')).place(x=160,y=150)
    Button(frame6, text='b.World Chess Association ',font=('Arial',25,'bold'),bg='plum',command=lambda:window_incorrect(6)).place(x=160,y=250)
    Button(frame6, text='c.World Chess Organisation',font=('Arial',25,'bold'),bg='plum',command=lambda:window_incorrect(6)).place(x=160,y=350)
    Button(frame6, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame6.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame7, text='Question7')

    Label(frame7, text='7. In order of their distances from the Sun, which of the following planets \n lie between Mars and Uranus?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame7, text='a.Earth and Jupiter',font=('Arial',25,'bold'),bg='lavender',command=lambda:window_incorrect(7)).place(x=160,y=150)
    Button(frame7, text='b.Jupiter and Saturn',font=('Arial',25,'bold'),bg='lavender',command=lambda:window_correct(7,'space')).place(x=160,y=250)
    Button(frame7, text='c.Saturn and Earth',font=('Arial',25,'bold'),bg='lavender',command=lambda:window_incorrect(7)).place(x=160,y=350)
    Button(frame7, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame7.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame8, text='Question8')

    Label(frame8, text='8. The water comes to Indira Gandhi Canal from the following Rivers?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame8, text='a.Sutlej Only',font=('Arial',25,'bold'),bg='gold',command=lambda:window_incorrect(8)).place(x=160,y=150)
    Button(frame8, text='b.Sutlej & Beas',font=('Arial',25,'bold'),bg='gold',command=lambda:window_correct(8,'gk')).place(x=160,y=250)
    Button(frame8, text='c.Sutlej , Beas & Ravi',font=('Arial',25,'bold'),bg='gold',command=lambda:window_incorrect(8)).place(x=160,y=350)
    Button(frame8, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame8.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame9, text='Question9')

    Label(frame9, text='9. A blackhole is a ',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame9, text='a.Contracted star with intense gravitational pull',font=('Arial',25,'bold'),bg='pale violet red',command=lambda:window_correct(9,'space')).place(x=160,y=150)
    Button(frame9, text='b.Star with very low surface temperature',font=('Arial',25,'bold'),bg='pale violet red',command=lambda:window_incorrect(9)).place(x=160,y=250)
    Button(frame9, text='c.Star with no atmosphere',font=('Arial',25,'bold'),bg='pale violet red',command=lambda:window_incorrect(9)).place(x=160,y=350)
    Button(frame9, text="Next",font=('Arial',25,'bold'),bg='grey',command=lambda:[frame9.destroy(),starttime()]).place(x=1000,y=500)

    window.add(frame10, text='Question10')


    Label(frame10, text='10. India played ther first T20 match against ?',font=('Arial',30,'bold')).place(x=40,y=20)
    Button(frame10, text='a.Australia',font=('Arial',25,'bold'),bg='pale green',command=lambda:window_incorrect(10)).place(x=160,y=150)
    Button(frame10, text='b.Pakistan',font=('Arial',25,'bold'),bg='pale green',command=lambda:window_incorrect(10)).place(x=160,y=250)
    Button(frame10, text='c.South Africa',font=('Arial',25,'bold'),bg='pale green',command=lambda:window_correct(10,'sports')).place(x=160,y=350)
    Button(frame10, text='Submit',font=('Arial',25,'bold'),bg='grey',command=lambda:[frame10.destroy(),disp_result()]).place(x=1000,y=500)


def sample():
    global t1
    global front
    global name1
    name1=t1.get()
    front.destroy()

def starttime():
    global start_time
    start_time=time.time()


def window_correct(qid,sub):
    subj[sub]+=1
    global stop_time
    global start_time
    stop_time=time.time()
    tot=stop_time-start_time
    global correct
    global incorrect
    global ans
    if ans[qid]=='':
        pass
    else:
        incorrect-=1
    correct+=1
    global time_arr
    ans[qid]="Correct"
    time_arr[qid]=tot

def window_incorrect(qid):
    global stop_time
    global start_time
    stop_time=time.time()
    tot=stop_time-start_time
    global incorrect
    global correct
    global ans
    if ans[qid]=='':
        pass
    else:
        correct-=1
    incorrect+=1
    global time_arr
    ans[qid]="Incorrect"
    time_arr[qid]=tot

    
    
def disp_result():
    window.destroy()
    end_result=Tk()
    end_result.title("Result Analysis")
    global incorrect
    global correct  
    global ans
    global time_arr
    global result
    result=correct*10
    correct1="Correct answers\t\t"+str(correct)
    incorrect1="Incorrect answers\t\t"+str(incorrect)
    result1="Result\t\t        "+str(result)+"%\n\n\n"
    Label(end_result,text="RESULTS\n\n",font=15).pack()
    Label(end_result,text=correct1).pack()
    Label(end_result,text=incorrect1).pack()
    Label(end_result,text=result1).pack()
    head="Question    Answer chosen    Time taken(s)"
    Label(end_result,text=head).pack()
    for i in range(0,10):
        if ans[i+1]!='':
            s=str(i+1)+"\t"+ans[i+1]+"\t\t"+str(round(time_arr[i+1],2))
        else:
            s=str(i+1)+"\t"+"Skipped"+"\t\t"+str(round(time_arr[i+1],2))
        Label(end_result,text=s).pack()

    Label(end_result,text="\n\nAnalysis").pack()

    for i in ['gk','sports']:
        if subj[i]==3:
            rev="Excellent"
        elif subj[i]==2:
            rev="Good"
        elif subj[i]<=1:
            rev="Needs improvement"
        str2=i+"  :  "+rev
        Label(end_result,text=str2).pack()

    if subj['space']==4:
        rev="Excellent"
    elif subj['space']==3 or subj['space']==2:
        rev="Good"
    elif subj['space']<=1:
        rev="Needs improvement"
    str2='space'+"  :  "+rev
    Label(end_result,text=str2).pack()
    prev_performance()
    end_result.mainloop()
    
    
def prev_performance():
    global name1
    global result
    with open ("prev_records.csv","a+") as f1:
        f1.write(name1)
        f1.write(",")
        f1.write(str(result))
        f1.write("\n")
    
    class data:
        def __init__(self,name,marks):
            self.name=name
            self.marks=marks
    d=[]
    with open ("prev_records.csv","r") as f1:
        details=f1.readlines()
        n=len(details)
        for i in range(n):
            name,marks=details[i].split(",")
            marks=int(marks)
            d.append(i)
            d[i]=data(name,marks)
    x=[]
    y=[]
    count=0
    for k in range(len(d)):
        if d[k].name==name1:
            y.append(d[k].marks)
            x.append(str(count+1))
            count+=1
    plt.bar(x,y)
    plt.xlabel("Attempt number")
    plt.ylabel("Result")
    plt.title("Performance Tracker")
    plt.show()

quiz(window)

window.pack()

window.mainloop()