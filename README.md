# ansible-role-disable-numa #

[![Build Status](https://travis-ci.com/cisagov/ansible-role-disable-numa.svg?branch=develop)](https://travis-ci.com/cisagov/ansible-role-disable-numa)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-disable-numa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-disable-numa/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-disable-numa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-disable-numa/context:python)

An Ansible role for configuring an instance to disable
[NUMA](https://en.wikipedia.org/wiki/Non-uniform_memory_access)
globally.

## Requirements ##

None.

## Role Variables ##

None.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - disable_numa
```

## Contributing ##

We welcome contributions!  Please see [here](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE.md).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
