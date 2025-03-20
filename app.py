from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():

    full_name = "Dio Brando"


    system_username = os.getenv("USER") or os.getenv("USERNAME")

 
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: {full_name}
    User: {system_username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
