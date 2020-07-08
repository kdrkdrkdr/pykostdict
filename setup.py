from setuptools import setup, find_packages


setup(
    name = 'Python Korean Standard Dictionary',
    version = '1.0',
    license = 'GPLv3',
    author = 'kdr',
    author_email = 'kdrhacker1234@gmail.com',
    description = '국립국어원 표준국어대사전 API',
    long_description = open('README.md').read(),
    url = 'https://github.com/kdrkdrkdr/pykostdict',
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Operating System :: OS Independent'
    ],
)