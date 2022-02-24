# Pdf2Img App

> 快速部署和体验Serverless架构下的PDF转图片的应用

- [Pdf2Img App](#pdf2img-app)
  - [体验前准备](#体验前准备)
  - [代码](#代码)
  - [快速部署和体验](#快速部署和体验)
    - [在线快速体验](#在线快速体验)
    - [在本地部署体验](#在本地部署体验)
  - [项目使用注意事项](#项目使用注意事项)
  - [应用详情](#应用详情)

## 体验前准备

该应用案例，需要您开通[阿里云函数计算](https://fcnext.console.aliyun.com/) 产品；并建议您当前的账号有一下权限存在`FCDefaultRole`。

## 代码

- [:octocat: 源代码](https://github.com/devsapp/start-pdf2img/tree/master/src)

## 快速部署和体验
### 在线快速体验

- 通过阿里云 **Serverless 应用中心**： 可以点击 [【🚀 部署】](https://fcnext.console.aliyun.com/applications/create?clone_url=https://github.com/huangfushan/hfs-test-5.git) ，按照引导填入参数，快速进行部署和体验。

<!-- mark, cloudshell 不支持 s build - 通过阿里云 **CloudShell**：可以点击 [【🏄 部署】](https://api.aliyun.com/new#/tutorial?action=git_open&git_repo=https://github.com/devsapp/devsapp-cloudshell-example.git&tutorial=tutorial/start-pdf2img.md) ，按照引导填入参数，快速进行部署和体验。 -->


### 在本地部署体验

1. 下载安装 Serverless Devs：`npm install @serverless-devs/s` 
    > 详细文档可以参考 [Serverless Devs 安装文档](https://github.com/Serverless-Devs/Serverless-Devs/blob/master/docs/zh/install.md)
2. 配置密钥信息：`s config add`
    > 详细文档可以参考 [阿里云密钥配置文档](https://github.com/devsapp/fc/blob/main/docs/zh/config.md)
3. 初始化项目：`s init start-pdf2img -d start-pdf2img`
4. 进入项目并部署：`cd start-pdf2img && s deploy`

> 在本地使用该项目时，不仅可以部署，还可以进行更多的操作，例如查看日志，查看指标，进行多种模式的调试等，这些操作详情可以参考[函数计算组件命令文档](https://github.com/devsapp/fc#%E6%96%87%E6%A1%A3%E7%9B%B8%E5%85%B3) ;

## 项目使用注意事项

项目Yaml中，声明了`actions`， 其对应的命令作用是 deploy 之前自动安装第三方依赖库， 同时 s deploy 部署的时候， 会自动增加相关的环境变量， 让您函数执行的时候能自动找到相关的依赖库。

## 应用详情

本应用是将 PDF 转 JPG 图片示例部署到阿里云函数计算（FC)。

通过 Serverless Devs 开发者工具，您只需要几步，就可以体验 Serverless 架构，带来的降本提效的技术红利。

部署完成之后，您可以看到系统返回给您的案例地址，例如：

![图片alt](https://img.alicdn.com/imgextra/i2/O1CN01FAltos1wqTJpEkTTR_!!6000000006359-2-tps-1776-584.png)

此时，可以 curl 调用函数， 然后可以得到一个 zip 包， zip 包里面是 pdf 每页截图的 jpg 文件

```bash
$ curl -d '{"pdf_url":"https://test-bucket.oss-cn-hangzhou.aliyuncs.com/test2.pdf"}' http://pdf2jpg.pdf2img.1986114430573743.cn-beijing.fc.devsapp.net > test.zip
```

-----

> - Serverless Devs 项目：https://www.github.com/serverless-devs/serverless-devs   
> - Serverless Devs 文档：https://www.github.com/serverless-devs/docs   
> - Serverless Devs 钉钉交流群：33947367    