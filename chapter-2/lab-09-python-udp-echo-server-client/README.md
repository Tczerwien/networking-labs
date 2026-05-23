---
lab-id: lab-09-python-udp-echo-server-client
plan-source: _MASTER-PLAN/phase-02-application-layer/02-ApplicationLayer_week-by-week.md
concept-notes: ["Socket Programming — UDP and TCP"]
---

# Lab NN — <Verb-phrase Title>

## Objective

Build a Python UDP echo server-and-client pair from the socket primitives up.

## Why this lab exists

- **Reinforces Concept Notes:** <NN, NN[, NN]>
- **Shotts TLCL chapters covered:** <Ch X[, Ch Y]>
- **Decision Gate N connection:** <One sentence: direct prep / indirect prep / no connection — and why.>

## Prerequisites

Verify each tool works before starting:

- [ ] `bash --version` (or `python3 --version`)
- [ ] `shellcheck --version` (or `ruff --version` for python)
- [ ] `<test-environment-tool> --version`
- [ ] `<command --version or test invocation>`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

<N hrs.>

## Script specification

**Input:** <stdin / argv / file path — describe shape>

> 

**Output:** <stdout / file / exit-code-only — describe shape>

> 

**Exit codes:** <0 = success; non-zero codes and what each means>

> 

## Procedure

1. **Write the failing test first.** <test-shape>.
2. **Implement the minimal version.** <implementation hint>.
3. **Run shellcheck / ruff.** Address every warning.
4. **Iterate against edge cases.** <known-edge-cases placeholder>.
5. **Commit.** <commit-message convention reminder>.

## What to capture

- [ ] Final script source: save as `assets/NN-<script-slug>.sh` (or `.py`)
- [ ] One sample run output: paste into lab-notes
- [ ] Test case table: fill in lab-notes
- [ ] <Artifact-description>: save as `assets/NN-<slug>.<ext>`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you write at least one failing test case before implementation?
- Did you verify exit codes match the specification (0 for success, non-zero for each failure mode)?
- Did you run shellcheck or ruff before declaring the script done?
- Did you test against the documented edge cases, not just the happy path?
- (Optional 5th — only add if the specific lab subtype reliably surfaces a recurring trap.)

## References

- Shotts TLCL, Chapter <X> (<topic name>)
- Concept Notes <NN, NN>
- <External URL with descriptive text>

### Cross-vault link format (frontmatter-only — D-09)

Every lab README opens with the following frontmatter block. The Obsidian vault discovers labs and concept-notes via these fields; no inline wikilinks live in the body of the README. Documented by Phase 3 D-09 / D-12; vault template frontmatter additions live in `/home/tc/vault/_Templates/Lab.md` and `Concept.md` (D-10 / D-11).

```yaml
---
lab-id: <lab-NN-kebab-slug>
plan-source: <_MASTER-PLAN/phase-NN-slug/02_week-by-week.md>
concept-notes: ["<Concept Note Title 1>", "<Concept Note Title 2>"]
---
```

*Last updated: 2026-05-21*
