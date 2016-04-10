Django Odnoklassniki Stats
===========================

[![PyPI version](https://badge.fury.io/py/django-odnoklassniki-stats.png)](http://badge.fury.io/py/django-odnoklassniki-stats) [![Build Status](https://travis-ci.org/ramusus/django-odnoklassniki-stats.png?branch=master)](https://travis-ci.org/ramusus/django-odnoklassniki-stats) [![Coverage Status](https://coveralls.io/repos/ramusus/django-odnoklassniki-stats/badge.png?branch=master)](https://coveralls.io/r/ramusus/django-odnoklassniki-stats)

Приложение позволяет взаимодействовать с группами соц. сети Одноклассники, их статистикой и пользователями групп через OK API используя стандартные модели Django

Установка
---------

    pip install django-odnoklassniki-stats

В `settings.py` необходимо добавить:

    INSTALLED_APPS = (
        ...
        'oauth_tokens',
        'taggit',
        'odnoklassniki_api',
        'odnoklassniki_groups',
        'odnoklassniki_discussions',
        'odnoklassniki_stats',
    )

    # oauth-tokens settings
    OAUTH_TOKENS_HISTORY = True                                             # to keep in DB expired access tokens
    OAUTH_TOKENS_ODNOKLASSNIKI_CLIENT_ID = 12345678                         # application id
    OAUTH_TOKENS_ODNOKLASSNIKI_CLIENT_PUBLIC = ''                           # application public key
    OAUTH_TOKENS_ODNOKLASSNIKI_CLIENT_SECRET = ''                           # application secret key
    OAUTH_TOKENS_ODNOKLASSNIKI_SCOPE = ['']                                 # application scopes
    OAUTH_TOKENS_ODNOKLASSNIKI_USERNAME = ''                                # user login
    OAUTH_TOKENS_ODNOKLASSNIKI_PASSWORD = ''                                # user password

Покрытие методов API
--------------------


Примеры использования
---------------------

