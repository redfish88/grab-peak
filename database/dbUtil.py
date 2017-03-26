# coding:utf-8
import sqlite3
import logging
import os
db_file = os.path.join(os.path.dirname(__file__), 'article.db')

conn = sqlite3.connect(db_file)

def execute_sql(sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
    except  Exception,e:
        logging.error(e.message)
    finally:
        conn.commit()
        conn.close()
def select_sql(sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        return values
        cursor.close()
    except  Exception,e:
        logging.error('exec sql error,sql : ',e.message)
    finally:
        conn.commit()
        conn.close()

if __name__ == '__main__':
    create_table_sql = 'create table blog_user(id INTEGER PRIMARY KEY autoincrement,name VARCHAR (100),description TEXT)'
    create_tag_sql = 'create table article_category('
    insert_sql = 'insert into blog_user(name,description) values(\'阮一峰的博客\',\'测试\')'
    selectsql = 'select * from blog_user'
    #print execute_sql(insert_sql)
    print select_sql(selectsql)
