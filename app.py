from flask import Flask, abort, jsonify
from googleapiclient.discovery import build
import os

app = Flask(__name__)

sheets_api_key = os.getenv('SHEETS_API_KEY')
sheet_id = os.getenv('SHEET_ID')
cell_range = os.getenv('CELL_RANGE')

@app.route('/')
def records():
    """ List data from the spreadsheet """

    # API client
    service = build('sheets', 'v4', developerKey=sheets_api_key)
    sheet = service.spreadsheets()

    # Call the Sheets API
    print(f'Querying sheet {sheet_id} for range {cell_range}')
    result = sheet.values().get(spreadsheetId=sheet_id, range=cell_range).execute()
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