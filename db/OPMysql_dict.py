import pymysql
from DBUtils.PooledDB import PooledDB

class OPMysql_dict(object):

    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.coon = OPMysql_dict.getmysqlconn()
        #该参数决定输出的结果集的集合形式是元组还是字典
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
        #self.cur = self.coon.cursor()

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        mysqlInfo = {
            "host": '192.168.134.201',
            "user": 'root',
            "passwd": 'hadoop',
            "db": 'python',
            "port": 3306,
            "charset": 'utf8'
        }

        if OPMysql_dict.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, \
                              host=mysqlInfo['host'], \
                              user=mysqlInfo['user'], \
                              passwd=mysqlInfo['passwd'], \
                              db=mysqlInfo['db'], \
                              port=mysqlInfo['port'], \
                              charset=mysqlInfo['charset'])
            print(__pool)
        return __pool.connection()

    # 插入\更新\删除sql
    def op_insert(self, sql):
        print('op_insert', sql)
        insert_num = self.cur.execute(sql)
        print('mysql sucess ', insert_num)
        self.coon.commit()
        return insert_num

    # 查询
    def op_select(self, sql):
        print('op_select', sql)
        self.cur.execute(sql)  # 执行sql
        select_res = self.cur.fetchall()  # 返回结果为字典
        select_desc=self.cur.description
        print('op_select', select_res)
        return select_res,select_desc

    #释放资源
    def dispose(self):
        self.coon.close()
        self.cur.close()
