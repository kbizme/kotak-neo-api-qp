from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.0"
# To install the library, run the following
#
# python setup.py install

REQUIRES = ['bidict', 'certifi', 'idna', 'numpy', 'pyjsparser', 'PyJWT',
            'python-dateutil', 'python-dotenv', 'requests', 'six', 'urllib3',
            'websocket-client', 'websockets', 'pandas', 'asyncio']

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API",
    author="ne API",
    author_email="",
    url="",
    keywords=["Neo-Trade API", "Neo Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
