### django 搭建博客系统django 搭建博客系统

- 前端基于 bootstrap3 框架实现
- django 版本 2.0.2
- mysql 数据库
- 支持 makedown ，基于 [Editor.md](https://pandao.github.io/editor.md/index.html "Editor.md") 实现 makedown


#####ACT 博客内容类型
```python
ACT_HTML = 1      # html 内容
ACT_MD_TEXT = 2   # makedown 内容
ACT_MD_FILE = 3   # makedown 文件
```

当 ACT_MD_FILE 类型时，文件名称规则[article type]-[name].md，这样就会把上传的 *.md 自动上传到 article type 类型的目录内，否则会上传到article的根目录下。