import pandas as pd
from opencc import OpenCC

# 初始化 OpenCC 转换器
converter = OpenCC('t2s.json')

def convert_to_simplified(text):
    """OpenCC 转换的封装函数，安全处理缺失值。"""
    if pd.isna(text) or text is None:
        return text 
    return converter.convert(str(text))

def convert_dataframe(df_input, columns_to_convert):
    """
    接收一个 DataFrame，对其指定列进行繁体到简体的转换，并返回新 DataFrame。
    """
    df_output = df_input.copy()  # 创建副本以避免修改原始数据
    
    print("\n--- [convert.py] ---")
    if df_output.empty:
        print("输入 DataFrame 为空，跳过转换。")
        return df_output

    print("开始批量转换繁体中文到简体中文...")
    
    for col in columns_to_convert:
        if col in df_output.columns:
            # 批量应用转换函数
            df_output[col] = df_output[col].apply(convert_to_simplified)
            print(f"✔ 列 '{col}' 转换完成。")
        else:
            print(f"⚠ 警告：未在 DataFrame 中找到列 '{col}'，跳过转换。")
            
    print("转换完成。")
    return df_output

if __name__ == "__main__":
    # 模块测试：使用示例数据测试转换功能
    data = {'标题': ['靜夜思', '將進酒'], '作者': ['李白', '李太白'], '文本': ['床前明月光', '君不見']}
    df_test = pd.DataFrame(data)
    
    df_converted = convert_dataframe(df_test, ['标题', '文本'])
    print("\n测试转换结果:")
    print(df_converted)