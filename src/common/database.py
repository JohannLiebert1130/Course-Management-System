import pymysql


class Database:
    DATABASE = None

    @staticmethod
    def initialize():
        Database.DATABASE = pymysql.connect("localhost", "root", "690527", "course_management_sys",
                                            use_unicode=True, charset="utf8")

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
            print('committed successfully!')
        except pymysql.Error as error:
            # 如果发生错误则回滚
            Database.DATABASE.rollback()
            raise error

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
        except pymysql.Error as error:
            print("Error: unable to fetch data")
            raise error

    @staticmethod
    def close():
        Database.DATABASE.close()

