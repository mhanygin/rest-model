=====
REST models
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'rest-models',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^rest/', include('rest.urls')),

3. Visit http://127.0.0.1:8000/rest/<model> or http://127.0.0.1:8000/rest/<model>/<id>