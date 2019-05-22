# import os
from flask import request, redirect, url_for, abort
from famgik import db, create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from famgik.models import FamgikUser, Role
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_security.forms import RegisterForm, StringField, Required
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = create_app()
migrate = Migrate(app, db)


# perm.register_commands(manager)


class FamgikAdminModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated and
                current_user.has_role('superuser')
                )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


admin = Admin(app, name='Famgik', template_mode='bootstrap3')
app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'
admin.add_view(FamgikAdminModelView(FamgikUser, db.session))
admin.add_view(FamgikAdminModelView(Role, db.session))


class ExtendedRegisterForm(RegisterForm):
    first_name = StringField('First Name', [Required()])
    last_name = StringField('Last Name', [Required()])


user_datastore = SQLAlchemyUserDatastore(db, FamgikUser, Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
