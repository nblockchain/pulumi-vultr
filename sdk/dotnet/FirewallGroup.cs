// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vultr
{
    /// <summary>
    /// Provides a Vultr Firewall Group resource. This can be used to create, read, modify, and delete Firewall Group.
    /// 
    /// ## Example Usage
    /// 
    /// Create a new Firewall group
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Vultr = Pulumi.Vultr;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var myFirewallgroup = new Vultr.FirewallGroup("myFirewallgroup", new Vultr.FirewallGroupArgs
    ///         {
    ///             Description = "base firewall",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Firewall Groups can be imported using the Firewall Group `FIREWALLGROUPID`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import vultr:index/firewallGroup:FirewallGroup my_firewallgroup c342f929
    /// ```
    /// </summary>
    [VultrResourceType("vultr:index/firewallGroup:FirewallGroup")]
    public partial class FirewallGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// The date the firewall group was created.
        /// </summary>
        [Output("dateCreated")]
        public Output<string> DateCreated { get; private set; } = null!;

        /// <summary>
        /// The date the firewall group was modified.
        /// </summary>
        [Output("dateModified")]
        public Output<string> DateModified { get; private set; } = null!;

        /// <summary>
        /// Description of the firewall group.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The number of instances that are currently using this firewall group.
        /// </summary>
        [Output("instanceCount")]
        public Output<int> InstanceCount { get; private set; } = null!;

        /// <summary>
        /// The number of max firewall rules this group can have.
        /// </summary>
        [Output("maxRuleCount")]
        public Output<int> MaxRuleCount { get; private set; } = null!;

        /// <summary>
        /// The number of firewall rules this group currently has.
        /// </summary>
        [Output("ruleCount")]
        public Output<int> RuleCount { get; private set; } = null!;


        /// <summary>
        /// Create a FirewallGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FirewallGroup(string name, FirewallGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("vultr:index/firewallGroup:FirewallGroup", name, args ?? new FirewallGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FirewallGroup(string name, Input<string> id, FirewallGroupState? state = null, CustomResourceOptions? options = null)
            : base("vultr:index/firewallGroup:FirewallGroup", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FirewallGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FirewallGroup Get(string name, Input<string> id, FirewallGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new FirewallGroup(name, id, state, options);
        }
    }

    public sealed class FirewallGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of the firewall group.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        public FirewallGroupArgs()
        {
        }
    }

    public sealed class FirewallGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The date the firewall group was created.
        /// </summary>
        [Input("dateCreated")]
        public Input<string>? DateCreated { get; set; }

        /// <summary>
        /// The date the firewall group was modified.
        /// </summary>
        [Input("dateModified")]
        public Input<string>? DateModified { get; set; }

        /// <summary>
        /// Description of the firewall group.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The number of instances that are currently using this firewall group.
        /// </summary>
        [Input("instanceCount")]
        public Input<int>? InstanceCount { get; set; }

        /// <summary>
        /// The number of max firewall rules this group can have.
        /// </summary>
        [Input("maxRuleCount")]
        public Input<int>? MaxRuleCount { get; set; }

        /// <summary>
        /// The number of firewall rules this group currently has.
        /// </summary>
        [Input("ruleCount")]
        public Input<int>? RuleCount { get; set; }

        public FirewallGroupState()
        {
        }
    }
}
