
import os

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
requires = filter(lambda r:'libs/' not in r,
    open(os.path.join(here, 'requirements.txt')).read().split())
packages = filter(lambda p:not p.startswith('xunit'), find_packages())

version = requires[0].replace('pyzmq==', '') + '.0.1'

setup(**{
    'name': 'zmqmin',
    'version': version,
    'description': u"Simplified python interface for ZMQ.",
    'long_description': README,
    'author':       'Jorge Timon',
    'author_email': 'jtimon@monetize.io',
    'url':          'http://www.github.com/jtimon/zmqmin/',
    'download_url': 'http://pypi.python.org/packages/source/p/zmqmin/zmqmin-%s.tar.gz' % version,
    'packages': packages,
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    'install_requires': requires,
})
