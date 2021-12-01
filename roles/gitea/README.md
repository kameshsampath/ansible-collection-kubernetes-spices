Gitea
=========

Role to install [gitea](https://gitea.io)

Role Variables
--------------

- `kubernetes_spices_gitea_cli_version`: gitea cli version, defaults to  `1.15.6`
- `kubernetes_spices_gitea_namespace`: namespace to install `gitea`, defaults `gitea`

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GPLv3
