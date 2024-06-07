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
    "providerhub sku update",
)
class Update(AAZCommand):
    """Update the resource type skus in the given resource type.
    """

    _aaz_info = {
        "version": "2024-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.providerhub/providerregistrations/{}/resourcetyperegistrations/{}/skus/{}", "2024-04-01-preview"],
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
            id_part="child_name_2",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.sku_settings = AAZListArg(
            options=["--sku-settings"],
            arg_group="Properties",
        )

        sku_settings = cls._args_schema.sku_settings
        sku_settings.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.sku_settings.Element
        _element.capabilities = AAZListArg(
            options=["capabilities"],
            nullable=True,
        )
        _element.capacity = AAZObjectArg(
            options=["capacity"],
            nullable=True,
        )
        _element.costs = AAZListArg(
            options=["costs"],
            nullable=True,
        )
        _element.family = AAZStrArg(
            options=["family"],
            nullable=True,
        )
        _element.kind = AAZStrArg(
            options=["kind"],
            nullable=True,
        )
        _element.location_info = AAZListArg(
            options=["location-info"],
            nullable=True,
        )
        _element.locations = AAZListArg(
            options=["locations"],
            nullable=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
        )
        _element.required_features = AAZListArg(
            options=["required-features"],
            nullable=True,
        )
        _element.required_quota_ids = AAZListArg(
            options=["required-quota-ids"],
            nullable=True,
        )
        _element.size = AAZStrArg(
            options=["size"],
            nullable=True,
        )
        _element.tier = AAZStrArg(
            options=["tier"],
            nullable=True,
        )

        capabilities = cls._args_schema.sku_settings.Element.capabilities
        capabilities.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_sku_capability_update(capabilities.Element)

        capacity = cls._args_schema.sku_settings.Element.capacity
        capacity.default = AAZIntArg(
            options=["default"],
            nullable=True,
        )
        capacity.maximum = AAZIntArg(
            options=["maximum"],
            nullable=True,
        )
        capacity.minimum = AAZIntArg(
            options=["minimum"],
        )
        capacity.scale_type = AAZStrArg(
            options=["scale-type"],
            nullable=True,
            enum={"Automatic": "Automatic", "Manual": "Manual", "None": "None"},
        )

        costs = cls._args_schema.sku_settings.Element.costs
        costs.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.sku_settings.Element.costs.Element
        _element.extended_unit = AAZStrArg(
            options=["extended-unit"],
            nullable=True,
        )
        _element.meter_id = AAZStrArg(
            options=["meter-id"],
        )
        _element.quantity = AAZIntArg(
            options=["quantity"],
            nullable=True,
        )

        location_info = cls._args_schema.sku_settings.Element.location_info
        location_info.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.sku_settings.Element.location_info.Element
        _element.extended_locations = AAZListArg(
            options=["extended-locations"],
            nullable=True,
        )
        _element.location = AAZStrArg(
            options=["location"],
        )
        _element.type = AAZStrArg(
            options=["type"],
            nullable=True,
            enum={"ArcZone": "ArcZone", "EdgeZone": "EdgeZone", "NotSpecified": "NotSpecified"},
        )
        _element.zone_details = AAZListArg(
            options=["zone-details"],
            nullable=True,
        )
        _element.zones = AAZListArg(
            options=["zones"],
            nullable=True,
        )

        extended_locations = cls._args_schema.sku_settings.Element.location_info.Element.extended_locations
        extended_locations.Element = AAZStrArg(
            nullable=True,
        )

        zone_details = cls._args_schema.sku_settings.Element.location_info.Element.zone_details
        zone_details.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.sku_settings.Element.location_info.Element.zone_details.Element
        _element.capabilities = AAZListArg(
            options=["capabilities"],
            nullable=True,
        )
        _element.name = AAZListArg(
            options=["name"],
            nullable=True,
        )

        capabilities = cls._args_schema.sku_settings.Element.location_info.Element.zone_details.Element.capabilities
        capabilities.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_sku_capability_update(capabilities.Element)

        name = cls._args_schema.sku_settings.Element.location_info.Element.zone_details.Element.name
        name.Element = AAZStrArg(
            nullable=True,
        )

        zones = cls._args_schema.sku_settings.Element.location_info.Element.zones
        zones.Element = AAZStrArg(
            nullable=True,
        )

        locations = cls._args_schema.sku_settings.Element.locations
        locations.Element = AAZStrArg(
            nullable=True,
        )

        required_features = cls._args_schema.sku_settings.Element.required_features
        required_features.Element = AAZStrArg(
            nullable=True,
        )

        required_quota_ids = cls._args_schema.sku_settings.Element.required_quota_ids
        required_quota_ids.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    _args_sku_capability_update = None

    @classmethod
    def _build_args_sku_capability_update(cls, _schema):
        if cls._args_sku_capability_update is not None:
            _schema.name = cls._args_sku_capability_update.name
            _schema.value = cls._args_sku_capability_update.value
            return

        cls._args_sku_capability_update = AAZObjectArg(
            nullable=True,
        )

        sku_capability_update = cls._args_sku_capability_update
        sku_capability_update.name = AAZStrArg(
            options=["name"],
        )
        sku_capability_update.value = AAZStrArg(
            options=["value"],
        )

        _schema.name = cls._args_sku_capability_update.name
        _schema.value = cls._args_sku_capability_update.value

    def _execute_operations(self):
        self.pre_operations()
        self.SkusGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.SkusCreateOrUpdate(ctx=self.ctx)()
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

    class SkusGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/{resourceType}/skus/{sku}",
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
            _UpdateHelper._build_schema_sku_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class SkusCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/{resourceType}/skus/{sku}",
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
            _UpdateHelper._build_schema_sku_resource_read(cls._schema_on_200)

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
                properties.set_prop("skuSettings", AAZListType, ".sku_settings", typ_kwargs={"flags": {"required": True}})

            sku_settings = _builder.get(".properties.skuSettings")
            if sku_settings is not None:
                sku_settings.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[]")
            if _elements is not None:
                _elements.set_prop("capabilities", AAZListType, ".capabilities")
                _elements.set_prop("capacity", AAZObjectType, ".capacity")
                _elements.set_prop("costs", AAZListType, ".costs")
                _elements.set_prop("family", AAZStrType, ".family")
                _elements.set_prop("kind", AAZStrType, ".kind")
                _elements.set_prop("locationInfo", AAZListType, ".location_info")
                _elements.set_prop("locations", AAZListType, ".locations")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("requiredFeatures", AAZListType, ".required_features")
                _elements.set_prop("requiredQuotaIds", AAZListType, ".required_quota_ids")
                _elements.set_prop("size", AAZStrType, ".size")
                _elements.set_prop("tier", AAZStrType, ".tier")

            capabilities = _builder.get(".properties.skuSettings[].capabilities")
            if capabilities is not None:
                _UpdateHelper._build_schema_sku_capability_update(capabilities.set_elements(AAZObjectType, "."))

            capacity = _builder.get(".properties.skuSettings[].capacity")
            if capacity is not None:
                capacity.set_prop("default", AAZIntType, ".default")
                capacity.set_prop("maximum", AAZIntType, ".maximum")
                capacity.set_prop("minimum", AAZIntType, ".minimum", typ_kwargs={"flags": {"required": True}})
                capacity.set_prop("scaleType", AAZStrType, ".scale_type")

            costs = _builder.get(".properties.skuSettings[].costs")
            if costs is not None:
                costs.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[].costs[]")
            if _elements is not None:
                _elements.set_prop("extendedUnit", AAZStrType, ".extended_unit")
                _elements.set_prop("meterId", AAZStrType, ".meter_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("quantity", AAZIntType, ".quantity")

            location_info = _builder.get(".properties.skuSettings[].locationInfo")
            if location_info is not None:
                location_info.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[].locationInfo[]")
            if _elements is not None:
                _elements.set_prop("extendedLocations", AAZListType, ".extended_locations")
                _elements.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("type", AAZStrType, ".type")
                _elements.set_prop("zoneDetails", AAZListType, ".zone_details")
                _elements.set_prop("zones", AAZListType, ".zones")

            extended_locations = _builder.get(".properties.skuSettings[].locationInfo[].extendedLocations")
            if extended_locations is not None:
                extended_locations.set_elements(AAZStrType, ".")

            zone_details = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails")
            if zone_details is not None:
                zone_details.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails[]")
            if _elements is not None:
                _elements.set_prop("capabilities", AAZListType, ".capabilities")
                _elements.set_prop("name", AAZListType, ".name")

            capabilities = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails[].capabilities")
            if capabilities is not None:
                _UpdateHelper._build_schema_sku_capability_update(capabilities.set_elements(AAZObjectType, "."))

            name = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails[].name")
            if name is not None:
                name.set_elements(AAZStrType, ".")

            zones = _builder.get(".properties.skuSettings[].locationInfo[].zones")
            if zones is not None:
                zones.set_elements(AAZStrType, ".")

            locations = _builder.get(".properties.skuSettings[].locations")
            if locations is not None:
                locations.set_elements(AAZStrType, ".")

            required_features = _builder.get(".properties.skuSettings[].requiredFeatures")
            if required_features is not None:
                required_features.set_elements(AAZStrType, ".")

            required_quota_ids = _builder.get(".properties.skuSettings[].requiredQuotaIds")
            if required_quota_ids is not None:
                required_quota_ids.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sku_capability_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

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

    _schema_sku_resource_read = None

    @classmethod
    def _build_schema_sku_resource_read(cls, _schema):
        if cls._schema_sku_resource_read is not None:
            _schema.id = cls._schema_sku_resource_read.id
            _schema.name = cls._schema_sku_resource_read.name
            _schema.properties = cls._schema_sku_resource_read.properties
            _schema.system_data = cls._schema_sku_resource_read.system_data
            _schema.type = cls._schema_sku_resource_read.type
            return

        cls._schema_sku_resource_read = _schema_sku_resource_read = AAZObjectType()

        sku_resource_read = _schema_sku_resource_read
        sku_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sku_resource_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sku_resource_read.properties = AAZObjectType()
        sku_resource_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        sku_resource_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sku_resource_read.properties
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.sku_settings = AAZListType(
            serialized_name="skuSettings",
            flags={"required": True},
        )

        sku_settings = _schema_sku_resource_read.properties.sku_settings
        sku_settings.Element = AAZObjectType()

        _element = _schema_sku_resource_read.properties.sku_settings.Element
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

        capabilities = _schema_sku_resource_read.properties.sku_settings.Element.capabilities
        capabilities.Element = AAZObjectType()
        cls._build_schema_sku_capability_read(capabilities.Element)

        capacity = _schema_sku_resource_read.properties.sku_settings.Element.capacity
        capacity.default = AAZIntType()
        capacity.maximum = AAZIntType()
        capacity.minimum = AAZIntType(
            flags={"required": True},
        )
        capacity.scale_type = AAZStrType(
            serialized_name="scaleType",
        )

        costs = _schema_sku_resource_read.properties.sku_settings.Element.costs
        costs.Element = AAZObjectType()

        _element = _schema_sku_resource_read.properties.sku_settings.Element.costs.Element
        _element.extended_unit = AAZStrType(
            serialized_name="extendedUnit",
        )
        _element.meter_id = AAZStrType(
            serialized_name="meterId",
            flags={"required": True},
        )
        _element.quantity = AAZIntType()

        location_info = _schema_sku_resource_read.properties.sku_settings.Element.location_info
        location_info.Element = AAZObjectType()

        _element = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element
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

        extended_locations = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element.extended_locations
        extended_locations.Element = AAZStrType()

        zone_details = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element.zone_details
        zone_details.Element = AAZObjectType()

        _element = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element.zone_details.Element
        _element.capabilities = AAZListType()
        _element.name = AAZListType()

        capabilities = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element.zone_details.Element.capabilities
        capabilities.Element = AAZObjectType()
        cls._build_schema_sku_capability_read(capabilities.Element)

        name = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element.zone_details.Element.name
        name.Element = AAZStrType()

        zones = _schema_sku_resource_read.properties.sku_settings.Element.location_info.Element.zones
        zones.Element = AAZStrType()

        locations = _schema_sku_resource_read.properties.sku_settings.Element.locations
        locations.Element = AAZStrType()

        required_features = _schema_sku_resource_read.properties.sku_settings.Element.required_features
        required_features.Element = AAZStrType()

        required_quota_ids = _schema_sku_resource_read.properties.sku_settings.Element.required_quota_ids
        required_quota_ids.Element = AAZStrType()

        system_data = _schema_sku_resource_read.system_data
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

        _schema.id = cls._schema_sku_resource_read.id
        _schema.name = cls._schema_sku_resource_read.name
        _schema.properties = cls._schema_sku_resource_read.properties
        _schema.system_data = cls._schema_sku_resource_read.system_data
        _schema.type = cls._schema_sku_resource_read.type


__all__ = ["Update"]
