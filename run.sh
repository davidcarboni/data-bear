export SHEETS_API_KEY=$(cat credentials/sheets-api-key.txt)
export FOLDER_ID=14a_DPP7dz2tLa3MmTQK7rAKzry8KQwG3

name=data-bear
docker build --tag $name . && 
docker run --rm -p 5000:5000 \
  -e SHEETS_API_KEY \
  -e FOLDER_ID \
  $name
