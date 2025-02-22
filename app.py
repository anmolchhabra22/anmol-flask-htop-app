from flask import Flask
import getpass
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    try:
        # Get system username
        username = getpass.getuser()

        # Get server time in IST
        ist_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        # Get top output safely
        top_output = subprocess.getoutput("top -b -n 1")

        # Format the response
        response = f"""
        <h1>Name: Anmol Chhabra</h1>
        <h2>Username: {"anmolchhabra"}</h2>
        <h2>Server Time (IST): {ist_time}</h2>
        <pre>{top_output}</pre>
        """
        return response

    except Exception as e:
        return f"<h1>Error</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
