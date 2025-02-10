
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-pdf2img-cap 帮助文档

<description>

本案例是将 pdf 转 img的逻辑封装成一个python函数，快速创建并部署到云原生应用开发平台 CAP。

</description>


## 资源准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  AliyunFCFullAccess | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |
| 日志服务 |  AliyunFCServerlessDevsRolePolicy | [帮助文档](https://help.aliyun.com/zh/sls) [计费文档](https://help.aliyun.com/zh/sls/product-overview/billing) |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [云原生应用开发平台 CAP](https://cap.console.aliyun.com/template-detail?template=start-pdf2img-cap) ，[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://cap.console.aliyun.com/template-detail?template=start-pdf2img-cap) 该应用。
   
</appcenter>
<deploy>
    
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例是将 pdf 转 img的逻辑封装成一个python函数，快速创建并部署到阿里云函数计算 FC。

运用了pdf2image 这一个 Python 库，专门用于将 PDF 文件转换为图像。这个库为 PDF 到图像的转换提供了简单的接口，并依赖于流行的开源软件 Poppler 工具进行实际的转换过程。

主要功能：

1、PDF 到图像的转换：能够将 PDF 页面转换为多种图像格式，如 JPEG、PNG 等。

2、定制选项：支持多种转换参数，包括分辨率、页面范围、单页图像输出等。

3、缩略图生成：快速生成 PDF 页面的缩略图。

通过 Serverless 开发平台，您只需要几步，就可以体验word 转 pdf，并享受 Serverless 架构带来的降本提效的技术红利。

</appdetail>







## 使用流程

<usedetail id="flushContent">

### 查看部署的案例

1、部署成功后，从资源信息栏，找到对应函数资源，点击函数名称跳转到函数计算控制台，如：
![](https://img.alicdn.com/imgextra/i1/O1CN012z93Rt28ZKAfNHqmj_!!6000000007946-0-tps-2038-430.jpg)
2、在代码页签，单击测试函数右侧的图标，从下拉列表中选择配置测试参数，输入如下示例测试参数，然后单击确定。
```bash
{
     "bucket" : "my-bucket",
     "region" : "cn-hangzhou",
     "src_object" : "test.pdf",
     "dst_object" : "test.zip"
}
```

其中：

|参数 |是否必填 |描述                      |
|--------|----------------|---------------------------|
| bucket | 必需 | pdf 文件所在的 bucket 名字 |
| region | 可选 | pdf 文件所在的 bucket 的 region, 不填默认使用函数所在的 region |
| src_object | 必需 | pdf 文件所在的 bucket 中的 object key |
| src_object | 必需 | 必须是 .zip 结尾, pdf 文件转成图片后的 zip 包所在的 object key |

3、单击测试函数，函数执行成功后，查看返回结果。

```bash
 SUCC
```
如果您需要使用 SDK 调用这个函数， 可以参考  [OpenAPI](https://next.api.aliyun.com/api/FC) 

您也可以使用 s 工具或者 SDK 调用函数，函数执行成功后， 就可以在 OSS 指定目标目录中得到一个 zip 包， zip 包里面是 pdf 每页截图的 jpg 文件

```bash
$ s invoke -e '{"bucket": "my-bucket", "region": "cn-hangzhou", "src_object": "test.pdf",  "dst_object": "test.zip"}'
```

</usedetail>

## 二次开发指南

<development id="flushContent">

您可以通过云端控制台 webIDE 的开发功能进行二次开发。

</development>






