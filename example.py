#!/usr/bin/env python3
"""
PythonUtils 加法函数使用示例

演示如何使用 python_utils 库中的各种加法函数。
"""

from python_utils import add
from python_utils.math import add_list, safe_add
from decimal import Decimal


def main():
    print("=== PythonUtils 加法函数示例 ===\n")
    
    # 1. 基础加法函数示例
    print("1. 基础加法函数 add()")
    print("-" * 30)
    
    # 整数加法
    result1 = add(1, 2, 3, 4, 5)
    print(f"add(1, 2, 3, 4, 5) = {result1}")
    
    # 浮点数加法
    result2 = add(1.5, 2.5, 3.0)
    print(f"add(1.5, 2.5, 3.0) = {result2}")
    
    # Decimal高精度加法
    result3 = add(Decimal('1.1'), Decimal('2.2'), Decimal('3.3'))
    print(f"add(Decimal('1.1'), Decimal('2.2'), Decimal('3.3')) = {result3}")
    
    # 混合类型加法
    result4 = add(1, 2.5, Decimal('3.3'))
    print(f"add(1, 2.5, Decimal('3.3')) = {result4}")
    print()
    
    # 2. 列表加法函数示例
    print("2. 列表加法函数 add_list()")
    print("-" * 30)
    
    # 整数列表
    numbers1 = [1, 2, 3, 4, 5]
    result5 = add_list(numbers1)
    print(f"add_list({numbers1}) = {result5}")
    
    # 浮点数列表
    numbers2 = [1.1, 2.2, 3.3, 4.4]
    result6 = add_list(numbers2)
    print(f"add_list({numbers2}) = {result6}")
    
    # Decimal列表
    numbers3 = [Decimal('0.1'), Decimal('0.2'), Decimal('0.3')]
    result7 = add_list(numbers3)
    print(f"add_list([Decimal('0.1'), Decimal('0.2'), Decimal('0.3')]) = {result7}")
    print()
    
    # 3. 安全加法函数示例
    print("3. 安全加法函数 safe_add()")
    print("-" * 30)
    
    # 字符串数字加法
    result8 = safe_add("1", "2", "3")
    print(f"safe_add('1', '2', '3') = {result8}")
    
    # 混合类型安全加法
    result9 = safe_add("1.5", 2, "3.5")
    print(f"safe_add('1.5', 2, '3.5') = {result9}")
    
    # 包含无效字符串的情况
    result10 = safe_add("1", "abc", "3")
    print(f"safe_add('1', 'abc', '3') = {result10}")
    
    # 空参数情况
    result11 = safe_add()
    print(f"safe_add() = {result11}")
    print()
    
    # 4. 错误处理示例
    print("4. 错误处理示例")
    print("-" * 30)
    
    try:
        # 尝试传入非数字类型
        add(1, "abc", 3)
    except TypeError as e:
        print(f"TypeError: {e}")
    
    try:
        # 尝试不传入任何参数
        add()
    except ValueError as e:
        print(f"ValueError: {e}")
    
    try:
        # 尝试传入空列表
        add_list([])
    except ValueError as e:
        print(f"ValueError: {e}")
    
    print("\n=== 示例结束 ===")


if __name__ == "__main__":
    main()