from jinja2 import Environment, PackageLoader, select_autoescape
from sanic.response import html


class Template(object):
    def __init__(self, current_user):
        self.current_user = current_user

    def get_env(self):
        env = Environment(
            loader=PackageLoader('app.view.user_blueprint', '../templates'),
            autoescape=select_autoescape(['html', 'xml', 'tpl']))

        env.globals["current_user"] = self.current_user
        return env

    def template(self, tpl, **kwargs):
        template = self.get_env().get_template(tpl)
        return html(template.render(kwargs))
