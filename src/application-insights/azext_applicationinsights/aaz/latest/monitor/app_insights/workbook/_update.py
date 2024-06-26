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
    "monitor app-insights workbook update",
)
class Update(AAZCommand):
    """Update a workbook.

    :example: Update workbook
        az monitor app-insights workbook update -n 00000000-0000-0000-0000-000000000000 -g rg --tags tag=test
    """

    _aaz_info = {
        "version": "2023-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/workbooks/{}", "2023-06-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.resource_name = AAZStrArg(
            options=["-n", "--name", "--resource-name"],
            help="The name of the workbook resource. The value must be an UUID.",
            required=True,
            id_part="name",
        )
        _args_schema.source_id = AAZStrArg(
            options=["--source-id"],
            help="Azure Resource Id that will fetch all linked workbooks.",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.category = AAZStrArg(
            options=["--category"],
            arg_group="Properties",
            help="Workbook category, as defined by the user at creation time.",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="The description of the workbook.",
            nullable=True,
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="The user-defined name (display name) of the workbook.",
        )
        _args_schema.serialized_data = AAZStrArg(
            options=["--serialized-data"],
            arg_group="Properties",
            help="Configuration of this particular workbook. Configuration data is a string containing valid JSON",
            nullable=True,
        )
        _args_schema.storage_uri = AAZStrArg(
            options=["--storage-uri"],
            arg_group="Properties",
            help="The resourceId to the storage account when bring your own storage is used",
            nullable=True,
        )
        _args_schema.version = AAZStrArg(
            options=["--version"],
            arg_group="Properties",
            help="Workbook schema version format, like 'Notebook/1.0', which should match the workbook in serializedData",
            nullable=True,
        )

        # define Arg Group "WorkbookProperties"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="WorkbookProperties",
            help="Identity used for BYOS",
            nullable=True,
        )
        _args_schema.kind = AAZStrArg(
            options=["--kind"],
            arg_group="WorkbookProperties",
            help="The kind of workbook. Only valid value is shared.",
            nullable=True,
            enum={"shared": "shared"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="WorkbookProperties",
            help="Resource tags.",
            nullable=True,
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned,UserAssigned": "SystemAssigned,UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
            nullable=True,
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WorkbooksGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.WorkbooksCreateOrUpdate(ctx=self.ctx)()
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

    class WorkbooksGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
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
                    "api-version", "2023-06-01",
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
            _UpdateHelper._build_schema_workbook_read(cls._schema_on_200)

            return cls._schema_on_200

    class WorkbooksCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/workbooks/{resourceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
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
                    "sourceId", self.ctx.args.source_id,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-06-01",
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

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_workbook_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("kind", AAZStrType, ".kind")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("category", AAZStrType, ".category", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("description", AAZStrType, ".description", typ_kwargs={"nullable": True})
                properties.set_prop("displayName", AAZStrType, ".display_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("serializedData", AAZStrType, ".serialized_data", typ_kwargs={"flags": {"required": True}, "nullable": True})
                properties.set_prop("storageUri", AAZStrType, ".storage_uri", typ_kwargs={"nullable": True})
                properties.set_prop("version", AAZStrType, ".version")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_workbook_read = None

    @classmethod
    def _build_schema_workbook_read(cls, _schema):
        if cls._schema_workbook_read is not None:
            _schema.etag = cls._schema_workbook_read.etag
            _schema.id = cls._schema_workbook_read.id
            _schema.identity = cls._schema_workbook_read.identity
            _schema.kind = cls._schema_workbook_read.kind
            _schema.location = cls._schema_workbook_read.location
            _schema.name = cls._schema_workbook_read.name
            _schema.properties = cls._schema_workbook_read.properties
            _schema.system_data = cls._schema_workbook_read.system_data
            _schema.tags = cls._schema_workbook_read.tags
            _schema.type = cls._schema_workbook_read.type
            return

        cls._schema_workbook_read = _schema_workbook_read = AAZObjectType()

        workbook_read = _schema_workbook_read
        workbook_read.etag = AAZStrType()
        workbook_read.id = AAZStrType(
            flags={"read_only": True},
        )
        workbook_read.identity = AAZObjectType()
        workbook_read.kind = AAZStrType()
        workbook_read.location = AAZStrType(
            flags={"required": True},
        )
        workbook_read.name = AAZStrType(
            flags={"read_only": True},
        )
        workbook_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        workbook_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        workbook_read.tags = AAZDictType()
        workbook_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_workbook_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_workbook_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_workbook_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_workbook_read.properties
        properties.category = AAZStrType(
            flags={"required": True},
        )
        properties.description = AAZStrType(
            nullable=True,
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
            flags={"required": True},
        )
        properties.revision = AAZStrType(
            nullable=True,
            flags={"read_only": True},
        )
        properties.serialized_data = AAZStrType(
            serialized_name="serializedData",
            flags={"required": True},
            nullable=True,
        )
        properties.storage_uri = AAZStrType(
            serialized_name="storageUri",
            nullable=True,
        )
        properties.time_modified = AAZStrType(
            serialized_name="timeModified",
            flags={"read_only": True},
        )
        properties.user_id = AAZStrType(
            serialized_name="userId",
            flags={"read_only": True},
        )
        properties.version = AAZStrType()

        system_data = _schema_workbook_read.system_data
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

        tags = _schema_workbook_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_workbook_read.etag
        _schema.id = cls._schema_workbook_read.id
        _schema.identity = cls._schema_workbook_read.identity
        _schema.kind = cls._schema_workbook_read.kind
        _schema.location = cls._schema_workbook_read.location
        _schema.name = cls._schema_workbook_read.name
        _schema.properties = cls._schema_workbook_read.properties
        _schema.system_data = cls._schema_workbook_read.system_data
        _schema.tags = cls._schema_workbook_read.tags
        _schema.type = cls._schema_workbook_read.type


__all__ = ["Update"]
