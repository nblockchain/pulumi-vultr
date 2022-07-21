// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi.Utilities;

namespace Pulumi.Vultr
{
    public static class GetRegion
    {
        /// <summary>
        /// Get information about a Vultr region.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// Get the information for a region by `id`:
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Vultr = Pulumi.Vultr;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var myRegion = Output.Create(Vultr.GetRegion.InvokeAsync(new Vultr.GetRegionArgs
        ///         {
        ///             Filters = 
        ///             {
        ///                 new Vultr.Inputs.GetRegionFilterArgs
        ///                 {
        ///                     Name = "id",
        ///                     Values = 
        ///                     {
        ///                         "sea",
        ///                     },
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetRegionResult> InvokeAsync(GetRegionArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRegionResult>("vultr:index/getRegion:getRegion", args ?? new GetRegionArgs(), options.WithVersion());

        /// <summary>
        /// Get information about a Vultr region.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// Get the information for a region by `id`:
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Vultr = Pulumi.Vultr;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var myRegion = Output.Create(Vultr.GetRegion.InvokeAsync(new Vultr.GetRegionArgs
        ///         {
        ///             Filters = 
        ///             {
        ///                 new Vultr.Inputs.GetRegionFilterArgs
        ///                 {
        ///                     Name = "id",
        ///                     Values = 
        ///                     {
        ///                         "sea",
        ///                     },
        ///                 },
        ///             },
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetRegionResult> Invoke(GetRegionInvokeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRegionResult>("vultr:index/getRegion:getRegion", args ?? new GetRegionInvokeArgs(), options.WithVersion());
    }


    public sealed class GetRegionArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private List<Inputs.GetRegionFilterArgs>? _filters;

        /// <summary>
        /// Query parameters for finding regions.
        /// </summary>
        public List<Inputs.GetRegionFilterArgs> Filters
        {
            get => _filters ?? (_filters = new List<Inputs.GetRegionFilterArgs>());
            set => _filters = value;
        }

        public GetRegionArgs()
        {
        }
    }

    public sealed class GetRegionInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("filters")]
        private InputList<Inputs.GetRegionFilterInputArgs>? _filters;

        /// <summary>
        /// Query parameters for finding regions.
        /// </summary>
        public InputList<Inputs.GetRegionFilterInputArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.GetRegionFilterInputArgs>());
            set => _filters = value;
        }

        public GetRegionInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRegionResult
    {
        /// <summary>
        /// The city the region is in.
        /// </summary>
        public readonly string City;
        /// <summary>
        /// The continent the region is in.
        /// </summary>
        public readonly string Continent;
        /// <summary>
        /// The country the region is in.
        /// </summary>
        public readonly string Country;
        public readonly ImmutableArray<Outputs.GetRegionFilterResult> Filters;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Shows whether options like ddos protection or block storage are available in the region.
        /// </summary>
        public readonly ImmutableArray<string> Options;

        [OutputConstructor]
        private GetRegionResult(
            string city,

            string continent,

            string country,

            ImmutableArray<Outputs.GetRegionFilterResult> filters,

            string id,

            ImmutableArray<string> options)
        {
            City = city;
            Continent = continent;
            Country = country;
            Filters = filters;
            Id = id;
            Options = options;
        }
    }
}
