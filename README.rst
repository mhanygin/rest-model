=====
RESTFull for models
=====

RESTFull interface for Django models/

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "rest" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'rest',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^rest/', include('rest.urls')),

3. Operations:
 - POST http://127.0.0.1:8000/rest/<model> -- create new model instance
 - GET http://127.0.0.1:8000/rest/<model>/<id>  -- get model instance with id
 - GET http://127.0.0.1:8000/rest/<model>?param1=value1&param2=value2 -- get models instance with conditions
 - PUT http://127.0.0.1:8000/rest/<model>/<id>?param1=value1&param2=value2 -- change model instance with id
 - DELETE http://127.0.0.1:8000/rest/<model>/<id>  -- delete model instance with id