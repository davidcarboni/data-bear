export SHEETS_API_KEY=$(cat credentials/sheets-api-key.txt)
export FOLDER_ID=1lTMzmb-N4F3nznDY5eV003O8NomPTYBg

name=data-bear
docker build --tag $name . && 
docker run --rm -p 5000:5000 \
  -e SHEETS_API_KEY \
  -e FOLDER_ID \
  $name
