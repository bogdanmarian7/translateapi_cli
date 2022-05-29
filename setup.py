from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Translates text from one language to another. It uses LibreTranslate Api.'


# Setting up
setup(
    name="translateapi",
    version=VERSION,
    author="Bogdan Marian",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['python', 'translate', 'translateapi'],
    entry_points={
        'console_scripts': [
            'translate-cli=src.run:main',
        ]

    },
    install_requires=["requests"]
)
