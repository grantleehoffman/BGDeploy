try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
import bgdeploy

setup(
    name='bgdeploy',
    description='Route53 Alis Record Change Script',
    author='Grant Hoffman',
    url='github.com/grantleehoffman/BGDeploy.',
    download_url='git@github.com:grantleehoffman/BGDeploy.git',
    author_email='grantleehoffman@gmail.com',
    install_requires=['boto>=2'],
    version=bgdeploy.__version__,
    packages=find_packages(),
    scripts=['bgdeploy/bgswitch'],
    )
