# Data Bear

Lets you serve a public Google folder of Sheets as a json api.

## Usage

You'll need to pass an environment variable for the ID of the folder you'd like to serve, e.g.:

    FOLDER_ID=14a_DPP7dz2tLa3MmTQK7rAKzry8KQwG3

You'll also need to set a variable for a Google API key that has permission to access both Drive and Sheets, e.g.:

    API_KEY=abcdefghijklmnopqrstuvwxyz1234567890000

You can see a working example here:

    https://data-bear-folder.herokuapp.com/

### Folder ID

You'll need the folder ID, which you can get from the url or sharing link of your folder.

If the url of your folder looks something like this:

    https://drive.google.com/drive/folders/14a_DPP7dz2tLa3MmTQK7rAKzry8KQwG3

Your folder ID is the last part of the url:

    14a_DPP7dz2tLa3MmTQK7rAKzry8KQwG3

### Data range

When a spreadsheet is accessed, the API will query for all cells in the first worksheet.

## Data format

The first row is assumed to contain headings. These headings will be used as json keys for the api. The rest of the rows are assumed to contain data values that will be mapped to the keys.

If your worksheet looks like this:

| key 1 | key 2 | key 3 |
|-------|-------|-------|
| a     | b     | c     |
| x     | y     | z     |
| 4     | 5     | 6     |

The json served by the api will look something like this:

    [
        {
            "key 1": "a",
            "key 2": "b",
            "key 3": "c"
        },
        {
            "key 1": "x",
            "key 2": "y",
            "key 3": "z"
        },
        {
            "key 1": "4",
            "key 2": "5",
            "key 3": "6"
        }
    ]

## Example API

Here's a sample folder:

https://drive.google.com/drive/folders/14a_DPP7dz2tLa3MmTQK7rAKzry8KQwG3

You can view the data as an api using this link:

https://data-bear-folder.herokuapp.com/

## Try it yourself

Here's how to try it out for yourself:

* Create a folder in Google Drive
* Set sharing to "anyone with the link" (you may need to use advanced options)
* Get the folder ID from the url
* Pass your api key and folder ID as environment variables (e.g. edit the `run.sh` script)
* Create a couple of spreadsheets in the folder and see them as data served by the api
