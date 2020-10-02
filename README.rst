==================
``pizza24ave`` (Official website repository of 24 AvePizza)
==================

This is the official repository of 24 Ave Pizza QR Code Generator made in Python3.8.


Installation
============


* Install from git::

    git clone https://github.com/24avepizza/qrgen.git

* ``Or directly download the zipfile.``


* Then use ``pip`` to install dependencies::

    pip install -r requirements.txt


* Then Run ``main.py  file or the main.exe file in the.zip folder``::

    python main.py


Quickstart for producion environment (``PythonAnywhere``)
==========
* Create ``database``

* Then run ``bash`` and type the follwing command::

    cd pizza24ave
 
 
* Run ``pip3.8`` to install the dependencies::

    pip3.8 install --user -r requirements.txt


* Run ``pip3.8`` to install the correct ``bcrypt`` version according to ``django`` version::

    pip3.8 install --user --force-reinstall bcrypt


* Run ``migrate``::

    python3.8 manage.py migrate
 
* Then run ``createsuperuser`` command to createsuperuser::

    python3.8 manage.py createsuperuser

* Then run ``collectstatic`` command ::

    python3.8 manage.py collectstatic


* SetUp the ``wsgi.py`` file of ``pythonanywhere`` as the following:

.. code-block:: python

   # +++++++++++ DJANGO +++++++++++
   # To use your own django app use code like this:
   import os
   import sys
   
   ## assuming your django settings file is at '/home/24avepizza/mysite/mysite/settings.py'
   ## and your manage.py is is at '/home/24avepizza/mysite/manage.py'
   path = '/home/24avepizza/pizza24ave'
   if path not in sys.path:
      sys.path.append(path)
   os.environ['DJANGO_SETTINGS_MODULE'] = 'pizza24ave.settings'
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()

   # add this block of code to send mails asynchronously after 60sec
   try:
      import uwsgidecorators
      from django.core.management import call_command

      @uwsgidecorators.timer(60)
      def send_queued_mail(num):
         """Send queued mail every 60 seconds"""
         call_command('send_queued_mail', processes=1)

   except ImportError:
      print("uwsgidecorators not found. Cron and timers are disabled")
      
WEB tab ``static`` section for pythonanywhere
------------------------------------------
* ``static section setup`` under the ``WEB Tab``

+---------------------------+---------------------------------------------------+
| URL                       | Directory                                         |
+---------------------------+---------------------------------------------------+
| ``/static/``              | ``/home/24avepizza/pizza24ave/staticfiles/``      |
+---------------------------+---------------------------------------------------+
| ``/static/admin/``        | ``/home/24avepizza/pizza24ave/staticfiles/admin/``|
+---------------------------+---------------------------------------------------+
| ``/media/``               | ``/home/24avepizza/pizza24ave/media/``            |
+---------------------------+---------------------------------------------------+


Task tab ``static`` setup for pythonanywhere
------------------------------------------
* ``Task tab setup``

+---------------------------+------------------------------------------------------------------+
| Time                      | Command	                                                       |
+---------------------------+------------------------------------------------------------------+
| ``09:49``                 | ``/home/24avepizza/pizza24ave/shop/sendmail_mgt/taskpy.py``      |
+---------------------------+------------------------------------------------------------------+



Credits
=========

Created and maintained by `Dhruva Shaw <https://dhruvacuber.pythonanywhere.com/>`_

