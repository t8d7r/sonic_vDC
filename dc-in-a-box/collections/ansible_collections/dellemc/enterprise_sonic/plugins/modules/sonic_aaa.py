#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_aaa
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = """
---
module: sonic_aaa
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
author: Abirami N (@abirami-n)
short_description: Configures aaa settings on Enterprise SONiC
description:
  - This module is used for configuration management of aaa parameters on devices running Enterprise SONiC.
options:
  config:
    description:
      - Specifies the aaa related configurations
    type: dict
    suboptions:
      authentication:
        description:
          - Specifies the configurations required for aaa authentication
        type: dict
        suboptions:
          data:
            description:
              - Specifies the data required for aaa authentication
            type: dict
            suboptions:
              fail_through:
                description:
                  - Specifies the state of failthrough
                type: bool
              local:
                description:
                  - Enable or Disable local authentication
                type: bool
              group:
                description:
                  - Specifies the method of aaa authentication
                type: str
                choices:
                  - ldap
                  - radius
                  - tacacs+

  state:
    description:
      - Specifies the operation to be performed on the aaa parameters configured on the device.
      - In case of merged, the input configuration will be merged with the existing aaa configuration on the device.
      - In case of deleted the existing aaa configuration will be removed from the device.
    default: merged
    choices: ['merged', 'deleted']
    type: str
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local

- name: Delete aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        data:
          local: True
    state: deleted

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method :


# Using deleted
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local

- name: Delete aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
    state: deleted

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  :
# login-method :


# Using merged
#
# Before state:
# -------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : False
# login-method :

- name: Merge aaa configurations
  dellemc.enterprise_sonic.sonic_aaa:
    config:
      authentication:
        data:
          local: true
          fail_through: true
    state: merged

# After state:
# ------------
#
# do show aaa
# AAA Authentication Information
# ---------------------------------------------------------
# failthrough  : True
# login-method : local


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
    of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
    of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.aaa.aaa import AaaArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.aaa.aaa import Aaa


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=AaaArgs.argument_spec,
                           supports_check_mode=True)

    result = Aaa(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
