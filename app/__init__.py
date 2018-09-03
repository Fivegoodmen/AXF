from flask import Flask

from app import settings
from app.ext import init_app
from app.urls import init_api


def create_app(envname):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(envname))#必须要把配置放在初始化上面{{每次都忘记}}}
    init_app(app)
    init_api(app)
    return app