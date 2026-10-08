# GitHub 首发检查表

这份清单用于把 `liang-qichao-skill` 从本地目录发布为一个完整的 GitHub 首发仓库。

## 1. 当前发布账号

本首发版已配置为：

```text
constantin2088/liang-qichao-skill
```

`SKILL.md` frontmatter 中的作者也已设置为：

```yaml
metadata:
  author: constantin2088
```

不要修改：

```yaml
name: liang-qichao-skill
```

这个名字应与 Skill 目录保持一致。

## 2. 本地检查

```bash
python scripts/check_structure.py
```

如果安装了 Agent Skills 参考校验器：

```bash
skills-ref validate .
```

确认：

- `SKILL.md` YAML frontmatter 可解析；
- `name` 为 `liang-qichao-skill`；
- README 中所有相对链接有效；
- 没有 API Key、Cookie、邮箱密码或本地绝对路径；
- 没有未经核实的梁启超引语。

## 3. 创建 GitHub 仓库

推荐仓库名：

```text
liang-qichao-skill
```

建议设置：

- Visibility: Public
- Default branch: `main`
- License: 不要在 GitHub 再自动生成；仓库已经包含 MIT `LICENSE`
- README: 不要自动创建；仓库已有 README

## 4. GitHub Description

推荐：

> 梁启超·自新与变局：一个用于职业转型、组织变革、认知更新与研究判断的中文 Agent Skill。不是角色扮演，而是可执行的方法论。

英文备选：

> A Chinese Agent Skill for transition diagnosis, self-renewal, belief revision, comparative reasoning and evidence-based research, inspired by Liang Qichao.

完整候选见 `docs/github-metadata.md`。

## 5. Topics

推荐添加：

```text
agent-skills
ai-agent
codex
claude-code
cursor
liang-qichao
chinese
reasoning
strategy
career
organizational-change
research
critical-thinking
learning
```

## 6. 第一次提交

```bash
git init
git add .
git commit -m "feat: launch Liang Qichao renewal and transition skill"
git branch -M main
git remote add origin https://github.com/constantin2088/liang-qichao-skill.git
git push -u origin main
```

## 7. 验证安装

GitHub 仓库公开后，用一个干净目录测试：

```bash
npx skills add constantin2088/liang-qichao-skill
```

确认 Skill 能被目标 Agent 发现。

## 8. 加 skills.sh 徽章

安装命令测试成功后，将 README 首屏加入：

```md
[![skills.sh](https://skills.sh/b/constantin2088/liang-qichao-skill)](https://skills.sh/constantin2088/liang-qichao-skill)
```

skills.sh 会根据 CLI 的匿名安装统计自动收录公开 Skill。

## 9. 创建 v1.0.0 Release

Tag：

```text
v1.0.0
```

Release title：

```text
v1.0.0 — 梁启超·自新与变局 Skill 首发
```

Release 正文可直接使用 `docs/launch-copy.md` 中的 GitHub Release 版本。

## 10. 首发传播顺序

建议不要同时发十个平台。先完成：

1. GitHub 仓库 + Release；
2. 自己真实安装一次；
3. 找 3–5 个不同类型问题实测；
4. 把最有说服力的一段 Demo 发出去；
5. 收集 Issue 后再做 v1.0.1。

首发时主打一句话：

> 不是把梁启超做成聊天角色，而是把“面对变局时如何更新自己”做成 Agent Skill。
