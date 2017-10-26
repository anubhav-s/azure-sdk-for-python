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


class OperationResource(Model):
    """The azure async operation response.

    :param status: The async operation state. Possible values include:
     'InProgress', 'Succeeded', 'Failed'
    :type status: str or ~azure.mgmt.hdinsight.models.AsyncOperationState
    :param error: The operation error information.
    :type error: ~azure.mgmt.hdinsight.models.Errors
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'AsyncOperationState'},
        'error': {'key': 'error', 'type': 'Errors'},
    }

    def __init__(self, status=None, error=None):
        self.status = status
        self.error = error
