from app import get_logger, get_config
import math
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import utils
from models import CfgNotify, wangge_point, User
from app.main.forms import CfgNotifyForm, wanggeForm, userForm
from . import main

logger = get_logger(__name__)
cfg = get_config()


# 通用列表查询
def common_list(DynamicModel, view):
    # 接收参数
    action = request.args.get('action')
    id = request.args.get('id')
    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else cfg.ITEMS_PER_PAGE

    # 删除操作
    if action == 'del' and id:
        try:
            DynamicModel.get(DynamicModel.id == id).delete_instance()
            flash('删除成功')
        except:
            flash('删除失败')

    # 查询列表
    query = DynamicModel.select()
    total_count = query.count()

    # 处理分页
    if page: query = query.paginate(page, length)

    dict = {'content': utils.query_to_list(query), 'total_count': total_count,
            'total_page': math.ceil(total_count / length), 'page': page, 'length': length}
    return render_template(view, form=dict, current_user=current_user)


# 通用单模型查询&新增&修改
def common_edit(DynamicModel, form, view):
    id = request.args.get('id', '')
    if id:
        # 查询
        model = DynamicModel.get(DynamicModel.id == id)
        if request.method == 'GET':
            utils.model_to_form(model, form)
        # 修改
        if request.method == 'POST':
            if form.validate_on_submit():
                utils.form_to_model(form, model)
                model.save()
                flash('修改成功')
            else:
                utils.flash_errors(form)
    else:
        # 新增
        if form.validate_on_submit():
            model = DynamicModel()
            utils.form_to_model(form, model)
            model.save()
            flash('保存成功')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form, current_user=current_user)


# 根目录跳转
@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


# 首页
@main.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', current_user=current_user)


# 通知方式查询
@main.route('/notifylist', methods=['GET', 'POST'])
@login_required
def notifylist():
    return common_list(CfgNotify, 'notifylist.html')


# 通知方式配置
@main.route('/notifyedit', methods=['GET', 'POST'])
@login_required
def notifyedit():
    return common_edit(CfgNotify, CfgNotifyForm(), 'notifyedit.html')


# 网格查询
@main.route('/wanggelist', methods=['GET', 'POST'])
@login_required
def wanggelist():
    return common_list(wangge_point, 'wanggelist.html')


# 网格修改
@main.route('/wanggeedit', methods=['GET', 'POST'])
@login_required
def wanggeedit():
    return common_edit(wangge_point, wanggeForm(), 'wanggeedit.html')


# 用户查询
@main.route('/userlist', methods=['GET', 'POST'])
@login_required
def userlist():
    return common_list(User, 'userlist.html')


# 用户修改
@main.route('/useredit', methods=['GET', 'POST'])
@login_required
def useredit():
    return common_edit(User, userForm(), 'useredit.html')