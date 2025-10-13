import os
from typing import List, Set, Dict, Tuple
import jieba.posseg as psg
from collections import defaultdict
import re

# ----------------------------------------------------------------
# 1. 辅助函数：加载停用词 (与上次代码相同)
# ----------------------------------------------------------------
def load_stop_words(path: str) -> Set[str]:
    """从文件中加载停用词列表。"""
    if not os.path.exists(path):
        print(f"警告：未找到停用词文件在 {path}。将使用空停用词集合。")
        return set()
        
    try:
        with open(path, 'r', encoding='utf-8') as f:
            stop_words = set([line.strip() for line in f if line.strip()])
            print(f"成功加载 {len(stop_words)} 个停用词。")
            return stop_words
    except Exception as e:
        print(f"加载停用词时发生错误：{e}")
        return set()


# ----------------------------------------------------------------
# 2. 核心函数：意象提取和分词
# ----------------------------------------------------------------
def extract_imagery_tokens(
    filtered_data: List[dict], 
    stop_words: Set[str],
    pos_tags_to_keep: List[str]
) -> Tuple[List[str], Dict[str, List[str]]]:
    """
    将作品列表合并文本，进行分词，过滤停用词和词性，提取意象词语。
    同时按作者分组存储。

    Args:
        filtered_data: 筛选后的唐宋八大家作品列表。
        stop_words: 停用词集合。
        pos_tags_to_keep: 需要保留的词性标签列表。

    Returns:
        一个包含两个元素的元组：(all_tokens, tokens_by_author)
        all_tokens: 所有作品中提取到的有效意象词语列表。
        tokens_by_author: 字典 {作者: [意象词列表]}。
    """
    if not filtered_data:
        return [], {}

    print("\n--- 正在进行文本合并、分词与意象提取 ---")
    
    # 结果存储结构初始化
    all_tokens = []
    # 使用 defaultdict 自动创建作者键
    tokens_by_author = defaultdict(list)
    
    for item in filtered_data:
        author = item.get("author", "Unknown")
        
        # 1. 文本合并与清洗
        # paragraphs 列表合并成一个字符串
        full_text = "".join(item.get('paragraphs', []))
        # 移除空格、全角空格和换行符，进行标准化处理
        full_text = re.sub(r'[\s\u3000\n]', '', full_text)
        
        # 2. 意象提取/分词
        words = psg.cut(full_text)
        
        current_work_tokens = []
        for word, flag in words:
            # 过滤逻辑：
            # 1. 过滤停用词
            # 2. 过滤掉长度为 1 的字（意象多为双字或多字词）
            # 3. 过滤掉非目标词性（如动词、助词、副词等）
            if word not in stop_words and len(word) > 1 and flag in pos_tags_to_keep:
                current_work_tokens.append(word)

        # 3. 结果存储
        all_tokens.extend(current_work_tokens)
        tokens_by_author[author].extend(current_work_tokens)


    print(f"意象提取完成。共提取 {len(all_tokens)} 个有效意象词语。")
    print(f"已按 {len(tokens_by_author)} 位作者分组存储。")
    return all_tokens, dict(tokens_by_author)


# ==============================================================================
# 3. 模块测试入口（请确保你有 data_loader.py 和一个测试数据）
# ==============================================================================
if __name__ == "__main__":
    # 警告：此测试需要 data_loader.py 和数据文件才能正常运行
    print("--- 启动 text_processor.py 模块自检 ---")
    
    # 临时常量定义（需与 main.py 配置保持一致）
    # 请根据您的实际文件结构修改路径！
    TEST_STOP_WORDS_PATH = '../assets/chinese_stop_words.txt' 
    TEST_POS_TAGS = ['n', 'a'] # 简化词性
    
    # 模拟数据加载结果（理想情况下，应该导入 data_loader.py 来获取真实数据）
    MOCK_FILTERED_DATA = [
        {"author": "苏轼", "paragraphs": ["明月幾時有，把酒問青天。"]},
        {"author": "苏轼", "paragraphs": ["十年生死兩茫茫，不思量，自難忘。"]},
        {"author": "韩愈", "paragraphs": ["一封朝奏九重天，夕貶潮州路八千。"]},
    ]
    
    # 1. 加载停用词
    test_stop_words = load_stop_words(TEST_STOP_WORDS_PATH)
    
    # 2. 提取意象
    all_tokens, tokens_by_author = extract_imagery_tokens(
        MOCK_FILTERED_DATA, 
        test_stop_words, 
        TEST_POS_TAGS
    )
    
    print("\n[测试结果概览]")
    print(f"总意象数量: {len(all_tokens)}")
    print(f"苏轼意象数量: {len(tokens_by_author.get('苏轼', []))}")
    print(f"韩愈意象列表示例: {tokens_by_author.get('韩愈', [])[:5]}")
    
    print("--- text_processor.py 模块自检完成 ---")