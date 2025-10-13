# main.py

# ==============================================================================
# 0. 配置和常量定义
# ==============================================================================
import os
import sys
import json
import pandas as pd
from collections import Counter # 【修正】新增导入 Counter
from typing import Dict # 【修正】新增导入 Dict 用于类型提示

# 文件路径配置：请根据您的实际目录结构进行核对！
DATA_DIRS = ['./chinese-poetry/全唐诗', './chinese-poetry/宋词'] 
STOP_WORDS_PATH = 'assets/chinese_stop_words.txt' 
FONT_PATH = 'assets/simhei.ttf' 

# 唐宋八大家作者列表 (包含常见的繁体和简体形式)
TANG_SONG_8 = [
    "韩愈", "柳宗元", 
    "欧阳修", "苏洵", "苏轼", "苏辙", "曾巩", "王安石",
    "韓愈", "柳宗元", 
    "歐陽修", "蘇洵", "蘇軾", '蘇轍', "曾鞏", "王安石"
]

# 用于意象提取的词性标签（主要保留名词和形容词）
POS_TAGS_TO_KEEP = ['n', 'nr', 'ns', 'nt', 'a'] 

# 统计配置
TOP_N_WORDS = 30


# ==============================================================================
# 1. 模块导入与主执行流程
# ==============================================================================

try:
    from data_loader import load_all_data_from_dirs, filter_works_by_author
    from text_processor import load_stop_words, extract_imagery_tokens 
    from analyzer import get_global_word_counts, get_author_word_counts 
except ImportError as e:
    print(f"致命错误：无法导入所需的模块。请检查模块文件是否存在且位于同一目录。错误详情: {e}")
    sys.exit(1)


def print_author_top_n(author_counts: Dict[str, Counter], top_n: int):
    """打印每个作者的 Top N 词频表格"""
    for author, counts in author_counts.items():
        top_words = counts.most_common(top_n)
        
        # 将结果转换为 DataFrame 以便格式化打印
        df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
        
        print(f"\n--- 作者: {author} (Top {top_n} 意象词汇表) ---")
        # 使用 to_string(index=False) 确保整个表格被打印且格式整齐
        print(df.to_string(index=False)) 
        print("-" * (len(f"--- 作者: {author} (Top {top_n} 意象词汇表) ---")))


def main():
    print("-" * 50)
    print("--- 启动唐宋八大家意象分析项目 ---")
    print(f"当前工作目录: {os.getcwd()}")
    print("-" * 50)
    
    # ------------------------------------------------------------------
    # 1. 数据加载与筛选 (Data Loading and Filtering)
    # ------------------------------------------------------------------
    print("\n--- 阶段 1: 数据加载与筛选 ---")
    
    for d in DATA_DIRS:
        if not os.path.isdir(d):
            print(f"【严重警告】配置的数据目录不存在: {d}")
    
    all_data = load_all_data_from_dirs(DATA_DIRS)
    
    if not all_data:
        print("程序终止：数据加载失败或文件内容为空。")
        return

    ts8_data = filter_works_by_author(all_data, TANG_SONG_8)
    
    if not ts8_data:
        print("程序终止：筛选结果为空，未找到唐宋八大家的作品。")
        return
        
    print(f"\n成功获取 {len(ts8_data)} 篇作品，流程继续...")
    
    # ------------------------------------------------------------------
    # 2. 文本处理 (Text Processing)
    # ------------------------------------------------------------------
    print("\n--- 阶段 2: 文本处理与意象提取 ---")
    
    stop_words = load_stop_words(STOP_WORDS_PATH)
    
    all_tokens, tokens_by_author = extract_imagery_tokens(
        ts8_data, 
        stop_words, 
        POS_TAGS_TO_KEEP
    )
    
    if not all_tokens:
        print("程序终止：未提取到任何有效意象词语。")
        return
        
    print("文本处理阶段完成，准备进入数据分析阶段...")
    
    # ------------------------------------------------------------------
    # 3. 数据分析 (Analysis)
    # ------------------------------------------------------------------
    print("\n--- 阶段 3: 数据分析与词频统计 ---")
    
    global_word_counts_df = get_global_word_counts(all_tokens, TOP_N_WORDS)
    author_word_counts = get_author_word_counts(tokens_by_author)
    
    if global_word_counts_df.empty:
        print("程序终止：数据分析结果为空。")
        return
        
    # 3.3. 打印全局 Top N 词汇表
    print(f"\n--- 全局 Top {TOP_N_WORDS} 意象词汇表 ---")
    print(global_word_counts_df.to_string(index=False))
    print("-" * 35)
    
    # 3.4. 打印每个作者的 Top N 词汇表
    print_author_top_n(author_word_counts, TOP_N_WORDS)
    
    
    # ------------------------------------------------------------------
    # 4. 数据可视化 (Visualization) - 仅打印完成信息
    # ------------------------------------------------------------------
    print("\n--- 项目分析已全部完成 ---")
    print("请根据终端输出的词频表格手动制作图表。")
    print("-" * 50)


if __name__ == "__main__":
    main()