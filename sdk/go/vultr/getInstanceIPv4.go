// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vultr

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about a Vultr instance IPv4.
//
// ## Example Usage
//
// Get the information for an IPv4 address by `instanceId`:
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
// 		_, err := vultr.LookupInstanceIPv4(ctx, &GetInstanceIPv4Args{
// 			Filters: []GetInstanceIPv4Filter{
// 				GetInstanceIPv4Filter{
// 					Name: "ip",
// 					Values: []string{
// 						"123.123.123.123",
// 					},
// 				},
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupInstanceIPv4(ctx *pulumi.Context, args *LookupInstanceIPv4Args, opts ...pulumi.InvokeOption) (*LookupInstanceIPv4Result, error) {
	var rv LookupInstanceIPv4Result
	err := ctx.Invoke("vultr:index/getInstanceIPv4:getInstanceIPv4", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getInstanceIPv4.
type LookupInstanceIPv4Args struct {
	// Query parameters for finding IPv4 address.
	Filters []GetInstanceIPv4Filter `pulumi:"filters"`
}

// A collection of values returned by getInstanceIPv4.
type LookupInstanceIPv4Result struct {
	Filters []GetInstanceIPv4Filter `pulumi:"filters"`
	// The gateway IP address.
	Gateway string `pulumi:"gateway"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The ID of the instance the IPv4 address.
	InstanceId string `pulumi:"instanceId"`
	// The IPv4 address in canonical format.
	Ip string `pulumi:"ip"`
	// The IPv4 netmask in dot-decimal notation.
	Netmask string `pulumi:"netmask"`
	// The reverse DNS information for this IP address.
	Reverse string `pulumi:"reverse"`
}

func LookupInstanceIPv4Output(ctx *pulumi.Context, args LookupInstanceIPv4OutputArgs, opts ...pulumi.InvokeOption) LookupInstanceIPv4ResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupInstanceIPv4Result, error) {
			args := v.(LookupInstanceIPv4Args)
			r, err := LookupInstanceIPv4(ctx, &args, opts...)
			return *r, err
		}).(LookupInstanceIPv4ResultOutput)
}

// A collection of arguments for invoking getInstanceIPv4.
type LookupInstanceIPv4OutputArgs struct {
	// Query parameters for finding IPv4 address.
	Filters GetInstanceIPv4FilterArrayInput `pulumi:"filters"`
}

func (LookupInstanceIPv4OutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceIPv4Args)(nil)).Elem()
}

// A collection of values returned by getInstanceIPv4.
type LookupInstanceIPv4ResultOutput struct{ *pulumi.OutputState }

func (LookupInstanceIPv4ResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupInstanceIPv4Result)(nil)).Elem()
}

func (o LookupInstanceIPv4ResultOutput) ToLookupInstanceIPv4ResultOutput() LookupInstanceIPv4ResultOutput {
	return o
}

func (o LookupInstanceIPv4ResultOutput) ToLookupInstanceIPv4ResultOutputWithContext(ctx context.Context) LookupInstanceIPv4ResultOutput {
	return o
}

func (o LookupInstanceIPv4ResultOutput) Filters() GetInstanceIPv4FilterArrayOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) []GetInstanceIPv4Filter { return v.Filters }).(GetInstanceIPv4FilterArrayOutput)
}

// The gateway IP address.
func (o LookupInstanceIPv4ResultOutput) Gateway() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) string { return v.Gateway }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupInstanceIPv4ResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the instance the IPv4 address.
func (o LookupInstanceIPv4ResultOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) string { return v.InstanceId }).(pulumi.StringOutput)
}

// The IPv4 address in canonical format.
func (o LookupInstanceIPv4ResultOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) string { return v.Ip }).(pulumi.StringOutput)
}

// The IPv4 netmask in dot-decimal notation.
func (o LookupInstanceIPv4ResultOutput) Netmask() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) string { return v.Netmask }).(pulumi.StringOutput)
}

// The reverse DNS information for this IP address.
func (o LookupInstanceIPv4ResultOutput) Reverse() pulumi.StringOutput {
	return o.ApplyT(func(v LookupInstanceIPv4Result) string { return v.Reverse }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupInstanceIPv4ResultOutput{})
}
