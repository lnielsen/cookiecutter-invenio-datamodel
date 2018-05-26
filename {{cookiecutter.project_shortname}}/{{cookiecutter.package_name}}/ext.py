{% include 'misc/header.py' %}
"""Flask extension for {{ cookiecutter.project_name }}."""

from __future__ import absolute_import, print_function

from . import config


class {{ cookiecutter.extension_class }}(object):
    """{{ cookiecutter.project_name}} extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['{{ cookiecutter.project_shortname}}'] = self

    def init_config(self, app):
        """Initialize configuration.

        This Override configuration variables with the values in this package.
        """
        for k in dir(config):
            if k.startswith('{{ cookiecutter.package_name | upper }}_'):
                app.config.setdefault(k, getattr(config, k))
            elif k == 'RECORDS_REST_ENDPOINTS' \
                    and app.config.get(
                        '{{ cookiecutter.package_name | upper }}_ENDPOINTS_ENABLED', True):
                app.config.setdefault('RECORDS_REST_ENDPOINTS', {})
                app.config['RECORDS_REST_ENDPOINTS'].update(getattr(config, k))
            elif k == 'PIDSTORE_RECID_FIELD':
                app.config['PIDSTORE_RECID_FIELD'] = getattr(config, k)
