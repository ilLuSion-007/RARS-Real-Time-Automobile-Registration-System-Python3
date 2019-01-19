from Database import Database as db
import os
#import HTML
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class details_email():
    
     @staticmethod
     def getmail(user_id,email_id):
         cur = db.getCursor()


         query1 = ("""select * from account_holder_details WHERE user_id = %s""")

         cur.execute(query1,[user_id])


         htmlcode = cur.fetchall()

         results50 = "User Account Information: %s" % (htmlcode) + "\n"

         curs = db.getCursor()


         query2 = ("""select * from vehicle_details WHERE user_id = %s""")

         curs.execute(query2,[user_id])


         html = curs.fetchall()

         results51 = "Vehicle Information: %s" % (html) + "\n"

         curso = db.getCursor()


         query3 = ("""select * from license_details WHERE user_id = %s""")

         curso.execute(query3,[user_id])


         htmlcod = curso.fetchall()

         results52 = "License Information: %s" % (htmlcod) 


         me = "rarsvehicle@gmail.com"
         you = email_id

         msg = MIMEMultipart('alternative')
         msg['Subject'] = "User Personal, Vehicle & License Information - RARS (rtovehicle.ooo)"
         msg['From'] = me
         msg['To'] = email_id


         body = results50 + results51 + results52


         part1 = MIMEText(body, 'plain')



         msg.attach(part1)

         mail = smtplib.SMTP('smtp.gmail.com', 587)

         mail.ehlo()

         mail.starttls()

         mail.login('rarsvehicle@gmail.com', 'rars@12345')
         mail.sendmail(me, you, msg.as_string())
         print("Mail Successfully Sent!")
         mail.quit()
         