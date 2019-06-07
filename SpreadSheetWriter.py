

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('build/ExperienceSampling/credentials.json', scope)

gc = gspread.authorize(credentials)
sh = gc.open('dati_experience')
# Open a worksheet from spreadsheet with one shot
worksheet = sh.get_worksheet(0)

worksheet.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
cell_list = worksheet.range('A1:B7')
