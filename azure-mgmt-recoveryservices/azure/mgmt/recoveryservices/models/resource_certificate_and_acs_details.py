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

from .resource_certificate_details import ResourceCertificateDetails


class ResourceCertificateAndAcsDetails(ResourceCertificateDetails):
    """Certificate details representing the Vault credentials for ACS.

    :param certificate: The base64 encoded certificate raw data string.
    :type certificate: bytearray
    :param friendly_name: Certificate friendlyname.
    :type friendly_name: str
    :param issuer: Certificate issuer.
    :type issuer: str
    :param resource_id: Resource ID of the vault.
    :type resource_id: long
    :param subject: Certificate Subject Name.
    :type subject: str
    :param thumbprint: Certificate thumbprint.
    :type thumbprint: str
    :param valid_from: Certificate Validity start Date time.
    :type valid_from: datetime
    :param valid_to: Certificate Validity End Date time.
    :type valid_to: datetime
    :param auth_type: Constant filled by server.
    :type auth_type: str
    :param global_acs_namespace: ACS namespace name - tenant for our service.
    :type global_acs_namespace: str
    :param global_acs_host_name: Acs mgmt host name to connect to.
    :type global_acs_host_name: str
    :param global_acs_rp_realm: Global ACS namespace RP realm.
    :type global_acs_rp_realm: str
    """

    _validation = {
        'auth_type': {'required': True},
        'global_acs_namespace': {'required': True},
        'global_acs_host_name': {'required': True},
        'global_acs_rp_realm': {'required': True},
    }

    _attribute_map = {
        'certificate': {'key': 'certificate', 'type': 'bytearray'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'issuer': {'key': 'issuer', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'long'},
        'subject': {'key': 'subject', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'valid_from': {'key': 'validFrom', 'type': 'iso-8601'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'},
        'auth_type': {'key': 'authType', 'type': 'str'},
        'global_acs_namespace': {'key': 'globalAcsNamespace', 'type': 'str'},
        'global_acs_host_name': {'key': 'globalAcsHostName', 'type': 'str'},
        'global_acs_rp_realm': {'key': 'globalAcsRPRealm', 'type': 'str'},
    }

    def __init__(self, global_acs_namespace, global_acs_host_name, global_acs_rp_realm, certificate=None, friendly_name=None, issuer=None, resource_id=None, subject=None, thumbprint=None, valid_from=None, valid_to=None):
        super(ResourceCertificateAndAcsDetails, self).__init__(certificate=certificate, friendly_name=friendly_name, issuer=issuer, resource_id=resource_id, subject=subject, thumbprint=thumbprint, valid_from=valid_from, valid_to=valid_to)
        self.global_acs_namespace = global_acs_namespace
        self.global_acs_host_name = global_acs_host_name
        self.global_acs_rp_realm = global_acs_rp_realm
        self.auth_type = 'AccessControlService'
