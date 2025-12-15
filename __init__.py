# ComfyUI-GateController/__init__.py
# 仅注册 LoraGate 系列节点（移除 ImageGate 相关）

# 导入 LoraGate 完整版（Model+Clip）
try:
    from .lora_gate_node import NODE_CLASS_MAPPINGS as LORA_GATE_MAPPINGS
    from .lora_gate_node import NODE_DISPLAY_NAME_MAPPINGS as LORA_GATE_DISPLAY_MAPPINGS
except ImportError:
    # 导入失败时兜底，避免整个插件加载异常
    LORA_GATE_MAPPINGS = {}
    LORA_GATE_DISPLAY_MAPPINGS = {}

# 导入 LoraGate 仅模型版
try:
    from .lora_gate_node_only_model import NODE_CLASS_MAPPINGS as LORA_GATE_MODEL_ONLY_MAPPINGS
    from .lora_gate_node_only_model import NODE_DISPLAY_NAME_MAPPINGS as LORA_GATE_MODEL_ONLY_DISPLAY_MAPPINGS
except ImportError:
    LORA_GATE_MODEL_ONLY_MAPPINGS = {}
    LORA_GATE_MODEL_ONLY_DISPLAY_MAPPINGS = {}

# 合并所有 LoraGate 节点映射
NODE_CLASS_MAPPINGS = {
    **LORA_GATE_MAPPINGS,
    **LORA_GATE_MODEL_ONLY_MAPPINGS
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **LORA_GATE_DISPLAY_MAPPINGS,
    **LORA_GATE_MODEL_ONLY_DISPLAY_MAPPINGS
}

# ComfyUI 要求的固定暴露变量
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']