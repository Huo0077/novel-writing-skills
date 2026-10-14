---
name: novel-segment-review
description: Reverse-review a novel passage after drafting to extract explicit facts, character and world-state changes, information leaks, contradictions, narrative function, foreshadowing changes, and state-change proposals. Use after writing or importing prose before updating canon.
---

# Novel Segment Review

## Workflow

1. Read the prose, its context packet, relevant canon, and current scene plan.
2. Pass one: extract only facts explicitly written in the segment; separate inferences.
3. Pass two: compare facts against character states, timeline, information boundaries, world rules, and prior review reports.
4. Pass three: identify what the segment changes—event, relationship, knowledge, risk, resource, goal, or unresolved question. Flag scenes that change nothing.
5. Pass four: identify foreshadowing, repeated motifs, and possible style observations without rewriting the passage.
6. Produce `.novel/schemas/review-report.md` format.
7. Convert real state changes into risk-classified proposal candidates for `novel-canon`; do not directly update canon.

## Required distinctions

- Observed fact vs inference.
- Contradiction vs intentional mystery.
- Information leak vs permitted dramatic irony.
- Useful repetition vs unintentional repetition.
- Existing canon vs text that is only DRAFT.

## Escalate immediately when

- The passage reveals a high-risk secret or changes a core rule.
- A character knows information outside the current information map.
- The passage makes a CANON contradiction that cannot be resolved by viewpoint, timing, or deliberate deception.
- The prose introduces a fact that would invalidate multiple downstream records.

## Resource

- Review checklist: `references/review-checklist.md`
