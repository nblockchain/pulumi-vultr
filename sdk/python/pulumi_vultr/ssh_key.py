# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SshKeyArgs', 'SshKey']

@pulumi.input_type
class SshKeyArgs:
    def __init__(__self__, *,
                 ssh_key: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SshKey resource.
        :param pulumi.Input[str] ssh_key: The public SSH key.
        :param pulumi.Input[str] name: The name/label of the SSH key.
        """
        pulumi.set(__self__, "ssh_key", ssh_key)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> pulumi.Input[str]:
        """
        The public SSH key.
        """
        return pulumi.get(self, "ssh_key")

    @ssh_key.setter
    def ssh_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "ssh_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name/label of the SSH key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SshKeyState:
    def __init__(__self__, *,
                 date_created: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SshKey resources.
        :param pulumi.Input[str] date_created: The date the SSH key was added to your Vultr account.
        :param pulumi.Input[str] name: The name/label of the SSH key.
        :param pulumi.Input[str] ssh_key: The public SSH key.
        """
        if date_created is not None:
            pulumi.set(__self__, "date_created", date_created)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ssh_key is not None:
            pulumi.set(__self__, "ssh_key", ssh_key)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date the SSH key was added to your Vultr account.
        """
        return pulumi.get(self, "date_created")

    @date_created.setter
    def date_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "date_created", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name/label of the SSH key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[pulumi.Input[str]]:
        """
        The public SSH key.
        """
        return pulumi.get(self, "ssh_key")

    @ssh_key.setter
    def ssh_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_key", value)


class SshKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Vultr SSH key resource. This can be used to create, read, modify, and delete SSH keys.

        ## Example Usage

        Create an SSH key

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_ssh_key = vultr.SshKey("mySshKey", ssh_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyVGaw1PuEl98f4/7Kq3O9ZIvDw2OFOSXAFVqilSFNkHlefm1iMtPeqsIBp2t9cbGUf55xNDULz/bD/4BCV43yZ5lh0cUYuXALg9NI29ui7PEGReXjSpNwUD6ceN/78YOK41KAcecq+SS0bJ4b4amKZIJG3JWmDKljtv1dmSBCrTmEAQaOorxqGGBYmZS7NQumRe4lav5r6wOs8OACMANE1ejkeZsGFzJFNqvr5DuHdDL5FAudW23me3BDmrM9ifUzzjl1Jwku3bnRaCcjaxH8oTumt1a00mWci/1qUlaVFft085yvVq7KZbF2OPPbl+erDW91+EZ2FgEi+v1/CSJ5 your_username@hostname")
        ```

        ## Import

        SSH keys can be imported using the SSH key `ID`, e.g.

        ```sh
         $ pulumi import vultr:index/sshKey:SshKey my_key 6b0876a7-f709-41ba-aed8-abed9d38ae45
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name/label of the SSH key.
        :param pulumi.Input[str] ssh_key: The public SSH key.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SshKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Vultr SSH key resource. This can be used to create, read, modify, and delete SSH keys.

        ## Example Usage

        Create an SSH key

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_ssh_key = vultr.SshKey("mySshKey", ssh_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyVGaw1PuEl98f4/7Kq3O9ZIvDw2OFOSXAFVqilSFNkHlefm1iMtPeqsIBp2t9cbGUf55xNDULz/bD/4BCV43yZ5lh0cUYuXALg9NI29ui7PEGReXjSpNwUD6ceN/78YOK41KAcecq+SS0bJ4b4amKZIJG3JWmDKljtv1dmSBCrTmEAQaOorxqGGBYmZS7NQumRe4lav5r6wOs8OACMANE1ejkeZsGFzJFNqvr5DuHdDL5FAudW23me3BDmrM9ifUzzjl1Jwku3bnRaCcjaxH8oTumt1a00mWci/1qUlaVFft085yvVq7KZbF2OPPbl+erDW91+EZ2FgEi+v1/CSJ5 your_username@hostname")
        ```

        ## Import

        SSH keys can be imported using the SSH key `ID`, e.g.

        ```sh
         $ pulumi import vultr:index/sshKey:SshKey my_key 6b0876a7-f709-41ba-aed8-abed9d38ae45
        ```

        :param str resource_name: The name of the resource.
        :param SshKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SshKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssh_key: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SshKeyArgs.__new__(SshKeyArgs)

            __props__.__dict__["name"] = name
            if ssh_key is None and not opts.urn:
                raise TypeError("Missing required property 'ssh_key'")
            __props__.__dict__["ssh_key"] = ssh_key
            __props__.__dict__["date_created"] = None
        super(SshKey, __self__).__init__(
            'vultr:index/sshKey:SshKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            date_created: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ssh_key: Optional[pulumi.Input[str]] = None) -> 'SshKey':
        """
        Get an existing SshKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] date_created: The date the SSH key was added to your Vultr account.
        :param pulumi.Input[str] name: The name/label of the SSH key.
        :param pulumi.Input[str] ssh_key: The public SSH key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SshKeyState.__new__(_SshKeyState)

        __props__.__dict__["date_created"] = date_created
        __props__.__dict__["name"] = name
        __props__.__dict__["ssh_key"] = ssh_key
        return SshKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[str]:
        """
        The date the SSH key was added to your Vultr account.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name/label of the SSH key.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> pulumi.Output[str]:
        """
        The public SSH key.
        """
        return pulumi.get(self, "ssh_key")

