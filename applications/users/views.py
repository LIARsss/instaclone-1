import flask

from flask.views import MethodView

from exceptions import LoginException

import forms


class UserRegistrationView(MethodView, FormViewMixin):
    form_class = forms.RegistrationForm
    template_name = 'registration.html'

    def post(self):
        form = self.get_form()

        if form.validate_on_submit():
            form.save()

        return flask.render_template(
            template_name_or_list=self.get_template_name(),
            form=form,
        )


class UserLoginView(MethodView, FormViewMixin):
    form_class = forms.LoginForm
    template_name = 'login.html'

    def post(self):
        form = self.get_form()

        if form.validate_on_submit():
            try:
                form.login()

            except LoginException as exception:
                flask.flash(message=str(exception))

        return flask.render_template(
            template_name_or_list=self.get_template_name(),
            form=form,
        )


class UserProfileView(MethodView):
    def get(self, user_id):
        user = User.query.get(user_id)

        if user is None:
            return 'User not found!', 404

        return flask.render_template(
            template_name_or_list='profile_photos.html',
            photos=user.photos,
        )