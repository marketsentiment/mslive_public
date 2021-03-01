import os
os.environ['dev'] = '1'
from live_sentiment import dev_server

if __name__ == '__main__':
    dev_server(debug=True) 