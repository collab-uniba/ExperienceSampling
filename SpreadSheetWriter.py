

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheetWriterClass:
    def __init__(self):
        self.takeCredentials()
        self.setSheet()

    def takeCredentials(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('build/ExperienceSampling/credentials.json',
                                                                       scope)
        self.gc = gspread.authorize(credentials)

    def setSheet(self):
        sh = self.gc.open('dati_experience')
        # Open a worksheet from spreadsheet with one shot
        self.worksheet = sh.get_worksheet(0)

    def writeOnsheet(self,arrayValues):
        values_list = self.worksheet.col_values(1)
        length = len(values_list) + 1
        self.worksheet.append_row(arrayValues,"RAW")

        if(self.confirmWrite(length,arrayValues[0]) == False):
            raise Exception('no value witten')

    def confirmWrite(self,lenght,openTime):
        if(self.worksheet.acell('A'+str(lenght)).value == str(openTime)):
            return True
        return False