# Contributing

感谢你改进 `liang-qichao-skill`。这个项目最看重的不是“更多梁启超味”，而是**方法是否可靠、来源是否可追、现代转译是否有边界**。

## 欢迎的贡献

- 修正史料出处、版本或年代；
- 补充更可靠的一手文本定位；
- 提交能暴露工作流缺陷的反例；
- 改善现代问题中的模型路由；
- 改善 Codex / Claude Code / Cursor 等客户端的兼容说明；
- 增加评测案例。

## 不建议的贡献

- 大量网络名言；
- 无出处的“梁启超会说……”；
- 单纯加强历史人物角色扮演；
- 把现代政治立场包装成梁启超原意；
- 用一个历史概念解释所有问题。

## 历史主张的四层标记

贡献时请尽量分清：

1. **历史事实**：发生过什么；
2. **梁启超的记录观点**：有明确文本依据；
3. **项目解释**：我们如何概括这些材料；
4. **现代转译**：如何把方法用于今天。

不要把第 3、4 层写成第 2 层。

## 新增引语

新增任何直接引语前：

1. 优先找到一手文本；
2. 在 `references/sources.md` 记录出处；
3. 若不同版本文字有差异，注明版本问题；
4. 无法确认时改为释义，不使用引号。

## 修改工作流

如果修改 `SKILL.md` 的核心逻辑，请同步：

- 更新对应 example；
- 新增或修改 `evals/test-cases.md`；
- 检查 README 的描述是否仍准确。

## 提交前检查

```bash
python scripts/check_structure.py
```

如果可用：

```bash
skills-ref validate .
```

## Commit 建议

```text
feat: add ...
fix: correct source for ...
docs: clarify ...
test: add eval for ...
refactor: simplify ...
```
