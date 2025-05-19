import sqlite3
import xml.etree.ElementTree as ET
import pickle
import os
from flask import Flask, request, make_response

app = Flask(__name__)

# Dead Code 1: Unreachable code
def dead_code_unreachable():
    return
    print("This code is never executed")

# Dead Code 2: Unused function
def dead_code_unused():
    a = 10
    b = 20
    return a + b

# Dead Code 3: Unused variable
unused_variable = "I am not used anywhere"

# Dead Code 4: Conditional block that never runs
if False:
    print("This will never run")

# Dead Code 5: Deprecated or insecure usage
def dead_code_pickle_example():
    pickled_data = pickle.dumps({"a": 1})
    # Function never called
    return pickle.loads(pickled_data)

def sql_injection(user_input):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def broken_auth(username, password):
    return username == "adminuser" and password == "xchzdhkrltu"

def store_sensitive_data():
    with open("passwords.txt", "w") as f:
        f.write("admin:Passwo#d@&1957")

def parse_xml(xml_data):
    tree = ET.ElementTree(ET.fromstring(xml_data))
    return tree

@app.route('/access_control', methods=['GET'])
def access_control():
    role = request.args.get('role')
    if role == "admin":
        return "Welcome Admin!"
    return "Access Denied!"

@app.route('/security_misconfig', methods=['GET'])
def security_misconfig():
    response = make_response("Security Misconfiguration Example")
    response.headers['X-Powered-By'] = "Python-Flask"
    return response

@app.route('/xss', methods=['GET'])
def xss_vulnerability():
    user_input = request.args.get('input')
    return f"<html><body>{user_input}</body></html>"

def insecure_deserialization(serialized_data):
    return pickle.loads(serialized_data)

# Dead Code 6: Dead import
import math  # not used

# Dead Code 7: Unused constant
UNUSED_CONSTANT = 42

if __name__ == "__main__":
    app.run(debug=True)
