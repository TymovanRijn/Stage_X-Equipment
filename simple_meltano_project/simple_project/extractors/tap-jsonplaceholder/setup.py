from setuptools import setup, find_packages

setup(
    name='tap-jsonplaceholder',
    version='0.1',
    description='A Singer tap for JSONPlaceholder',
    py_modules=['tap_jsonplaceholder'],
    install_requires=[
        'requests',
        'singer-python'
    ],
    entry_points='''
        [console_scripts]
        tap-jsonplaceholder=tap_jsonplaceholder:main
    ''',
)
