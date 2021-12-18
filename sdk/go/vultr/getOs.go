// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vultr

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get information about operating systems that can be launched when creating a Vultr VPS.
//
// ## Example Usage
//
// Get the information for an operating system by `name`:
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
// 		_, err := vultr.GetOs(ctx, &GetOsArgs{
// 			Filters: []GetOsFilter{
// 				GetOsFilter{
// 					Name: "name",
// 					Values: []string{
// 						"CentOS 7 x64",
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
func GetOs(ctx *pulumi.Context, args *GetOsArgs, opts ...pulumi.InvokeOption) (*GetOsResult, error) {
	var rv GetOsResult
	err := ctx.Invoke("vultr:index/getOs:getOs", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOs.
type GetOsArgs struct {
	// Query parameters for finding operating systems.
	Filters []GetOsFilter `pulumi:"filters"`
}

// A collection of values returned by getOs.
type GetOsResult struct {
	// The architecture of the operating system.
	Arch string `pulumi:"arch"`
	// The family of the operating system.
	Family  string        `pulumi:"family"`
	Filters []GetOsFilter `pulumi:"filters"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name of the operating system.
	Name string `pulumi:"name"`
}

func GetOsOutput(ctx *pulumi.Context, args GetOsOutputArgs, opts ...pulumi.InvokeOption) GetOsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetOsResult, error) {
			args := v.(GetOsArgs)
			r, err := GetOs(ctx, &args, opts...)
			return *r, err
		}).(GetOsResultOutput)
}

// A collection of arguments for invoking getOs.
type GetOsOutputArgs struct {
	// Query parameters for finding operating systems.
	Filters GetOsFilterArrayInput `pulumi:"filters"`
}

func (GetOsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOsArgs)(nil)).Elem()
}

// A collection of values returned by getOs.
type GetOsResultOutput struct{ *pulumi.OutputState }

func (GetOsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetOsResult)(nil)).Elem()
}

func (o GetOsResultOutput) ToGetOsResultOutput() GetOsResultOutput {
	return o
}

func (o GetOsResultOutput) ToGetOsResultOutputWithContext(ctx context.Context) GetOsResultOutput {
	return o
}

// The architecture of the operating system.
func (o GetOsResultOutput) Arch() pulumi.StringOutput {
	return o.ApplyT(func(v GetOsResult) string { return v.Arch }).(pulumi.StringOutput)
}

// The family of the operating system.
func (o GetOsResultOutput) Family() pulumi.StringOutput {
	return o.ApplyT(func(v GetOsResult) string { return v.Family }).(pulumi.StringOutput)
}

func (o GetOsResultOutput) Filters() GetOsFilterArrayOutput {
	return o.ApplyT(func(v GetOsResult) []GetOsFilter { return v.Filters }).(GetOsFilterArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetOsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetOsResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name of the operating system.
func (o GetOsResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetOsResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetOsResultOutput{})
}
