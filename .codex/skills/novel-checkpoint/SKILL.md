---
name: novel-checkpoint
description: Save and restore a resumable checkpoint for a novel project after a task, scene, chapter, or writing phase. Use when finishing a writing session, switching tasks, pausing automation, or recovering from a previous session without losing story state or pending decisions.
---

# Novel Checkpoint

## Workflow

1. Read the current project state, latest review report, accepted decisions, tentative changes, and pending proposals.
2. Record the exact story location and the selected collaboration mode.
3. Summarize confirmed canon separately from tentative changes and unresolved proposals.
4. Record completed work, the next safe action, unresolved questions, and information that must not be revealed next.
5. List the context files needed for recovery and the files intentionally excluded.
6. Save a new checkpoint under `.novel/checkpoints/` using `.novel/schemas/checkpoint.md`.
7. On resume, load the newest checkpoint first, then verify that its referenced files still exist and that no newer high-risk proposal is pending.

## Safety

A checkpoint is a snapshot, not a license to approve proposals. Do not fold tentative or proposed content into confirmed canon while saving it.

## Cadence

- Author assistant: after each task or explicit pause.
- Co-author: after each scene and before major-choice confirmation.
- Semi-automatic: after each chapter and whenever a high-risk item pauses progress.

## Resource

- Checkpoint schema: `.novel/schemas/checkpoint.md`
- Recovery rules: `references/checkpoint-rules.md`
