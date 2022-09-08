// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Vultr Firewall Rule resource. This can be used to create, read, modify, and delete Firewall rules.
 *
 * ## Example Usage
 *
 * Create a Firewall Rule
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as vultr from "@pulumi/vultr";
 *
 * const myFirewallgroup = new vultr.FirewallGroup("myFirewallgroup", {description: "base firewall"});
 * const myFirewallrule = new vultr.FirewallRule("myFirewallrule", {
 *     firewallGroupId: myFirewallgroup.id,
 *     protocol: "tcp",
 *     ipType: "v4",
 *     subnet: "0.0.0.0",
 *     subnetSize: 0,
 *     port: "8090",
 *     notes: "my firewall rule",
 * });
 * ```
 *
 * ## Import
 *
 * Firewall Rules can be imported using the Firewall Group `ID` and Firewall Rule `ID`, e.g.
 *
 * ```sh
 *  $ pulumi import vultr:index/firewallRule:FirewallRule my_rule b6a859c5-b299-49dd-8888-b1abbc517d08,1
 * ```
 */
export class FirewallRule extends pulumi.CustomResource {
    /**
     * Get an existing FirewallRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallRuleState, opts?: pulumi.CustomResourceOptions): FirewallRule {
        return new FirewallRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'vultr:index/firewallRule:FirewallRule';

    /**
     * Returns true if the given object is an instance of FirewallRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FirewallRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FirewallRule.__pulumiType;
    }

    /**
     * The firewall group that the firewall rule will belong to.
     */
    public readonly firewallGroupId!: pulumi.Output<string>;
    /**
     * The type of ip for this firewall rule. Possible values (v4, v6) **Note** they must be lowercase
     */
    public readonly ipType!: pulumi.Output<string>;
    /**
     * A simple note for a given firewall rule
     */
    public readonly notes!: pulumi.Output<string | undefined>;
    /**
     * TCP/UDP only. This field can be a specific port or a colon separated port range.
     */
    public readonly port!: pulumi.Output<string | undefined>;
    /**
     * The type of protocol for this firewall rule. Possible values (icmp, tcp, udp, gre, esp, ah) **Note** they must be lowercase
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * Possible values ("", cloudflare)
     */
    public readonly source!: pulumi.Output<string | undefined>;
    /**
     * IP address that you want to define for this firewall rule.
     */
    public readonly subnet!: pulumi.Output<string>;
    /**
     * The number of bits for the subnet in CIDR notation. Example: 32.
     */
    public readonly subnetSize!: pulumi.Output<number>;

    /**
     * Create a FirewallRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FirewallRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirewallRuleArgs | FirewallRuleState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FirewallRuleState | undefined;
            resourceInputs["firewallGroupId"] = state ? state.firewallGroupId : undefined;
            resourceInputs["ipType"] = state ? state.ipType : undefined;
            resourceInputs["notes"] = state ? state.notes : undefined;
            resourceInputs["port"] = state ? state.port : undefined;
            resourceInputs["protocol"] = state ? state.protocol : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["subnet"] = state ? state.subnet : undefined;
            resourceInputs["subnetSize"] = state ? state.subnetSize : undefined;
        } else {
            const args = argsOrState as FirewallRuleArgs | undefined;
            if ((!args || args.firewallGroupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'firewallGroupId'");
            }
            if ((!args || args.ipType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipType'");
            }
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            if ((!args || args.subnet === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnet'");
            }
            if ((!args || args.subnetSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetSize'");
            }
            resourceInputs["firewallGroupId"] = args ? args.firewallGroupId : undefined;
            resourceInputs["ipType"] = args ? args.ipType : undefined;
            resourceInputs["notes"] = args ? args.notes : undefined;
            resourceInputs["port"] = args ? args.port : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["subnet"] = args ? args.subnet : undefined;
            resourceInputs["subnetSize"] = args ? args.subnetSize : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FirewallRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FirewallRule resources.
 */
export interface FirewallRuleState {
    /**
     * The firewall group that the firewall rule will belong to.
     */
    firewallGroupId?: pulumi.Input<string>;
    /**
     * The type of ip for this firewall rule. Possible values (v4, v6) **Note** they must be lowercase
     */
    ipType?: pulumi.Input<string>;
    /**
     * A simple note for a given firewall rule
     */
    notes?: pulumi.Input<string>;
    /**
     * TCP/UDP only. This field can be a specific port or a colon separated port range.
     */
    port?: pulumi.Input<string>;
    /**
     * The type of protocol for this firewall rule. Possible values (icmp, tcp, udp, gre, esp, ah) **Note** they must be lowercase
     */
    protocol?: pulumi.Input<string>;
    /**
     * Possible values ("", cloudflare)
     */
    source?: pulumi.Input<string>;
    /**
     * IP address that you want to define for this firewall rule.
     */
    subnet?: pulumi.Input<string>;
    /**
     * The number of bits for the subnet in CIDR notation. Example: 32.
     */
    subnetSize?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a FirewallRule resource.
 */
export interface FirewallRuleArgs {
    /**
     * The firewall group that the firewall rule will belong to.
     */
    firewallGroupId: pulumi.Input<string>;
    /**
     * The type of ip for this firewall rule. Possible values (v4, v6) **Note** they must be lowercase
     */
    ipType: pulumi.Input<string>;
    /**
     * A simple note for a given firewall rule
     */
    notes?: pulumi.Input<string>;
    /**
     * TCP/UDP only. This field can be a specific port or a colon separated port range.
     */
    port?: pulumi.Input<string>;
    /**
     * The type of protocol for this firewall rule. Possible values (icmp, tcp, udp, gre, esp, ah) **Note** they must be lowercase
     */
    protocol: pulumi.Input<string>;
    /**
     * Possible values ("", cloudflare)
     */
    source?: pulumi.Input<string>;
    /**
     * IP address that you want to define for this firewall rule.
     */
    subnet: pulumi.Input<string>;
    /**
     * The number of bits for the subnet in CIDR notation. Example: 32.
     */
    subnetSize: pulumi.Input<number>;
}
