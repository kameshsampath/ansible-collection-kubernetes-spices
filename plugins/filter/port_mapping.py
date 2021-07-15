# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Kamesh Sampath (@kamesh_sampath) <kamesh.sampaath@hotmail.com>
# Apache License v2.0 (see COPYING or https://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


def mapped_port(mappings, protocol='tcp', host_ip='0.0.0.0'):
    """
    mapped_port gets an dict of simplified mapping of ports typically like { port: port-value }
    :param mappings: the docket port mappings as JSON e.g docker inspect 4938bd0ba96d -f '{{.NetworkSettings.Ports }}'
    :param protocol: the protocol of the port to extract
    :param host_ip: the host interface ip that the port is mapped to 
    :return: a dict of port and its mappings
    """
    # print(f"{mappings}")
    simple_mapping = {}
    for k, v in mappings.items():
        key = k.split(f"/{protocol}")[0]
        for j in v:
            if j['HostIp'] == '0.0.0.0':
                simple_mapping[key] = int(j['HostPort'])
    return simple_mapping


class FilterModule(object):
    ''' Ansible vault jinja2 filters '''

    def filters(self):
        filters = {
            'port_mapping': mapped_port
        }

        return filters
