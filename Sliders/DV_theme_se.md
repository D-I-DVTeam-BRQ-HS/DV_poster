---
marp: true
theme: academic
paginate: true
footer: " 2025.9 "
_class: position-layout



---
<!-- 定义两列布局的 CSS -->
<style>
.two-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}
</style>

<!-- 定义三列布局的 CSS -->
<style>
.three-columns {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    justify-items: center; /* 列内内容水平居中 */
    align-items: center;   /* 列内内容垂直居中 */
    align-items: start; /* 列内内容顶部对齐 */
    height: 100;         /* 确保容器高度占满父元素 */
}
</style>

<!-- 定义两行布局的 CSS -->
<style>
.two-rows {
    display: grid;
    grid-template-rows: 1fr 1fr;
    gap: 20px;
}
</style>

<style>
/* 自定义小字号样式 */
.small-text {
    font-size: 26px; /* 调整为需要的字号 */
}
</style>

<style>
  /* 矩形排布 */
  .two-column-list {
    display: flex;
    flex-wrap: wrap;  
  }
  .two-column-list > .left-col {
    width: 15%; /* 左边栏宽度，你可以根据内容调整 */
    text-align: left;
  }
  .two-column-list > .right-col {
    width: 16%; /* 右边栏宽度，与左边相加为 100% */
    text-align: right;
  }
</style>

<header></header>

<h1 style="font-size: 68px;">大数据可视分析导论</h1>
<h2 style="font-size: 48px; font-style: italic; margin-top: 0px;">主题选定汇报</h2>


<div style="margin-top: 50px;">  
<div class="two-column-list">
  <div class="left-col">指导老师</div>
  <div class="right-col">曹楠</div>
</div>

<div class="two-column-list">
  <div class="left-col">成员</div>
  <div class="right-col">白芊润 何山</div>
</div>
</div>

<!-- _paginate: skip --> # 不显示页码

---
<header>FRAMEWORK</header>
<div class="three-columns">
<div>

**动机**
  背景介绍
  选题价值

**关于数据**
  数据来源
  数据描述
  数据预处理
</div>
<div>

**可视化方案**
  可视化目标
  目标受众
  核心图表类型
  初步设计稿
</div>
<div>

**预期**
  预期成果
  预期洞察
  可能遇到的挑战 

**时间安排与分工**
  时间计划
  分工
</div>

---
<header>MOTIVATION</header>
<div class="two-rows">
<div>

**背景介绍**
<div class="small-text">
111
</div>
</div>
<div>

**选题价值**
<div class="small-text">
222
</div>

</div>  

---
<header>DATA</header>
<div class="three-columns">
<div>

**数据来源**
<div class="small-text">
111
</div>
</div>
<div>

**数据描述**
<div class="small-text">
222
</div>
</div>
<div>

**数据预处理**
<div class="small-text">
333
</div>
</div>
</div>

---
<header>BLUEPRINT</header>
<div class="three-columns">
<div>

**可视化目标**
<div class="small-text">
向大众介绍钟馗这个文化符号，弘扬中国传统文化。用
</div>
</div>
<div>

**目标受众**
<div class="small-text">
任何对中国传统文化或者钟馗这个文化符号感兴趣的人
</div>
</div>
<div>

**核心图表类型**
<div class="small-text">
333
</div>
</div>
</div>

---
<header>BLUEPRINT</header>
<div class="two-rows">
<div>

<style>
/* 整个幻灯片作为定位容器 */
.marp-slide {
  position: relative;
}

/* 左侧面板样式 */
.left-pane {
  position: absolute;
  top: 50%;
  left: 5%; /* 调整左侧距离 */
  transform: translateY(-50%); /* 垂直居中 */
  width: 60%; /* 调整宽度 */
}

/* 右侧面板样式 */
.right-pane {
  position: absolute;
  top: 50%;
  right: 5%; /* 调整右侧距离 */
  transform: translateY(-50%); /* 垂直居中 */
  width: 25%; /* 调整宽度 */
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 颜色色块样式 */
.color-swatch {
  width: 50px;
  height: 50px;
  margin: 15px; /* 调整这里的间距 */
  border: 1px solid #ddd;
}
</style>

<div class="split-container">
  <div class="left-pane">

  ![我的设计稿](design_mockup.png?fit)  
  </div>
  <div class="right-pane">
    <div class="color-swatch" style="background-color: #FF5733;"></div>
    <div class="color-swatch" style="background-color: #33FFBD;"></div>
    <div class="color-swatch" style="background-color: #3366FF;"></div>
  </div>
</div>

---
<header>EXPECTATION</header>
<div class="three-columns">
<div>

**预期成果**
<div class="small-text">
111
</div>
</div>
<div>

**预期洞察**
<div class="small-text">
222
</div>
</div>
<div>

**可能遇到的挑战**
<div class="small-text">
333
</div>
</div>
</div>


---
<header>ARRANGEMENTS  </header>
<div class="two-rows">
<div>

**时间计划**
<div class="small-text">
111
</div>
</div>
<div>

**分工**
<div class="small-text">
222
</div>
</div>
</div>

---
<!-- _paginate: skip --> # 不显示页码
<style>
/* 幻灯片容器需要是相对定位 */
.marp-slide {
  position: relative;
}

/* 文字容器 */
.center-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* 完美的居中技巧 */
  text-align: center;
}

/* 调整标题样式 */
h1 {
  font-size: 1.2em;
  color: #333;
}
</style>

<div class="center-text">
  <h1>Thanks for watching！</h1>
</div>

  


