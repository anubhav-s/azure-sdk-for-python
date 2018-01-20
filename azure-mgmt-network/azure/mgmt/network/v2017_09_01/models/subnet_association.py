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


class SubnetAssociation(Model):
    """Network interface and its custom security rules.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Subnet ID.
    :vartype id: str
    :param security_rules: Collection of custom security rules.
    :type security_rules:
     list[~azure.mgmt.network.v2017_09_01.models.SecurityRule]
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'security_rules': {'key': 'securityRules', 'type': '[SecurityRule]'},
    }

    def __init__(self, **kwargs):
        super(SubnetAssociation, self).__init__(**kwargs)
        self.id = None
        self.security_rules = kwargs.get('security_rules', None)
