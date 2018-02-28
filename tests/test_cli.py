import pytest

from pgbackup import cli

url = "postgres://bob:password@example.com:5432/db_one"

def test_parser_without_driver():
	"""
	Without a specified driver the parser will exit
	"""
	parser = cli.create_parser()
	with pytest.raises(SystemExit):
		parser.parse_args([url])
		
def test_parsers_with_driver():
	"""
	The parser will eixt if it receives a driver without a destination.
	"""
	parser = cli.create_parser()
	with pytest.raises(SystemExit):
                  parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination():
	"""
	The parser will not exit if it receives a driver and 
	a destination
	"""
	parser = cli.create_parser()
	args = parser.parse_args([url, '--driver', 'local', '/some/path'])

	assert args.driver == 'local'
	assert args.destination == '/some/path'


def test_parser_with_unknown_driver():
	"""
	This one will exit if the driver name is unknown.
	"""
	parser = cli.create_parser()
 	with pytest.raises(SystemExit):
 		parser.parse_args([url, '--driver', 'azure', 'destination'])


def test_parser_with_known_drivers():
	"""
	The parser will not exit if the driver name is known.
	"""
	parser = cli.create_parser()
	
	for driver in ['local', 's3']:
		assert parser.parse_args([url, '--driver', driver, 'destination'])

#	with pytest.raises(SystemExit):
#		parser.parse_args([url, '--driver', 'azure', 'destination'])



	
