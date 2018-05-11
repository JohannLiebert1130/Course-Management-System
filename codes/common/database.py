import pymysql

from common.utils import Utils


class Database:
    DATABASE = None

    @staticmethod
    def initialize():
        Database.DATABASE = pymysql.connect("localhost", "root", "690527", "course_management_sys")

    @staticmethod
    def data_handle(sql, *arg):
        """
        支持对数据库的增删改操作
        :param sql: the mysql code you written to update/delete/update data.
        """

        # 使用cursor()方法获取操作游标
        cursor = Database.DATABASE.cursor()

        try:
            # 执行sql语句
            cursor.execute(sql, arg)
            # 提交到数据库执行
            Database.DATABASE.commit()
        except pymysql.Error as e:
            # 如果发生错误则回滚
            Database.DATABASE.rollback()
            print(e)

        # 关闭数据库连接
        Database.DATABASE.close()

    @staticmethod
    def query(sql, *arg):
        # 使用cursor()方法获取操作游标
        cursor = Database.DATABASE.cursor()

        try:
            # 执行sql语句
            cursor.execute(sql, arg)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except pymysql.Error as e:
            print("Error: unable to fetch data")
            print(e)

        # 关闭数据库连接
        Database.DATABASE.close()


if __name__ == '__main__':
    password = 'test_pw'
    user_id = 'test_id'
    hashed_password = Utils.hash_password(password, user_id)
    print(hashed_password)
    sql = """
    INSERT INTO accounts(id, user_id, password)
    VALUES (1, %s, %s)
    """

    Database.initialize()
    Database.data_handle(sql, user_id, hashed_password)

