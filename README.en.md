# Novel Writing Skills

[简体中文](README.md) | **English**

**Write long-form fiction with AI—without giving up control of your story.**

This skill suite connects story records, planning, drafting, passage review, and revision. It helps writers address continuity drift, interchangeable characters, repetitive prose, uneven pacing, and overly obvious foreshadowing through a structured, traceable workflow.

You do not need to memorize all 31 skill names. Start with `novel-router` and describe your task in ordinary language.

[Download v1.1](https://github.com/Huo0077/novel-writing-skills/releases/tag/v1.1) · [Full guide (Chinese)](docs/novel-skills/skills组使用指南.md) · [Quick start (Chinese)](小说skills-快速开始.md) · [Release history](https://github.com/Huo0077/novel-writing-skills/releases)

> This is **not a standalone novel generator**. It is a collection of instructions and tools for an AI assistant that can read and edit local files and follow skill workflows. Downloading the files does not automatically enable those abilities in a basic chat interface.

## Why this suite exists

Generating one fluent passage is not the same as sustaining a novel. Long-form collaboration requires maintaining prior events, character states, clues, and the consequences of edits—not merely finding more elegant sentences.

The suite breaks those problems into tasks that can be inspected, discussed, and tracked:

| Writing pain point | What it looks like | How the suite addresses it |
|---|---|---|
| **Lost context and contradictory state** | Injuries disappear, possessions change hands without explanation, promises are forgotten, or established world rules are bypassed | External world, character, event, and timeline records; task-specific context before writing and actual change extraction afterward |
| **Homogenized prose** | The same gestures, syntax, metaphors, or punctuation recur; synonym swaps leave the same template intact | Locate repetitions, judge them in context, protect intentional motifs, and propose changes to sentence groups or narrative approach |
| **Interchangeable or drifting characters** | Everyone sounds alike, motives shift to serve the plot, or distrust suddenly becomes trust | Check goals, boundaries, relationships, and knowledge sources; distinguish voices through attention, dialogue strategy, and responses under pressure |
| **Uneven pacing and premature explanation** | Too much exposition at once, early answers to the main mystery, unearned emotional peaks, or no aftermath | Bound chapter and scene functions, set stopping conditions, separate presenting conflict from explaining it, and review information load and emotional consequences |
| **Obvious clues and unearned reveals** | Repeated “meaningful glances,” only one plausible explanation, or twists built from newly invented facts | Give clues a present-scene purpose, support competing interpretations with evidence, and review distribution, reveal gates, and retrospective meaning |
| **Broken causality and weak agency** | A lucky discovery solves everything, choices lack reasons, or victories carry no consequences | Review goals, obstacles, choices, costs, results, and delayed consequences; distinguish missing support from payoff not yet reached |
| **Revision ripple effects** | Early edits invalidate later knowledge, chronology, relationships, or clues | Separate wording changes from factual changes, trace loaded dependencies and unread gaps, preserve old drafts, and identify synchronization scope |
| **Invented facts when information is missing** | A plausible guess becomes canon or an AI recommendation is treated as author approval | Ask one blocking question at a time, offer 2–3 directions and trade-offs, allow custom answers or deferral, and preserve the scope of your decision |
| **Difficult session recovery** | It is unclear where you stopped, which decisions are pending, or whether a planned outcome actually occurred | Checkpoints distinguish confirmed, tentative, and pending material, with sources, unmet targets, and a safe next action |

These mechanisms **reduce risk and make problems traceable**. They do not guarantee perfect memory or universally surprising twists.

## Key advantages: a maintainable workflow, not just a longer prompt

### 1. One entry point, only the relevant skills

`novel-router` selects the necessary parts of the 31-skill suite for your task. You can ask to continue a scene or review a clue without assembling the whole workflow or loading every rule.

### 2. Story state lives outside the conversation

The `.novel/` directory holds world limits, character states, chronology, events, clues, and knowledge boundaries. Records carry sources, status, and effective story time. A confirmed future plan is not an event a character has already experienced.

### 3. Planning, drafting, review, and decisions have separate roles

```text
Plan a bounded unit → Assemble relevant context → Draft
→ Review actual changes → Confirm by risk → Update records and checkpoint
```

The intended outcome is recorded separately from what the prose actually establishes. Fluent text does not automatically become canon. This is a workflow the assistant follows, not an autonomous background pipeline.

### 4. You set the direction; AI supplies options

Choose author-assistant, co-author, or semi-automatic long-form mode. Missing information prompts a question rather than a default decision. Major changes require clear approval, and a local answer does not authorize the entire plot.

### 5. Variety without erasing your story's identity

Protect deliberate motifs, recurring phrases, and meaningful repetition. Prefer removing redundancy or changing information order and sentence groups over replacing every frequent word with an obscure synonym. New actions, commitments, or clues still need review.

### 6. Foreshadowing balances naturalness, fairness, and consequences

The goal is not simply to prevent readers from guessing. Clues serve the current scene; reveals need earlier support and should change interpretation and action. Reader materials are separated from author answers, and unperformed tests are not reported as reader feedback.

### 7. Readable local records and non-overwriting migration

Drafts, proposals, sources, and progress are stored in inspectable files. A clean project seed, shared protocols, and templates travel with the suite. Initialization previews changes first and adds missing files without overwriting existing ones.

### 8. Computation is kept separate from literary judgment

There are executable tools for repetition statistics, reader-packet field checks, state validation, and suite verification. Character, causality, pacing, and clue quality still require contextual judgment and author feedback. Automated checks reduce operational mistakes; they do not replace taste.

## Who is it for?

- Writers with ideas or existing drafts who want help organizing, continuing, and reviewing them.
- Novelists and serial-fiction writers maintaining characters, subplots, clues, and progress over many sessions.
- Authors who welcome proactive suggestions but want to retain control over plot decisions.

It does not promise a high-quality, fully unattended novel generated from a single prompt.

## Get started in three steps

### 1. Download and open the complete project

Download `novel-writing-skills-v1.1.zip` from the [v1.1 Release](https://github.com/Huo0077/novel-writing-skills/releases/tag/v1.1). Extract it into an **empty new directory**, then open that directory with your AI assistant.

Keep the complete directory, including `.codex/` and `.novel/`; some file managers hide dot-prefixed folders. Do not copy just one `SKILL.md`, because the skills share protocols and templates.

Do not extract the ZIP over an existing novel project. Start in a new directory, then use the additive initialization workflow to bring in existing material. See the [full guide (Chinese)](docs/novel-skills/skills组使用指南.md).

### 2. Ask your assistant to use the router

Copy this request:

```text
Read .codex/skills/novel-router/SKILL.md in this project and follow it for my writing task.

I want to start a novel. First learn my goals and existing ideas, asking one key question at a time.
When information is missing, offer 2–3 distinct directions with their implications.
Let me provide my own answer or defer the decision. Do not turn your recommendation into canon.
```

If the assistant cannot find the file, provide the **absolute path** to `novel-router/SKILL.md` in your extracted project. File availability does not prove automatic skill loading; explicitly ask it to read the instructions when needed.

Already have a draft? Provide the latest chapter, relevant records, or the current problem, and distinguish confirmed material from tentative ideas. You do not need a complete story encyclopedia before starting.

### 3. Choose your collaboration mode

| Mode | Use it when you want… | How the assistant works |
|---|---|---|
| **Author assistant** | To decide the plot yourself and get organization, expansion, and review | Primarily follows your intent and offers suggestions |
| **Co-author** | To discuss character choices, plot options, and clues together | Can propose directions and explain their consequences |
| **Semi-automatic long-form** | To advance in batches along an approved direction | Plans and drafts within authorized scope, pausing for major changes |

Switch modes by project or task. **Semi-automatic does not mean unsupervised**: core world-rule changes, motivations, key-event outcomes, or full reveals still need approval.

## Requests you can use

After establishing the router entry point, describe the task rather than manually naming every skill.

### Continue the current scene

```text
Continue this scene. First check injuries, possessions, relationships, and knowledge boundaries.
Identify the scene goal and what must not be revealed. Ask me if essential information is missing.
Draft only after the scope is clear. Stop at the scene's exit condition and review actual changes.
Do not automatically move on to the next chapter.
```

### Find continuity problems

```text
Check this passage against the existing story records.
Separate confirmed contradictions, possible issues, and missing information, with source references.
Offer repair directions first; do not change canon.
```

### Reduce repetitive prose

```text
Check repeated phrases, syntax, gestures, and punctuation in this chapter.
Distinguish useful, questionable, and ineffective repetition. Preserve motifs and character voices.
Offer contextual alternatives and flag new actions or changes in meaning. Do not mechanically swap synonyms.
```

### Improve an obvious clue

```text
This clue is too conspicuous. Check its present-scene purpose and any excessive narrator emphasis.
Propose evidence-supported competing interpretations and check what changes on a reread.
If the truth or scene function is undecided, ask me first rather than inventing a new secret.
```

### End a writing session

```text
Save current progress: confirmed facts, tentative changes, and pending decisions.
Record unfulfilled promises, clues to advance, the next safe task, and information that must not be revealed yet.
```

## You retain decision-making authority

**Ask before filling critical gaps.** The assistant checks existing material, then asks about the current blocker. Options explain trade-offs; you can choose, customize, or defer. A partial answer confirms only that part.

**Drafts are not automatically canon.** Confirmed facts, tentative material, proposals, and drafts remain distinct. Planning to obtain a ledger does not mean the scene actually obtained it; review checks the result.

**Confirmation follows impact.**

- Low risk: may be recorded as tentative.
- Medium risk: collected for confirmation at a task or phase boundary.
- High risk: pause, explain consequences, and ask first.

**Keep the original draft.** Revisions are saved as new versions. A new action, commitment, clue, or knowledge state is treated as a factual change—not disguised as wording cleanup.

## Where your writing lives

```text
.codex/skills/   Skill instructions and tools; novel-router is the entry point
.novel/
  canon/        World, characters, timeline, events, clues, and information boundaries
  planning/     Outline, chapter plans, and scene plans
  drafts/       Prose drafts and earlier versions
  reviews/      Passage, expression, continuity, and pacing reviews
  proposals/    Suggestions, state changes, and clarification questions awaiting decisions
  checkpoints/  Resumable writing progress
  schemas/      Shared protocols
  templates/    Record templates
```

Being stored in `canon/` does not automatically confirm every record. Status and sources still matter.

Characters and stories in test directories are **QA fixtures, not your novel's canon**. The public download is a clean project seed, not a copy of a writer's private work.

> **Protect your unpublished work:** This repository is public. Do not push your populated `.novel/`, prose, author secrets, or private proposals into it. Work locally or in your own private workspace, and maintain backups.

## Optional tools and checks

Everyday use involves an assistant reading and following the skills. Statistics, packet preparation, suite validation, and migration tools require Python; full validation also requires PyYAML.

**Language scope:** Most skill instructions and reference materials are currently in Chinese. This English README does not imply that the entire suite is localized or that English-fiction performance has been validated. The expression analyzer's default phrases, syntax patterns, and character-fragment analysis target Chinese prose. Explicit phrase matching is configurable, but it is not a complete English linguistic analyzer.

From the project root:

```powershell
python -m pip install "PyYAML>=6.0,<7.0"
python .codex/skills/novel-router/scripts/suite.py validate --tests
```

Preview initialization before applying it:

```powershell
python .codex/skills/novel-router/scripts/suite.py bootstrap my-new-novel
python .codex/skills/novel-router/scripts/suite.py bootstrap my-new-novel --apply
```

Initialization preserves existing files, but preservation is not an automatic version merge. Existing projects still need compatibility review. An external ZIP extractor is not covered by this rule; do not extract over your old project.

## What has—and has not—been verified

v1.1 fixes six state-validation defects and adds the shared clarification protocol. Re-downloading the public Release and running validation produced **122 cases: 121 passed, 1 skipped because of symbolic-link permissions, and 0 failures**.

These checks verify file structures, tools, and handoffs—not independent model conversations, human first-read reactions, or long-form literary quality. Keep these limits in mind:

- Reliable state reading and updating over a long manuscript still needs real-project testing.
- Repetition statistics are not Chinese word segmentation or AI-authorship detection.
- A context that already knows the answer is not an independent reader. First-read tests need a fresh answer-free context or a human reader.
- Separating public writer packets from author notes is a procedural boundary, not technical access isolation.
- Global installation, automatic UI discovery, and autonomous multi-agent writing are not guaranteed.

See the [verification report (Chinese)](docs/novel-skills/GitHub-v1.1-复核报告.md) and [machine-readable summary](docs/novel-skills/verification/v1.1-public-verification.json). Historical v1.0 remains available in Releases, but has known validation defects; use v1.1.

## Further reading and feedback

- [中文 README](README.md)
- [Full guide and all 31 module responsibilities (Chinese)](docs/novel-skills/skills组使用指南.md)
- [Quick start (Chinese)](小说skills-快速开始.md)
- [Release notes (Chinese)](RELEASES.md)
- [Downloads and historical releases](https://github.com/Huo0077/novel-writing-skills/releases)

When reporting a problem, include your task, a minimal reproducible excerpt, expected behavior, and actual results. Anonymize unpublished work; do not post private plot answers or a full manuscript in public discussions.
