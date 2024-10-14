import pandas as pd
from constants import MY_EMAIL,PASSWORD
from smtplib import SMTP



class mail_aplication_class:
    def mail_subject_and_body_method(self,POSITION_NAME='POSITION_NAME',RECRUITERS_NAME='RECRUITERS_NAME',COMPANY_NAME='COMPANY_NAME'):
        MAIL_SUBJECT = f"""Subject: Request for Job Reference for {POSITION_NAME} position.\n\n"""

        MAIL_BODY = f"""        Dear {RECRUITERS_NAME},\n

                I hope this email finds you well. I am applying for a {POSITION_NAME} position at {COMPANY_NAME}, and I would be grateful if you could provide a reference for me. During my time, I gained valuable experience in [mention key skills or projects], and your recommendation would greatly support my application.

                If you are willing, the hiring manager may contact you at your convenience. Please let me know if you need any additional information from me.

                Thank you for your consideration and support.

                Best regards,
                Siddesha O B
                
                """
        MAIL_CONTENT=MAIL_SUBJECT+MAIL_BODY

        return MAIL_CONTENT

    def read_data_from_csv_file_method(self):
        list_deteils=[]
        data_file = pd.read_csv('pythoncsv.csv')

        # storing each rows as a dict ///list of dict
        for _, row in data_file.iterrows():
            list_deteils.append(row.to_dict())

        return list_deteils

    def smtp_connection_and_sending_method(self):
        connection = SMTP('smtp.gmail.com', 587)
        connection.starttls()

        connection.login(user=MY_EMAIL,password=PASSWORD)

        dict_list_csv_data=self.read_data_from_csv_file_method()
        for i in dict_list_csv_data:
                RECRUITERS_MAIL_ID = i.get('RECRUITERS_MAIL_ID')
                POSITION_NAME = i.get('POSITION_NAME')
                RECRUITERS_NAME = i.get('RECRUITERS_NAME')
                COMPANY_NAME = i.get('COMPANY_NAME')

                msg=self.mail_subject_and_body_method(POSITION_NAME,RECRUITERS_NAME,COMPANY_NAME)
                print(f'\n-@@@@@@@@@@@@@@@@@@@@@@@@@@@@{RECRUITERS_MAIL_ID}---{POSITION_NAME},{RECRUITERS_NAME},{COMPANY_NAME}-')

                connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECRUITERS_MAIL_ID, msg=msg)
        connection.close()



mail_aplication_class_obj=mail_aplication_class()
print(f'------------------------printing mail_subject_and_body_method---------------------------------')
print(mail_aplication_class_obj.mail_subject_and_body_method())

print(f'------------------------printing read_data_from_csv_file_method---------------------------------')
print(mail_aplication_class_obj.read_data_from_csv_file_method())

print(f'------------------------printing smtp_connection_and_sending_method---------------------------------')
print(mail_aplication_class_obj.smtp_connection_and_sending_method())