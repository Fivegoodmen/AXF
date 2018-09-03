
from flask_restful import Api

from app.apis import Cat, first

api =Api()                           #创建了一个新的接口对象

api.add_resource(Cat,'/cat/')  #添加接口的匹配方式，匹配到哪个接口就执行哪个类中的方法

api.add_resource(first,'/first/')
def init_api(app):
    api.init_app(app=app)