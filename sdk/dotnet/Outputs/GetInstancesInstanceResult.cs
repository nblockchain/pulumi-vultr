// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vultr.Outputs
{

    [OutputType]
    public sealed class GetInstancesInstanceResult
    {
        public readonly int AllowedBandwidth;
        public readonly int AppId;
        public readonly string Backups;
        public readonly ImmutableDictionary<string, object> BackupsSchedule;
        public readonly string DateCreated;
        public readonly int Disk;
        public readonly ImmutableArray<string> Features;
        public readonly string FirewallGroupId;
        public readonly string GatewayV4;
        public readonly string Hostname;
        public readonly string Id;
        public readonly string ImageId;
        public readonly string InternalIp;
        public readonly string Kvm;
        public readonly string Label;
        public readonly string Location;
        public readonly string MainIp;
        public readonly string NetmaskV4;
        public readonly string Os;
        public readonly int OsId;
        public readonly string Plan;
        public readonly string PowerStatus;
        public readonly ImmutableArray<string> PrivateNetworkIds;
        public readonly int Ram;
        public readonly string Region;
        public readonly string ServerStatus;
        public readonly string Status;
        public readonly string Tag;
        public readonly ImmutableArray<string> Tags;
        public readonly string V6MainIp;
        public readonly string V6Network;
        public readonly int V6NetworkSize;
        public readonly int VcpuCount;
        public readonly ImmutableArray<string> VpcIds;

        [OutputConstructor]
        private GetInstancesInstanceResult(
            int allowedBandwidth,

            int appId,

            string backups,

            ImmutableDictionary<string, object> backupsSchedule,

            string dateCreated,

            int disk,

            ImmutableArray<string> features,

            string firewallGroupId,

            string gatewayV4,

            string hostname,

            string id,

            string imageId,

            string internalIp,

            string kvm,

            string label,

            string location,

            string mainIp,

            string netmaskV4,

            string os,

            int osId,

            string plan,

            string powerStatus,

            ImmutableArray<string> privateNetworkIds,

            int ram,

            string region,

            string serverStatus,

            string status,

            string tag,

            ImmutableArray<string> tags,

            string v6MainIp,

            string v6Network,

            int v6NetworkSize,

            int vcpuCount,

            ImmutableArray<string> vpcIds)
        {
            AllowedBandwidth = allowedBandwidth;
            AppId = appId;
            Backups = backups;
            BackupsSchedule = backupsSchedule;
            DateCreated = dateCreated;
            Disk = disk;
            Features = features;
            FirewallGroupId = firewallGroupId;
            GatewayV4 = gatewayV4;
            Hostname = hostname;
            Id = id;
            ImageId = imageId;
            InternalIp = internalIp;
            Kvm = kvm;
            Label = label;
            Location = location;
            MainIp = mainIp;
            NetmaskV4 = netmaskV4;
            Os = os;
            OsId = osId;
            Plan = plan;
            PowerStatus = powerStatus;
            PrivateNetworkIds = privateNetworkIds;
            Ram = ram;
            Region = region;
            ServerStatus = serverStatus;
            Status = status;
            Tag = tag;
            Tags = tags;
            V6MainIp = v6MainIp;
            V6Network = v6Network;
            V6NetworkSize = v6NetworkSize;
            VcpuCount = vcpuCount;
            VpcIds = vpcIds;
        }
    }
}
