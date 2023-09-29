import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of your access
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Specify the path to your credentials JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name('app/mcqgenerator.json', scope)

# Authenticate with Google Sheets
client = gspread.authorize(creds)


def update_sheet(data,sheet_name,worksheet_name,subtopic):
    # Open the spreadsheet by title
    sheet = client.open(sheet_name).worksheet(worksheet_name)
    rows = []
    for question in data["questions"]:
           
            options = question['options']
            if question.get("code"):
                row = [subtopic,question['question'].split("```")[0],question['code'],options[0],options[1],options[2],options[3],question['answer']]
            else:
                row = [subtopic,question['question'],"",options[0],options[1],options[2],options[3],question['answer']]
            sheet.append_row(row)
    return True
  