IPython 0.12 includes a wonderful Notebook interface.


This (trivial) django app provides the command

    ./manage.py notebook

to launch the IPython notebook as a Django shell.


Installation (on Ubuntu)
-----------------------
Install the dependencies

    sudo aptitude install libzmq1 libzmq-dev
    pip install --upgrade ipython tornado pyzmq

Then clone this repository into your Django project and add it to the INSTALLED_APPS list in your settings file.


Licence
-------
Public domain
