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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling.async_poller import async_poller, AsyncNoPolling
from msrestazure.polling.async_arm_polling import AsyncARMPolling

from .. import models
from .public_ip_addresses_operations import PublicIPAddressesOperations as _PublicIPAddressesOperations


class PublicIPAddressesOperations(_PublicIPAddressesOperations):


    async def _delete_initial_async(
            self, resource_group_name, public_ip_address_name, *, custom_headers=None, raw=False, **operation_config):
        api_version = "2017-11-01"

        # Construct URL
        url = self.delete_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'publicIpAddressName': self._serialize.url("public_ip_address_name", public_ip_address_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    async def delete_async(
            self, resource_group_name, public_ip_address_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes the specified public IP address.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the subnet.
        :type public_ip_address_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._delete_initial_async(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    delete_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}'}

    async def get_async(
            self, resource_group_name, public_ip_address_name, expand=None, *, custom_headers=None, raw=False, **operation_config):
        """Gets the specified public IP address in a specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the subnet.
        :type public_ip_address_name: str
        :param expand: Expands referenced resources.
        :type expand: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PublicIPAddress or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.network.v2017_11_01.models.PublicIPAddress or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2017-11-01"

        # Construct URL
        url = self.get_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'publicIpAddressName': self._serialize.url("public_ip_address_name", public_ip_address_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PublicIPAddress', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}'}


    async def _create_or_update_initial_async(
            self, resource_group_name, public_ip_address_name, parameters, *, custom_headers=None, raw=False, **operation_config):
        api_version = "2017-11-01"

        # Construct URL
        url = self.create_or_update_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'publicIpAddressName': self._serialize.url("public_ip_address_name", public_ip_address_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'PublicIPAddress')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PublicIPAddress', response)
        if response.status_code == 201:
            deserialized = self._deserialize('PublicIPAddress', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def create_or_update_async(
            self, resource_group_name, public_ip_address_name, parameters, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Creates or updates a static or dynamic public IP address.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the public IP address.
        :type public_ip_address_name: str
        :param parameters: Parameters supplied to the create or update public
         IP address operation.
        :type parameters:
         ~azure.mgmt.network.v2017_11_01.models.PublicIPAddress
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of PublicIPAddress or
         ClientRawResponse<PublicIPAddress> if raw==True
        :rtype: ~~azure.mgmt.network.v2017_11_01.models.PublicIPAddress or
         ~msrest.pipeline.ClientRawResponse[~azure.mgmt.network.v2017_11_01.models.PublicIPAddress]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._create_or_update_initial_async(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
            parameters=parameters,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('PublicIPAddress', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}'}


    async def _update_tags_initial_async(
            self, resource_group_name, public_ip_address_name, tags=None, *, custom_headers=None, raw=False, **operation_config):
        parameters = models.TagsObject(tags=tags)

        api_version = "2017-11-01"

        # Construct URL
        url = self.update_tags_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'publicIpAddressName': self._serialize.url("public_ip_address_name", public_ip_address_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'TagsObject')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PublicIPAddress', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def update_tags_async(
            self, resource_group_name, public_ip_address_name, tags=None, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Updates public IP address tags.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the public IP address.
        :type public_ip_address_name: str
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of PublicIPAddress or
         ClientRawResponse<PublicIPAddress> if raw==True
        :rtype: ~~azure.mgmt.network.v2017_11_01.models.PublicIPAddress or
         ~msrest.pipeline.ClientRawResponse[~azure.mgmt.network.v2017_11_01.models.PublicIPAddress]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._update_tags_initial_async(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
            tags=tags,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('PublicIPAddress', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    update_tags_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}'}

    def list_all(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Gets all the public IP addresses in a subscription.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PublicIPAddress
        :rtype:
         ~azure.mgmt.network.v2017_11_01.models.PublicIPAddressPaged[~azure.mgmt.network.v2017_11_01.models.PublicIPAddress]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2017-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_all.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            return request, header_parameters

        def internal_paging(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        async def internal_paging_async(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = await self._client.async_send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PublicIPAddressPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list_all.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Network/publicIPAddresses'}

    def list(
            self, resource_group_name, *, custom_headers=None, raw=False, **operation_config):
        """Gets all public IP addresses in a resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PublicIPAddress
        :rtype:
         ~azure.mgmt.network.v2017_11_01.models.PublicIPAddressPaged[~azure.mgmt.network.v2017_11_01.models.PublicIPAddress]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2017-11-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            return request, header_parameters

        def internal_paging(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        async def internal_paging_async(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = await self._client.async_send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PublicIPAddressPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses'}

    def list_virtual_machine_scale_set_public_ip_addresses(
            self, resource_group_name, virtual_machine_scale_set_name, *, custom_headers=None, raw=False, **operation_config):
        """Gets information about all public IP addresses on a virtual machine
        scale set level.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_machine_scale_set_name: The name of the virtual machine
         scale set.
        :type virtual_machine_scale_set_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PublicIPAddress
        :rtype:
         ~azure.mgmt.network.v2017_11_01.models.PublicIPAddressPaged[~azure.mgmt.network.v2017_11_01.models.PublicIPAddress]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2017-03-30"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_virtual_machine_scale_set_public_ip_addresses.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'virtualMachineScaleSetName': self._serialize.url("virtual_machine_scale_set_name", virtual_machine_scale_set_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            return request, header_parameters

        def internal_paging(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        async def internal_paging_async(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = await self._client.async_send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PublicIPAddressPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list_virtual_machine_scale_set_public_ip_addresses.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/publicipaddresses'}

    def list_virtual_machine_scale_set_vm_public_ip_addresses(
            self, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, ip_configuration_name, *, custom_headers=None, raw=False, **operation_config):
        """Gets information about all public IP addresses in a virtual machine IP
        configuration in a virtual machine scale set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_machine_scale_set_name: The name of the virtual machine
         scale set.
        :type virtual_machine_scale_set_name: str
        :param virtualmachine_index: The virtual machine index.
        :type virtualmachine_index: str
        :param network_interface_name: The network interface name.
        :type network_interface_name: str
        :param ip_configuration_name: The IP configuration name.
        :type ip_configuration_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of PublicIPAddress
        :rtype:
         ~azure.mgmt.network.v2017_11_01.models.PublicIPAddressPaged[~azure.mgmt.network.v2017_11_01.models.PublicIPAddress]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2017-03-30"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_virtual_machine_scale_set_vm_public_ip_addresses.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'virtualMachineScaleSetName': self._serialize.url("virtual_machine_scale_set_name", virtual_machine_scale_set_name, 'str'),
                    'virtualmachineIndex': self._serialize.url("virtualmachine_index", virtualmachine_index, 'str'),
                    'networkInterfaceName': self._serialize.url("network_interface_name", network_interface_name, 'str'),
                    'ipConfigurationName': self._serialize.url("ip_configuration_name", ip_configuration_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            return request, header_parameters

        def internal_paging(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        async def internal_paging_async(next_link=None):
            request, header_parameters = prepare_request(next_link)

            response = await self._client.async_send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.PublicIPAddressPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list_virtual_machine_scale_set_vm_public_ip_addresses.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses'}

    async def get_virtual_machine_scale_set_public_ip_address_async(
            self, resource_group_name, virtual_machine_scale_set_name, virtualmachine_index, network_interface_name, ip_configuration_name, public_ip_address_name, expand=None, *, custom_headers=None, raw=False, **operation_config):
        """Get the specified public IP address in a virtual machine scale set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_machine_scale_set_name: The name of the virtual machine
         scale set.
        :type virtual_machine_scale_set_name: str
        :param virtualmachine_index: The virtual machine index.
        :type virtualmachine_index: str
        :param network_interface_name: The name of the network interface.
        :type network_interface_name: str
        :param ip_configuration_name: The name of the IP configuration.
        :type ip_configuration_name: str
        :param public_ip_address_name: The name of the public IP Address.
        :type public_ip_address_name: str
        :param expand: Expands referenced resources.
        :type expand: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: PublicIPAddress or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.network.v2017_11_01.models.PublicIPAddress or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = "2017-03-30"

        # Construct URL
        url = self.get_virtual_machine_scale_set_public_ip_address_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'virtualMachineScaleSetName': self._serialize.url("virtual_machine_scale_set_name", virtual_machine_scale_set_name, 'str'),
            'virtualmachineIndex': self._serialize.url("virtualmachine_index", virtualmachine_index, 'str'),
            'networkInterfaceName': self._serialize.url("network_interface_name", network_interface_name, 'str'),
            'ipConfigurationName': self._serialize.url("ip_configuration_name", ip_configuration_name, 'str'),
            'publicIpAddressName': self._serialize.url("public_ip_address_name", public_ip_address_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('PublicIPAddress', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_virtual_machine_scale_set_public_ip_address_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses/{publicIpAddressName}'}
