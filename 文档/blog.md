# 博客项目

[TOC]

## 数据库表(Django模型)

### Category(类别)

|    字段名     | 字段说明 | 数据类型 | 允许为空 |    备注    |
| :-----------: | :------: | :------: | :------: | :--------: |
|      id       |  类别ID  |   整型   |    否    | 主键, 自增 |
| category_name | 类别名称 | 字符(15) |    否    |            |

### Article(文章)

|      字段名      |     字段说明     | 数据类型 | 允许为空 |    备注    |
| :--------------: | :--------------: | :------: | :------: | :--------: |
|        id        |      文章ID      |   整型   |    否    | 主键, 自增 |
|      title       |     文章标题     | 字符(50) |    否    |            |
|     category     |    文章类别ID    |   整型   |    否    |    外键    |
|     content      |     文章内容     |   文本   |    否    |            |
|      author      |    文章作者ID    |   整型   |    否    |    外键    |
|    post_date     |   文章发布日期   | 日期时间 |    否    |            |
| last_updated_date | 文章最后更新日期 | 日期时间 |    否    |            |

## 功能模块

### 分页器

```python
from django.core.paginator import Paginator
def paginator(articles, request):
    """文章分页器"""
    paginator = Paginator(articles, 5)  # 实例化分页器对象(传参分页对象列表, 每页数量)
    get_page_number = request.GET.get('page', 1)  # 获取url页面参数 默认为1
    current_page = paginator.get_page(get_page_number)  # 返回有效页面
    current_page_number = current_page.number  # 当前页面的页码
    # 页码范围 例: 当前页 5; 范围  3, 4, 5, 6, 7 判断 i 是否属于分页器范围内的页码
    page_number_range = [
        i for i in range(current_page_number-2, current_page_number+3) if i in paginator.page_range
    ]
    # 省略号标记
    if page_number_range[0] - 1 >= 2:
        page_number_range.insert(0, '...')
    if paginator.num_pages - page_number_range[-1] >= 2:
        page_number_range.append('...')
    # 添加第一页和最后一页
    if page_number_range[0] != 1:
        page_number_range.insert(0, 1)
    if page_number_range[-1] != paginator.num_pages:
        page_number_range.append(paginator.num_pages)
    return current_page, page_number_range # 返回当前页面和页码范围
```
