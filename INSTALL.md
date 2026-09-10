# Global Installation Guide / 全局接入指南

> How to make this skill active globally in every conversation, not just one project.
> 如何让这个技能在所有对话中全局生效，而不仅限于单个项目。

---

## 1. Codey CLI / Codey 命令行

Codey loads `SYSTEM.md` files automatically from two locations (in order):
Codey 会自动从以下两个位置按顺序加载 `SYSTEM.md`：

| Scope / 范围 | Path / 路径 |
|--------------|-------------|
| Global / 全局 | `~/.config/codey/SYSTEM.md` |
| Project / 项目 | `.codey/SYSTEM.md` |

### Global install / 全局安装（推荐）

```bash
# 1. Create config directory / 创建配置目录
mkdir -p ~/.config/codey

# 2. Clone the skill / 克隆技能
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git /tmp/expert-epistemic-rules

# 3. Append skill content to global SYSTEM.md / 将技能内容追加到全局 SYSTEM.md
cat /tmp/expert-epistemic-rules/SKILL.md >> ~/.config/codey/SYSTEM.md

# 4. Verify / 验证
tail -20 ~/.config/codey/SYSTEM.md
```

Now every Codey session, in any directory, will follow these rules.
此后在任何目录下启动 Codey，都会自动遵守这些规则。

### Project-only install / 仅项目级安装

```bash
mkdir -p .codey
cat /path/to/expert-epistemic-rules/SKILL.md >> .codey/SYSTEM.md
```

---

## 2. Gemini Code Assist (VS Code) / Gemini Code Assist（VS Code 插件）

Google 的 Codey 现已整合为 Gemini Code Assist，通过 VS Code 设置注入全局自定义指令。

### Steps / 操作步骤

1. Open VS Code Settings / 打开 VS Code 设置：`Cmd + ,`（mac）或 `Ctrl + ,`（Win）
2. Search for `Gemini Code Assist` / 搜索 `Gemini Code Assist`
3. Find **Custom Instructions** / 找到「自定义指令」
4. Paste the content of `SKILL.md` / 将 `SKILL.md` 的内容粘贴进去
5. Save / 保存

Or via `settings.json`:
或直接编辑 `settings.json`：

```json
{
  "gemini.codeAssist.customInstructions": "把 SKILL.md 的完整内容粘贴到这里"
}
```

---

## 3. 豆包本地 Agent (Doubao Desktop / Agent Mode) / 豆包电脑端智能体模式

豆包电脑端在「工作任务」模式下支持本地技能目录，技能放在 `.user_skills` 下自动发现。

### Steps / 操作步骤

```bash
# 1. Locate your .user_skills directory / 找到 .user_skills 目录
#    Typically under the agent workspace, e.g.:
#    通常在智能体工作空间下，例如：
#    ~/Library/Application Support/Doubao/.../workspace/.user_skills/

# 2. Clone the skill into it / 克隆技能到该目录
cd /path/to/your/.user_skills
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git

# 3. Restart Doubao or start a new session / 重启豆包或开新会话
```

The skill auto-triggers when you ask for rigorous, source-tagged, or accuracy-first replies.
当你要求严谨、标注来源或准确优先时，技能自动触发。

### One-liner / 一键命令

```bash
# Replace with your actual .user_skills path / 替换为你的实际 .user_skills 路径
SKILLS_DIR="$HOME/Library/Application Support/Doubao/Default/.doubao/agent_mode/workspace/.user_skills"
mkdir -p "$SKILLS_DIR" && git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git "$SKILLS_DIR/expert-epistemic-rules"
```

---

## 4. 豆包网页版 / APP（创建自定义智能体）

如果你用的是豆包网页版或手机 APP，通过创建自定义智能体来全局使用。

### Steps / 操作步骤

1. Open 豆包 / 打开豆包
2. Go to 智能体广场 → 右上角「创建智能体」/ 进入智能体广场，点击创建智能体
3. Fill in name and description / 填写名称和简介
   - Name / 名称：`认知纪律助手` 或 `Epistemic Judge`
   - Description / 简介：`每条陈述标注认知来源，强制置信度，反谄媚反事后归因`
4. In **设定描述** (人设与回复逻辑), paste the full content of `SKILL.md` / 在「设定描述」中粘贴 `SKILL.md` 完整内容
5. Save and publish / 保存并发布

此后每次和这个智能体对话，规则全局生效。

---

## 5. Codex (OpenAI) / Codex 智能体

### Via skills directory / 通过技能目录（推荐）

```bash
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git ~/.codex/skills/expert-epistemic-rules
```

### Via global AGENTS.md / 通过全局 AGENTS.md

```bash
# Append to global AGENTS.md / 追加到全局 AGENTS.md
cat expert-epistemic-rules/SKILL.md >> ~/.codex/AGENTS.md
```

---

## 6. Claude Code / Claude Code 智能体

```bash
# Global / 全局
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git ~/.claude/skills/expert-epistemic-rules

# Or via settings.json system prompt / 或通过 settings.json 系统提示词
# Add to ~/.claude/settings.json:
# "systemPromptAddendum": "把 SKILL.md 内容粘贴到这里"
```

---

## 7. Universal Method / 通用方法（任何 AI 工具）

如果你的工具不支持技能目录，**最简单的通用方法**是把 `SKILL.md` 的内容直接粘贴到工具的「自定义指令」「系统提示词」「人设」或「Custom Instructions」输入框中。

```bash
# Print the content to copy / 打印内容以便复制
cat expert-epistemic-rules/SKILL.md
```

Then paste it into:
然后粘贴到：
- ChatGPT: Settings → Custom Instructions
- Claude.ai: Settings → Custom Instructions
- 文心一言 / Kimi / 通义千问: 智能体设定 / 系统提示词
- Any other tool with a system prompt field / 任何有系统提示词字段的工具

---

## Verification / 验证是否生效

After installation, test with:
安装后，用以下问题测试：

```
你觉得我是什么性格？顺便预测一下我明年的财运。
```

If the skill is active, you should see:
如果技能生效，你应该看到：
- `[框架]` or `[猜测]` tags on the personality/fortune claims / 性格和财运陈述带有 `[框架]` 或 `[猜测]` 标签
- `置信度：低` at the end / 末尾标注 `置信度：低`
- No fabricated certainty / 没有编造的确定性

## Updating / 更新

```bash
# Inside the skill directory / 在技能目录内
cd ~/.codex/skills/expert-epistemic-rules   # or your install path
git pull
```

If you appended to `SYSTEM.md` or `AGENTS.md`, re-append after pulling (or manage the file yourself).
如果你是追加到 `SYSTEM.md` 或 `AGENTS.md`，pull 后需要重新追加（或自行管理该文件）。
