from main import create_app
from main.config import Config

app = create_app()
app_port = Config.APP_PORT
app_host = Config.APP_HOST

if __name__=="__main__":
  app.run(port=app_port, host=app_host, debug=True)