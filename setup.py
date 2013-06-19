from setuptools import setup, find_packages

setup(
    name='cmsplugin-contact-extensible',
    version='0.1',
    description='Allow to extend cmsplugin-contact with custom fields',
    author='Alban Tiberghien',
    author_email='alban.tiberghien@gmail.com',
    url='http://github.com/atibergien/cmsplugin-contact-extensible',
    packages=find_packages(),
    install_requires=[],
    keywords='contact form django cms django-cms extendable',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
