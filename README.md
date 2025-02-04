[English](README_en.md) | 简体中文

[![向量脉络](resources/images/vector-vein-with-text-primary-zh.svg)](https://vectorvein.com)

# 🔀 向量脉络 VectorVein

利用AI的力量构建您的个人知识库+自动化工作流程。

无需编程，只需拖拽即可创建强大的工作流，自动化所有任务。

[![在线版向量脉络](resources/images/demo-zh.gif)](https://github.com/AndersonBY/vector-vein)

向量脉络是受到 [LangChain](https://github.com/hwchase17/langchain) 以及 [langflow](https://github.com/logspace-ai/langflow) 的启发而开发的无代码AI工作流软件，旨在结合大语言模型的强大能力并让用户通过简单的拖拽即可实现各类日常工作流的智能化和自动化。

## 🌐 在线体验

您可以在 [这里](https://vectorvein.com) 体验向量脉络的在线版本，无需下载安装。

## 📦 安装及配置

### 安装

下载后打开VectorVein软件，初次打开时程序会在安装目录下创建data文件夹，用于存放数据库及静态文件资源。

软件采用了pywebview搭建，基于webview2内核，因此需要安装webview2运行时，如果出现软件无法打开，可能需要手动下载webview2运行时，下载地址：[https://developer.microsoft.com/zh-cn/microsoft-edge/webview2/](https://developer.microsoft.com/zh-cn/microsoft-edge/webview2/)

### 配置

软件正常打开后点击打开设置按钮，请填入OpenAI的API Key以使用AI功能，并选择输出文件夹用于存放工作流输出时的文件。如果需要用到邮件发送的功能请在设置页面一并填入邮箱信息。

![设置](resources/images/settings1-zh.jpg)

## 💻 使用方式

### 📖 基本概念

一个工作流代表了一个工作任务流程，包含了输入、输出以及工作流的触发方式。你可以任意定义输入是什么，输出是什么，以及输入是如何处理并到达输出结果的。

几个例子：

- **翻译工作流**，输入是一个英文的Word文档，输出也是Word文档，你可以设计工作流将输入的中文文档翻译后生成中文文档。
- **思维导图工作流**，如果将翻译工作流的输出改为思维导图，那么你就可以得到一个读取英文Word文档并总结为中文思维导图的工作流。
- **网络文章摘要工作流**，如果将思维导图工作流的输入改为网络文章的URL，那么你就可以得到一个读取网络文章并总结为中文思维导图的工作流。
- **客户差评自动分类工作流**，输入是一个包含差评内容的表格，并自定义需要分类的关键词，即可自动将差评分类，输出就是自动生成包含分类结果的Excel表格。

### 🔎 使用界面

每个工作流都有一个**使用界面**和一个**编辑界面**，使用界面用于日常运行工作流，编辑界面用于编辑工作流。通常而言一个设计好的工作流您平时只需要在使用界面中运行即可，不需要再去编辑界面中修改。

![使用界面](resources/images/user-interface1-zh.jpg)

使用界面如上所示，分为输入、输出、触发器（通常是一个运行按钮）三个部分。日常使用可以直接输入内容，点击运行按钮即可在输出看到结果。

想查看运行过的工作流可以点击【工作流运行记录】，如下图所示。

![工作流运行记录](resources/images/workflow-record-zh.jpg)

### ✏️ 创建工作流

您可以添加我们提供的官方模板到自己的工作流中，也可以自己创建一个新的工作流。刚开始时建议先用官方模板熟悉一下工作流的使用。

![工作流编辑界面](resources/images/editor-zh.jpg)

工作流编辑界面如上图所示，顶部可以编辑名称、标签以及详细描述。左侧是工作流的节点列表，右侧是工作流的画布，您可以从左侧找到想要的节点拖拽到画布中，然后通过连线连接节点，形成工作流。

您可以查看一个简易的爬虫+AI总结思维导图工作流的[创建教学](TUTORIAL.md)。

## 📄 协议

向量脉络是一个开源的软件，支持个人非商业使用，具体协议请参考 [LICENSE](LICENSE.md)。