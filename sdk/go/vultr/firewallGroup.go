// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vultr

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a Vultr Firewall Group resource. This can be used to create, read, modify, and delete Firewall Group.
//
// ## Example Usage
//
// Create a new Firewall group
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-vultr/sdk/go/vultr"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := vultr.NewFirewallGroup(ctx, "myFirewallgroup", &vultr.FirewallGroupArgs{
// 			Description: pulumi.String("base firewall"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// Firewall Groups can be imported using the Firewall Group `FIREWALLGROUPID`, e.g.
//
// ```sh
//  $ pulumi import vultr:index/firewallGroup:FirewallGroup my_firewallgroup c342f929
// ```
type FirewallGroup struct {
	pulumi.CustomResourceState

	// The date the firewall group was created.
	DateCreated pulumi.StringOutput `pulumi:"dateCreated"`
	// The date the firewall group was modified.
	DateModified pulumi.StringOutput `pulumi:"dateModified"`
	// Description of the firewall group.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The number of instances that are currently using this firewall group.
	InstanceCount pulumi.IntOutput `pulumi:"instanceCount"`
	// The number of max firewall rules this group can have.
	MaxRuleCount pulumi.IntOutput `pulumi:"maxRuleCount"`
	// The number of firewall rules this group currently has.
	RuleCount pulumi.IntOutput `pulumi:"ruleCount"`
}

// NewFirewallGroup registers a new resource with the given unique name, arguments, and options.
func NewFirewallGroup(ctx *pulumi.Context,
	name string, args *FirewallGroupArgs, opts ...pulumi.ResourceOption) (*FirewallGroup, error) {
	if args == nil {
		args = &FirewallGroupArgs{}
	}

	var resource FirewallGroup
	err := ctx.RegisterResource("vultr:index/firewallGroup:FirewallGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFirewallGroup gets an existing FirewallGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFirewallGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FirewallGroupState, opts ...pulumi.ResourceOption) (*FirewallGroup, error) {
	var resource FirewallGroup
	err := ctx.ReadResource("vultr:index/firewallGroup:FirewallGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FirewallGroup resources.
type firewallGroupState struct {
	// The date the firewall group was created.
	DateCreated *string `pulumi:"dateCreated"`
	// The date the firewall group was modified.
	DateModified *string `pulumi:"dateModified"`
	// Description of the firewall group.
	Description *string `pulumi:"description"`
	// The number of instances that are currently using this firewall group.
	InstanceCount *int `pulumi:"instanceCount"`
	// The number of max firewall rules this group can have.
	MaxRuleCount *int `pulumi:"maxRuleCount"`
	// The number of firewall rules this group currently has.
	RuleCount *int `pulumi:"ruleCount"`
}

type FirewallGroupState struct {
	// The date the firewall group was created.
	DateCreated pulumi.StringPtrInput
	// The date the firewall group was modified.
	DateModified pulumi.StringPtrInput
	// Description of the firewall group.
	Description pulumi.StringPtrInput
	// The number of instances that are currently using this firewall group.
	InstanceCount pulumi.IntPtrInput
	// The number of max firewall rules this group can have.
	MaxRuleCount pulumi.IntPtrInput
	// The number of firewall rules this group currently has.
	RuleCount pulumi.IntPtrInput
}

func (FirewallGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallGroupState)(nil)).Elem()
}

type firewallGroupArgs struct {
	// Description of the firewall group.
	Description *string `pulumi:"description"`
}

// The set of arguments for constructing a FirewallGroup resource.
type FirewallGroupArgs struct {
	// Description of the firewall group.
	Description pulumi.StringPtrInput
}

func (FirewallGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*firewallGroupArgs)(nil)).Elem()
}

type FirewallGroupInput interface {
	pulumi.Input

	ToFirewallGroupOutput() FirewallGroupOutput
	ToFirewallGroupOutputWithContext(ctx context.Context) FirewallGroupOutput
}

func (*FirewallGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallGroup)(nil)).Elem()
}

func (i *FirewallGroup) ToFirewallGroupOutput() FirewallGroupOutput {
	return i.ToFirewallGroupOutputWithContext(context.Background())
}

func (i *FirewallGroup) ToFirewallGroupOutputWithContext(ctx context.Context) FirewallGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallGroupOutput)
}

