import json
from os import path
from setuptools import setup, find_namespace_packages

here = path.abspath(path.dirname(__file__))

requires = [
    'Flask-SQLAlchemy>=2.4.1',
    'psycopg2>=2.8.4',
    'digital.forge.http.server',
]

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the configuration (dictionary) from the setup.json file.
with open(path.join(here, 'setup.json'), encoding='utf-8') as f:
    cfg = json.loads(f.read())

setup(
    name=cfg['project_name'],
    version=cfg['version'],
    description=cfg['description'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=cfg['url'],
    author=cfg['author'],
    author_email=cfg['author_email'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: SOHO Developers',
        'Topic :: Software Development :: IT',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: ' + cfg['python_version'],
    ],
    keywords=cfg['keywords'],
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src', exclude=['*.test']),
    python_requires='>=' + cfg['python_version'],
    install_requires=requires,
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={},
    project_urls={},
)
