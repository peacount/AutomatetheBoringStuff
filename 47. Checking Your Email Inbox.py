# Internet Message Access Protocol
import imapclient, datetime
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login ('doublermad@gmail.com', 'JongWonSunJong12')
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search(['SINCE', datetime.date(2020, 12, 20)])  # refer to table 16-3
print(UIDs)
rawMessage = conn.fetch([6733], ['BODY[]', 'FLAGS'])
# print(rawMessage)

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[6733][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))
print(message.text_part)
print(message.html_part)
message.html_part == None

print(message.text_part.get_payload().decode('UTF-8'))
print(message.text_part.charset)

print(conn.list_folders())
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['ON', datetime.date(2013, 11, 11)]) 
print(UIDs)
# conn.delete_messages(UIDs)