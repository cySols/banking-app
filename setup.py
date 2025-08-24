from setuptools import setup, find_packages

setup(
    name='banking-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here, e.g. 'click' or 'argparse'
    ],
    entry_points={
        'console_scripts': [
            'banking-app=banking.main:main',
        ],
    },
    author='cySols',
    author_email='you@example.com',  # Optional
    description='A simple command-line banking application',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/cySols/banking-app',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
