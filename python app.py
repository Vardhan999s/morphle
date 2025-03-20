from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get full name (you can hardcode or use an env variable)
    full_name = "Your Full Name"

    # Get system username
    system_username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Run `top` command and get output
    top_output = subprocess.getoutput("top -b -n 1")

    # Generate HTML output
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
