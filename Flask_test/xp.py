import os

from flask import Flask, render_template, request, send_from_directory

from final_code import conversion

UPLOAD_FOLDER = '/home/anish/Documents/data_test'

ALLOWED_EXTENSION = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = ALLOWED_EXTENSION

def allowed_file(filename):
   return '.' in filename and \
      filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
   if request.method == 'POST':
      if 'file' not in request.files:
         return render_template('upload.html', msg='No file selected')
         
      file = request.files['file']

      if file.filename == '':
         return render_template('upload.html', msg='No file selected')

      if file and allowed_file(file.filename):
         extracted_text = conversion(file)
         return render_template('result.html',
                                 msg='Successfully processed',
                                 extracted_text=extracted_text,
                                 img_src=UPLOAD_FOLDER + file.filename)

   elif request.method == 'GET':
      return render_template('upload.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8000', debug=True)