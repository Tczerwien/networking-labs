---
lab-id: lab-02-traceroute-deep-dive
plan-source: _MASTER-PLAN/phase-01-networking-foundations/03-NetworkingFoundation_deliverables.md
concept-notes: ["Network Core & ISP Hierarchy", "Performance — The Four Components Of Delay"]
enrichment_status: pending
---

# Lab 02 — Traceroute Deep Dive

## Objective

Trace the path packets take from your end system to three distinct destinations and record the per-hop identity and round-trip times along each path.

## Why this lab exists

- **Reinforces Concept Notes:** 5, 6
- **K&R sections covered:** §1.3, §1.3.3, §1.4, §1.4.3
- **Decision Gate 1 connection:** Indirect prep — Decision Gate 1 walks every header field in a single packet; this lab walks the sequence of packet switches a packet visits, giving the layered-header view the path context that explains why the destination IP in the IP header maps to a hop-by-hop route through the network core.

## Prerequisites

Verify each tool works before starting:

- [ ] `traceroute --version`
- [ ] `mtr --version`
- [ ] `whois --version`
- [ ] `curl --version`
- [ ] Browser available to open `https://bgp.tools/`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

1. Run `traceroute <near-destination>` (a host inside your own ISP, or `cloudflare.com`) and capture the output to `assets/01-traceroute-near.txt`. Note the IP address and any hostname of every hop in `lab-notes.md`.
2. Run `traceroute <far-destination>` (a host on the opposite coast or a major cloud provider such as `amazon.com`) and capture the output to `assets/02-traceroute-far.txt`. Note any hop whose round-trip time jumps significantly relative to the previous hop, without yet labelling the cause.
3. Run `traceroute <international-destination>` (a host on another continent such as `bbc.co.uk` or `lemonde.fr`) and capture the output to `assets/03-traceroute-international.txt`. Note any hop whose round-trip time jumps significantly relative to the previous hop.
4. Run `mtr -r -c 30 <far-destination>` and capture the output to `assets/04-mtr.txt`. Note the per-hop loss percentage and average round-trip time in `lab-notes.md`.
5. Run `whois <ip>` for 5-10 interesting hop IPs (hops at round-trip-time jumps, hops with transit-looking hostnames). Note the ASN and AS owner per hop in `lab-notes.md`.
6. Open `https://bgp.tools/` and inspect the AS path for one of the far-destination hop IPs from step 5. Note the AS sequence between your starting hop and the destination AS in `lab-notes.md`.

## What to capture

- [ ] Near-destination traceroute saved as `assets/01-traceroute-near.txt`
- [ ] Far-destination traceroute saved as `assets/02-traceroute-far.txt`
- [ ] International-destination traceroute saved as `assets/03-traceroute-international.txt`
- [ ] `mtr` output saved as `assets/04-mtr.txt`
- [ ] ASN lookups for 5-10 hops recorded in `lab-notes.md`
- [ ] Optional: hand-drawn or ASCII-art diagram of one path through AS tiers in `lab-notes.md`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify each prerequisite tool runs cleanly before starting?
- Some intermediate packet switches silently drop traceroute probes and appear as `* * *` lines in the output — note their hop number and continue.
- ICMP rate-limiting on intermediate routers can make round-trip times for a single hop vary widely across the three probes per row; record all three values.
- `mtr` requires raw-socket capability and may need `sudo`; the `-r` flag prints a final report rather than the live-updating TUI.
- `whois <ip>` output varies by regional Internet registry; if the ASN is absent or unclear, look the same IP up on `https://bgp.tools/`.

## References

- K&R, Section 1.4.3 (End-to-End Delay + Traceroute mechanism)
- K&R, Section 1.3.3 (A Network of Networks)
- Concept Notes 5, 6
- Lecture 2 (Data Communications) — ISP hierarchy and Internet Exchange Points
- `man traceroute`, `man mtr`, `man whois`

<!-- citations-v1.1
- K&R 8e §1.4.3 (End-to-End Delay + Traceroute mechanism) [sha256:f70869c43d06] 2026-05-26
- K&R 8e §1.3.3 (A Network of Networks) [sha256:86f62b6ac57b] 2026-05-26
- Lecture2 00:14:00-00:18:00 (ISP hierarchy and Internet Exchange Points) [sha256:6f07c8bfc1bf] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 10 Plan 10-01 enrichment per NET-03*
