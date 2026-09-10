# 全局安装 / Global installation

把以下一句话发给有本地文件读写能力的智能体：

> 请把 https://github.com/zhangxiaomeng1/expert-epistemic-rules 安装为当前工具的用户级全局规则：读取仓库 INSTALL.md、RULES.md 和安装脚本，识别当前工具支持的全局配置文件，备份后合并规则、保留其他内容并避免重复，执行后回读验证并报告路径；我授权这次配置文件修改。如果当前环境不能写入，请说明具体限制并给出手动步骤。

## Codex：自动安装

要求本地有 Git、Python 3，以及目标配置目录写权限。在尚未克隆仓库的目录运行：

```bash
git clone https://github.com/zhangxiaomeng1/expert-epistemic-rules.git
cd expert-epistemic-rules
# 先读取 RULES.md 和 scripts/install.py，检查待安装内容
python3 scripts/install.py --target codex --dry-run
python3 scripts/install.py --target codex
```

脚本使用 `$CODEX_HOME`，未设置时使用 `~/.codex`；如果有非空的 `AGENTS.override.md`，写入该文件，否则写入 `AGENTS.md`。仅更新 `<expert-epistemic-rules>` 块，保留其他内容。已有同样规则时不写入；更改前生成唯一备份并输出位置。

旧版安装如已把整个 SKILL.md 无标记追加到配置，脚本会停止：先备份，确认旧段边界，再将旧技能段替换为 RULES.md，保留其他内容。脚本不猜测删除边界。

更新：在克隆目录执行 `git pull --ff-only`，检查改动后再次运行安装命令。恢复：将安装时报告的备份恢复到目标文件；如安装后有其他修改，需合并恢复，避免覆盖那些修改。

依据：[Codex 官方全局规则文档](https://developers.openai.com/codex/guides/agents-md/)。用户级规则仍受指令层级、项目规则和文档加载大小限制影响。

## Claude Code：文件合并

将 RULES.md 中的完整规则块合并到 `~/.claude/CLAUDE.md`，修改前备份、已有块则替换、保留其他内容。本仓库脚本目前只自动处理 Codex。

依据：[Claude Code 官方记忆文档](https://code.claude.com/docs/en/memory)。

## 其他工具与纯聊天环境

先查当前产品官方文档和实际环境，确认支持的用户级自定义指令入口。只有技能目录时，安装技能表示可供调用，不代表每次对话都会加载。只有聊天能力、无法写文件或操作设置时，复制 RULES.md 到工具支持的自定义指令输入框；如果长度超限，需要用户选择删减内容，不能声称完整安装。

不再使用未经核实的产品目录或 settings.json 字段。自定义智能体内的设定也不等于整个账号的全局规则。

## 验证

1. 回读实际目标文件，确认完整规则块仅出现一次、其他内容保留。
2. 在新会话中询问：“请列出当前加载的用户级全局指令来源，并总结认知标签要求。”
3. 再测试未知事实和框架推断问题，检查标签、置信度和不编造要求。

文件写入成功、宿主加载成功、模型行为符合规则是三个不同验证结果。不要只凭旧会话的一条回答宣称所有后续对话已生效。
