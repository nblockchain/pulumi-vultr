// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Vultr.Inputs
{

    public sealed class GetVPCFilterInputArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Attribute name to filter with.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("values", required: true)]
        private InputList<string>? _values;

        /// <summary>
        /// One or more values filter with.
        /// </summary>
        public InputList<string> Values
        {
            get => _values ?? (_values = new InputList<string>());
            set => _values = value;
        }

        public GetVPCFilterInputArgs()
        {
        }
        public static new GetVPCFilterInputArgs Empty => new GetVPCFilterInputArgs();
    }
}
