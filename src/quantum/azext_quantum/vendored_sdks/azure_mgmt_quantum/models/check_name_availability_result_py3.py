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


class CheckNameAvailabilityResult(Model):
    """Result of check name availability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name_available: Indicator of availability of the Quantum Workspace
     resource name.
    :type name_available: bool
    :param reason: The reason of unavailability.
    :type reason: str
    :ivar message: The detailed info regarding the reason associated with the
     Namespace.
    :vartype message: str
    """

    _validation = {
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, name_available: bool=None, reason: str=None, **kwargs) -> None:
        super(CheckNameAvailabilityResult, self).__init__(**kwargs)
        self.name_available = name_available
        self.reason = reason
        self.message = None