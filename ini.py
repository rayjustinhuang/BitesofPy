import configparser

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
        raw_string = self.config['tox']['envlist']
        if ',' in raw_string:
            raw_list = raw_string.split(',')
        elif '\n' in raw_string:
            raw_list = raw_string.split("\n")
        else:
            raw_list = raw_string.split(" ")
        raw_list = [word.replace(' ','').replace(',','').replace('\n','') for word in raw_list]
        raw_list = list(filter(None,raw_list))

        return raw_list
        pass

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        bases = []
        for sect in self.config.sections():
            for k,v in self.config.items(sect):
                if k == 'basepython':
                    bases.append(v)
        return list(set(bases))
        pass