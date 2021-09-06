from src.app import start_app
from config import configuration

config = configuration['dev']
app = start_app(config)

if __name__ == '__main__':
    app.run()
