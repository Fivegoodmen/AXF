# import flask_restful

from flask_restful import Resource, marshal_with, fields  # Resource父类，封装了区分请求方式并且分配到不同函数名的方法

from app.models import user


class Cat(Resource):                   #创建一个接口类，必须要继承Resource父类，定义不同请求方式的方法
    def get(self):                     #get方式请求执行方法 -->意味着数据库查询
        return {"message":"get"}

    def put(self):                     #put式请求执行方法 -->意味着数据库更新
        return {"massage":'put'}

    def post(self):                     #post式请求执行方法 -->意味着数据库增加
        return {"massage":'post'}

    def delete(self):                     #delete式请求执行方法 -->意味着数据库删除
        return {"massage":'delete'}

class Dog(Resource):
    def get(self):
        return 'get'

    def put(self):
        return 'post'
#格式化 每一个对象中的属性，也就是字段名
# ----》》》只有格式化里面的键值对才能在return中返回《《《------
username = {
    "id":fields.Integer,
    "name":fields.String,
}

#格式化  一个对象，将一个对象一个字典的形式返回
users={
    'message':fields.String,
    "data": fields.Nested(username)
}
#格式化  一个列表，将一个列表一个字典的形式返回
userlist={
    'message':fields.String,
    'data':fields.List(fields.Nested(username))
}
class first(Resource):
    @marshal_with(userlist)                 #数据格式化，需要按照users的格式来,将对象转化为字典的格式
    def get(self):
        # username = user.query.first()
        users = user.query.all()
        # for user in users:
        data={
            'message':'完成',
            'data':users,
        }
        return data