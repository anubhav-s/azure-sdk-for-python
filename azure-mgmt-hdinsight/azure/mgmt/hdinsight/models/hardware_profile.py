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


class HardwareProfile(Model):
    """The hardware profile.

    :param vm_size: The size of the VM
    :type vm_size: str
    """

    _attribute_map = {
        'vm_size': {'key': 'vmSize', 'type': 'str'},
    }

    def __init__(self, vm_size=None):
        super(HardwareProfile, self).__init__()
        self.vm_size = vm_size
