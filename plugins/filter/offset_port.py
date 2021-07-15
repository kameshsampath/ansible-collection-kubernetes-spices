# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Kamesh Sampath (@kamesh_sampath) <kamesh.sampaath@hotmail.com>
# Apache License v2.0 (see COPYING or https://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.errors import AnsibleFilterError
import socket

# max node port value allowed by Kubernetes node port range
max_port = 32767


def offset_port(port=30000, offset=100):
    """
    finds a free port on the localhost and returns it. If the port is not 
    free then it returns port + offset value
    :param port: the port to bind or offset, the default value 30000 is the start range of Kubernetes node port
    :param offset: the offset value that needs to be added to port
    :return: the port if its available or the port + offset value
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while port <= max_port:
        try:
            sock.bind(('localhost', port))
            sock.close()
            return port
        except OSError:
            # TODO if there a much better way to do this ??
            # for any ports less than 1024 try to increase the offset by 1000 + offset
            if port < 1024:
                port += (1000 + offset)
            else:
                port += offset
    raise AnsibleFilterError(f'no free ports between {port} and {max_port}')


class FilterModule(object):
    ''' Ansible vault jinja2 filters '''

    def filters(self):
        filters = {
            'offset_port': offset_port
        }

        return filters
