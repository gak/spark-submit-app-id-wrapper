from fabric.decorators import task
from fabric.operations import local


@task
def release(version):
    local('git flow release start {}'.format(version))
    local('python setup.py bdist_wheel upload')
    local('git flow release finish {}'.format(version))
