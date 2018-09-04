# import flask_restful
from flask import jsonify, session
from flask_restful import Resource

from app.models import UserModel, CartModel


class axf(Resource):
    def get(self):
        return '11'



class cart(Resource):
    def get(self):
        # 先判断用户是否登录，如果登录则可进入购物车页面，如果没有登录接则跳转到我的页面
        # userid = session.get("user_id")
        userid=1
        user = UserModel.query.filter(UserModel.id == userid).first()
        data={
            'code':'200'
        }
        if not user:
            data['code']='400'
            return data
        # 获取到该用户所有的购买商品信息-------->集合
        GoodCarts = CartModel.query.filter(CartModel.c_user==user)
        # 获取数据库中的数据，并且计算购物车中被选中的商品的数量和商品的总价
        counts = 0
        AllPrice = 0
        for GoodCart in GoodCarts:
            if GoodCart.c_isselect:
                counts += GoodCart.c_num
                AllPrice += GoodCart.c_num * GoodCart.c_goods.price

        # 在页面加载的时候，需要获取全选的状态
        noselect = []
        for GoodCart in GoodCarts:
            if not GoodCart.c_isselect:
                noselect.append(GoodCart.c_isselect)
        if len(noselect):
            isallselect = False
        else:
            isallselect = True

        # 将商品数据转化为字典格式
        user_dic=user.user_dict
        GoodCarts = []
        for Good in GoodCarts:
            GoodCart = Good.Cart_dict()
            GoodCarts.append(GoodCart)

        data["user"] = user_dic
        data["GoodCarts"]= GoodCarts
        data["counts"]= counts
        data["AllPrice"]= AllPrice
        data["is_allselect"]= isallselect
        return jsonify(data)

