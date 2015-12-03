from setuptools import setup

import ssaiw

setup(
    name='spark-submit-app-id-wrapper',
    version=ssaiw.__version__,
    description=ssaiw.__doc__,
    author=ssaiw.__author__,
    author_email=ssaiw.__author_email__,
    url=ssaiw.__url__,
    license='Apache Licence 2.0',
    packages=['ssaiw'],
    entry_points={
        'console_scripts': [
            'ssaiw=ssaiw:wrap',
        ],
    },
)
