# ComfyUI-GateController
一个用于 ComfyUI 的实用插件，提供 Lora 加载状态的快速切换控制，帮助你在生成过程中灵活切换原始模型与加载 Lora 后的模型状态，提升工作流效率。

ComfyUI LoraGate 通断控制器
一个用于 ComfyUI 的实用插件，提供 Lora 加载状态的快速切换控制，帮助你在生成过程中灵活切换原始模型与加载 Lora 后的模型状态，提升工作流效率。
功能介绍
本插件包含两个节点，分别适用于不同的使用场景：
LoraGate 通断控制器：支持同时控制模型（MODEL）和 CLIP 的 Lora 状态切换
LoraGate 通断控制器（仅模型）：仅控制模型（MODEL）的 Lora 状态切换，适用于不需要 CLIP 控制的场景
通过简单的开关操作，你可以在生成过程中实时切换使用原始模型还是加载了 Lora 的模型，无需反复插拔节点，简化工作流设计。
安装方法
打开 ComfyUI 的custom_nodes目录
克隆本仓库：
bash
运行
git clone https://github.com/你的用户名/你的仓库名.git
重启 ComfyUI

使用说明：
节点位置：

安装后，两个节点会出现在 ComfyUI 的节点菜单中，路径为：Lora/控制器
LoraGate 通断控制器（两者）

照常连通model/clip,一份由lora连出，一份直接模型连出，通过开关控制on/off是否加载lora模型，后端照常连通下个节点



使用场景
快速对比同一 prompt 下原始模型与 Lora 模型的生成效果
在复杂工作流中关闭 / 开启 Lora 效果，无需重新连接节点及书写复杂的workflow，直接注释on/off即可。
