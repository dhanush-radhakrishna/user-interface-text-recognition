from tkinter import *
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox
import writing_to_excel as write
import pdf
import text_file
root=Tk()
image_list=[]
#function to store image name and display image path
def openimage():
    path=filedialog.askopenfilenames(initialdir="\DHANUSH's\PYTHON programs",title="image open")
    lst=list(path)
    for i in lst:
        s=i.split('/')
        image_list.append(s[-1])
    print(image_list)
    txt=str(image_list[:])
    pathLabel=Label(root,text=txt).place(x=150,y=160)
#radio function
def sel():
   print(str(radio.get()))
#close function
def close():
    root.destroy()
#pragraphs
para1=Label(root,text="Three simple steps to scan images and extract the text",font=('times new roman',15,'bold')).place(x=50,y=10)
para2=Label(root,text="1. Browse and open the images you want to scan",font=('arial',12,'italic')).place(x=50,y=50)
para3=Label(root,text="2. Select type of the file you want to write the text",font=('arial',12,'italic')).place(x=50,y=85)
para4=Label(root,text="3. Click on finish",font=('arial',12,'italic')).place(x=50,y=120)

#browse button
browse_button=Button(root,text="Browse",command=openimage).place(x=50,y=160)

#radio buttons,,    var_radio.get() contains the option selected
radio=IntVar()
radio_val=radio.get()
rd1=Radiobutton(root,text="Excel file",font=("arial",11),variable=radio,value=1,command=sel).place(x=50,y=205)
rd2=Radiobutton(root,text="PDF file",font=("arial",11),variable=radio,value=2,command=sel).place(x=400,y=205)
rd3=Radiobutton(root,text=".txt file",font=("arial",11),variable=radio,value=3,command=sel).place(x=730,y=205)

#excel forms//   n contains the no. of columns
col_label1=Label(root,text="Enter number of ",font=("arial",8)).place(x=70,y=250)
col_label1=Label(root,text="columns in excel sheet",font=("arial",8)).place(x=70,y=265)
cols= Entry(root, width=3, borderwidth=3,font=('times new roman',15))
cols.place(x=200,y=250)
no_of_cols=cols.get()
def validate():
    n=cols.get()
    r=radio.get()
    if n.isdigit() and (r==1):
        return
    else:
        error1=messagebox.showerror("Invalid Entry",'''Any of the below mistake must have occurred.\n1. You have entered a letter/string.\n 2. You have selected other file format.\n 3. You have not selected any file format''')
cols_validate=Button(root,text="confirm",command=validate).place(x=250,y=250)
#column  names form 
cols_name_label=Label(root,text="Enter the colums ",font=("arial",8)).place(x=70,y=320)
cols_name= Entry(root, width=17, borderwidth=3,font=('times new roman',13))
cols_name.place(x=175,y=320)

#function to send column names and array of images to writing_to_excel module
def sendvalues():
    select=radio.get()
    if select==1:
        column_names=cols_name.get()
        fname=excel_file_name.get()
        if len(column_names)==0:
            write.openandwrite(fname,image_list)
        else:
            write.openandwrite(fname1,image_list,column_names)
    elif select==2:
        fname=pdf_file_name.get()
        pdf.write(fname,image_list)
    elif select==3:
        fname=text_file_name.get()
        text.write(fname,image_list)
    else:
        error2=messagebox.showerror("Error",'''Any of the below mistake must have occurred.\n1. You have entered a letter/string.\n 2. You have selected other file format.\n 3. You have not selected any file format''')

#file name form for excel files
excel_file_name_label1=Label(root,text="Enter the file name ",font=("arial",8)).place(x=70,y=380)
excel_file_name_label1=Label(root,text="(existing)",font=("arial",8)).place(x=70,y=400)
excel_file_name= Entry(root, width=17, borderwidth=3,font=('times new roman',15))
excel_file_name.place(x=175,y=380)
#file name for PDF files
pdf_file_name_label=Label(root,text="Enter the file name ",font=("arial",12)).place(x=450,y=270)
pdf_file_name=Entry(root,width=17,borderwidth=3,font=("times new roman",15))
pdf_file_name.place(x=450,y=310)
#file name for text file
text_file_name_label=Label(root,text="Enter the file name ",font=("arial",12)).place(x=750,y=270)
text_file_name=Entry(root,width=17,borderwidth=3,font=("times new roman",15))
text_file_name.place(x=750,y=310)
#SUBMIT button
submit=Button(root,width=13,height=2,text="SUBMIT",command=sendvalues).place(x=500,y=430)
#exit button
exit_button=Button(root,width=13,height=2,text="Exit",command=close).place(x=860,y=430)


#main loop
root.geometry("1000x500")
root.mainloop()
