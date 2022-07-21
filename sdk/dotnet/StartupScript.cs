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
    /// Provides a Vultr Startup Script resource. This can be used to create, read, modify, and delete Startup Scripts.
    /// 
    /// ## Example Usage
    /// 
    /// Create a new Startup Script
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Vultr = Pulumi.Vultr;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var myScript = new Vultr.StartupScript("myScript", new Vultr.StartupScriptArgs
    ///         {
    ///             Script = "echo $PATH",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Startup Scripts can be imported using the Startup Scripts `ID`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import vultr:index/startupScript:StartupScript my_script ff8f36a8-eb86-4b8d-8667-b9d5459b6390
    /// ```
    /// </summary>
    [VultrResourceType("vultr:index/startupScript:StartupScript")]
    public partial class StartupScript : Pulumi.CustomResource
    {
        /// <summary>
        /// Date the script was created.
        /// </summary>
        [Output("dateCreated")]
        public Output<string> DateCreated { get; private set; } = null!;

        /// <summary>
        /// Date the script was last modified.
        /// </summary>
        [Output("dateModified")]
        public Output<string> DateModified { get; private set; } = null!;

        /// <summary>
        /// Name of the given script.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Contents of the startup script base64 encoded.
        /// </summary>
        [Output("script")]
        public Output<string> Script { get; private set; } = null!;

        /// <summary>
        /// Type of startup script. Possible values are boot or pxe - default is boot.
        /// </summary>
        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;


        /// <summary>
        /// Create a StartupScript resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StartupScript(string name, StartupScriptArgs args, CustomResourceOptions? options = null)
            : base("vultr:index/startupScript:StartupScript", name, args ?? new StartupScriptArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StartupScript(string name, Input<string> id, StartupScriptState? state = null, CustomResourceOptions? options = null)
            : base("vultr:index/startupScript:StartupScript", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing StartupScript resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StartupScript Get(string name, Input<string> id, StartupScriptState? state = null, CustomResourceOptions? options = null)
        {
            return new StartupScript(name, id, state, options);
        }
    }

    public sealed class StartupScriptArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the given script.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Contents of the startup script base64 encoded.
        /// </summary>
        [Input("script", required: true)]
        public Input<string> Script { get; set; } = null!;

        /// <summary>
        /// Type of startup script. Possible values are boot or pxe - default is boot.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public StartupScriptArgs()
        {
        }
    }

    public sealed class StartupScriptState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Date the script was created.
        /// </summary>
        [Input("dateCreated")]
        public Input<string>? DateCreated { get; set; }

        /// <summary>
        /// Date the script was last modified.
        /// </summary>
        [Input("dateModified")]
        public Input<string>? DateModified { get; set; }

        /// <summary>
        /// Name of the given script.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Contents of the startup script base64 encoded.
        /// </summary>
        [Input("script")]
        public Input<string>? Script { get; set; }

        /// <summary>
        /// Type of startup script. Possible values are boot or pxe - default is boot.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public StartupScriptState()
        {
        }
    }
}
