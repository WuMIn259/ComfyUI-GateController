# 适配ComfyUI的模型/Clip类型
from typing import Tuple

class LoraGateNode:
    @classmethod
    def INPUT_TYPES(cls) -> dict:
        return {
            "required": {
                # 原始模型/Clip（未加载Lora的输入）
                "original_model": ("MODEL",),
                "original_clip": ("CLIP",),
                # 加载Lora后的模型/Clip（Load Lora节点的输出）
                "lora_model": ("MODEL",),
                "lora_clip": ("CLIP",),
                # 通断开关：ON=走Lora，OFF=走原始
                "switch": (["ON", "OFF"], {"default": "OFF"}),
            }
        }

    # 输出类型需匹配ComfyUI标准：MODEL和CLIP
    RETURN_TYPES: Tuple[str, str] = ("MODEL", "CLIP")
    RETURN_NAMES: Tuple[str, str] = ("output_model", "output_clip")
    FUNCTION: str = "control_lora"
    CATEGORY: str = "Lora/控制器"  # 左侧菜单分类

    def control_lora(
        self,
        original_model,
        original_clip,
        lora_model,
        lora_clip,
        switch: str
    ) -> Tuple[object, object]:
        """根据开关选择输出对应的Model和Clip"""
        if switch == "ON":
            # 开关打开：输出Lora后的模型/Clip
            return (lora_model, lora_clip)
        else:
            # 开关关闭：输出原始模型/Clip
            return (original_model, original_clip)


# 节点注册映射（必须）
NODE_CLASS_MAPPINGS = {
    "LoraGateNode": LoraGateNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoraGateNode": "LoraGate通断控制器"
}