// FirewallGroupArrayInput is an input type that accepts FirewallGroupArray and FirewallGroupArrayOutput values.
// You can construct a concrete instance of `FirewallGroupArrayInput` via:
//
//          FirewallGroupArray{ FirewallGroupArgs{...} }
type FirewallGroupArrayInput interface {
	pulumi.Input

	ToFirewallGroupArrayOutput() FirewallGroupArrayOutput
	ToFirewallGroupArrayOutputWithContext(context.Context) FirewallGroupArrayOutput
}

type FirewallGroupArray []FirewallGroupInput

func (FirewallGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*FirewallGroup)(nil)).Elem()
}

func (i FirewallGroupArray) ToFirewallGroupArrayOutput() FirewallGroupArrayOutput {
	return i.ToFirewallGroupArrayOutputWithContext(context.Background())
}

func (i FirewallGroupArray) ToFirewallGroupArrayOutputWithContext(ctx context.Context) FirewallGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallGroupArrayOutput)
}

// FirewallGroupMapInput is an input type that accepts FirewallGroupMap and FirewallGroupMapOutput values.
// You can construct a concrete instance of `FirewallGroupMapInput` via:
//
//          FirewallGroupMap{ "key": FirewallGroupArgs{...} }
type FirewallGroupMapInput interface {
	pulumi.Input

	ToFirewallGroupMapOutput() FirewallGroupMapOutput
	ToFirewallGroupMapOutputWithContext(context.Context) FirewallGroupMapOutput
}

type FirewallGroupMap map[string]FirewallGroupInput

func (FirewallGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*FirewallGroup)(nil)).Elem()
}

func (i FirewallGroupMap) ToFirewallGroupMapOutput() FirewallGroupMapOutput {
	return i.ToFirewallGroupMapOutputWithContext(context.Background())
}

func (i FirewallGroupMap) ToFirewallGroupMapOutputWithContext(ctx context.Context) FirewallGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FirewallGroupMapOutput)
}

type FirewallGroupOutput struct{ *pulumi.OutputState }

func (FirewallGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FirewallGroup)(nil)).Elem()
}

func (o FirewallGroupOutput) ToFirewallGroupOutput() FirewallGroupOutput {
	return o
}

func (o FirewallGroupOutput) ToFirewallGroupOutputWithContext(ctx context.Context) FirewallGroupOutput {
	return o
}

type FirewallGroupArrayOutput struct{ *pulumi.OutputState }

func (FirewallGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*FirewallGroup)(nil)).Elem()
}

func (o FirewallGroupArrayOutput) ToFirewallGroupArrayOutput() FirewallGroupArrayOutput {
	return o
}

func (o FirewallGroupArrayOutput) ToFirewallGroupArrayOutputWithContext(ctx context.Context) FirewallGroupArrayOutput {
	return o
}

func (o FirewallGroupArrayOutput) Index(i pulumi.IntInput) FirewallGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *FirewallGroup {
		return vs[0].([]*FirewallGroup)[vs[1].(int)]
	}).(FirewallGroupOutput)
}

type FirewallGroupMapOutput struct{ *pulumi.OutputState }

func (FirewallGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*FirewallGroup)(nil)).Elem()
}

func (o FirewallGroupMapOutput) ToFirewallGroupMapOutput() FirewallGroupMapOutput {
	return o
}

func (o FirewallGroupMapOutput) ToFirewallGroupMapOutputWithContext(ctx context.Context) FirewallGroupMapOutput {
	return o
}

func (o FirewallGroupMapOutput) MapIndex(k pulumi.StringInput) FirewallGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *FirewallGroup {
		return vs[0].(map[string]*FirewallGroup)[vs[1].(string)]
	}).(FirewallGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallGroupInput)(nil)).Elem(), &FirewallGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallGroupArrayInput)(nil)).Elem(), FirewallGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*FirewallGroupMapInput)(nil)).Elem(), FirewallGroupMap{})
	pulumi.RegisterOutputType(FirewallGroupOutput{})
	pulumi.RegisterOutputType(FirewallGroupArrayOutput{})
	pulumi.RegisterOutputType(FirewallGroupMapOutput{})
}
