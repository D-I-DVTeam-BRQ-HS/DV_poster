import pandas as pd
from pathlib import Path

# 在函数签名中添加 skiprows 参数，并设置默认值为 0
def read_all_txt_files(folder_path_str, sep='\t', header=None, encoding='utf-8', skiprows=0): 
    """
    遍历指定文件夹下的所有 TXT 文件，并合并成一个 DataFrame。
    新增参数 skiprows：用于跳过文件开头的指定行数。
    """
    folder_path = Path(folder_path_str)
    
    if not folder_path.is_dir():
        print(f"错误：文件夹 '{folder_path_str}' 不存在或不是一个目录。")
        return pd.DataFrame()
        
    txt_files = list(folder_path.glob('*.txt'))
    df_list = []
    
    # 将 skiprows 也加入读取参数中
    read_params = {'sep': sep, 'header': header, 'encoding': encoding, 'skiprows': skiprows} 
    
    print(f"\n--- [read.py] ---")
    # 打印提示信息，包含跳过行数
    print(f"在 '{folder_path_str}' 中找到 {len(txt_files)} 个文件，开始读取 (跳过每文件前 {skiprows} 行)...")

    for file_path in txt_files:
        try:
            # 读取数据时使用 **read_params 传入 skiprows
            df = pd.read_csv(file_path, **read_params)
            df['source_file'] = file_path.name
            df_list.append(df)
        except Exception as e:
            print(f"  - 警告：读取文件 {file_path.name} 失败。错误信息: {e}")

    if df_list:
        final_df = pd.concat(df_list, ignore_index=True)
        print(f"读取完成。总行数: {final_df.shape[0]}")
        return final_df
    else:
        print("未成功读取任何 TXT 文件。")
        return pd.DataFrame()

# 模块测试入口
if __name__ == "__main__":
    # 请替换为你的实际数据路径进行测试
    test_folder = './KR4h0115' 
    # 测试时传入 skiprows=9
    df_raw = read_all_txt_files(test_folder, skiprows=9) 
    if not df_raw.empty:
        print("\n测试数据前5行:")
        print(df_raw.head())