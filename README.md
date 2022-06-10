# nephelaiio.nfs

[![Build Status](https://github.com/nephelaiio/ansible-role-nfs/workflows/CI/badge.svg)](https://github.com/nephelaiio/ansible-role-nfs/actions)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-nephelaiio.nfs-blue.svg)](https://galaxy.ansible.com/nephelaiio/nfs/)

An [ansible role](https://galaxy.ansible.com/nephelaiio/nfs) to install and configure nfs

## Role Variables

NFS server configuration is set by default
```
nfs_server: yes
```
Set to false for client-only installation

NFS export list is empty by default
```
nfs_exports: []
```

You can customize them as a list of /etc/exports file entries:

```
nfs_exports:
  - / *(ro,fsid=0)
  - /home *(rw,sync,nohide)
```

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Example Playbook
```
- hosts: nfs
  vars:
     nfs_exports:
       - /var/nfs/backups -sec=sys,rw,anon=0
  roles:
     - role: nephelaiio.nfs
```

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):
  * Ubuntu Bionic
  * Ubuntu Xenial
  * CentOS 7
  * Debian Stretch

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [MIT License](/LICENSE)
