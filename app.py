from flask import Flask, abort, jsonify
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import urllib.parse
import os

app = Flask(__name__)

sheets_api_key = os.getenv('SHEETS_API_KEY')
folder_id = os.getenv('FOLDER_ID')

file_list = None

@app.route('/')
def list_sheets():
    items = list_folder(refresh=True)

    if not items:
        abort(404, 'No files found.')
    else:
        result = []
        for item in items:
            result.append({
                'name': item['name'],
                'link': '/' + urllib.parse.quote(item['name']),
            })
        return jsonify(result)

@app.route('/<name>')
def records(name):
    """ List data from a spreadsheet """

    # Decide which spreadsheet we're serving
    sheet_id = ""
    items = list_folder()
    for item in items:
        if name.lower() == item["name"].lower():
            sheet_id = item["id"]
    if not sheet_id:
        abort(404, f'Dataset {name} not found.')

    # Call the Sheets API
    try:
        service = build('sheets', 'v4', developerKey=sheets_api_key)
        sheets = service.spreadsheets()
        # Get the first worksheet name to use as the cell range
        metadata = sheets.get(spreadsheetId=sheet_id).execute()
        worksheets = metadata.get('sheets', '')
        worksheet = worksheets[0].get("properties", {}).get("title", "Sheet1")
        # Now retrieve the data
        print(f'Querying sheet {sheet_id} for cell data in {worksheet}')
        result = sheets.values().get(spreadsheetId=sheet_id, range=worksheet).execute()
        values = result.get('values', [])
    except HttpError as e:
        abort(500, e)

    # Process the return
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

def list_folder(refresh=False):
    global file_list

    if file_list and not refresh:
        return file_list

    service = build('drive', 'v3', developerKey=sheets_api_key)

    # Call the Drive v3 API
    results = service.files().list(q=f"'{folder_id}' in parents",
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    result = []
    print('Files:')
    for item in items:
        result.append({
            'name': item['name'],
            'id': item['id'],
        })
    file_list = result
    return file_list


if __name__ == '__main__':
    app.run(host='0.0.0.0')