import torch

def variable_step_tensor(start, end, length):
    """
    生成一个变步长的一维张量，确保最后一个值是end。
    
    参数:
    start -- 序列的起始值
    end -- 序列的结束值
    length -- 生成的张量长度
    
    返回:
    一个一维张量，其步长逐渐减小，且最后一个值是end。
    """
    # 确保起始值小于结束值
    if start >= end:
        raise ValueError("起始值必须小于结束值")
    
    # 计算总步长
    total_step = end - start
    
    # 初始化张量
    t1=torch.linspace(0,1,length)
    t2=torch.tanh(3*t1)
    t2=t2/t2.max()
    out = start+t2*total_step
    
    return out

# 使用示例
start_value = 0
end_value = 50000
tensor_length = 100

# 生成张量
variable_step_tensor = variable_step_tensor(start_value, end_value, tensor_length)
print(variable_step_tensor)
