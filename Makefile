
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
				&& open htmlcov/index.html

pylint:
				pylint imapinboxrules/

test_requirements: requirements
				pip3 install -r requirements.test.txt