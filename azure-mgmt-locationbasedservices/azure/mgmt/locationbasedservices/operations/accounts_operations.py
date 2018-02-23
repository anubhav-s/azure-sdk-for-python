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

from .. import models


class AccountsOperations(object):
    """AccountsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2017-01-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2017-01-01-preview"

        self.config = config

    def create_or_update(
            self, resource_group_name, account_name, location_based_services_account_create_parameters, custom_headers=None, raw=False, **operation_config):
        """Create or update a Location Based Services Account. A Location Based
        Services Account holds the keys which allow access to the Location
        Based Services REST APIs.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param account_name: The name of the Location Based Services Account.
        :type account_name: str
        :param location_based_services_account_create_parameters: The new or
         updated parameters for the Location Based Services Account.
        :type location_based_services_account_create_parameters:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccountCreateParameters
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LocationBasedServicesAccount or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccount
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str')
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
        body_content = self._serialize.body(location_based_services_account_create_parameters, 'LocationBasedServicesAccountCreateParameters')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LocationBasedServicesAccount', response)
        if response.status_code == 201:
            deserialized = self._deserialize('LocationBasedServicesAccount', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}'}

    def update(
            self, resource_group_name, account_name, tags=None, sku=None, custom_headers=None, raw=False, **operation_config):
        """Updates a Location Based Services Account. Only a subset of the
        parameters may be updated after creation, such as Sku and Tags.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param account_name: The name of the Location Based Services Account.
        :type account_name: str
        :param tags: Gets or sets a list of key value pairs that describe the
         resource. These tags can be used in viewing and grouping this resource
         (across resource groups). A maximum of 15 tags can be provided for a
         resource. Each tag must have a key no greater than 128 characters and
         value no greater than 256 characters.
        :type tags: dict[str, str]
        :param sku: The SKU of this account.
        :type sku: ~azure.mgmt.locationbasedservices.models.Sku
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LocationBasedServicesAccount or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccount
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        location_based_services_account_update_parameters = models.LocationBasedServicesAccountUpdateParameters(tags=tags, sku=sku)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str')
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
        body_content = self._serialize.body(location_based_services_account_update_parameters, 'LocationBasedServicesAccountUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LocationBasedServicesAccount', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}'}

    def delete(
            self, resource_group_name, account_name, custom_headers=None, raw=False, **operation_config):
        """Delete a Location Based Services Account.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param account_name: The name of the Location Based Services Account.
        :type account_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str')
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
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}'}

    def get(
            self, resource_group_name, account_name, custom_headers=None, raw=False, **operation_config):
        """Get a Location Based Services Account.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param account_name: The name of the Location Based Services Account.
        :type account_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LocationBasedServicesAccount or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccount
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str')
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
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LocationBasedServicesAccount', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}'}

    def list_by_resource_group(
            self, resource_group_name, custom_headers=None, raw=False, **operation_config):
        """Get all Location Based Services Accounts in a Resource Group.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of LocationBasedServicesAccount
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccountPaged[~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccount]
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str')
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
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.LocationBasedServicesAccountPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LocationBasedServicesAccountPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts'}

    def list_by_subscription(
            self, custom_headers=None, raw=False, **operation_config):
        """Get all Location Based Services Accounts in a Subscription.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of LocationBasedServicesAccount
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccountPaged[~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccount]
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']
                path_format_arguments = {
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
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.LocationBasedServicesAccountPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LocationBasedServicesAccountPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.LocationBasedServices/accounts'}

    def move(
            self, resource_group_name, target_resource_group, resource_ids, custom_headers=None, raw=False, **operation_config):
        """Moves Location Based Services Accounts from one ResourceGroup (or
        Subscription) to another.

        :param resource_group_name: The name of the resource group that
         contains Location Based Services Account to move.
        :type resource_group_name: str
        :param target_resource_group: The name of the destination resource
         group.
        :type target_resource_group: str
        :param resource_ids: A list of resource names to move from the source
         resource group.
        :type resource_ids: list[str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        move_request = models.LocationBasedServicesAccountsMoveRequest(target_resource_group=target_resource_group, resource_ids=resource_ids)

        # Construct URL
        url = self.move.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str')
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
        body_content = self._serialize.body(move_request, 'LocationBasedServicesAccountsMoveRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    move.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources'}

    def list_keys(
            self, resource_group_name, account_name, custom_headers=None, raw=False, **operation_config):
        """Get the keys to use with the Location Based Services APIs. A key is
        used to authenticate and authorize access to the Location Based
        Services REST APIs. Only one key is needed at a time; two are given to
        provide seamless key regeneration.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param account_name: The name of the Location Based Services Account.
        :type account_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LocationBasedServicesAccountKeys or ClientRawResponse if
         raw=true
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccountKeys
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        # Construct URL
        url = self.list_keys.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str')
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
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LocationBasedServicesAccountKeys', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}/listKeys'}

    def regenerate_keys(
            self, resource_group_name, account_name, key_type, custom_headers=None, raw=False, **operation_config):
        """Regenerate either the primary or secondary key for use with the
        Location Based Services APIs. The old key will stop working
        immediately.

        :param resource_group_name: The name of the Azure Resource Group.
        :type resource_group_name: str
        :param account_name: The name of the Location Based Services Account.
        :type account_name: str
        :param key_type: Whether the operation refers to the primary or
         secondary key. Possible values include: 'primary', 'secondary'
        :type key_type: str or
         ~azure.mgmt.locationbasedservices.models.KeyType
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LocationBasedServicesAccountKeys or ClientRawResponse if
         raw=true
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesAccountKeys
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        key_specification = models.LocationBasedServicesKeySpecification(key_type=key_type)

        # Construct URL
        url = self.regenerate_keys.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'accountName': self._serialize.url("account_name", account_name, 'str')
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
        body_content = self._serialize.body(key_specification, 'LocationBasedServicesKeySpecification')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 404]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LocationBasedServicesAccountKeys', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    regenerate_keys.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LocationBasedServices/accounts/{accountName}/regenerateKey'}

    def list_operations(
            self, custom_headers=None, raw=False, **operation_config):
        """List operations available for the Location Based Services Resource
        Provider.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of
         LocationBasedServicesOperationsValueItem
        :rtype:
         ~azure.mgmt.locationbasedservices.models.LocationBasedServicesOperationsValueItemPaged[~azure.mgmt.locationbasedservices.models.LocationBasedServicesOperationsValueItem]
        :raises:
         :class:`ErrorException<azure.mgmt.locationbasedservices.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_operations.metadata['url']

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
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.LocationBasedServicesOperationsValueItemPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.LocationBasedServicesOperationsValueItemPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_operations.metadata = {'url': '/providers/Microsoft.LocationBasedServices/operations'}
