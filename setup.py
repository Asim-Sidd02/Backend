import setuptools

setuptools.setup(
    name='Sign Sense',
    version='0.1.0',
    description='Python project',
    author='Asim Sidd',
    author_email='',
    url='',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)