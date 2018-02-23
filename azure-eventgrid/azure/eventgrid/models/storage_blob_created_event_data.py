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


class StorageBlobCreatedEventData(Model):
    """Schema of the Data property of an EventGridEvent for an
    Microsoft.Storage.BlobCreated event.

    :param api: The name of the API/operation that triggered this event.
    :type api: str
    :param client_request_id: A request id provided by the client of the
     storage API operation that triggered this event.
    :type client_request_id: str
    :param request_id: The request id generated by the Storage service for the
     storage API operation that triggered this event.
    :type request_id: str
    :param e_tag: The etag of the object at the time this event was triggered.
    :type e_tag: str
    :param content_type: The content type of the blob. This is the same as
     what would be returned in the Content-Type header from the blob.
    :type content_type: str
    :param content_length: The size of the blob in bytes. This is the same as
     what would be returned in the Content-Length header from the blob.
    :type content_length: int
    :param blob_type: The type of blob.
    :type blob_type: str
    :param url: The path to the blob.
    :type url: str
    :param sequencer: An opaque string value representing the logical sequence
     of events for any particular blob name. Users can use standard string
     comparison to understand the relative sequence of two events on the same
     blob name.
    :type sequencer: str
    :param storage_diagnostics: For service use only. Diagnostic data
     occasionally included by the Azure Storage service. This property should
     be ignored by event consumers.
    :type storage_diagnostics: object
    """

    _attribute_map = {
        'api': {'key': 'api', 'type': 'str'},
        'client_request_id': {'key': 'clientRequestId', 'type': 'str'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'content_length': {'key': 'contentLength', 'type': 'int'},
        'blob_type': {'key': 'blobType', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'sequencer': {'key': 'sequencer', 'type': 'str'},
        'storage_diagnostics': {'key': 'storageDiagnostics', 'type': 'object'},
    }

    def __init__(self, api=None, client_request_id=None, request_id=None, e_tag=None, content_type=None, content_length=None, blob_type=None, url=None, sequencer=None, storage_diagnostics=None):
        super(StorageBlobCreatedEventData, self).__init__()
        self.api = api
        self.client_request_id = client_request_id
        self.request_id = request_id
        self.e_tag = e_tag
        self.content_type = content_type
        self.content_length = content_length
        self.blob_type = blob_type
        self.url = url
        self.sequencer = sequencer
        self.storage_diagnostics = storage_diagnostics