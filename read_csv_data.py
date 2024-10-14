import pandas as pd

class read_csv_file_data:
#---fun for adding RECRUITERS_MAIL_ID from csv file
    list_deteils=[]

    def load_RECRUITERS_Data(self):
        data_file = pd.read_csv('pythoncsv.csv')
        self.list_deteils


        for _,row in data_file.iterrows():
            self.list_deteils.append(row.to_dict())

        print(f"my dict- {self.list_deteils}")


    # calling below mehod
 readFile=read_csv_file_data()
readFile.load_RECRUITERS_Data()

for i, j in readFile.list_deteils:
    print(f'{i}:{j}')







