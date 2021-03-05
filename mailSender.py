import os
import smtplib
import imghdr
from email.message import EmailMessage
import datetime

#Converting the integer value of dt.month() to a string value corresponding to the name of the month
mesec=''
dt=datetime.datetime.today()
mes=dt.month

if mes==1:
    mesec='Januar'
elif mes==2:
    mesec='Februar'
elif mes==3:
    mesec='Mart'
elif mes==4:
    mesec='April'
elif mes==5:
    mesec='Maj'
elif mes==6:
    mesec='Jun'
elif mes==7:
    mesec='Jul'
elif mes==8:
    mesec='Avgust'
elif mes==9:
    mesec='Septembar'
elif mes==10:
    mesec='Oktobar'
elif mes==11:
    mesec='Novembar'
elif mes==12:
    mesec='Decembar'
else:
    exit()


EMAIL_ADRESS=os.environ.get('EMAIL_USER')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')
EMAIL_TO=os.environ.get('EMAIL_TO')


msg=EmailMessage()
msg['Subject'] = 'Izveštaj za {}'.format(mesec)
msg['From'] = EMAIL_ADRESS
msg['To'] = EMAIL_TO
msg.set_content('Postovani, \nU prilogu ovog mejla Vam dostavljam izveštaje za {}'.format(mesec))

#Getting the PDF-s 
pdf_path = os.path.dirname(os.path.realpath(__file__))
pdf_path=pdf_path + "/pdfs/"
pdfs = os.listdir('pdfs')
for file in pdfs:
    with open(pdf_path + file, 'rb') as f:
        file_data=f.read()
        file_name=os.path.basename(f.name)
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

#Getting the images
img_path = os.path.dirname(os.path.realpath(__file__))
img_path=img_path + "/images/"
images = os.listdir('images')
for file in images:
    with open(img_path + file, 'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=os.path.basename(f.name)
    msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)


   

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    
