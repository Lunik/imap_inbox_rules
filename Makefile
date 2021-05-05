
default: requirements build test

requirements:
				pip3 install -r requirements.txt

build:
				echo "Not implemented"

test: pytest pylint

pytest: test_requirements
				pytest \
				  --cov imapinboxrules \
				  --cov-branch \
				  --cov-report term-missing \
				  --cov-report html \
				  --cov-report xml \
				&& open htmlcov/index.html

pylint:
				pylint tests/ imapinboxrules/

imap_server: start_imap_server init_imap_server

start_imap_server:
				docker run -d \
				  --name imap-server \
				  -p 3143:3143 \
				  greenmail/standalone &

init_imap_server:
				python imapinboxrules/tests/init/setup.py

test_requirements: requirements
				pip3 install -r requirements.test.txt