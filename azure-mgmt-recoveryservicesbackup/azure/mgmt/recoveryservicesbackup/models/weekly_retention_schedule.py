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


class WeeklyRetentionSchedule(Model):
    """Weekly retention schedule.

    :param days_of_the_week: List of days of week for weekly retention policy.
    :type days_of_the_week: list[str or
     ~azure.mgmt.recoveryservicesbackup.models.DayOfWeek]
    :param retention_times: Retention times of retention policy.
    :type retention_times: list[datetime]
    :param retention_duration: Retention duration of retention Policy.
    :type retention_duration:
     ~azure.mgmt.recoveryservicesbackup.models.RetentionDuration
    """

    _attribute_map = {
        'days_of_the_week': {'key': 'daysOfTheWeek', 'type': '[DayOfWeek]'},
        'retention_times': {'key': 'retentionTimes', 'type': '[iso-8601]'},
        'retention_duration': {'key': 'retentionDuration', 'type': 'RetentionDuration'},
    }

    def __init__(self, days_of_the_week=None, retention_times=None, retention_duration=None):
        super(WeeklyRetentionSchedule, self).__init__()
        self.days_of_the_week = days_of_the_week
        self.retention_times = retention_times
        self.retention_duration = retention_duration
