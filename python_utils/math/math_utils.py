"""
数学工具模块

提供常用的数学计算函数。
"""

from typing import Union, List
from decimal import Decimal


def add(*args: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
    """
    计算多个数字的加法。
    
    支持整数、浮点数和Decimal类型的加法运算。
    可以接受任意数量的参数进行相加。
    
    Args:
        *args: 要相加的数字，支持int、float、Decimal类型
        
    Returns:
        Union[int, float, Decimal]: 所有参数的和
        
    Raises:
        TypeError: 当参数不是数字类型时抛出
        ValueError: 当没有提供参数时抛出
        
    Examples:
        >>> add(1, 2, 3)
        6
        >>> add(1.5, 2.5)
        4.0
        >>> add(Decimal('1.1'), Decimal('2.2'))
        Decimal('3.3')
        >>> add(1, 2.5, Decimal('3.3'))
        Decimal('6.8')
    """
    if not args:
        raise ValueError("至少需要提供一个参数")
    
    # 检查所有参数是否为数字类型
    for arg in args:
        if not isinstance(arg, (int, float, Decimal)):
            raise TypeError(f"参数必须是数字类型，得到: {type(arg).__name__}")
    
    # 如果有Decimal类型，将所有参数转换为Decimal以保持精度
    if any(isinstance(arg, Decimal) for arg in args):
        return sum(Decimal(str(arg)) for arg in args)
    
    # 如果有浮点数，返回浮点数结果
    if any(isinstance(arg, float) for arg in args):
        return sum(args)
    
    # 全部是整数，返回整数结果
    return sum(args)


def add_list(numbers: List[Union[int, float, Decimal]]) -> Union[int, float, Decimal]:
    """
    计算列表中所有数字的加法。
    
    Args:
        numbers: 包含数字的列表
        
    Returns:
        Union[int, float, Decimal]: 列表中所有数字的和
        
    Raises:
        TypeError: 当参数不是列表或列表中包含非数字类型时抛出
        ValueError: 当列表为空时抛出
        
    Examples:
        >>> add_list([1, 2, 3, 4])
        10
        >>> add_list([1.1, 2.2, 3.3])
        6.6
    """
    if not isinstance(numbers, list):
        raise TypeError("参数必须是列表类型")
    
    if not numbers:
        raise ValueError("列表不能为空")
    
    return add(*numbers)


def safe_add(*args: Union[int, float, str]) -> Union[int, float, None]:
    """
    安全的加法函数，会尝试将字符串转换为数字。
    
    Args:
        *args: 要相加的值，支持int、float、str类型
        
    Returns:
        Union[int, float, None]: 所有参数的和，如果转换失败返回None
        
    Examples:
        >>> safe_add(1, "2", 3.5)
        6.5
        >>> safe_add("1.5", "2.5")
        4.0
        >>> safe_add("abc", 1)
        None
    """
    if not args:
        return None
    
    converted_args = []
    
    for arg in args:
        try:
            if isinstance(arg, str):
                # 尝试转换为整数
                if '.' not in arg:
                    converted_args.append(int(arg))
                else:
                    converted_args.append(float(arg))
            elif isinstance(arg, (int, float)):
                converted_args.append(arg)
            else:
                return None
        except (ValueError, TypeError):
            return None
    
    return add(*converted_args)