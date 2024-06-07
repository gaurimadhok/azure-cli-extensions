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
    "providerhub sku nested-resource-type-first show",
)
class Show(AAZCommand):
    """Get the sku details for the given resource type and sku name.
    """

    _aaz_info = {
        "version": "2024-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.providerhub/providerregistrations/{}/resourcetyperegistrations/{}/resourcetyperegistrations/{}/skus/{}", "2024-04-01-preview"],
        ]
    }

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
        _args_schema.nested_resource_type_first = AAZStrArg(
            options=["--nested-resource-type-first"],
            help="The first child resource type.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.provider_namespace = AAZStrArg(
            options=["--provider-namespace"],
            help="The name of the resource provider hosted within ProviderHub.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_type = AAZStrArg(
            options=["--resource-type"],
            help="The resource type.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--sku", "--name"],
            help="The SKU.",
            required=True,
            id_part="child_name_3",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SkusGetNestedResourceTypeFirst(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SkusGetNestedResourceTypeFirst(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/{resourceType}/resourcetypeRegistrations/{nestedResourceTypeFirst}/skus/{sku}",
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
                    "nestedResourceTypeFirst", self.ctx.args.nested_resource_type_first,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerNamespace", self.ctx.args.provider_namespace,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceType", self.ctx.args.resource_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "sku", self.ctx.args.name,
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sku_settings = AAZListType(
                serialized_name="skuSettings",
                flags={"required": True},
            )

            sku_settings = cls._schema_on_200.properties.sku_settings
            sku_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element
            _element.capabilities = AAZListType()
            _element.capacity = AAZObjectType()
            _element.costs = AAZListType()
            _element.family = AAZStrType()
            _element.kind = AAZStrType()
            _element.location_info = AAZListType(
                serialized_name="locationInfo",
            )
            _element.locations = AAZListType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.required_features = AAZListType(
                serialized_name="requiredFeatures",
            )
            _element.required_quota_ids = AAZListType(
                serialized_name="requiredQuotaIds",
            )
            _element.size = AAZStrType()
            _element.tier = AAZStrType()

            capabilities = cls._schema_on_200.properties.sku_settings.Element.capabilities
            capabilities.Element = AAZObjectType()
            _ShowHelper._build_schema_sku_capability_read(capabilities.Element)

            capacity = cls._schema_on_200.properties.sku_settings.Element.capacity
            capacity.default = AAZIntType()
            capacity.maximum = AAZIntType()
            capacity.minimum = AAZIntType(
                flags={"required": True},
            )
            capacity.scale_type = AAZStrType(
                serialized_name="scaleType",
            )

            costs = cls._schema_on_200.properties.sku_settings.Element.costs
            costs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element.costs.Element
            _element.extended_unit = AAZStrType(
                serialized_name="extendedUnit",
            )
            _element.meter_id = AAZStrType(
                serialized_name="meterId",
                flags={"required": True},
            )
            _element.quantity = AAZIntType()

            location_info = cls._schema_on_200.properties.sku_settings.Element.location_info
            location_info.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element.location_info.Element
            _element.extended_locations = AAZListType(
                serialized_name="extendedLocations",
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.type = AAZStrType()
            _element.zone_details = AAZListType(
                serialized_name="zoneDetails",
            )
            _element.zones = AAZListType()

            extended_locations = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.extended_locations
            extended_locations.Element = AAZStrType()

            zone_details = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details
            zone_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details.Element
            _element.capabilities = AAZListType()
            _element.name = AAZListType()

            capabilities = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details.Element.capabilities
            capabilities.Element = AAZObjectType()
            _ShowHelper._build_schema_sku_capability_read(capabilities.Element)

            name = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details.Element.name
            name.Element = AAZStrType()

            zones = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zones
            zones.Element = AAZStrType()

            locations = cls._schema_on_200.properties.sku_settings.Element.locations
            locations.Element = AAZStrType()

            required_features = cls._schema_on_200.properties.sku_settings.Element.required_features
            required_features.Element = AAZStrType()

            required_quota_ids = cls._schema_on_200.properties.sku_settings.Element.required_quota_ids
            required_quota_ids.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_sku_capability_read = None

    @classmethod
    def _build_schema_sku_capability_read(cls, _schema):
        if cls._schema_sku_capability_read is not None:
            _schema.name = cls._schema_sku_capability_read.name
            _schema.value = cls._schema_sku_capability_read.value
            return

        cls._schema_sku_capability_read = _schema_sku_capability_read = AAZObjectType()

        sku_capability_read = _schema_sku_capability_read
        sku_capability_read.name = AAZStrType(
            flags={"required": True},
        )
        sku_capability_read.value = AAZStrType(
            flags={"required": True},
        )

        _schema.name = cls._schema_sku_capability_read.name
        _schema.value = cls._schema_sku_capability_read.value


__all__ = ["Show"]
