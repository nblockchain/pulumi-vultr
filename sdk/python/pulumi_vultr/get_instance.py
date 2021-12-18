# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetInstanceResult',
    'AwaitableGetInstanceResult',
    'get_instance',
    'get_instance_output',
]

@pulumi.output_type
class GetInstanceResult:
    """
    A collection of values returned by getInstance.
    """
    def __init__(__self__, allowed_bandwidth=None, app_id=None, backups=None, backups_schedule=None, date_created=None, disk=None, features=None, filters=None, firewall_group_id=None, gateway_v4=None, hostname=None, id=None, image_id=None, internal_ip=None, kvm=None, label=None, location=None, main_ip=None, netmask_v4=None, os=None, os_id=None, plan=None, power_status=None, ram=None, region=None, server_status=None, status=None, tag=None, v6_main_ip=None, v6_network=None, v6_network_size=None, vcpu_count=None):
        if allowed_bandwidth and not isinstance(allowed_bandwidth, int):
            raise TypeError("Expected argument 'allowed_bandwidth' to be a int")
        pulumi.set(__self__, "allowed_bandwidth", allowed_bandwidth)
        if app_id and not isinstance(app_id, int):
            raise TypeError("Expected argument 'app_id' to be a int")
        pulumi.set(__self__, "app_id", app_id)
        if backups and not isinstance(backups, str):
            raise TypeError("Expected argument 'backups' to be a str")
        pulumi.set(__self__, "backups", backups)
        if backups_schedule and not isinstance(backups_schedule, dict):
            raise TypeError("Expected argument 'backups_schedule' to be a dict")
        pulumi.set(__self__, "backups_schedule", backups_schedule)
        if date_created and not isinstance(date_created, str):
            raise TypeError("Expected argument 'date_created' to be a str")
        pulumi.set(__self__, "date_created", date_created)
        if disk and not isinstance(disk, int):
            raise TypeError("Expected argument 'disk' to be a int")
        pulumi.set(__self__, "disk", disk)
        if features and not isinstance(features, list):
            raise TypeError("Expected argument 'features' to be a list")
        pulumi.set(__self__, "features", features)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if firewall_group_id and not isinstance(firewall_group_id, str):
            raise TypeError("Expected argument 'firewall_group_id' to be a str")
        pulumi.set(__self__, "firewall_group_id", firewall_group_id)
        if gateway_v4 and not isinstance(gateway_v4, str):
            raise TypeError("Expected argument 'gateway_v4' to be a str")
        pulumi.set(__self__, "gateway_v4", gateway_v4)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_id and not isinstance(image_id, str):
            raise TypeError("Expected argument 'image_id' to be a str")
        pulumi.set(__self__, "image_id", image_id)
        if internal_ip and not isinstance(internal_ip, str):
            raise TypeError("Expected argument 'internal_ip' to be a str")
        pulumi.set(__self__, "internal_ip", internal_ip)
        if kvm and not isinstance(kvm, str):
            raise TypeError("Expected argument 'kvm' to be a str")
        pulumi.set(__self__, "kvm", kvm)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if main_ip and not isinstance(main_ip, str):
            raise TypeError("Expected argument 'main_ip' to be a str")
        pulumi.set(__self__, "main_ip", main_ip)
        if netmask_v4 and not isinstance(netmask_v4, str):
            raise TypeError("Expected argument 'netmask_v4' to be a str")
        pulumi.set(__self__, "netmask_v4", netmask_v4)
        if os and not isinstance(os, str):
            raise TypeError("Expected argument 'os' to be a str")
        pulumi.set(__self__, "os", os)
        if os_id and not isinstance(os_id, int):
            raise TypeError("Expected argument 'os_id' to be a int")
        pulumi.set(__self__, "os_id", os_id)
        if plan and not isinstance(plan, str):
            raise TypeError("Expected argument 'plan' to be a str")
        pulumi.set(__self__, "plan", plan)
        if power_status and not isinstance(power_status, str):
            raise TypeError("Expected argument 'power_status' to be a str")
        pulumi.set(__self__, "power_status", power_status)
        if ram and not isinstance(ram, int):
            raise TypeError("Expected argument 'ram' to be a int")
        pulumi.set(__self__, "ram", ram)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if server_status and not isinstance(server_status, str):
            raise TypeError("Expected argument 'server_status' to be a str")
        pulumi.set(__self__, "server_status", server_status)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if v6_main_ip and not isinstance(v6_main_ip, str):
            raise TypeError("Expected argument 'v6_main_ip' to be a str")
        pulumi.set(__self__, "v6_main_ip", v6_main_ip)
        if v6_network and not isinstance(v6_network, str):
            raise TypeError("Expected argument 'v6_network' to be a str")
        pulumi.set(__self__, "v6_network", v6_network)
        if v6_network_size and not isinstance(v6_network_size, int):
            raise TypeError("Expected argument 'v6_network_size' to be a int")
        pulumi.set(__self__, "v6_network_size", v6_network_size)
        if vcpu_count and not isinstance(vcpu_count, int):
            raise TypeError("Expected argument 'vcpu_count' to be a int")
        pulumi.set(__self__, "vcpu_count", vcpu_count)

    @property
    @pulumi.getter(name="allowedBandwidth")
    def allowed_bandwidth(self) -> int:
        """
        The server's allowed bandwidth usage in GB.
        """
        return pulumi.get(self, "allowed_bandwidth")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> int:
        """
        The server's application ID.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def backups(self) -> str:
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="backupsSchedule")
    def backups_schedule(self) -> Mapping[str, Any]:
        """
        The current configuration for backups
        """
        return pulumi.get(self, "backups_schedule")

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> str:
        """
        The date the server was added to your Vultr account.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def disk(self) -> int:
        """
        The description of the disk(s) on the server.
        """
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter
    def features(self) -> Sequence[str]:
        """
        Array of which features are enabled.
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetInstanceFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter(name="firewallGroupId")
    def firewall_group_id(self) -> str:
        """
        The ID of the firewall group applied to this server.
        """
        return pulumi.get(self, "firewall_group_id")

    @property
    @pulumi.getter(name="gatewayV4")
    def gateway_v4(self) -> str:
        """
        The server's IPv4 gateway.
        """
        return pulumi.get(self, "gateway_v4")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        The hostname assigned to the server.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> str:
        """
        The Marketplace ID for this application.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="internalIp")
    def internal_ip(self) -> str:
        """
        The server's internal IP address.
        """
        return pulumi.get(self, "internal_ip")

    @property
    @pulumi.getter
    def kvm(self) -> str:
        """
        The server's current KVM URL. This URL will change periodically. It is not advised to cache this value.
        """
        return pulumi.get(self, "kvm")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        The server's label.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mainIp")
    def main_ip(self) -> str:
        """
        The server's main IP address.
        """
        return pulumi.get(self, "main_ip")

    @property
    @pulumi.getter(name="netmaskV4")
    def netmask_v4(self) -> str:
        """
        The server's IPv4 netmask.
        """
        return pulumi.get(self, "netmask_v4")

    @property
    @pulumi.getter
    def os(self) -> str:
        """
        The operating system of the instance.
        """
        return pulumi.get(self, "os")

    @property
    @pulumi.getter(name="osId")
    def os_id(self) -> int:
        """
        The server's operating system ID.
        """
        return pulumi.get(self, "os_id")

    @property
    @pulumi.getter
    def plan(self) -> str:
        """
        The server's plan ID.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="powerStatus")
    def power_status(self) -> str:
        """
        Whether the server is powered on or not.
        """
        return pulumi.get(self, "power_status")

    @property
    @pulumi.getter
    def ram(self) -> int:
        """
        The amount of memory available on the instance in MB.
        """
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region ID of the server.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="serverStatus")
    def server_status(self) -> str:
        """
        A more detailed server status (none, locked, installingbooting, isomounting, ok).
        """
        return pulumi.get(self, "server_status")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the server's subscription.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tag(self) -> str:
        """
        The server's tag.
        """
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter(name="v6MainIp")
    def v6_main_ip(self) -> str:
        """
        The main IPv6 network address.
        """
        return pulumi.get(self, "v6_main_ip")

    @property
    @pulumi.getter(name="v6Network")
    def v6_network(self) -> str:
        """
        The IPv6 subnet.
        """
        return pulumi.get(self, "v6_network")

    @property
    @pulumi.getter(name="v6NetworkSize")
    def v6_network_size(self) -> int:
        """
        The IPv6 network size in bits.
        """
        return pulumi.get(self, "v6_network_size")

    @property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> int:
        """
        The number of virtual CPUs available on the server.
        """
        return pulumi.get(self, "vcpu_count")


class AwaitableGetInstanceResult(GetInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceResult(
            allowed_bandwidth=self.allowed_bandwidth,
            app_id=self.app_id,
            backups=self.backups,
            backups_schedule=self.backups_schedule,
            date_created=self.date_created,
            disk=self.disk,
            features=self.features,
            filters=self.filters,
            firewall_group_id=self.firewall_group_id,
            gateway_v4=self.gateway_v4,
            hostname=self.hostname,
            id=self.id,
            image_id=self.image_id,
            internal_ip=self.internal_ip,
            kvm=self.kvm,
            label=self.label,
            location=self.location,
            main_ip=self.main_ip,
            netmask_v4=self.netmask_v4,
            os=self.os,
            os_id=self.os_id,
            plan=self.plan,
            power_status=self.power_status,
            ram=self.ram,
            region=self.region,
            server_status=self.server_status,
            status=self.status,
            tag=self.tag,
            v6_main_ip=self.v6_main_ip,
            v6_network=self.v6_network,
            v6_network_size=self.v6_network_size,
            vcpu_count=self.vcpu_count)


def get_instance(filters: Optional[Sequence[pulumi.InputType['GetInstanceFilterArgs']]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceResult:
    """
    Get information about a Vultr instance.

    ## Example Usage

    Get the information for a instance by `label`:

    ```python
    import pulumi
    import pulumi_vultr as vultr

    my_instance = vultr.get_instance(filters=[vultr.GetInstanceFilterArgs(
        name="label",
        values=["my-instance-label"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetInstanceFilterArgs']] filters: Query parameters for finding instances.
    """
    __args__ = dict()
    __args__['filters'] = filters
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vultr:index/getInstance:getInstance', __args__, opts=opts, typ=GetInstanceResult).value

    return AwaitableGetInstanceResult(
        allowed_bandwidth=__ret__.allowed_bandwidth,
        app_id=__ret__.app_id,
        backups=__ret__.backups,
        backups_schedule=__ret__.backups_schedule,
        date_created=__ret__.date_created,
        disk=__ret__.disk,
        features=__ret__.features,
        filters=__ret__.filters,
        firewall_group_id=__ret__.firewall_group_id,
        gateway_v4=__ret__.gateway_v4,
        hostname=__ret__.hostname,
        id=__ret__.id,
        image_id=__ret__.image_id,
        internal_ip=__ret__.internal_ip,
        kvm=__ret__.kvm,
        label=__ret__.label,
        location=__ret__.location,
        main_ip=__ret__.main_ip,
        netmask_v4=__ret__.netmask_v4,
        os=__ret__.os,
        os_id=__ret__.os_id,
        plan=__ret__.plan,
        power_status=__ret__.power_status,
        ram=__ret__.ram,
        region=__ret__.region,
        server_status=__ret__.server_status,
        status=__ret__.status,
        tag=__ret__.tag,
        v6_main_ip=__ret__.v6_main_ip,
        v6_network=__ret__.v6_network,
        v6_network_size=__ret__.v6_network_size,
        vcpu_count=__ret__.vcpu_count)


@_utilities.lift_output_func(get_instance)
def get_instance_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstanceFilterArgs']]]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceResult]:
    """
    Get information about a Vultr instance.

    ## Example Usage

    Get the information for a instance by `label`:

    ```python
    import pulumi
    import pulumi_vultr as vultr

    my_instance = vultr.get_instance(filters=[vultr.GetInstanceFilterArgs(
        name="label",
        values=["my-instance-label"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetInstanceFilterArgs']] filters: Query parameters for finding instances.
    """
    ...
