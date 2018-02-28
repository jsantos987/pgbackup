from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
	readme = f.read()

setup(
	name='pgbackup',
	version='0.1.0',
	description='Database backups locally or to AWS S3.',
	long_description=remote,
	author='John Santos',
	author_email='jas.santos.987@gmail.com',
	packages=find_packagaes('src'),
	package_dir={'', 'src'},
	install_requires=[]
)
