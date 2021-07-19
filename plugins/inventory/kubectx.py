# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Kamesh Sampath (@kamesh_sampath) <kamesh.sampaath@hotmail.com>
# Apache License v2.0 (see COPYING or https://www.apache.org/licenses/LICENSE-2.0.txt)


from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import kubernetes
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from kubernetes.config.kube_config import KUBE_CONFIG_DEFAULT_LOCATION

DOCUMENTATION = '''
    name: kubectx
    plugin_type: inventory
    author:
      - Kamesh Sampath<@kamesh_sampath>
    
    short_description: Kubernetes contexts inventory source
    
    description:
      - Builds a inventory to based on the contexts available as part of the $KUBECONFIG
      - Helps running the same playbook against multiple Kubernetes cluster contexts
    options:
      plugin:
        description: token that ensures this is a source file for the 'k8s' plugin.
        required: True
        choices: ["kameshsampath.kubernetes_spices.kubectx"]
      use_contexts:
        description:
          - Optional list of cluster context settings. If no connections are provided, the default
            I(~/.kube/config) and active context will be used.
        suboptions:
          name:
            description:
              - Required name of the context.
          kubeconfig:
            description:
              - Optional path to an existing Kubernetes config file where the context can be found. If not provided
                this will be set to the default KUBECONFIG file I(~/.kube/config).
    
    requirements:
      - "python >= 3.6"
      - "kubernetes >= 12.0.0"
      - "PyYAML >= 3.11"

'''

EXAMPLES = '''
# File must be named kubectx.yaml or kubectx.yml

# A specific context that will be loaded from default Kubeconfig file ~/.kube.
plugin: kameshsampath.kubernetes_spices.kubectx
use_contexts:
  - name: 'awx/192-168-64-4:8443/developer'
    
# Use a custom config file, and a specific context.
plugin: kameshsampath.kubernetes_spices.kubectx
use_contexts:
  - from: /path/to/config
    context: 'awx/192-168-64-4:8443/developer'
'''

try:
    from kubernetes.dynamic.exceptions import DynamicApiError
except ImportError:
    pass


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = 'kameshsampath.kubernetes_spices.kubectx'

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        cache_key = self._get_cache_prefix(path)
        config_data = self._read_config_data(path)
        self.setup(config_data, cache, cache_key)

    def setup(self, config_data, cache, cache_key):
        kube_config = KUBE_CONFIG_DEFAULT_LOCATION
        t_contexts = kubernetes.config.list_kube_config_contexts(kube_config)

        use_contexts = config_data.get('use_contexts')
        # print(f"Contexts: {contexts}")

        if use_contexts is None or len(use_contexts) == 0:
            # print(f"Adding default current context to list {t_contexts[1]}")
            ctx = dict(t_contexts[1])
            name = ctx.get("name")
            self._set_host_vars(name, ctx)
            self.set_variable(name, 'kubeconfig_file', kube_config)
        else:
            for ctx in use_contexts:
                # print(f"{t_contexts[0]}")
                for item in t_contexts[0]:
                    t = dict(item)
                    name = t.get('name')
                    # print(f"Processing Item{t}")
                    # print(f"comparing { ctx.get('name')} == {name}")
                    if name == ctx.get('name'):
                        self._set_host_vars(name, t)
                        kubeconfig_file = ctx.get("from")
                        # print(f"Context {name} Kubeconfig {kubeconfig_file}")
                        if kubeconfig_file is None:
                            self.inventory.set_variable(name, 'kubeconfig_file', '~/.kube/config')
                        else:
                            self.inventory.set_variable(name, 'kubeconfig_file', kubeconfig_file)

    def _set_host_vars(self, name, context):
        self.inventory.add_host(name)
        self.inventory.set_variable(name, 'k8s_current_context', name)
        self.inventory.set_variable(name, 'k8s_context_cluster', context.get("context").get("cluster"))
        self.inventory.set_variable(name, 'k8s_context_user', context.get("context").get("user"))
