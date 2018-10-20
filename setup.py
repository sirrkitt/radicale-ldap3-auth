#!/usr/bin/env python3

from distutils.core import setup

setup(
  name='radicale_ldap3_auth',
  version='0.0.1',
  description='Simple, rough, LDAP3 auth plugin for Radicale',
  long_description=open('README').read(),
  license='LICENSE',
  author='Jacob Louis Lemus Peschel',
  author_email='jacob@tlacuache.us',
  install_requires=['radicale', 'ldap3'],
  packages=['radicale_ldap3_auth']
)
