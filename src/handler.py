import os
import sys

cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, f'{cur_path}/..')

from api.application import get_app

app = get_app()

if __name__ == '__main__':
    app.run()
