# _*_ coding: utf-8 _*_
# @时间    : 2018/1/16 13:49
# @作者  : 梁佳霖
# @文件名    : models.py

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, ModelMixin):
    __tablename__ = 'account_users'

    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('account_roles.id'))
    username = db.Column(db.String(50), unique=True, nullable=False)
    nickname = db.Column(db.String(50))
    password_hash = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    mobile = db.Column(db.Integer)
    is_supper = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    access_token = db.Column(db.String(32))
    token_expired = db.Column(db.Integer)

    role = db.relationship('Role')
    proj_ids = db.Column(db.String(512), default='')    # 负责项目

    @property
    def password(self):
        raise AttributeError('password only can write')

    @password.setter
    def password(self, plain):
        self.password_hash = generate_password_hash(plain)

    @property
    def permissions(self):
        if self.is_supper:
            return set()
        return Role.get_permissions(self.role_id)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_deploy_permission(self, env_id, app_id):
        if self.is_supper:
            return True
        env_ids = self.role.env_ids.split(',') if self.role.env_ids else []
        app_ids = self.role.app_ids.split(',') if self.role.app_ids else []
        return str(env_id) in env_ids and str(app_id) in app_ids

    def __repr__(self):
        return '<User %r>' % self.username
