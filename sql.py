import mysql.connector as connector

con = connector.connect(host='localhost',
                        user='root',
                        password='',
                        database='chatbot')
cursor = con.cursor()

def add_keyword(userid,word):
    Qstr = "delete from keywords where user_id={}".format(userid)
    cursor.execute(Qstr)
    con.commit()
    Qstr = "insert into keywords values({},\"{}\")".format(userid,word)
    cursor.execute(Qstr)
    con.commit()
    return word

def get_userid(username,password):
    Qstr = "select user_id from userdata where username = \"{}\" and passkey = \"{}\"".format(username,password)
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    for row in rows:
        return row[0]

def check_login(username, password):
    Qstr = "SELECT username,passkey from userdata where username=\"" + str(username) + "\"" "and passkey=\"" + str(password) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    if len(rows)==0:
        return False
    for row in rows:
        if (username==row[0] and password==row[1]):
            return True
    return False

def add_signup(username,password):
    Qstr = "SELECT username from userdata where username=\"" + str(username) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    if len(rows)!=0:
        return False
    else:
        Qstr = "insert into userdata(username,passkey) values(\"{}\",\"{}\")".format(username,password)
        cursor.execute(Qstr)
        con.commit()
        return True

def get_keyword(userid):
    Qstr = "select keyword from keywords where user_id = {}".format(userid)
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    for row in rows:
        return str(row[0]).lower()
    return "null"
