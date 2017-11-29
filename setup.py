from setuptools import setup, find_packages

setup(
    name='sat-api-client',
    version='0.1',
    description='Query Developmentseed\'s SAT-API',
    author='Jonas Solvsteen',
    author_email='josl@dhigroup.com',
    url='https://www.dhigroup.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dateutil',
        'geojson'
        ],
    )
