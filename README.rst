pgbackup
==========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

Preparing for Development
-----------------------------

1. Ensure ''pip'' and ''pipenv'' are installed.
2. Clone repository: ''git clone git@github.com:example/pgbackup''.
3. Fetch developmnet dependencies: ''make install''.

Usage
-----------------------------

Pass in a full database URL, the storage driver, and destination.

S3 Sxample w/ bucket name:

::

	$ pgbackup postgres://bob@examples.com:5432/db_one -- driver s3 backups

LOCAL Example w/ local path:

::

	$ pgbackup postgres://bob@example.com:5432/db_one -- driver local /var/local/db_one/backups/dump.sql

Running Tests
-----------------------------

Run test locally using ''make'' if virtualenv is active:

::

	$ make

If virtualenv isn't active then use:

::

	$ pipenv run make

