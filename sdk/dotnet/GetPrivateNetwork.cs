// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vultr
{
    public static class GetPrivateNetwork
    {
        /// <summary>
        /// Get information about a Vultr private network.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// Get the information for a private network by `description`:
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Vultr = Pulumi.Vultr;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myNetwork = Vultr.GetPrivateNetwork.Invoke(new()
        ///     {
        ///         Filters = new[]
        ///         {
        ///             new Vultr.Inputs.GetPrivateNetworkFilterInputArgs
        ///             {
        ///                 Name = "description",
        ///                 Values = new[]
        ///                 {
        ///                     "my-network-description",
        ///                 },
        ///             },
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPrivateNetworkResult> InvokeAsync(GetPrivateNetworkArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPrivateNetworkResult>("vultr:index/getPrivateNetwork:getPrivateNetwork", args ?? new GetPrivateNetworkArgs(), options.WithDefaults());

        /// <summary>
        /// Get information about a Vultr private network.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// Get the information for a private network by `description`:
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Vultr = Pulumi.Vultr;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var myNetwork = Vultr.GetPrivateNetwork.Invoke(new()
        ///     {
        ///         Filters = new[]
        ///         {
        ///             new Vultr.Inputs.GetPrivateNetworkFilterInputArgs
        ///             {
        ///                 Name = "description",
        ///                 Values = new[]
        ///                 {
        ///                     "my-network-description",
        ///                 },
        ///             },
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPrivateNetworkResult> Invoke(GetPrivateNetworkInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPrivateNetworkResult>("vultr:index/getPrivateNetwork:getPrivateNetwork", args ?? new GetPrivateNetworkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPrivateNetworkArgs : global::Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetPrivateNetworkFilterArgs>? _filters;

        /// <summary>
        /// Query parameters for finding private networks.
        /// </summary>
        public List<Inputs.GetPrivateNetworkFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetPrivateNetworkFilterArgs>());
            set => _filters = value;
        }

        public GetPrivateNetworkArgs()
        {
        }
        public static new GetPrivateNetworkArgs Empty => new GetPrivateNetworkArgs();
    }

    public sealed class GetPrivateNetworkInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetPrivateNetworkFilterInputArgs>? _filters;

        /// <summary>
        /// Query parameters for finding private networks.
        /// </summary>
        public InputList<Inputs.GetPrivateNetworkFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetPrivateNetworkFilterInputArgs>());
            set => _filters = value;
        }

        public GetPrivateNetworkInvokeArgs()
        {
        }
        public static new GetPrivateNetworkInvokeArgs Empty => new GetPrivateNetworkInvokeArgs();
    }


    [OutputType]
    public sealed class GetPrivateNetworkResult
    {
        /// <summary>
        /// The date the private network was added to your Vultr account.
        /// </summary>
        public readonly string DateCreated;
        /// <summary>
        /// The private network's description.
        /// </summary>
        public readonly string Description;
        public readonly ImmutableArray<Outputs.GetPrivateNetworkFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The ID of the region that the private network is in.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// The IPv4 network address. For example: 10.1.1.0.
        /// </summary>
        public readonly string V4Subnet;
        /// <summary>
        /// The number of bits for the netmask in CIDR notation. Example: 20
        /// </summary>
        public readonly int V4SubnetMask;

        [OutputConstructor]
        private GetPrivateNetworkResult(
            string dateCreated,

            string description,

            ImmutableArray<Outputs.GetPrivateNetworkFilterResult> filters,

            string id,

            string region,

            string v4Subnet,

            int v4SubnetMask)
        {
            DateCreated = dateCreated;
            Description = description;
            Filters = filters;
            Id = id;
            Region = region;
            V4Subnet = v4Subnet;
            V4SubnetMask = v4SubnetMask;
        }
    }
}
