from flask import request, jsonify
import pymysql

from config.rdsConfig import getConnection

from . import routes


@routes.route('/db', methods=['post'])
def post_db():
    params = request.get_json()
    db = getConnection()
    curs = db.cursor()

    sql = "insert into test (name, password, age) values (%s, %s, %s)"
    curs.execute(sql, (params['name'], params['password'], params['age']))
    db.commit()
    db.close()
    return 'ok'


@routes.route('/db', methods=['get'])
def getAll():
    ret = []
    db = getConnection()
    curs = db.cursor()

    sql = "select * from test"
    curs.execute(sql)
    rows = curs.fetchall()

    for e in rows:
        temp = {'test_id': e[0],
                'name': e[1],
                'password': e[2],
                'age': e[3]}
        ret.append(temp)
    db.commit()
    db.close()
    return jsonify(ret)


@routes.route('/db/<int:id>', methods=['get'])
def getOne(id):
    db = getConnection()
    curs = db.cursor()

    sql = "select * from test where test_id = %s"
    curs.execute(sql, id)
    rows = curs.fetchone()
    db.commit()
    db.close()
    return jsonify(
        test_id=rows[0],
        name=rows[1],
        password=rows[2],
        age=rows[3]
    )
