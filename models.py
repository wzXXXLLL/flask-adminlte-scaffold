# -*- coding: utf-8 -*-

from peewee import MySQLDatabase, Model, CharField, BooleanField, IntegerField, BigIntegerField
import json
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login_manager
from conf.config import config
import os

cfg = config[os.getenv('FLASK_CONFIG') or 'default']

db = MySQLDatabase(host=cfg.DB_HOST, user=cfg.DB_USER, passwd=cfg.DB_PASSWD, database=cfg.DB_DATABASE)


class BaseModel(Model):
    class Meta:
        database = db

    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        # return str(r)
        return json.dumps(r, ensure_ascii=False)


# 管理员工号
class User(UserMixin, BaseModel):
    username = CharField()  # 用户名
    password = CharField()  # 密码
    fullname = CharField()  # 真实性名
    email = CharField()  # 邮箱
    phone = CharField()  # 电话
    status = BooleanField(default=True)  # 生效失效标识

    def verify_password(self, raw_password):
        return check_password_hash(self.password, raw_password)


# 通知人配置
class CfgNotify(BaseModel):
    check_order = IntegerField()  # 排序
    notify_type = CharField()  # 通知类型：MAIL/SMS
    notify_name = CharField()  # 通知人姓名
    notify_number = CharField()  # 通知号码
    status = BooleanField(default=True)  # 生效失效标识


# 网格配置
class wangge_point(BaseModel):
    # 日期 = CharField()
    riqi = CharField()
    # 县市 = CharField()
    xianshi = CharField()
    # 县市编号
    xianshi_bianhao = BigIntegerField()
    # 区域
    quyu = CharField()
    # 区域编号
    quyu_bianhao = BigIntegerField()
    # 乡镇街道
    xiangzhen = CharField()
    # 乡镇街道编号
    xiangzhen_biahao = BigIntegerField()
    # 社区
    shequ = CharField()
    # 社区编号
    shequ_bianhao = BigIntegerField()
    # 行政村
    xingzhengcun = CharField()
    # 行政村编号
    xingzhengcun_bianhao = BigIntegerField()
    # 最终组织编号
    zuizhongzuzhi_bianhao = BigIntegerField()
    # 最终组织
    zuizhongzuzhi = CharField()
    # 县市
    # xianshi = CharField()
    # 网格经理账号
    wanggejingli_zhanghao = CharField()
    # 网格经理
    wanggejingli = CharField()
    # 对应大市场网格编号
    dashichangwangge_bianhao = BigIntegerField()
    # 对应大市场网格名称
    dashichangwangge_mingcheng = CharField()

    status = BooleanField(default=True)  # 生效失效标识

# 资源点配置
class resource_point(BaseModel):
    # 日期 = CharField()
    riqi = CharField()
    # 县市 = CharField()
    xianshi = CharField()
    # 县市编号
    xianshi_bianhao = BigIntegerField()
    # 区域
    quyu = CharField()
    # 区域编号
    quyu_bianhao = BigIntegerField()
    # 乡镇街道
    xiangzhen = CharField()
    # 乡镇街道编号
    xiangzhen_biahao = BigIntegerField()
    # 社区
    shequ = CharField()
    # 社区编号
    shequ_bianhao = BigIntegerField()
    # 行政村
    xingzhengcun = CharField()
    # 行政村编号
    xingzhengcun_bianhao = BigIntegerField()
    # 最终组织编号
    zuizhongzuzhi_bianhao = BigIntegerField()
    # 最终组织
    zuizhongzuzhi = CharField()
    # 县市
    # xianshi = CharField()
    # 网格经理账号
    wanggejingli_zhanghao = CharField()
    # 网格经理
    wanggejingli = CharField()
    # 对应大市场网格编号
    dashichangwangge_bianhao = BigIntegerField()
    # 对应大市场网格名称
    dashichangwangge_mingcheng = CharField()

    status = BooleanField(default=True)  # 生效失效标识

@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))


# 建表
def create_table():
    db.connect()
    db.create_tables([wangge_point, resource_point, CfgNotify, User])


if __name__ == '__main__':
    create_table()
