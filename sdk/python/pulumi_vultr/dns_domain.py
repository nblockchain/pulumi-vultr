# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DnsDomainArgs', 'DnsDomain']

@pulumi.input_type
class DnsDomainArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 dns_sec: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DnsDomain resource.
        :param pulumi.Input[str] domain: Name of domain.
        :param pulumi.Input[str] dns_sec: The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        :param pulumi.Input[str] ip: Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        pulumi.set(__self__, "domain", domain)
        if dns_sec is not None:
            pulumi.set(__self__, "dns_sec", dns_sec)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        Name of domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="dnsSec")
    def dns_sec(self) -> Optional[pulumi.Input[str]]:
        """
        The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        """
        return pulumi.get(self, "dns_sec")

    @dns_sec.setter
    def dns_sec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_sec", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)


@pulumi.input_type
class _DnsDomainState:
    def __init__(__self__, *,
                 date_created: Optional[pulumi.Input[str]] = None,
                 dns_sec: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DnsDomain resources.
        :param pulumi.Input[str] date_created: The date the domain was added to your account.
        :param pulumi.Input[str] dns_sec: The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        :param pulumi.Input[str] domain: Name of domain.
        :param pulumi.Input[str] ip: Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        if date_created is not None:
            pulumi.set(__self__, "date_created", date_created)
        if dns_sec is not None:
            pulumi.set(__self__, "dns_sec", dns_sec)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> Optional[pulumi.Input[str]]:
        """
        The date the domain was added to your account.
        """
        return pulumi.get(self, "date_created")

    @date_created.setter
    def date_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "date_created", value)

    @property
    @pulumi.getter(name="dnsSec")
    def dns_sec(self) -> Optional[pulumi.Input[str]]:
        """
        The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        """
        return pulumi.get(self, "dns_sec")

    @dns_sec.setter
    def dns_sec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_sec", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        Name of domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)


class DnsDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_sec: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Vultr DNS Domain resource. This can be used to create, read, modify, and delete DNS Domains.

        ## Example Usage

        Create a new DNS Domain

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_domain = vultr.DnsDomain("myDomain",
            domain="domain.com",
            ip="66.42.94.227")
        ```

        ## Import

        DNS Domains can be imported using the Dns Domain `domain`, e.g.

        ```sh
         $ pulumi import vultr:index/dnsDomain:DnsDomain name domain.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_sec: The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        :param pulumi.Input[str] domain: Name of domain.
        :param pulumi.Input[str] ip: Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DnsDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Vultr DNS Domain resource. This can be used to create, read, modify, and delete DNS Domains.

        ## Example Usage

        Create a new DNS Domain

        ```python
        import pulumi
        import pulumi_vultr as vultr

        my_domain = vultr.DnsDomain("myDomain",
            domain="domain.com",
            ip="66.42.94.227")
        ```

        ## Import

        DNS Domains can be imported using the Dns Domain `domain`, e.g.

        ```sh
         $ pulumi import vultr:index/dnsDomain:DnsDomain name domain.com
        ```

        :param str resource_name: The name of the resource.
        :param DnsDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DnsDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_sec: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
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
            __props__ = DnsDomainArgs.__new__(DnsDomainArgs)

            __props__.__dict__["dns_sec"] = dns_sec
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["ip"] = ip
            __props__.__dict__["date_created"] = None
        super(DnsDomain, __self__).__init__(
            'vultr:index/dnsDomain:DnsDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            date_created: Optional[pulumi.Input[str]] = None,
            dns_sec: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            ip: Optional[pulumi.Input[str]] = None) -> 'DnsDomain':
        """
        Get an existing DnsDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] date_created: The date the domain was added to your account.
        :param pulumi.Input[str] dns_sec: The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        :param pulumi.Input[str] domain: Name of domain.
        :param pulumi.Input[str] ip: Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DnsDomainState.__new__(_DnsDomainState)

        __props__.__dict__["date_created"] = date_created
        __props__.__dict__["dns_sec"] = dns_sec
        __props__.__dict__["domain"] = domain
        __props__.__dict__["ip"] = ip
        return DnsDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> pulumi.Output[str]:
        """
        The date the domain was added to your account.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter(name="dnsSec")
    def dns_sec(self) -> pulumi.Output[Optional[str]]:
        """
        The Domain's DNSSEC status. Valid options are `enabled` or `disabled`. Note `disabled` is default
        """
        return pulumi.get(self, "dns_sec")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        Name of domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[Optional[str]]:
        """
        Instance IP you want associated to domain. If omitted this will create a domain with no records.
        """
        return pulumi.get(self, "ip")

