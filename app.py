from flask import Flask, abort, jsonify
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

app = Flask(__name__)

@app.route('/')
def records():
    """ List data from the spreadsheet """

    api_key = os.getenv('API_KEY')
    sheet_id = os.getenv('SHEET_ID')
    cell_range = os.getenv('CELL_RANGE')

    # API client
    service = build('sheets', 'v4', developerKey=api_key)
    sheet = service.spreadsheets()

    try:
        # Call the Sheets API
        print(f'Querying sheet {sheet_id} for range {cell_range}')
        result = sheet.values().get(spreadsheetId=sheet_id, range=cell_range).execute()
        values = result.get('values', [])
    except HttpError as e:
        abort(500, e)

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
                # Some rows may contain blank columns 
                # and are shorter than the heading row
                if len(row) > i and row[i]:
                    record[heading] = row[i]
            records.append(record)

    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0')