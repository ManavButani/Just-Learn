"""
Create a dummy configuration file (some of extension of such a file can be: .conf, .cfg, .config, .ini) in key value pair (refer this document for details).
Using ConfigParser library of Python, read the file and write the contents of the old file in a new configuration file.
The code should work on both Py2 and Py3. Use try-catch blocks wherever necessary.
"""
try:
    import configparser
except ImportError:
    from six.moves import configparser
try:
    configure=configparser.ConfigParser()
    configure.read('demo_config.ini')
    with open('demo_new_config.ini','w') as file:
        configure.write(file)
except FileNotFoundError as error:
    print(error)
except ValueError as error:
    print(error)