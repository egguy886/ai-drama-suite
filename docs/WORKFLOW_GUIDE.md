# AI 短剧工业级生产工作流 Skill 集合（升级优化版）

> 本集合融合了 **开源电影理论体系（好莱坞视听与物理控制）** 与 **MiniMax H3 / AutoDL 落地工程铠甲（声线克隆、静音配乐隔离、不可变台词、首尾帧咬合）**。

---

## 一、 核心管道模块（按生产时序）

| 阶段 | 模块名称 (Skill Name) | 核心职责与工业合同 |
| :---: | :--- | :--- |
| **01 剧本编剧** | `director-agent` | 剧本三层读法、因果节拍提炼、潜台词分析、人物弧光。 |
| **02 资产合同** | `character-asset`<br>`scene-asset`<br>`prop-asset` | 静态三视图、无情绪标准光定妆、锁定特征表、不可逆 `approved` 门禁与 `asset_registry.json` 注册。 |
| **03 空间调度** | `ai-storyboard-director` | 五列人读分镜表、180° 行动轴锁定（`blocking_map`）、世界坐标、非等分时间轴与复合运镜路径。 |
| **04 总控编排** | `ai-short-drama-production`<br>*(★已升级)* | **【三大增强合同】**：<br>1. **声线锚定系统**（`voice_anchor_contract`，绑定 VoxCPM2 WAV）<br>2. **不可变台词防篡改台账**（`immutable_dialogue_ledger`，一字不差）<br>3. **配乐静音隔离协议**（`non_diegetic_music: SILENT`）<br>4. 打戏防回弹账本（`action_ledger`，Anti-Bounce 刚体约束） |
| **05 提示词编译** | `produce-ai-video`<br>*(★已升级)* | 编译【六大模块外层 ＋ 数字 10 内核】标准提示词，适配 MiniMax H3 / Kling 通信协议。 |
| **06 串行成片** | `h3-drama-director`<br>`minimax-h3-video` | AutoDL ComfyUI 载荷组装、`-0.35s` 稳定尾帧提取接力、全回放 QC 验收与 FFmpeg 剪辑拼接。 |

---

## 二、 类型风格视觉增强库

用于根据剧本类型直接调用材质、光学与布光偏好：
* `epic-design`：史诗宏大、全景奇观、王朝帝国
* `fantasy-design`：暗黑奇幻、魔法、古堡、巨龙
* `cyberpunk-design`：赛博朋克、未来工业都市、机甲义体、霓虹雨夜
* `hard-sci-fi-visual-director`：硬核科幻、工程机械、外星生态
* `noir-design`：黑色电影、犯罪悬疑、冷调暗夜
* `wuxia-design`：东方武侠、江湖冷兵器
* `war-design`：战地军事、爆炸烟尘
* `romance-design`：情感浪漫、柔光亲密
* `horror-design`：心理惊悚、阴森怪物

---

## 三、 本地安装与部署路径

1. **当前项目工作区**：  
   `d:/剧本项目/.agents/skills/`
2. **全局 Agent 技能目录**：  
   `C:/Users/egguy_sh/.gemini/config/skills/`
3. **独立离线打包文件**：  
   `d:/剧本项目/龙陨之契/ai_film_skills_upgraded_workflow.zip`
