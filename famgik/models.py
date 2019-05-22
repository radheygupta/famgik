from famgik import db
# from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('famgik_user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return self.name


class FamgikUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, unique=False, default=True)
    admin = db.Column(db.Boolean, unique=False, default=False)
    staff = db.Column(db.Boolean, unique=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('famgik_users', lazy='dynamic'))

    def __repr__(self):
        return self.email


