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


class MabJobTaskDetails(Model):
    """MAB workload-specific job task details.

    :param task_id: The task display name.
    :type task_id: str
    :param start_time: The start time.
    :type start_time: datetime
    :param end_time: The end time.
    :type end_time: datetime
    :param duration: Time elapsed for task.
    :type duration: timedelta
    :param status: The status.
    :type status: str
    """

    _attribute_map = {
        'task_id': {'key': 'taskId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'duration': {'key': 'duration', 'type': 'duration'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, task_id=None, start_time=None, end_time=None, duration=None, status=None):
        super(MabJobTaskDetails, self).__init__()
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.duration = duration
        self.status = status
