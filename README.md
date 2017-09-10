# nephelaiio.nfs

[![Build Status](https://travis-ci.org/nephelaiio/ansible-role-nfs.svg?branch=master)](https://travis-ci.org/nephelaiio/ansible-role-nfs)

An [ansible role](https://galaxy.ansible.com/nephelaiio/nfs) to install and configure nfs

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook

- hosts: servers
  roles:
     - role: nfs
       nfs_exports:
         - /var/nfs/backups -sec=sys,rw,anon=0


## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch
  * Arch Linux

You can test the role directly from sources using command ` molecule test `
Travis configuration is provided in the [Travis-CI configuration file](/.travis.yml)
Please review the [documentation](http://docs.ansible.com/ansible/galaxy.html#setup-travis-integrations) in order to add continuous integration for the role using [Travis CI](https://travis-ci.org). 

## License

This project is licensed under the terms of the [MIT License](/LICENSE)