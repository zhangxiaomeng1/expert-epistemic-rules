# Expert Epistemic Rules / 专家认知规则

> Make every AI statement traceable. Make uncertainty explicit. Separate symbolic frames from reality.
> 让每一条 AI 陈述的认知来源可追溯，让不确定性显性化，让符号框架与现实严格分离。

## What is this / 这是什么

**English:** A reusable skill that enforces epistemic discipline on any AI agent. It requires every factual claim to carry a cognitive-source tag, mandates confidence labeling, forbids translating symbolic frameworks into real-world claims without disclosure, and includes anti-sycophancy and post-hoc detection rules.

**中文：** 一个可复用的智能体技能，为任何 AI 智能体强制执行认知纪律。它要求每一条事实性陈述都打上认知来源标签，强制标注置信度，禁止把符号框架未经声明地翻译为现实主张，并包含反谄媚与事后归因检测规则。

Originally extracted from the `<expert-epistemic-rules>` block in a local Codex agent's global `AGENTS.md`.
最初提取自本地 Codex 智能体全局 `AGENTS.md` 中的 `<expert-epistemic-rules>` 块。

## Core Rules / 核心规则

| # | Rule / 规则 | Description / 说明 |
|---|-------------|---------------------|
| 1 | **Cognitive Tagging / 认知标签** | Tag every claim: `[已知]` `[计算]` `[推断]` `[常识]` `[框架]` `[猜测]` |
| 2 | **Frame→Reality Forbidden / 框架→现实禁止** | Symbolic frames (astrology, typologies) cannot become real-world claims (medicine, law, finance) without explicit flagging |
| 3 | **Confidence Labeling / 置信度标注** | End every Chinese reply with `置信度：高/中/低/很低/未知` |
| 4 | **Don't Know / 不知道就说** | First line: `我不知道。` — never fabricate, never bury |
| 5 | **Anti-Sycophancy / 反谄媚** | Detect: overly elegant prose, one-pattern-explains-all, agreeing after pushback without evidence |
| 6 | **Post-hoc Detection / 事后归因检测** | Ask: would this frame predict this without knowing the outcome? If no, tag `[推断，事后归因]` |

### Tag Definitions / 标签定义

| Tag / 标签 | Meaning / 含义 | Example / 示例 |
|------------|----------------|----------------|
| `[已知]` | Training-data fact / 训练数据事实 | 水的沸点是 100°C |
| `[计算]` | Calculated result / 计算得出 | 12% × 5000 = 600 |
| `[推断]` | Evidence-based deduction / 有依据的推理 | 营收下滑可能源于渠道收缩 |
| `[常识]` | Standard field knowledge / 领域标准知识 | HTTP 404 = Not Found |
| `[框架]` | Symbolic system, coherent ≠ real / 符号系统自洽 | MBTI INTJ 倾向内向直觉 |
| `[猜测]` | No basis / 无依据推测 | 该公司可能在筹备融资 |

### Confidence Mapping / 置信度映射

| Level / 等级 | Range / 区间 | Cap / 上限规则 |
|--------------|--------------|----------------|
| 高 (High) | ≥80% | — |
| 中 (Medium) | 50–80% | — |
| 低 (Low) | 20–50% | `[框架]`→现实, `[猜测]` cap here |
| 很低 (Very Low) | <20% | — |
| 未知 (Unknown) | — | Cannot assess |

## Installation / 安装与接入

### Option 1: Codex (OpenAI) / Codex 智能体

```bash
# Clone into Codex skills directory / 克隆到 Codex skills 目录
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git ~/.codex/skills/expert-epistemic-rules
```

Codex auto-discovers skills under `~/.codex/skills/`. The skill triggers when the user asks for rigorous, source-tagged, or accuracy-first replies.
Codex 会自动发现 `~/.codex/skills/` 下的技能。当用户要求严谨、标注来源或准确优先时，该技能自动触发。

### Option 2: Claude Code / Claude Code 智能体

```bash
# Global install / 全局安装
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git ~/.claude/skills/expert-epistemic-rules

# Or per-project / 或项目级安装
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git ./.claude/skills/expert-epistemic-rules
```

### Option 3: Doubao / 豆包智能体

Place the folder under your agent's skills directory:
将文件夹放到智能体的 skills 目录下：

```
<agent-workspace>/.user_skills/expert-epistemic-rules/
└── SKILL.md
```

### Option 4: Any Agent — Direct Prompt Injection / 任意智能体 — 直接注入提示词

No skill system? Copy the content of `SKILL.md` directly into your agent's system prompt or `AGENTS.md`:
如果你的智能体没有技能系统，直接把 `SKILL.md` 的内容复制到系统提示词或 `AGENTS.md` 中：

```bash
# Example for Codex AGENTS.md / 以 Codex 为例
cat expert-epistemic-rules/SKILL.md >> ~/.codex/AGENTS.md
```

Or paste the `<expert-epistemic-rules>` block into any system prompt.
或将 `<expert-epistemic-rules>` 块粘贴到任意系统提示词中。

### Option 5: Update / 更新

```bash
cd ~/.codex/skills/expert-epistemic-rules  # or your install path
git pull
```

## Usage Example / 使用示例

**Without the skill / 未使用时:**
> "The company will probably raise funding next quarter. Their MBTI suggests they're aggressive."

**With the skill / 使用后:**
> `[猜测]` 该公司可能在下个季度融资，目前无公开证据。
> `[框架]` MBTI 中 ENTJ 常被描述为进攻型人格，但这是符号框架内的分类，不能作为融资决策的现实依据。
>
> 置信度：低

## File Structure / 文件结构

```
expert-epistemic-rules/
├── SKILL.md      # The skill itself / 技能本体（智能体加载此文件）
└── README.md     # This file / 本说明文件
```

## License / 许可证

MIT
