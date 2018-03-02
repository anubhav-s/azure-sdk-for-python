# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RoleDefinitionFilter(Model):
    """Role Definitions filter.

    :param role_name: Returns role definition with the specific name.
    :type role_name: str
    :param type: Returns role definition with the specific type.
    :type type: str
    """

    _attribute_map = {
        'role_name': {'key': 'roleName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, role_name=None, type=None):
        super(RoleDefinitionFilter, self).__init__()
        self.role_name = role_name
        self.type = type
