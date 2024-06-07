# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "providerhub notification-registration update",
)
class Update(AAZCommand):
    """Update a notification registration.
    """

    _aaz_info = {
        "version": "2024-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.providerhub/providerregistrations/{}/notificationregistrations/{}", "2024-04-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.notification_registration_name = AAZStrArg(
            options=["-n", "--name", "--notification-registration-name"],
            help="The notification registration.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.provider_namespace = AAZStrArg(
            options=["--provider-namespace"],
            help="The name of the resource provider hosted within ProviderHub.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.included_events = AAZListArg(
            options=["--included-events"],
            arg_group="Properties",
            help="These are the events that the RP should be messaged on. The message format is in the form {RP Namespace}/{ResourceType}/{action}. The available actions are: write, delete and move/action.",
            nullable=True,
        )
        _args_schema.message_scope = AAZStrArg(
            options=["--message-scope"],
            arg_group="Properties",
            help="Limits the messages that are sent to the RP. The default value is RegisteredSubscriptions. The available values are Global (all messages in Azure) and RegisteredSubscriptions (only messages in subscriptions registered by RP).",
            nullable=True,
            enum={"NotSpecified": "NotSpecified", "RegisteredSubscriptions": "RegisteredSubscriptions"},
        )
        _args_schema.notification_endpoints = AAZListArg(
            options=["--notification-endpoints"],
            arg_group="Properties",
            help="These are the locations for the notification messages. Notifications will be sent to the region of the event resource's location (e.g. VM in East Us will send message to the specified endpoint in East US).",
            nullable=True,
        )
        _args_schema.notification_mode = AAZStrArg(
            options=["--notification-mode"],
            arg_group="Properties",
            help="Determines how the notifications are sent to the RP. The two available modes are EventHub and Webhook.",
            nullable=True,
            enum={"EventHub": "EventHub", "NotSpecified": "NotSpecified", "WebHook": "WebHook"},
        )

        included_events = cls._args_schema.included_events
        included_events.Element = AAZStrArg(
            nullable=True,
        )

        notification_endpoints = cls._args_schema.notification_endpoints
        notification_endpoints.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.notification_endpoints.Element
        _element.locations = AAZListArg(
            options=["locations"],
            nullable=True,
        )
        _element.notification_destination = AAZStrArg(
            options=["notification-destination"],
            nullable=True,
        )

        locations = cls._args_schema.notification_endpoints.Element.locations
        locations.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NotificationRegistrationsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.NotificationRegistrationsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NotificationRegistrationsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/notificationRegistrations/{notificationRegistrationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "notificationRegistrationName", self.ctx.args.notification_registration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerNamespace", self.ctx.args.provider_namespace,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_notification_registration_read(cls._schema_on_200)

            return cls._schema_on_200

    class NotificationRegistrationsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/notificationRegistrations/{notificationRegistrationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "notificationRegistrationName", self.ctx.args.notification_registration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerNamespace", self.ctx.args.provider_namespace,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_notification_registration_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("includedEvents", AAZListType, ".included_events")
                properties.set_prop("messageScope", AAZStrType, ".message_scope")
                properties.set_prop("notificationEndpoints", AAZListType, ".notification_endpoints")
                properties.set_prop("notificationMode", AAZStrType, ".notification_mode")

            included_events = _builder.get(".properties.includedEvents")
            if included_events is not None:
                included_events.set_elements(AAZStrType, ".")

            notification_endpoints = _builder.get(".properties.notificationEndpoints")
            if notification_endpoints is not None:
                notification_endpoints.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.notificationEndpoints[]")
            if _elements is not None:
                _elements.set_prop("locations", AAZListType, ".locations")
                _elements.set_prop("notificationDestination", AAZStrType, ".notification_destination")

            locations = _builder.get(".properties.notificationEndpoints[].locations")
            if locations is not None:
                locations.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_notification_registration_read = None

    @classmethod
    def _build_schema_notification_registration_read(cls, _schema):
        if cls._schema_notification_registration_read is not None:
            _schema.id = cls._schema_notification_registration_read.id
            _schema.name = cls._schema_notification_registration_read.name
            _schema.properties = cls._schema_notification_registration_read.properties
            _schema.system_data = cls._schema_notification_registration_read.system_data
            _schema.type = cls._schema_notification_registration_read.type
            return

        cls._schema_notification_registration_read = _schema_notification_registration_read = AAZObjectType()

        notification_registration_read = _schema_notification_registration_read
        notification_registration_read.id = AAZStrType(
            flags={"read_only": True},
        )
        notification_registration_read.name = AAZStrType(
            flags={"read_only": True},
        )
        notification_registration_read.properties = AAZObjectType()
        notification_registration_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        notification_registration_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_notification_registration_read.properties
        properties.included_events = AAZListType(
            serialized_name="includedEvents",
        )
        properties.message_scope = AAZStrType(
            serialized_name="messageScope",
        )
        properties.notification_endpoints = AAZListType(
            serialized_name="notificationEndpoints",
        )
        properties.notification_mode = AAZStrType(
            serialized_name="notificationMode",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        included_events = _schema_notification_registration_read.properties.included_events
        included_events.Element = AAZStrType()

        notification_endpoints = _schema_notification_registration_read.properties.notification_endpoints
        notification_endpoints.Element = AAZObjectType()

        _element = _schema_notification_registration_read.properties.notification_endpoints.Element
        _element.locations = AAZListType()
        _element.notification_destination = AAZStrType(
            serialized_name="notificationDestination",
        )

        locations = _schema_notification_registration_read.properties.notification_endpoints.Element.locations
        locations.Element = AAZStrType()

        system_data = _schema_notification_registration_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_notification_registration_read.id
        _schema.name = cls._schema_notification_registration_read.name
        _schema.properties = cls._schema_notification_registration_read.properties
        _schema.system_data = cls._schema_notification_registration_read.system_data
        _schema.type = cls._schema_notification_registration_read.type


__all__ = ["Update"]
