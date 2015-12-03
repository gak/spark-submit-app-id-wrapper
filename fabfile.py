from fabric.decorators import task
from fabric.operations import local


@task
def upload():
    local('python setup.py bdist_wheel upload')
