import argparse

from docker_flask.api.app import launch

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--port", type=str, default="8081")
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = parser.parse_args()
    port = args.port
    host = args.host
    launch(port=port, host=host)
