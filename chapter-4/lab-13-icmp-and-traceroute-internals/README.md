---
lab-id: lab-13-icmp-and-traceroute-internals
plan-source: _MASTER-PLAN/phase-03-transport-network-layers/02-TransportNetworkLayers_week-by-week.md
concept-notes: ["ICMP, Traceroute Mechanics, Forwarding Concepts"]
---

# Lab NN — <Verb-phrase Title>

## Objective

Capture ping and traceroute traffic and decode the ICMP layer end-to-end.

## Why this lab exists

- **Reinforces Concept Notes:** <NN, NN[, NN]>
- **K&R sections covered:** <X.Y[, X.Y]>
- **Decision Gate N connection:** <One sentence: direct prep / indirect prep / no connection — and why.>

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `<command --version or test invocation>`
- [ ] `<command --version or test invocation>`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

<N hrs.>

## Procedure

**Capture filter (BPF syntax):** `<bpf-filter-expression-with-<placeholders>>`

**Display filter (Wireshark syntax):** `<display-filter-expression-with-<placeholders>>`

1. **<Verb-phrase step name>.** Command: `<command-with-<placeholders>>`.
2. **<Verb-phrase step name>.** Command: `<command-with-<placeholders>>`.
3. **<Verb-phrase step name>.** Command: `<command-with-<placeholders>>`.
4. **<Verb-phrase step name>.** Command: `<command-with-<placeholders>>`.
5. **<Verb-phrase step name>.** Command: `<command-with-<placeholders>>`.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |

## What to capture

- [ ] Packet capture saved as `assets/NN-<capture-slug>.pcapng`
- [ ] Dissector-pane screenshot with all relevant layers expanded: save as `assets/NN-<slug>.png`
- [ ] <Artifact-description>: save as `assets/NN-<slug>.<ext>`
- [ ] <Artifact-description>: save as `assets/NN-<slug>.<ext>`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Did your capture filter actually match the traffic you intended to see?
- Did you stop the capture before exporting, or did you let it grow unboundedly?
- Did you pick a single packet from the conversation before expanding the dissector pane, instead of trying to interpret the whole stream at once?
- (Optional 5th — only add if the specific lab subtype reliably surfaces a recurring trap.)

## References

- K&R, Section <X.Y> (<topic name>)
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
