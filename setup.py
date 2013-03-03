from setuptools import setup, find_packages

version = '2.13.19.1'

setup(name='hoka.adapter.portal',
      version=version,
      description='Adapter to get the portal root of a plone site',
      long_description=open("README.rst").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Intended Audience :: Other Audience",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        ],
      keywords='adapter portal plone hoka',
      author='Kai Hoppert',
      author_email='kai.hoppert@online.de',
      url='http://github.com//hoka/hoka.adapter.portal',
      license='GPL version 2',
      packages=find_packages(),
      namespace_packages=['hoka','hoka.adapter'],
      include_package_data=True,
      install_requires=[
        'setuptools',
        'plone',
        'z3c.autoinclude',
        'hoka.patches.get_adapter',
        'hoka.adapter.base',

      ],
      extras_require={'test': [
        'collective.testcaselayer',
      ]},
      platforms='Any',
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = plone
''',
)