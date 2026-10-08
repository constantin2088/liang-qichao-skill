# AGENTS.md

This repository contains one Agent Skill: `liang-qichao-skill`.

## For agents working in this repository

- Treat `SKILL.md` as the canonical runtime instruction file.
- Keep the YAML `name` exactly `liang-qichao-skill`; it must match the skill directory name.
- Keep `SKILL.md` concise enough for progressive disclosure. Move detailed historical evidence, voice notes and research procedures into `references/`.
- Do not add unverified quotes attributed to Liang Qichao.
- When adding a historical claim, add a source entry to `references/sources.md`.
- Distinguish four layers: historical fact, Liang's documented view, project interpretation, modern transfer.
- Do not make the skill endorse or oppose contemporary political candidates, parties or campaigns.
- Do not make the skill claim Liang Qichao's opinion about events after 1929.
- Do not optimize the README for historical-roleplay appeal at the expense of reasoning quality.
- Keep README demos behaviorally consistent with `SKILL.md` and `evals/test-cases.md`.

## Quality bar for changes

Before committing changes:

1. Run `python scripts/check_structure.py`.
2. If `skills-ref` is installed, run `skills-ref validate .`.
3. Check new behavior against `evals/test-cases.md`.
4. Ensure README examples still match the current `SKILL.md` workflow.
5. Ensure any new public-facing claim is either a project claim or supported in `references/sources.md`.
