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

from .sub_resource import SubResource


class SecurityRule(SubResource):
    """Network security rule.

    All required parameters must be populated in order to send to Azure.

    :param id: Resource ID.
    :type id: str
    :param description: A description for this rule. Restricted to 140 chars.
    :type description: str
    :param protocol: Required. Network protocol this rule applies to. Possible
     values are 'Tcp', 'Udp', and '*'. Possible values include: 'Tcp', 'Udp',
     '*'
    :type protocol: str or
     ~azure.mgmt.network.v2017_08_01.models.SecurityRuleProtocol
    :param source_port_range: The source port or range. Integer or range
     between 0 and 65535. Asterix '*' can also be used to match all ports.
    :type source_port_range: str
    :param destination_port_range: The destination port or range. Integer or
     range between 0 and 65535. Asterix '*' can also be used to match all
     ports.
    :type destination_port_range: str
    :param source_address_prefix: The CIDR or source IP range. Asterix '*' can
     also be used to match all source IPs. Default tags such as
     'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If
     this is an ingress rule, specifies where network traffic originates from.
    :type source_address_prefix: str
    :param source_address_prefixes: The CIDR or source IP ranges.
    :type source_address_prefixes: list[str]
    :param destination_address_prefix: The destination address prefix. CIDR or
     destination IP range. Asterix '*' can also be used to match all source
     IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and
     'Internet' can also be used.
    :type destination_address_prefix: str
    :param destination_address_prefixes: The destination address prefixes.
     CIDR or destination IP ranges.
    :type destination_address_prefixes: list[str]
    :param source_port_ranges: The source port ranges.
    :type source_port_ranges: list[str]
    :param destination_port_ranges: The destination port ranges.
    :type destination_port_ranges: list[str]
    :param access: Required. The network traffic is allowed or denied.
     Possible values are: 'Allow' and 'Deny'. Possible values include: 'Allow',
     'Deny'
    :type access: str or
     ~azure.mgmt.network.v2017_08_01.models.SecurityRuleAccess
    :param priority: The priority of the rule. The value can be between 100
     and 4096. The priority number must be unique for each rule in the
     collection. The lower the priority number, the higher the priority of the
     rule.
    :type priority: int
    :param direction: Required. The direction of the rule. The direction
     specifies if rule will be evaluated on incoming or outcoming traffic.
     Possible values are: 'Inbound' and 'Outbound'. Possible values include:
     'Inbound', 'Outbound'
    :type direction: str or
     ~azure.mgmt.network.v2017_08_01.models.SecurityRuleDirection
    :param provisioning_state: The provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: The name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'protocol': {'required': True},
        'access': {'required': True},
        'direction': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'source_port_range': {'key': 'properties.sourcePortRange', 'type': 'str'},
        'destination_port_range': {'key': 'properties.destinationPortRange', 'type': 'str'},
        'source_address_prefix': {'key': 'properties.sourceAddressPrefix', 'type': 'str'},
        'source_address_prefixes': {'key': 'properties.sourceAddressPrefixes', 'type': '[str]'},
        'destination_address_prefix': {'key': 'properties.destinationAddressPrefix', 'type': 'str'},
        'destination_address_prefixes': {'key': 'properties.destinationAddressPrefixes', 'type': '[str]'},
        'source_port_ranges': {'key': 'properties.sourcePortRanges', 'type': '[str]'},
        'destination_port_ranges': {'key': 'properties.destinationPortRanges', 'type': '[str]'},
        'access': {'key': 'properties.access', 'type': 'str'},
        'priority': {'key': 'properties.priority', 'type': 'int'},
        'direction': {'key': 'properties.direction', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, protocol, access, direction, id: str=None, description: str=None, source_port_range: str=None, destination_port_range: str=None, source_address_prefix: str=None, source_address_prefixes=None, destination_address_prefix: str=None, destination_address_prefixes=None, source_port_ranges=None, destination_port_ranges=None, priority: int=None, provisioning_state: str=None, name: str=None, etag: str=None, **kwargs) -> None:
        super(SecurityRule, self).__init__(id=id, **kwargs)
        self.description = description
        self.protocol = protocol
        self.source_port_range = source_port_range
        self.destination_port_range = destination_port_range
        self.source_address_prefix = source_address_prefix
        self.source_address_prefixes = source_address_prefixes
        self.destination_address_prefix = destination_address_prefix
        self.destination_address_prefixes = destination_address_prefixes
        self.source_port_ranges = source_port_ranges
        self.destination_port_ranges = destination_port_ranges
        self.access = access
        self.priority = priority
        self.direction = direction
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
