import os
import pickle
import subprocess

# --- Vulnerable Functions (some called, some not) ---

def dangerous_eval(user_input):
    eval(user_input)  # Not safe
    print("Executed eval")

def insecure_deserialization(data):
    obj = pickle.loads(data)  # Insecure deserialization
    print("Deserialized object:", obj)

def command_injection(user_cmd):
    os.system("ping " + user_cmd)  # Command injection risk

def unsafe_subprocess(user_input):
    subprocess.call(user_input, shell=True)  # Dangerous usage of shell=True

# --- Dead Code Vulnerabilities (not called anywhere) ---

def unused_dangerous_eval():
    eval("__import__('os').system('ls')")

def unused_pickle_loads():
    data = b"cos\nsystem\n(S'ls'\ntR."
    pickle.loads(data)

def unused_subprocess_shell():
    subprocess.Popen("ls -la", shell=True)

# --- Safe Functions ---

def greet(name):
    print(f"Hello, {name}!")

def main():
    greet("Alice")
    # Call some vulnerable functions
    user_input = "1+2"
    dangerous_eval(user_input)

    serialized = pickle.dumps({'key': 'value'})
    insecure_deserialization(serialized)

    cmd = "localhost"
    command_injection(cmd)

if __name__ == "__main__":
    main()
