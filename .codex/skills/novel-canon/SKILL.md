---
name: novel-canon
description: Maintain a novel project's canon, tentative facts, proposals, rejected ideas, and archived history without silently overwriting confirmed story truth. Use when recording story facts, accepting or rejecting state changes, resolving contradictions, or deciding whether a draft change becomes canon.
---

# Novel Canon Management

## Workflow

1. Read the relevant canon records, source reference, current mode, and any review report.
2. Separate observed facts, creator-confirmed facts, AI inferences, and proposals.
3. Classify each change as low, medium, or high risk using `references/decision-rules.md`.
4. Create a status-change proposal using `.novel/schemas/status-change.md`.
5. Apply the confirmation rule:
   - low: record as `TENTATIVE` without interrupting;
   - medium: keep as `PROPOSAL` for batch confirmation;
   - high: pause immediately and ask the creator before any canon update.
6. On creator decision, append the decision and impact note. Preserve the previous value in history; never silently overwrite `CANON`.
7. Report accepted, tentative, rejected, and still-pending changes separately.

## State discipline

- `CANON` is confirmed truth.
- `TENTATIVE` is a low-risk working fact.
- `PROPOSAL` is an unconfirmed change or idea.
- `DRAFT` is text that has not passed reverse review.
- `REJECTED` and `ARCHIVED` remain traceable and are not reused as current truth.

## Conflict handling

If two canon records conflict, do not choose the more recent one automatically. Show both sources, describe the downstream impact, ask a focused question, and record the resolution as a new decision.

## Deterministic validation

Run `scripts/validate_novel_project.py <project-root>` to validate required files and proposal fields. The validator is side-effect free.

## Resources

- Decision rules: `references/decision-rules.md`
- State-change schema: `.novel/schemas/status-change.md`

## 缺信息与用户选项
遵守 `.novel/schemas/clarification-contract.md`：先查已有答案，一次问一个当前关键缺口，给2–3个不同方向及后果，并允许自定义或暂不决定。未知/冲突/授权缺失不能靠猜测补正史；仅暂停依赖步骤。用户答复按实际来源和明确范围记录，高风险许可不足仍交novel-canon暂停。
