import pandas as pd
from collections import Counter
from typing import List, Dict, Tuple

# ----------------------------------------------------------------
# 1. 核心函数：统计全局词频
# ----------------------------------------------------------------
def get_global_word_counts(all_tokens: List[str], top_n: int) -> pd.DataFrame:
    """
    对所有作者的意象词语进行全局词频统计，并返回 Top N 结果。

    Args:
        all_tokens: 所有作品中提取到的有效意象词语列表。
        top_n: 需要返回的 Top N 数量。

    Returns:
        包含 Top N 词语及其频率的 Pandas DataFrame。
    """
    if not all_tokens:
        print("警告：全局词语列表为空，无法进行统计。")
        return pd.DataFrame(columns=['Word', 'Frequency'])

    # 使用 Counter 统计词频
    word_counts = Counter(all_tokens)
    
    # 获取 Top N
    top_words_data = word_counts.most_common(top_n)
    
    # 转换为 DataFrame
    df = pd.DataFrame(top_words_data, columns=['Word', 'Frequency'])
    
    print(f"\n--- 数据分析：全局 Top {len(df)} 意象词频统计完成 ---")
    return df


# ----------------------------------------------------------------
# 2. 核心函数：统计按作者分组的词频
# ----------------------------------------------------------------
def get_author_word_counts(tokens_by_author: Dict[str, List[str]]) -> Dict[str, Counter]:
    """
    对每个作者的意象词语进行单独的词频统计。

    Args:
        tokens_by_author: 字典 {作者: [意象词列表]}。

    Returns:
        字典 {作者: Counter对象}。
    """
    if not tokens_by_author:
        print("警告：按作者分组的意象词语字典为空，无法进行统计。")
        return {}
    
    author_word_counts = {}
    
    print("\n--- 数据分析：按作者进行词频统计 ---")
    
    for author, tokens in tokens_by_author.items():
        if tokens:
            author_word_counts[author] = Counter(tokens)
            print(f"  - 完成统计：{author} (词汇总数: {len(tokens)})")
        
    return author_word_counts

# ----------------------------------------------------------------
# 3. 模块测试入口
# ----------------------------------------------------------------
if __name__ == "__main__":
    print("--- 启动 analyzer.py 模块自检 ---")
    
    # 模拟 text_processor.py 的输出
    MOCK_ALL_TOKENS = [
        "明月", "青天", "十年", "生死", "潮州", "路", "明月", "青天", "潮州"
    ]
    
    MOCK_TOKENS_BY_AUTHOR = {
        "苏轼": ["明月", "青天", "十年", "生死", "明月", "青天"],
        "韩愈": ["潮州", "路", "潮州"],
        "柳宗元": ["山水", "清泉", "清泉"]
    }
    
    # 1. 全局统计 
    global_df = get_global_word_counts(MOCK_ALL_TOKENS, top_n=5)
    print("\n[全局 Top 5 结果]")
    print(global_df)
    
    # 2. 按作者统计
    author_counts = get_author_word_counts(MOCK_TOKENS_BY_AUTHOR)
    print("\n[作者词频示例：苏轼 Top 2]")
    print(author_counts["苏轼"].most_common(2))
    
    print("--- analyzer.py 模块自检完成 ---")