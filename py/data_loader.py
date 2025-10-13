import json
import os
from typing import List, Set

def load_data_from_file(file_path: str) -> list:
    """
    辅助函数：加载单个 JSON 文件中的作品数据。
    
    Args:
        file_path: 单个 JSON 文件的路径。
        
    Returns:
        该文件中的作品数据列表，或加载失败时返回空列表。
    """
    if not os.path.exists(file_path):
        return []
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # 确保加载的是列表类型
            if isinstance(data, list):
                return data
            else:
                # 打印警告而不是错误，以避免大量重复信息
                # print(f"警告：文件 {file_path} 内容不是预期的 JSON 列表格式，跳过。")
                return []
    except json.JSONDecodeError:
        print(f"警告：文件 {file_path} 格式不正确，跳过。")
        return []
    except Exception as e:
        print(f"警告：加载文件 {file_path} 时发生未知错误：{e}，跳过。")
        return []


def load_all_data_from_dirs(dir_paths: List[str]) -> list:
    """
    遍历指定目录列表，递归加载所有找到的 JSON 文件内容。
    
    Args:
        dir_paths: 包含 JSON 文件的目录路径列表。
        
    Returns:
        包含所有作品数据的合并列表。
    """
    all_combined_data = []
    total_files_found = 0
    
    print("--- 正在遍历目录并加载所有 JSON 数据文件 ---")
    
    for dir_path in dir_paths:
        if not os.path.isdir(dir_path):
            print(f"警告：目录 {dir_path} 不存在或不是目录，跳过。")
            continue
            
        # os.walk 会递归遍历 dir_path 下的所有子目录
        for root, _, files in os.walk(dir_path):
            for file_name in files:
                if file_name.endswith('.json'):
                    file_path = os.path.join(root, file_name)
                    total_files_found += 1
                    
                    # 使用辅助函数加载单个文件
                    file_data = load_data_from_file(file_path)
                    if file_data:
                        all_combined_data.extend(file_data)
                        
    print(f"总计在指定目录中找到 {total_files_found} 个 JSON 文件。")
    print(f"成功合并 {len(all_combined_data)} 条作品数据。")
    return all_combined_data


def filter_works_by_author(data: list, authors_list: List[str]) -> list:
    """
    从作品列表中筛选出指定作者的作品。（此函数逻辑保持不变）
    """
    if not data:
        return []

    target_authors = set(authors_list)

    filtered_data = [
        item for item in data
        if item.get("author") in target_authors
    ]

    authors_found = sorted(list(set(item.get('author') for item in filtered_data if item.get('author'))))
    print(f"\n--- 数据筛选结果 ---")
    print(f"筛选出 {len(filtered_data)} 篇唐宋八大家的作品。")
    if authors_found:
        print(f"包含的作者: {', '.join(authors_found)}")
    else:
        print("警告：未找到任何唐宋八大家的作品，请检查作者名单或数据。")

    return filtered_data


# ==============================================================================
# 5. 模块测试入口（请根据您的实际目录结构修改路径）
# ==============================================================================
if __name__ == "__main__":
    print("--- 启动 data_loader.py 模块自检 ---")
    
    # 【注意】请务必根据您的实际文件结构修改这些测试路径！
    TEST_DATA_DIRS = ['./chinese-poetry/全唐诗', './chinese-poetry/宋词'] 
    
    # 临时的唐宋八大家名单用于测试
    TEST_TANG_SONG_8 = [
        "韩愈", "柳宗元", "欧阳修", "苏轼", "蘇軾", "王安石"
    ]

    # 执行测试流程
    all_data = load_all_data_from_dirs(TEST_DATA_DIRS)
    
    if all_data:
        filter_works_by_author(all_data, TEST_TANG_SONG_8)
    
    print("--- data_loader.py 模块自检完成 ---")