# AI简历分析助手

一个基于Python + Flask + DeepSeek API开发的Web应用，支持上传PDF简历，自动提取文本并调用大语言模型进行分析，返回优缺点和改进建议。

## 功能

- PDF简历上传与文本提取
- 调用DeepSeek API进行智能分析
- 网页端实时展示分析结果

## 技术栈

- **后端**：Python, Flask
- **PDF解析**：PyPDF2
- **AI能力**：DeepSeek API
- **前端**：HTML, JavaScript（原生）

## 项目背景

在准备暑期实习投递的过程中，发现市面上缺少针对在校生的简历快速反馈工具，因此开发了这个小工具，用于自动分析简历内容、给出改进建议。

## 运行方式

```bash
pip install flask PyPDF2 requests
python app.py
```

访问 `http://127.0.0.1:5001`

## 待完善功能
- [ ] 部署到公网（Railway/Render）
- [ ] 增加面试模拟问题生成

## 开发说明

本项目为个人学习项目，开发过程中使用AI工具（Claude/ChatGPT）辅助调试和学习，核心架构设计与功能实现独立完成。
