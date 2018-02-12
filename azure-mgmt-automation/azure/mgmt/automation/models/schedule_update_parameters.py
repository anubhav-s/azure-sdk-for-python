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


class ScheduleUpdateParameters(Model):
    """The parameters supplied to the update schedule operation.

    :param name: Gets or sets the name of the schedule.
    :type name: str
    :param description: Gets or sets the description of the schedule.
    :type description: str
    :param is_enabled: Gets or sets a value indicating whether this schedule
     is enabled.
    :type is_enabled: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'is_enabled': {'key': 'properties.isEnabled', 'type': 'bool'},
    }

    def __init__(self, name=None, description=None, is_enabled=None):
        super(ScheduleUpdateParameters, self).__init__()
        self.name = name
        self.description = description
        self.is_enabled = is_enabled
