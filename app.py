from flask import Flask,request, jsonify
from savetable import TableSaver
import re
from flask_cors import CORS
import pandas as pd

saver = TableSaver(db_path='quasar.db')


def split_string_by_commas(string):
    # Find the index of the first comma
    first_comma_index = string.find(',')

    # Find the index of the last comma
    last_comma_index = string.rfind(',')

    # Find the index of the second to last comma
    second_last_comma_index = string.rfind(',', 0, last_comma_index)

    # Split the string based on the positions of commas
    first_part = string[:first_comma_index]
    second_part = string[first_comma_index + 1:second_last_comma_index]
    third_part = string[second_last_comma_index + 1:last_comma_index]
    last_part = string[last_comma_index + 1:]

    return first_part, second_part, third_part, last_part

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def getData():
    data = []
    with open('summary.txt', 'r') as file:
        lines = file.readlines()

        # Use findall to extract all parts from the line
        for line in lines:
            a,b,c,d = split_string_by_commas(line)
            data.append({"name":a, "column":b, "row":c, "filesize":d.strip()})
        return jsonify(data)

@app.route('/upload', methods=['POST'])
def addTable():
    name = request.form.get('name')
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        try:
            df = pd.read_csv(file)
            file_size_in_bytes = request.content_length
            saver.write_binary_to_db(df, name, file_size_in_bytes)
            return jsonify({'success': True, 'message': 'File uploaded and processed successfully'})
        except Exception as e:
            return f'Error processing file: {str(e)}', 500

if __name__ == '__main__':
    # Specify the port here
    port = 4000
    app.run(debug=True, port=port)