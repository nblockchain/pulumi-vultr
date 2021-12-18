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
    'GetIsoPrivateResult',
    'AwaitableGetIsoPrivateResult',
    'get_iso_private',
    'get_iso_private_output',
]

@pulumi.output_type
class GetIsoPrivateResult:
    """
    A collection of values returned by getIsoPrivate.
    """
    def __init__(__self__, date_created=None, filename=None, filters=None, id=None, md5sum=None, sha512sum=None, size=None, status=None):
        if date_created and not isinstance(date_created, str):
            raise TypeError("Expected argument 'date_created' to be a str")
        pulumi.set(__self__, "date_created", date_created)
        if filename and not isinstance(filename, str):
            raise TypeError("Expected argument 'filename' to be a str")
        pulumi.set(__self__, "filename", filename)
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if md5sum and not isinstance(md5sum, str):
            raise TypeError("Expected argument 'md5sum' to be a str")
        pulumi.set(__self__, "md5sum", md5sum)
        if sha512sum and not isinstance(sha512sum, str):
            raise TypeError("Expected argument 'sha512sum' to be a str")
        pulumi.set(__self__, "sha512sum", sha512sum)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="dateCreated")
    def date_created(self) -> str:
        """
        The date the ISO file was added to your Vultr account.
        """
        return pulumi.get(self, "date_created")

    @property
    @pulumi.getter
    def filename(self) -> str:
        """
        The ISO file's filename.
        """
        return pulumi.get(self, "filename")

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetIsoPrivateFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def md5sum(self) -> str:
        """
        The md5 hash of the ISO file.
        """
        return pulumi.get(self, "md5sum")

    @property
    @pulumi.getter
    def sha512sum(self) -> str:
        """
        The sha512 hash of the ISO file.
        """
        return pulumi.get(self, "sha512sum")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the ISO file in bytes.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the ISO file.
        """
        return pulumi.get(self, "status")


class AwaitableGetIsoPrivateResult(GetIsoPrivateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIsoPrivateResult(
            date_created=self.date_created,
            filename=self.filename,
            filters=self.filters,
            id=self.id,
            md5sum=self.md5sum,
            sha512sum=self.sha512sum,
            size=self.size,
            status=self.status)


def get_iso_private(filters: Optional[Sequence[pulumi.InputType['GetIsoPrivateFilterArgs']]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIsoPrivateResult:
    """
    Get information about an ISO file uploaded to your Vultr account.

    ## Example Usage

    Get the information for a ISO file by `filename`:

    ```python
    import pulumi
    import pulumi_vultr as vultr

    my_iso = vultr.get_iso_private(filters=[vultr.GetIsoPrivateFilterArgs(
        name="filename",
        values=["my-iso-filename"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetIsoPrivateFilterArgs']] filters: Query parameters for finding ISO files.
    """
    __args__ = dict()
    __args__['filters'] = filters
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vultr:index/getIsoPrivate:getIsoPrivate', __args__, opts=opts, typ=GetIsoPrivateResult).value

    return AwaitableGetIsoPrivateResult(
        date_created=__ret__.date_created,
        filename=__ret__.filename,
        filters=__ret__.filters,
        id=__ret__.id,
        md5sum=__ret__.md5sum,
        sha512sum=__ret__.sha512sum,
        size=__ret__.size,
        status=__ret__.status)


@_utilities.lift_output_func(get_iso_private)
def get_iso_private_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetIsoPrivateFilterArgs']]]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIsoPrivateResult]:
    """
    Get information about an ISO file uploaded to your Vultr account.

    ## Example Usage

    Get the information for a ISO file by `filename`:

    ```python
    import pulumi
    import pulumi_vultr as vultr

    my_iso = vultr.get_iso_private(filters=[vultr.GetIsoPrivateFilterArgs(
        name="filename",
        values=["my-iso-filename"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetIsoPrivateFilterArgs']] filters: Query parameters for finding ISO files.
    """
    ...
