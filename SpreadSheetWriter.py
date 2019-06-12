

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import Utility as ut

class SpreadSheetWriterClass:
    def __init__(self):
        self.status = self.takeCredentials()
        self.status2 = self.setSheet()

    def takeCredentials(self):
        try:
            scope = ['https://spreadsheets.google.com/feeds',
                     'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('build/ExperienceSampling/credentials.json',
                                                                           scope)
            self.gc = gspread.authorize(credentials)
        except:
            return False

    def setSheet(self):
        try:
            sh = self.gc.open('dati_experience')
            # Open a worksheet from spreadsheet with one shot
            self.worksheet = sh.get_worksheet(0)
        except:
            return False

    def writeOnsheet(self,arrayValues):
        if(ut.internet_on()):
            if self.status == False:
                self.status = self.takeCredentials()
            if self.status2 == False:
                self.status2 = self.setSheet()
            self.insertFromOffline()
            values_list = self.worksheet.col_values(1)
            length = len(values_list) + 1
            self.worksheet.append_row(arrayValues,"RAW")

            if(self.confirmWrite(length,arrayValues[0]) == False):
                raise Exception('no value witten')
        else:
            file = open('toCommit.txt', 'a')
            stringValues =  ','.join(str(e) for e in arrayValues)
            file.write(stringValues+"\n")
            file.close()
    def insertFromOffline(self):

        lines = open('toCommit.txt').readlines()
        if(len(lines) > 0):
            line = lines[0]
            with open('toCommit.txt', 'w') as f:
                f.writelines(lines[1:])
                f.close()
            self.writeOnsheet(line.split(","))
        return



    def confirmWrite(self,lenght,openTime):
        if(self.worksheet.acell('A'+str(lenght)).value == str(openTime)):
            return True
        return False