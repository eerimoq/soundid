|buildstatus|_
|coverage|_

About
=====

A Python package for sound identification.

References:

- https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf

Installation
============

.. code-block:: python

    pip install soundid

Example Usage
=============

Command line tool
-----------------

Create a database, ``db.sid``, of two mp3-files
``tests/files/foo.mp3`` and ``tests/files/bar.mp3``.

.. code-block:: text

   $ soundid database_create db.sid tests/files/{foo,bar}.mp3

Show basic information about the database ``db.sid``.

.. code-block:: text

   $ soundid database_info db.sid
   1. Foo Band - Foo Song (0m5s, 4520 hashes)
   2. Bar Artist - Bar Song (0m4s, 3023 hashes)
   $

Try to find the title for the song ``tests/files/foo.mp3``.

.. code-block:: text

   $ soundid file tests/files/db.sid tests/files/foo.mp3
   Foo Band - Foo Song
   $

Try to find the title for the song ``tests/files/fie.mp3``. It should
not be found as its not part of the database.

.. code-block:: text

   $ soundid file tests/files/db.sid tests/files/fie.mp3

Try to identify a song using the mic ``MIC``.

.. code-block:: text

   $ soundid mic tests/files/db.sid MIC
   Foo Band - Foo Song
   $

Scripting
---------

.. code-block:: python

   >>> database = soundid.Database('db.sid', ['tests/files/{foo,bar}.mp3'])
   >>> database.identify_file('tests/files/foo.mp3')
   Foo Band - Foo Song
   >>> database.identify_file('tests/files/fie.mp3')
   None
   >>> database.identify_mic('MIC')
   Foo Band - Foo Song
   >>>

Contributing
============

#. Fork the repository.

#. Install prerequisites.

   .. code-block:: text

      $ pip install -r requirements.txt

#. Implement the new feature or bug fix.

#. Implement test case(s) to ensure that future changes do not break
   legacy.

#. Run the tests.

   .. code-block:: text

      $ make test

#. Create a pull request.

.. |buildstatus| image:: https://travis-ci.org/eerimoq/soundid.svg?branch=master
.. _buildstatus: https://travis-ci.org/eerimoq/soundid

.. |coverage| image:: https://coveralls.io/repos/github/eerimoq/soundid/badge.svg?branch=master
.. _coverage: https://coveralls.io/github/eerimoq/soundid
