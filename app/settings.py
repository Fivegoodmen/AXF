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
        'host':'localhost',
        'port':'3306',
        'database':'flask_day04',
    }
    SQLALCHEMY_DATABASE_URI=getdata(data)

env={
    'develop':developConfig
}