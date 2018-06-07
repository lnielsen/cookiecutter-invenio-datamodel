{% include 'misc/header.rst' %}

{{ '=' * (cookiecutter.project_name|length + 2) }}
 {{ cookiecutter.project_name }}
{{ '=' * (cookiecutter.project_name|length + 2) }}

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_repo }}.svg
        :target: https://github.com/{{ cookiecutter.github_repo }}/blob/master/LICENSE

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_repo }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_repo }}

.. image:: https://img.shields.io/coveralls/{{ cookiecutter.github_repo }}.svg
        :target: https://coveralls.io/r/{{ cookiecutter.github_repo }}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_shortname }}.svg
        :target: https://pypi.org/pypi/{{ cookiecutter.project_shortname }}

{{ cookiecutter.description }}

Further documentation is available on
https://{{ cookiecutter.project_shortname }}.readthedocs.io/

