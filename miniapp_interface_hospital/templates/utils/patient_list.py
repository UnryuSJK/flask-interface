import pymysql


def mysql_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='sjk020527',
                           db='hospital', charset="utf8")
    cusor = conn.cursor()
    return conn, cusor


def mysql_close(conn, cursor):
    cursor.close()
    conn.close()


def query_patient(patient_info: dict):
    print(patient_info['openid'])
    sql = f"SELECT * FROM patient_tab WHERE openid='{patient_info['openid']}'"
    conn, cursor = mysql_conn()
    cursor.execute(sql)
    res = cursor.fetchall()
    mysql_close(conn, cursor)
    if res != ():
        return {
            'openid': res[0][0],
            'name': res[0][1],
            'img': res[0][2]
        }
    else:
        return None


def add_patient(patient_info: dict):
    if query_patient(patient_info) != None:
        return 'existed'
    else:
        sql = f"INSERT INTO patient_tab VALUES('{patient_info['openid']}','{patient_info['name']}','{patient_info['img']}')"
        conn, cursor = mysql_conn()
        cursor.execute(sql)
        conn.commit()
        mysql_close(conn, cursor)
        return {
            "cmd": "registered",
            "info": patient_info
        }


if __name__ == '__main__':
    print(query_patient(
        {'openid': '55', 'name': '按了队常', 'img': 'http://dummyimage.com/400x400'}
    ))
