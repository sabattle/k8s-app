import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='python-app-sabattle',
    version='0.0.1',
    author='Sebastian Battle',
    author_email='sabattle@eckerd.edu',
    description='Simple Flask app for k8s',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sabattle/k8s-app',
    packages=setuptools.find_packages()
)