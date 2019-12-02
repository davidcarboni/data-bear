import os
from googleapiclient.discovery import build
from flask import Flask, request, abort, jsonify

# The ID and range of a sample spreadsheet.
SHEET_ID = os.getenv('SHEET_ID') or '1cCUTcpmcxyKndVHCDvnl6IwBE7zXP1Lhq1kct-aytB0'
CELL_RANGE = os.getenv('CELL_RANGE') or 'Sheet1!a1:e4'

app = Flask(__name__)


@app.route('/', defaults={'sheet': '', 'cells': ''})
@app.route('/<sheet>', defaults={'cells': ''})
@app.route('/<sheet>/<cells>')
def get(sheet, cells):
    """ List all data from the spreadsheet, using either the path or get parameters """

    # The source sheet and cell range
    spreadsheet = sheet or request.args.get('sheet') or SHEET_ID
    cells = cells or request.args.get('range') or CELL_RANGE

    # API client
    sheets_api_key = os.getenv('SHEETS_API_KEY')
    service = build('sheets', 'v4', developerKey=sheets_api_key)
    sheet = service.spreadsheets()

    # Call the Sheets API
    result = sheet.values().get(spreadsheetId=spreadsheet, range=cells).execute()
    values = result.get('values', [])

    # Process the return
    if not values:
        print('No data found.')
        abort(404)
    else:
        headings = values[0]
        records = []
        for row in values[1:]:
            record = {}
            for i, heading in enumerate(headings):
                record[heading] = row[i]
            records.append(record)

    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


