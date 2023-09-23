from flask import Flask, render_template, redirect, request, send_file, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    file_list = list_files()
    
    # Create an HTML table to display the files
    table_html = '<table>'
    table_html += '<tr><th>File Name</th><th>Download</th></tr>'
    
    for file in file_list:
        download_link = f'<a href="/files/{file}">Download</a>'
        table_html += f'<tr><td>{file}</td><td>{download_link}</td></tr>'
    
    table_html += '</table>'

    # Your HTML template
    index_html = f"""
    <body>
    <form method="post" enctype="multipart/form-data" action="/upload" method="post">
      <div style="justify-content: center;
    color: white;
    background: linear-gradient(to bottom, #3498db, #2980b9);
    padding: 5px;
    margin-bottom: 10px;
    border: 1px solid #3498db;
    border-radius: 10px;
    text-align: justify; 
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.25);
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 2px solid #3498db;
    padding: 7px;
    border-radius: 5px;
    cursor: pointer;">
        <label for="file">Select file to upload</label>
        <input type="file" id="file" name="form_file" accept="image/jpeg" />
      </div>
      <div>
        <center><button style="background: linear-gradient(to bottom, #3498db, #2980b9);color: white;cursor: pointer;padding: 5px;
    margin-bottom: 10px;
    border: 1px solid #3498db;
    border-radius: 10px;
    text-align: justify; 
    text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.25);
    display: flex;
    align-items: center;">Submit</button> </center>
      </div>
    </form>
    <br>
    </body>
    <h2 style="display:block;width: 200px; /* Set a specific width */
      background-color: lightblue;
      padding: 10px;
      margin-bottom: 20px;">Uploaded Files</h2>
    {table_html}
    </ul>
    """
    
    return index_html



@app.route("/upload", methods=['POST'])
def upload():
    if 'form_file' in request.files:
        file = request.files['form_file']
        if file.filename != '':
            # Save the uploaded file to the 'files' directory
            file.save(os.path.join("files", os.path.basename(file.filename)))

    return redirect("/")
@app.route('/files/<filename>')
def get_file(filename):

     return send_file('./files/'+filename)

def list_files():
    files = os.listdir("files")
    jpegs = [file for file in files if file.lower().endswith(".jpeg") or file.lower().endswith(".jpg")]
    return jpegs

if  __name__ == "__main__":

   app.run(host='0.0.0.0',port=80)                                                                                                             