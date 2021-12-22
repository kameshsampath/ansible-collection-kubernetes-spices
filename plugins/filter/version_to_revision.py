# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Kamesh Sampath (@kamesh_sampath) <kamesh.sampaath@hotmail.com>
# Apache License v2.0 (see COPYING or https://www.apache.org/licenses/LICENSE-2.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import re


def version_to_revision(version, prefix=None, patch=True):
    regex = r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)\-*(?P<micro>[\w+]*)"
    if patch:
        subst = "\\g<major>-\\g<minor>-\\g<patch>"
    else:
        subst = "\\g<major>-\\g<minor>"
    if prefix:
        subst = prefix + '-' + subst
    """
    version_to_revision takes a string version like 1.10.1 and converts it to a revision 1-10 excluding the patch version
    :param version: the version
    :param prefix: the prefix to add to revision
    :param micro: include micro version in revision
    :return: the "-" seperated revision string
    """
    if version:
        revision = re.sub(regex, subst, version, 1)
        if revision:
            return revision


class FilterModule(object):
    """ Ansible vault jinja2 filters """

    def filters(self):
        filters = {
            'version_to_revision': version_to_revision
        }

        return filters
