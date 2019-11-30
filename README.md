# Data Bear

Lets you serve a public Google Sheet as a json api.

## Usage

You'll need to pass two parameters, a sheet ID and a cell range. The url will be of the format:

    https://data-bear.herokuapp.com/?sheet=<sheet ID>&range=<cell range>

### Sheet ID

You'll need the sheet ID, which you can get from the url or sharing link of your sheet.

If the url of your sheet looks something like this:

    https://docs.google.com/spreadsheets/d/1cCUTcpmcxyKndVHCDvnl6IwBE7zXP1Lhq1kct-aytB0/edit#gid=0

Your sheet ID is the segment after `https://docs.google.com/spreadsheets/d/`:

    1cCUTcpmcxyKndVHCDvnl6IwBE7zXP1Lhq1kct-aytB0

### Cell range

You'll also need the range of cells you'd like to serve. The range is `worksheet name`!`top-left`:`bottom right`, for example, `Sheet1!a1:c3` would serve rows 1-3 from columns a-c from the worksheet named "Sheet1".

## Data format

The first row sholud contain headings. These headings will be used as json keys for the api. The rest of the rows should contain data values.

If your range looks like this:

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

## Example spreadsheet API

Here's a sample sheet:

https://docs.google.com/spreadsheets/d/1cCUTcpmcxyKndVHCDvnl6IwBE7zXP1Lhq1kct-aytB0/edit#gid=0

You can view this data as an api using this link:

https://data-bear.herokuapp.com/?sheet=1cCUTcpmcxyKndVHCDvnl6IwBE7zXP1Lhq1kct-aytB0&range=Sheet1!a1:e4

