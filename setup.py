from setuptools import setup

import ssaiw

print(ssaiw.__doc__)
print(ssaiw.__version__)
print(ssaiw.__author__)

setup(
    name='spark-submit-app-id-wrapper',
    version=ssaiw.__version__,
    description=ssaiw.__doc__,
    author=ssaiw.__author__,
)
