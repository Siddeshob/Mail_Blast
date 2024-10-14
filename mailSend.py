from smtplib import SMTP
from constants import MY_EMAIL,PASSWORD,RECRUITERS_MAIL_ID,RECRUITERS_NAME,POSITION_NAME,COMPANY_NAME
from  read_csv_data import read_csv_file_data

class mail_send_app:

    def __init__(self):
        pass

    def dect_to_store_csv_date(self):
        pass


    def smtp_connection_method(self):
        connection = SMTP('smtp.gmail.com', 587)
        connection.starttls()  # Start TLS encryption
        connection.login(user=MY_EMAIL, password=PASSWORD)


        #***** creating OBJECT for read_csv_file_data
        read_csv_obj=read_csv_file_data()
        read_csv_obj.load_RECRUITERS_Data()


        # Format the email message
        subject = "Subject: Good Morning\n"
        body = "Hello\n\nGood morning2!"
        msg = subject + body

        # Looping dict to find & send multiple email

        for i,j in read_csv_obj.list_deteils:
            print(f'{i}:{j}')

        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECRUITERS_MAIL_ID, msg=msg)
        connection.close()
