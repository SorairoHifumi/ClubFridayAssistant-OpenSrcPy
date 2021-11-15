import time
from googleapiclient.discovery import build
from google.oauth2 import service_account
values = []


def getCurrentItem():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    sheet_id = '1-0sX1kDW_S86B9c9pfKdPxbfrjxeKkhEfx4T3mvtC7I'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range="Sheet1!A1:H999").execute()
    values = result.get('values', [])
    return values


def removerow(row):
    row = int(row) + 1
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    sheet_id = '1-0sX1kDW_S86B9c9pfKdPxbfrjxeKkhEfx4T3mvtC7I'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id,
                                range="Sheet1!A1:E999").execute()
    values = result.get('values', [])

    temp = ["", "", "", "", "", "", "", "", "", "", "", ""]

    # print(temp)
    aoa = [temp]

    new_cell = f"Sheet1!A{row}"
    # print(new_cell)
    print('Removing...')

    request = sheet.values().update(spreadsheetId=sheet_id, range=new_cell,
                                    valueInputOption="USER_ENTERED", body={"values": aoa}).execute()
    print('Success!~')


def modifyList(std_name, due_date, due_month, gradenum, classnum, via, desc, mode):
    if mode == 'append':
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID and range of a sample spreadsheet.
        sheet_id = '1-0sX1kDW_S86B9c9pfKdPxbfrjxeKkhEfx4T3mvtC7I'

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range="Sheet1!A1:E999").execute()
        values = result.get('values', [])

        new_rows_avail = 1
        for new_row in range(len(values)):
            try:
                if values[new_rows_avail] == []:
                    break
                else:
                    new_rows_avail += 1
            except:
                new_rows_avail = len(values)
        new_rows_avail += 1

        temp = []
        temp.append(new_rows_avail-1)
        temp.append(std_name)
        temp.append(gradenum)
        temp.append(classnum)
        temp.append(due_date)
        temp.append(due_month)
        temp.append(via)
        temp.append(desc)

        # print(temp)
        aoa = [temp]

        new_cell = f"Sheet1!A{new_rows_avail}"
        # print(new_cell)
        print('Uploading...')

        request = sheet.values().update(spreadsheetId=sheet_id, range=new_cell,
                                        valueInputOption="USER_ENTERED", body={"values": aoa}).execute()
        print('Success!~')
        print(f'Assingnment ID: {new_rows_avail - 1}')
        print("")
        time.sleep(1)
