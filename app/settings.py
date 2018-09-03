def getdata(datainfo):
    dilict=datainfo.get('dilict')
    driver = datainfo.get('driver')
    user = datainfo.get('user')
    password = datainfo.get('password')
    host = datainfo.get('host')
    port = datainfo.get('port')
    database = datainfo.get('database')
    return '{}+{}://{}:{}@{}:{}/{}'.format(dilict,driver,user,password,host,port,database)


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class developConfig(Config):
    DEBUG = True
    data={
        'dilict':'mysql',
        'driver':'pymysql',
        'user':'root',
        'password':'123456',
        'host':'10.11.68.40',
        'port':'3306',
        'database':'flask_axf',
    }
    SQLALCHEMY_DATABASE_URI=getdata(data)

env={
    'develop':developConfig
}