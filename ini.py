import configparser

cookiecutter = """[tox]
envlist = py27, py34, py35, py36, pypy, flake8

[testenv]
passenv = LC_ALL, LANG, HOME
commands = pytest --cov=cookiecutter {posargs:tests}
deps = -rtest_requirements.txt

[testenv:flake8]
deps =
    flake8==3.5.0
commands =
    flake8 cookiecutter tests setup.py

[testenv:cov-report]
commands = pytest --cov=cookiecutter --cov-report=term --cov-report=html"""

class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        pass

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())
        pass

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envs = []
        for sect in self.config.sections():
            envs.append(sect[envlist])
        pass

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        bases = []
        for sect in self.config.sections():
            bases.append(sect[basepython])
        pass
    
#reader = ToxIniParser(cookiecutter)
#reader.number_of_sections

#parser = configparser.ConfigParser().read_string(cookiecutter)
#print(len(parser.sections()))