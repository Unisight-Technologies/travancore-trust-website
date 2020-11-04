import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)



def RegularDonation(name, email, contact, gender, occupation, city, zipcode, type, amount):


    sheet = client.open("Travancore").sheet1

    data = sheet.get_all_records()

    insertRow = [name, email, contact, gender, occupation, city, zipcode, type, amount]
    sheet.insert_row(len(data))


def AnonymousDonation(zipcode, type, amunt):


    sheet = client.open("Travancore").sheet2
