from setuptools import setup, find_packages

setup(
    name='aemscan',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'aemscan': ['aemscan/data/']},
    zip_safe=False,
    url='https://github.com/raz0r/aemscan',
    license='MIT',
    author='raz0r',
    author_email='me@raz0r.name',
    description='Adobe Experience Manager Vulnerability Scanner',
    install_requires=[
        'click==6.6',
        'requests==2.20.0',
    ],
    entry_points={
        'console_scripts': [
            'aemscan = aemscan:main',
        ],
    },
    test_suite='nose.collector',
    tests_require=['nose==1.3.7'],
)
