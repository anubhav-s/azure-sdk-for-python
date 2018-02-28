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


class SchemaComparisonValidationResultType(Model):
    """Description about the errors happen while performing migration validation.

    :param object_name: Name of the object that has the difference
    :type object_name: str
    :param object_type: Type of the object that has the difference. e.g
     (Table/View/StoredProcedure). Possible values include: 'StoredProcedures',
     'Table', 'User', 'View', 'Function'
    :type object_type: str or ~azure.mgmt.datamigration.models.ObjectType
    :param update_action: Update action type with respect to target. Possible
     values include: 'DeletedOnTarget', 'ChangedOnTarget', 'AddedOnTarget'
    :type update_action: str or
     ~azure.mgmt.datamigration.models.UpdateActionType
    """

    _attribute_map = {
        'object_name': {'key': 'objectName', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'ObjectType'},
        'update_action': {'key': 'updateAction', 'type': 'UpdateActionType'},
    }

    def __init__(self, object_name=None, object_type=None, update_action=None):
        super(SchemaComparisonValidationResultType, self).__init__()
        self.object_name = object_name
        self.object_type = object_type
        self.update_action = update_action
