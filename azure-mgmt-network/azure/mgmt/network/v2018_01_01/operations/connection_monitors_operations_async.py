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
from .connection_monitors_operations import ConnectionMonitorsOperations as _ConnectionMonitorsOperations


class ConnectionMonitorsOperations(_ConnectionMonitorsOperations):


    async def _create_or_update_initial_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, parameters, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create_or_update_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
            'connectionMonitorName': self._serialize.url("connection_monitor_name", connection_monitor_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        body_content = self._serialize.body(parameters, 'ConnectionMonitor')

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
            deserialized = self._deserialize('ConnectionMonitorResult', response)
        if response.status_code == 201:
            deserialized = self._deserialize('ConnectionMonitorResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def create_or_update_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, parameters, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Create or update a connection monitor.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param connection_monitor_name: The name of the connection monitor.
        :type connection_monitor_name: str
        :param parameters: Parameters that define the operation to create a
         connection monitor.
        :type parameters:
         ~azure.mgmt.network.v2018_01_01.models.ConnectionMonitor
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of ConnectionMonitorResult or
         ClientRawResponse<ConnectionMonitorResult> if raw==True
        :rtype:
         ~~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorResult or
         ~msrest.pipeline.ClientRawResponse[~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorResult]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._create_or_update_initial_async(
            resource_group_name=resource_group_name,
            network_watcher_name=network_watcher_name,
            connection_monitor_name=connection_monitor_name,
            parameters=parameters,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('ConnectionMonitorResult', response)

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
    create_or_update_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}'}

    async def get_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, **operation_config):
        """Gets a connection monitor by name.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param connection_monitor_name: The name of the connection monitor.
        :type connection_monitor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ConnectionMonitorResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorResult
         or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
            'connectionMonitorName': self._serialize.url("connection_monitor_name", connection_monitor_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
            deserialized = self._deserialize('ConnectionMonitorResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}'}


    async def _delete_initial_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
            'connectionMonitorName': self._serialize.url("connection_monitor_name", connection_monitor_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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

        if response.status_code not in [202, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    async def delete_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Deletes the specified connection monitor.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param connection_monitor_name: The name of the connection monitor.
        :type connection_monitor_name: str
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
            network_watcher_name=network_watcher_name,
            connection_monitor_name=connection_monitor_name,
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
    delete_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}'}


    async def _stop_initial_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.stop_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
            'connectionMonitorName': self._serialize.url("connection_monitor_name", connection_monitor_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    async def stop_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Stops the specified connection monitor.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param connection_monitor_name: The name of the connection monitor.
        :type connection_monitor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._stop_initial_async(
            resource_group_name=resource_group_name,
            network_watcher_name=network_watcher_name,
            connection_monitor_name=connection_monitor_name,
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
    stop_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/stop'}


    async def _start_initial_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.start_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
            'connectionMonitorName': self._serialize.url("connection_monitor_name", connection_monitor_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    async def start_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Starts the specified connection monitor.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param connection_monitor_name: The name of the connection monitor.
        :type connection_monitor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of None or ClientRawResponse<None> if raw==True
        :rtype: ~None or ~msrest.pipeline.ClientRawResponse[None]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._start_initial_async(
            resource_group_name=resource_group_name,
            network_watcher_name=network_watcher_name,
            connection_monitor_name=connection_monitor_name,
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
    start_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/start'}


    async def _query_initial_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.query_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
            'connectionMonitorName': self._serialize.url("connection_monitor_name", connection_monitor_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ConnectionMonitorQueryResult', response)
        if response.status_code == 202:
            deserialized = self._deserialize('ConnectionMonitorQueryResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def query_async(
            self, resource_group_name, network_watcher_name, connection_monitor_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Query a snapshot of the most recent connection states.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param connection_monitor_name: The name given to the connection
         monitor.
        :type connection_monitor_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of ConnectionMonitorQueryResult or
         ClientRawResponse<ConnectionMonitorQueryResult> if raw==True
        :rtype:
         ~~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorQueryResult
         or
         ~msrest.pipeline.ClientRawResponse[~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorQueryResult]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._query_initial_async(
            resource_group_name=resource_group_name,
            network_watcher_name=network_watcher_name,
            connection_monitor_name=connection_monitor_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('ConnectionMonitorQueryResult', response)

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
    query_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/query'}

    def list(
            self, resource_group_name, network_watcher_name, *, custom_headers=None, raw=False, **operation_config):
        """Lists all connection monitors for the specified Network Watcher.

        :param resource_group_name: The name of the resource group containing
         Network Watcher.
        :type resource_group_name: str
        :param network_watcher_name: The name of the Network Watcher resource.
        :type network_watcher_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ConnectionMonitorResult
        :rtype:
         ~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorResultPaged[~azure.mgmt.network.v2018_01_01.models.ConnectionMonitorResult]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'networkWatcherName': self._serialize.url("network_watcher_name", network_watcher_name, 'str'),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        deserialized = models.ConnectionMonitorResultPaged(
            internal_paging, self._deserialize.dependencies, header_dict, async_command=internal_paging_async)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors'}
