# python-utils

PythonUtils 是一个 Python 工具库，提供了一些常用的工具函数和类。

## 功能特性

### 数学工具 (math_utils)

提供了多种数字加法计算函数：

- **add()**: 基础加法函数，支持多个参数
- **add_list()**: 列表加法函数
- **safe_add()**: 安全加法函数，支持字符串转换

## 安装

```bash
# 克隆项目
git clone <repository-url>
cd python-utils

# 安装依赖（如果有的话）
pip install -r requirements.txt
```

## 使用方法

### 基础加法函数

```python
from python_utils import add

# 基础用法
result = add(1, 2, 3)  # 返回 6
print(result)

# 支持浮点数
result = add(1.5, 2.5, 3.0)  # 返回 7.0
print(result)

# 支持Decimal类型（高精度计算）
from decimal import Decimal
result = add(Decimal('1.1'), Decimal('2.2'))  # 返回 Decimal('3.3')
print(result)

# 混合类型（自动转换为Decimal保持精度）
result = add(1, 2.5, Decimal('3.3'))  # 返回 Decimal('6.8')
print(result)
```

### 列表加法函数

```python
from python_utils.math_utils import add_list

# 计算列表中所有数字的和
numbers = [1, 2, 3, 4, 5]
result = add_list(numbers)  # 返回 15
print(result)

# 支持浮点数列表
float_numbers = [1.1, 2.2, 3.3]
result = add_list(float_numbers)  # 返回 6.6
print(result)
```

### 安全加法函数

```python
from python_utils.math_utils import safe_add

# 自动转换字符串为数字
result = safe_add("1", "2", 3)  # 返回 6
print(result)

# 处理浮点数字符串
result = safe_add("1.5", "2.5")  # 返回 4.0
print(result)

# 无法转换时返回None
result = safe_add("abc", 1)  # 返回 None
print(result)
```

## API 文档

### add(*args)

计算多个数字的加法。

**参数:**
- `*args`: 要相加的数字，支持int、float、Decimal类型

**返回值:**
- `Union[int, float, Decimal]`: 所有参数的和

**异常:**
- `TypeError`: 当参数不是数字类型时
- `ValueError`: 当没有提供参数时

### add_list(numbers)

计算列表中所有数字的加法。

**参数:**
- `numbers`: 包含数字的列表

**返回值:**
- `Union[int, float, Decimal]`: 列表中所有数字的和

**异常:**
- `TypeError`: 当参数不是列表或列表中包含非数字类型时
- `ValueError`: 当列表为空时

### safe_add(*args)

安全的加法函数，会尝试将字符串转换为数字。

**参数:**
- `*args`: 要相加的值，支持int、float、str类型

**返回值:**
- `Union[int, float, None]`: 所有参数的和，如果转换失败返回None

## 许可证

请查看 LICENSE 文件了解详细信息。