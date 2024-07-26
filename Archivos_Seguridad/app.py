from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Descargar Archivo</h1>
    <p>Haga clic <a href="/download">aquí</a> para descargar el archivo.</p>
    '''

@app.route('/download')
def download_file():
    return send_from_directory('files', 'antivirus.exe')
    
UPLOAD_FOLDER = 'uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return jsonify({"message": "File uploaded successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.53')
