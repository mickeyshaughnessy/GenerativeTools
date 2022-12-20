from setuptools import setup, find_packages


setup(
    name='publish_pygentools',
    version='0.6',
    author='Michael Shaughnessy'
    author_email='michaelshaughnessy114@yahoo.com'
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mickeyshaughnessy/GenerativeTools/'
    keywords='pygentools ML',
    install_requires=[
          'scikit-learn',
      ],

)
