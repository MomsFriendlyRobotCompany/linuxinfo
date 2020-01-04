from __future__ import print_function
from setuptools import setup
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import SetGitTag
from build_utils import get_pkg_version


VERSION = get_pkg_version('linuxinfo/__init__.py')

PACKAGE_NAME = 'linuxinfo'
BuildCommand.pkg = PACKAGE_NAME
BuildCommand.py2 = False  # not supporting python2 anymore
# BuildCommand.test = False  # don't do tests?
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
SetGitTag.version = VERSION
README = open('readme.md').read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="Kevin Walchko",
    keywords=['raspberry pi', 'pi', 'info', 'proc', 'cpu', 'linux'],
    author_email="walchko@noreply.github.com",
    description="A python library to get linux/raspberry pi info",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'build_utils'     # installing and building the library
    ],
    url="https://github.com/MomsFriendlyRobotCompany/{}".format(PACKAGE_NAME),
    long_description=README,
    long_description_content_type='text/markdown',
    packages=[PACKAGE_NAME],
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand,
        'tag': SetGitTag
    }
)
