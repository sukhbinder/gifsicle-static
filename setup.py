from setuptools import setup
import os

# Read the long description from README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gifsicle-cli',
    version='0.1.0',
    py_modules=['gif'],  # This tells setuptools to include gif.py as a module
    entry_points={
        'console_scripts': [
            'gif=gif:main',  # This creates a 'gif' command that calls gif.py's main function
        ],
    },
    install_requires=[], # No external Python dependencies for this wrapper
    author='Your Name', # Placeholder
    author_email='your.email@example.com', # Placeholder
    description='A Python wrapper for the gifsicle command-line tool.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/gifsicle-cli', # Placeholder
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Assuming MIT, can be changed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
