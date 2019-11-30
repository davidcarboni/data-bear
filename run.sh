export SHEETS_API_KEY=$(cat credentials/sheets-api-key.txt)

name=sheets-api
docker build --tag $name . && \
docker run -it --rm -p 5000:5000 -e SHEETS_API_KEY $name
