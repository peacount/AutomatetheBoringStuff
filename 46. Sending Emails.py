# SMTP: Simple Mail Transfer Protocol
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
print(type(conn))
conn.ehlo()
conn.starttls()
conn.login('doublermad@gmail.com', 'xxxx') # enter password
conn.sendmail('doublermad@gmail.com', 'doublermad@gmail.com', 'Subject: So long...\n\nDear Jenny, \n So long, and thanks for all the fish. \n\n-Jenny')
conn.quit()

