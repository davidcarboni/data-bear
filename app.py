from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
import json
from flask import Flask, request, abort, jsonify

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1tceHkbkFN1sz7t6kQAp702CMMmQP3Cu7lEKn4rnD2pY'
SAMPLE_RANGE_NAME = 'Sheet1!A1:L16'

app = Flask(__name__)

@app.route('/')
def list():
    """ List all data from the spreadsheet """

    # The source sheet and cell range
    spreadsheet = request.args.get('sheet') or SAMPLE_SPREADSHEET_ID
    cells = request.args.get('range') or SAMPLE_RANGE_NAME

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
        print('Here goes.')
        headings = values[0]
        records = []
        for row in values[1:]:
            record = {}
            for i, heading in enumerate(headings):
                record[heading] = row[i]
                print(f'{heading}={row[i]}')
            records.append(record)

    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


