from setuptools import setup, find_packages

test_req = ['pytest==4.0.2', 'pytest-flask==0.14.0', 'pytest-cov==2.6.0',
            'responses==0.9.0', "coverage==4.5.2", "testing.postgresql"]

setup(name='dryvo',
      version='0.2',
      description='Dryvo Application',
      url='https://bitbucket.org/dryvo',
      author='Dryvo',
      author_email='',
      license='MIT',
      packages=['server'],
      install_requires=[
          'gunicorn==19.9.0',
          'SQLAlchemy==1.2.11',
          'SQLAlchemy-Utils==0.33.4',
          'Flask==1.0.2',
          'Flask-Login==0.4.1',
          'Flask-SQLAlchemy==2.3.2',
          'Flask-Script==2.0.6',
          'Flask-Session==0.3.1',
          'pyjwt==1.4.2',
          'loguru==0.2.4',
          'Flask-Migrate==2.3.1',
      ],
      tests_require=test_req,
      setup_requires=['pytest-runner==4.2'],
      extras_require={
          'test': test_req
      },
      zip_safe=False)
