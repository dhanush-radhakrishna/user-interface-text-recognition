from fpdf import FPDF
import pytesseract as tes
from PIL import Image
def write(fname,image_list):
    #saving pdf is a type of FPDF class
    pdf=FPDF()
    print("entered pdf module")
    pdf.add_page()
    pdf.set_font("Arial",size=12)
    for i in image_list:
        img=Image.open(i)
        text=tes.image_to_string(img,lang='eng')
        details=text.split('\n')
        new=[]
        for k in details:
            if len(k)>2:
                new.append(k)
        print(new)
        for j in new:
            pdf.cell(0,10,txt=j,ln=1,align='L')
        pdf.cell(0,10,txt='-------------------------------------------------',ln=1,align='L')
    pdf.output(fname+".pdf")
    print("finished writing")

