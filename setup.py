from setuptools import setup

# with open("LICENSE.txt", "r") as file:
#     license_file = file

setup(
    name='calcrec',
    version='0.0.1',
    description='Calculadora de antecipação de recebíveis',
    url='git@github.com:andrefgj/calculadora_antecipacao.git',
    author='André Ferreira G Jr',
    author_email='andrefgj@gmail.com',
    # license=license_file,
    packages=['calcrec'],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "calcrec = calcrec.__main__:main"
        ]
    },

)