from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, PasswordField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo


class CfgNotifyForm(FlaskForm):
    check_order = StringField('排序', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_type = SelectField('通知类型', choices=[('MAIL', '邮件通知'), ('SMS', '短信通知')],
                              validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_name = StringField('通知人姓名', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_number = StringField('通知号码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    status = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')

class resourceForm(FlaskForm):
    check_order = StringField('排序', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_type = SelectField('通知类型', choices=[('MAIL', '邮件通知'), ('SMS', '短信通知')],
                              validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_name = StringField('通知人姓名', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    notify_number = StringField('通知号码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    status = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')

class wanggeForm(FlaskForm):
    quyu = StringField('区域', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    xiangzhen = StringField('乡镇街道', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    shequ = StringField('社区', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    xingzhengcun = StringField('行政村', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    zuizhongzuzhi = StringField('最终组织', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    wanggejingli = StringField('网格经理', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    dashichangwangge = StringField('对应大市场网格', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    dashichangwangge_bianhao = IntegerField('对应大市场网格编号')
    status = BooleanField('生效标识', default=True)
    submit = SubmitField('提交')
