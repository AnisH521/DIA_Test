from flask import Flask, render_template, request
from final_code2 import conversion

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_page():
   if request.method == 'POST':
      file = request.files['file']

      if file.filename == '':
         return render_template('result.html', msg='\nPlease Select a File!')

      else:
         text = conversion(file)
         return render_template('result.html',
                                 msg='\nImage is Successfully processed',
                                 converted_text=text)

   elif request.method == 'GET':
      return render_template('result.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8000', debug=True)