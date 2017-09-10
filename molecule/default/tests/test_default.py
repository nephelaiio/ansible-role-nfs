import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_host(host):
    for config_file in ['/etc/exports']:
        assert host.file(config_file).exists
        assert host.file(config_file).user == 'root'
        assert host.file(config_file).group == 'root'
        assert host.file(config_file).mode == 0o644
    print(host.system_info.distribution)
    if host.system_info.distribution.lower() in ['debian', 'ubuntu']:
        service_names = ['nfs-kernel-server']
    elif host.system_info.distribution.lower() in ['centos']:
        service_names = ['nfs-server', 'rpcbind']
    elif host.system_info.distribution.lower() in ['arch']:
        service_names = ['nfs-server']
    for service_name in service_names:
        assert host.service(service_name).is_running
