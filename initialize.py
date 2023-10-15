import psutil
import webbrowser
import socket
import sys


def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("localhost", 0))
        return sock.getsockname()[1]


react_port = find_available_port()
node_port = find_available_port()
flask_port = find_available_port()


if not (react_port and node_port and flask_port):
    print("No available ports.")
    sys.exit()


def find_process_by_port(port):
    for process in psutil.net_connections(kind="inet"):
        if process.laddr.port == port:
            return process.pid
    return None


def kill_process_by_port(port):
    pid = find_process_by_port(port)
    if pid:
        try:
            process = psutil.Process(pid)
            process.terminate()  # You can use process.kill() for a forceful termination
            print(f"Process with PID {pid} on port {port} terminated.")
        except psutil.NoSuchProcess:
            print(f"No such process with PID {pid}.")
    else:
        print(f"No process found on port {port}.")


# Specify the port you want to search for and kill processes on
# react_port = 3000  # Change this to the desired port
# node_port = 5000
# flask_port = 6789
# Find and kill the process on the specified port
kill_process_by_port(react_port)
kill_process_by_port(node_port)
kill_process_by_port(flask_port)
import subprocess

REACT_APP_DIR = "./news-feed-extractor-frontend"
NODE_APP_DIR = "./news-feed-extractor-backend"
FLASK_APP_DIR = "./news-feed-extractor"
# Run a simple shell command
# result = subprocess.run(
#     f"cd {NODE_APP_DIR} ; start node server.js ",
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True,
# )

react_server = subprocess.Popen(
    f"cd {REACT_APP_DIR} && set REACT_APP_NEWS_EXTRACTOR_NODE_PORT={node_port}&& set PORT={react_port}&&set REACT_APP_NEWS_EXTRACTOR_FLASK_PORT={flask_port}&& npm start",
    shell=True,
    # stdout=subprocess.PIPE,
    # stderr=subprocess.PIPE,
    text=True,
)

node_server = subprocess.Popen(
    f"cd {NODE_APP_DIR} && npm start {node_port}",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

flask_server = subprocess.Popen(
    f'cd {FLASK_APP_DIR} && "env/Scripts/activate" && set NEWS_EXTRACTOR_REACT_PORT={react_port} && set NEWS_EXTRACTOR_NODE_PORT={node_port} && flask run --port={flask_port}',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

print("react_port", react_port, "node_port", node_port, "flask_port", flask_port)
# if node_server.poll() is None:
#     print("Process is still running.")
# node_server.kill()

react_url = f"http://localhost:{flask_port}"
# time.sleep(4)
webbrowser.open(react_url)
# print(node_server)
# print(react_server)
node_server.wait()
react_server.wait()
