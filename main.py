from flask import Flask, request
import pandas as pd

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        excel_data = pd.read_excel(file)
        json_data = excel_data.to_json()
        return json_data

    return 'Error occurred while reading the file'


if __name__ == '__main__':
    app.run(debug=True)