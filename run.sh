export API_KEY=$(cat credentials/sheets-api-key.txt)
export SHEET_ID=1cCUTcpmcxyKndVHCDvnl6IwBE7zXP1Lhq1kct-aytB0
export CELL_RANGE=Sheet1!a:e

name=data-bear
docker build --tag $name . && 
docker run --rm -p 5000:5000 \
  -e API_KEY \
  -e SHEET_ID \
  -e CELL_RANGE \
  $name
