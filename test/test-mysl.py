import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='password',
                             db='mysql',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
