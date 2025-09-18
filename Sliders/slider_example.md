---
marp: true                 # 启用 Marp
theme: default             # default / gaia / uncover …
paginate: true             # 是否自动加页码
size: 16:9                 # 4:3 / 16:9 / A4 …
headingDivider: 2          # 用 ## 自动分页（可省 ---）
---

# 我是封面

---

## 列表页
- 点 1
- 点 2


| 语法                                   | 效果             |
| -------------------------------------- | ---------------- |
| `<!-- _class: lead -->`                | 本页居中封面风格 |
| `<!-- _paginate: skip -->`             | 本页不显示页码   |
| `<!-- backgroundColor: #123 -->`       | 本页背景色       |
| `<!-- backgroundImage: url('...') -->` | 本页背景图       |
| `<!-- class: invert -->`               | 本页反色主题     |


![bg](img.jpg)            # 全屏背景（bg = background）
![bg right:40%](img.jpg)   # 右侧 40 % 宽度，剩余空间写字
![bg cover](img.jpg)       # 铺满（contain 等比缩放）
![bg auto right](img.jpg)  # 自动高度 + 右对齐
![bg blur:10px](img.jpg)   # 背景虚化（v3.6+）


---
# 两栏图文

![bg left:45%](pic.jpg)

::: column
## 右侧标题
- 要点 1
- 要点 2
:::


---
style: |
  h1 { color: #ff0066; }
  section { justify-content: flex-start; }
---


/* 三列文本 */
.multicolumn { column-count: 3; gap: 20px; }

/* 网格 */
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }

/* 淡入动画 */
@keyframes fadeIn { from {opacity:0} to {opacity:1} }
.fade { animation: fadeIn 1s ease-in-out; }


---

## 渐进列表

- 第一项 <!-- element class="fade" -->
- 第二项 <!-- element class="fade" data-delay="200" -->


---
## 标题

正文内容

<!--
备注：这里写给讲者自己看，不会投屏。
-->


<!-- backgroundColor: 🌈 -->   # 背景emoji


# 自动页眉页脚
---
header: "**CONFIDENTIAL**"
footer: "© 2025  作者"
---