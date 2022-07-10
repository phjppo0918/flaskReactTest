import pymysql

RDS_HOST = 'qwer'
RDS_DATABASE = 'blossom'
RDS_USER = 'asdf'
RDS_PASSWORD = 'zxcv'


def getConnection():
    return pymysql.connect(
        host=RDS_HOST,
        user=RDS_USER,
        db=RDS_DATABASE,
        password=RDS_PASSWORD,
        charset='utf8')
