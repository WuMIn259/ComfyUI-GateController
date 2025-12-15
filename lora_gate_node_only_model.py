# 适配ComfyUI仅Model类型的Lora控制
from typing import Tuple

class LoraGateNodeOnlyModel:
    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                # 原始Model（未加载Lora的输入）
                "original_model": ("MODEL",),
                # 仅加载Lora后的Model（Load Lora节点的model输出）
                "lora_model": ("MODEL",),
                # 通断开关：ON=走Lora Model，OFF=走原始Model
                "switch": (["ON", "OFF"], {"default": "OFF"}),
            }
        }

    # 仅输出MODEL类型，匹配ComfyUI标准
    RETURN_TYPES: Tuple[str] = ("MODEL",)
    RETURN_NAMES: Tuple[str] = ("output_model",)
    FUNCTION: str = "control_lora_model"
    CATEGORY: str = "Lora/控制器"  # 与完整版同分类，方便查找

    def control_lora_model(
        self,
        original_model,
        lora_model,
        switch: str
    ) -> Tuple[object]:
        """仅控制Model的通断，适配仅Model类型的Lora"""
        if switch == "ON":
            # 开关打开：输出Lora后的Model
            return (lora_model,)
        else:
            # 开关关闭：输出原始Model
            return (original_model,)


# 节点注册映射
NODE_CLASS_MAPPINGS = {
    "LoraGateNodeOnlyModel": LoraGateNodeOnlyModel
}

# 节点显示名增加「（仅模型）」标识
NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraGateNodeOnlyModel": "LoraGate通断控制器（仅模型）"
}