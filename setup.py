from setuptools import setup

setup(name='NKPy',

      version='0.1.26',

      url='https://github.com/NKPy/NKPy',

      license='MIT',

      author='Helloyunho, Func, Preta 「 プレタ 」, BGM',

      author_email='yunho050840@gmail.com',

      description='Nanhe Korean Python',

      packages=['nkpy', 'py2nkpy'],

      long_description=open('README.md').read(),

      zip_safe=False,

      scripts=['bin/nkpy', 'bin/py2nkpy']
      )
