# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PrivateNetworkArgs', 'PrivateNetwork']

@pulumi.input_type
class PrivateNetworkArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 v4_subnet: Optional[pulumi.Input[str]] = None,
                 v4_subnet_mask: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a PrivateNetwork resource.
        :param pulumi.Input[str] region: The region ID that you want the network to be created in.
        :param pulumi.Input[str] description: The description you want to give your network.
        :param pulumi.Input[str] v4_subnet: The IPv4 subnet to be used when attaching instances to this network.
        :param pulumi.Input[int] v4_subnet_mask: The number of bits for the netmask in CIDR notation. Example: 32
        """
        pulumi.set(__self__, "region", region)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if v4_subnet is not None:
            pulumi.set(__self__, "v4_subnet", v4_subnet)
        if v4_subnet_mask is not None:
            pulumi.set(__self__, "v4_subnet_mask", v4_subnet_mask)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region ID that you want the network to be created in.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description you want to give your network.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="v4Subnet")
    def v4_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 subnet to be used when attaching instances to this network.
        """
        return pulumi.get(self, "v4_subnet")

    @v4_subnet.setter
    def v4_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "v4_subnet", value)

    @property
    @pulumi.getter(name="v4SubnetMask")
    def v4_subnet_mask(self) -> Optional[pulumi.Input[int]]:
        """
        The number of bits for the netmask in CIDR notation. Example: 32
        """
        return pulumi.get(self, "v4_subnet_mask")

    @v4_subnet_mask.setter
    def v4_subnet_mask(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "v4_subnet_mask", value)


@pulumi.input_type
class _PrivateNetworkState:
    def __init__(__self__, *,
                 date_created: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 v4_subnet: Optional[pulumi.Input[str]] = None,
                 v4_subnet_mask: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering PrivateNetwork resources.
        :param pulumi.Input[str] date_created: The date that the network was added to your Vultr account.
        :param pulumi.Input[str] description: The description you want to give your network.
        :param pulumi.Input[str] region: The region ID that you want the network to be created in.
        :param pulumi.Input[str] v4_subnet: The IPv4 subnet to be used when attaching instances to this network.
        :param pulumi.Input[int] v4_subnet_mask: The number of bits for the netmask in CIDR notation. Example: 32
        """
        if date_created is not None:
            pulumi.set(__self__, "date_created", date_created)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if v4_subnet is not None:
            pulumi.set(__self__, "v4_subnet", v4_subnet)
        if v4_subnet_mask is not None:
            pulumi.set(__self__, "v4_subnet_mask", v4_subnet_mask)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date that the network was added to your Vultr account.
        """
        return pulumi.get(self, "date_created")

    @date_created.setter
    def date_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "date_created", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description you want to give your network.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region ID that you want the network to be created in.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="v4Subnet")
    def v4_subnet(self) -> Optional[pulumi.Input[str]]:
        """
        The IPv4 subnet to be used when attaching instances to this network.
        """
        return pulumi.get(self, "v4_subnet")

    @v4_subnet.setter
    def v4_subnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "v4_subnet", value)

    @property
    @pulumi.getter(name="v4SubnetMask")
    def v4_subnet_mask(self) -> Optional[pulumi.Input[int]]:
        """
        The number of bits for the netmask in CIDR notation. Example: 32
        """
        return pulumi.get(self, "v4_subnet_mask")

    @v4_subnet_mask.setter
    def v4_subnet_mask(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "v4_subnet_mask", value)


class PrivateNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 v4_subnet: Optional[pulumi.Input[str]] = None,
                 v4_subnet_mask: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Vultr private network resource. This can be used to create, read, and delete private networks on your Vultr account.

        ## Example Usage

        Create a new private network with an automatically generated CIDR block:

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_network = vultr.PrivateNetwork("myNetwork",
            description="my private network",
            region="ewr")
        ```

        Create a new private network with a specified CIDR block:

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_network = vultr.PrivateNetwork("myNetwork",
            description="my private network",
            region="ewr",
            v4_subnet="10.0.0.0",
            v4_subnet_mask=24)
        ```

        ## Import

        Networks can be imported using the network `ID`, e.g.

        ```sh
         $ pulumi import vultr:index/privateNetwork:PrivateNetwork my_network 0e04f918-575e-41cb-86f6-d729b354a5a1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description you want to give your network.
        :param pulumi.Input[str] region: The region ID that you want the network to be created in.
        :param pulumi.Input[str] v4_subnet: The IPv4 subnet to be used when attaching instances to this network.
        :param pulumi.Input[int] v4_subnet_mask: The number of bits for the netmask in CIDR notation. Example: 32
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Vultr private network resource. This can be used to create, read, and delete private networks on your Vultr account.

        ## Example Usage

        Create a new private network with an automatically generated CIDR block:

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_network = vultr.PrivateNetwork("myNetwork",
            description="my private network",
            region="ewr")
        ```

        Create a new private network with a specified CIDR block:

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_network = vultr.PrivateNetwork("myNetwork",
            description="my private network",
            region="ewr",
            v4_subnet="10.0.0.0",
            v4_subnet_mask=24)
        ```

        ## Import

        Networks can be imported using the network `ID`, e.g.

        ```sh
         $ pulumi import vultr:index/privateNetwork:PrivateNetwork my_network 0e04f918-575e-41cb-86f6-d729b354a5a1
        ```

        :param str resource_name: The name of the resource.
        :param PrivateNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 v4_subnet: Optional[pulumi.Input[str]] = None,
                 v4_subnet_mask: Optional[pulumi.Input[int]] = None,
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
            __props__ = PrivateNetworkArgs.__new__(PrivateNetworkArgs)

            __props__.__dict__["description"] = description
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["v4_subnet"] = v4_subnet
            __props__.__dict__["v4_subnet_mask"] = v4_subnet_mask
            __props__.__dict__["date_created"] = None
        super(PrivateNetwork, __self__).__init__(
            'vultr:index/privateNetwork:PrivateNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            date_created: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            v4_subnet: Optional[pulumi.Input[str]] = None,
            v4_subnet_mask: Optional[pulumi.Input[int]] = None) -> 'PrivateNetwork':
        """
        Get an existing PrivateNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] date_created: The date that the network was added to your Vultr account.
        :param pulumi.Input[str] description: The description you want to give your network.
        :param pulumi.Input[str] region: The region ID that you want the network to be created in.
        :param pulumi.Input[str] v4_subnet: The IPv4 subnet to be used when attaching instances to this network.
        :param pulumi.Input[int] v4_subnet_mask: The number of bits for the netmask in CIDR notation. Example: 32
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PrivateNetworkState.__new__(_PrivateNetworkState)

        __props__.__dict__["date_created"] = date_created
        __props__.__dict__["description"] = description
        __props__.__dict__["region"] = region
        __props__.__dict__["v4_subnet"] = v4_subnet
        __props__.__dict__["v4_subnet_mask"] = v4_subnet_mask
        return PrivateNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[str]:
        """
        The date that the network was added to your Vultr account.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description you want to give your network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region ID that you want the network to be created in.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="v4Subnet")
    def v4_subnet(self) -> pulumi.Output[str]:
        """
        The IPv4 subnet to be used when attaching instances to this network.
        """
        return pulumi.get(self, "v4_subnet")

    @property
    @pulumi.getter(name="v4SubnetMask")
    def v4_subnet_mask(self) -> pulumi.Output[int]:
        """
        The number of bits for the netmask in CIDR notation. Example: 32
        """
        return pulumi.get(self, "v4_subnet_mask")

