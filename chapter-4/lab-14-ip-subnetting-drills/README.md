---
lab-id: lab-14-ip-subnetting-drills
plan-source: _MASTER-PLAN/phase-03-transport-network-layers/03-TransportNetworkLayers_deliverables.md
concept-notes: ["CIDR & Subnet Mask Notation", "Address Aggregation & Longest-Prefix Match"]
enrichment_status: pending
---

# Lab 14 — IP Subnetting Drills

## Objective

Convert between CIDR notation and dotted-decimal subnet mask form, decompose IPv4 addresses into network address + broadcast + host range, and design non-overlapping subnets to host-count requirements — all by hand.

## Why this lab exists

- **Reinforces Concept Notes:** CIDR & Subnet Mask Notation; Address Aggregation & Longest-Prefix Match
- **K&R sections covered:** §4.3.2 (IPv4 Addressing — subnet mask, CIDR, longest prefix matching, DHCP), §4.3.3 (Network Address Translation)
- **Decision Gate 2 connection:** Indirect prep — Gate 2 demos production-support incident triage; subnetting fluency lets you decode a forwarding or addressing incident from the address+mask alone, without reaching for a calculator under interview pressure.

This lab makes the prefix arithmetic concrete. CIDR (classless interdomain routing) replaced classful addressing in 1993; the network prefix length (the `/N` after the address) controls how many bits identify the network vs the host. Dynamic Host Configuration Protocol (DHCP) assigns each host an address plus a subnet mask plus a default gateway — every field exercised here. Network address translation (NAT) governs the private-address ranges Part B addresses are drawn from.

## Prerequisites

Verify each tool works before starting:

- [ ] Pen and paper (or a tablet with a stylus) — non-negotiable for "by hand first"
- [ ] `sipcalc --version` (or bookmark a subnet calculator URL such as <https://www.subnet-calculator.com>) — verification tool, not solving tool
- [ ] `lab-notes.md` open in editor with Part A / Part B / Part C section stubs ready
- [ ] Concept Note "CIDR & Subnet Mask Notation" drafted (or stubbed) in vault
- [ ] A 60–90 min uninterrupted block

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

60–90 min.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

1. Open `lab-notes.md`. Set up sections "Part A — Notation conversion", "Part B — Address decomposition", and "Part C — Subnet design".
2. Note solutions for Part A (5 problems), Part B (5 problems), and Part C (1 problem) with explicit work shown. Problem-set details appear in the `## Problem Set` section below.
3. Verify Parts A and B by re-running each problem through a subnet calculator AFTER solving by hand.
4. Compare the calculator output against the hand-solved answers. Note any discrepancies and trace the reasoning error.

## Constraints

Solve all of the following on paper or in `lab-notes.md` with explicit work shown. **Do them by hand first.** Use a subnet calculator only to verify, never to solve.

## Problem Set

**Part A — Notation conversion (5 problems):**

For each, give the alternative form and the number of usable hosts:

1. `192.168.1.0/24` → ___ subnet mask, ___ usable hosts.
2. `10.0.0.0/16` → ___ subnet mask, ___ usable hosts.
3. `172.16.0.0/12` → ___ subnet mask, ___ usable hosts.
4. `192.168.50.128/25` → ___ subnet mask, ___ usable hosts.
5. `10.20.30.0/30` → ___ subnet mask, ___ usable hosts.

**Part B — Address decomposition (5 problems):**

For each address, give the network address, broadcast address, and host range:

1. `192.168.5.45/24`
2. `10.10.10.130/25`
3. `172.16.20.50/22`
4. `192.168.100.200/27`
5. `10.5.0.10/29`

**Part C — Subnet design (1 problem):**

Given the network `10.0.0.0/16`, design subnets that meet these requirements:

- Subnet A: 500 hosts (e.g., a wired LAN floor).
- Subnet B: 200 hosts (e.g., a wifi network).
- Subnet C: 50 hosts (e.g., a server VLAN).
- Subnet D: 4 hosts (e.g., a small management network — point-to-point links).

Allocate non-overlapping subnets from `10.0.0.0/16`. Show network address, mask (CIDR), broadcast, and host range for each.

**Verification:**

For Parts A and B, after solving by hand, verify with a subnet calculator. Document any discrepancies and figure out where my reasoning went wrong.

## What to capture

- [ ] Pencil-and-paper solutions for all 11 problems (Part A + Part B + Part C): scan or photograph as `assets/01-hand-solutions.pdf` (or `.jpg`)
- [ ] Subnet calculator verification screenshots for Part A and Part B: save as `assets/02-calculator-verification.png`
- [ ] Reasoning-error analysis paragraph in `lab-notes.md` covering any discrepancies between hand-solved and calculator-verified answers
- [ ] 1-paragraph reflection in `lab-notes.md`: "what tripped me up? what's the heuristic I'll use under interview pressure?"

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Off-by-one on usable hosts: a `/N` subnet contains `2^(32-N)` addresses; usable hosts excludes the network address and the broadcast address, so usable = `2^(32-N) − 2`. A `/30` has 4 addresses and 2 usable hosts; a `/29` has 8 addresses and 6 usable hosts. RFC 3021 introduces the `/31` point-to-point convention as an exception — do not generalize to other prefix lengths.
- CIDR vs classful confusion in Part C: `10.0.0.0/16` is a CIDR-style sub-allocation of the 10.0.0.0/8 historical Class A range. Modern forwarding uses longest prefix matching against CIDR prefixes (per K&R §4.1.1 the router-local data-plane action is forwarding, distinct from network-wide routing); classful addressing is historical context only.
- Broadcast-address miscount: the broadcast address is `network address + (2^host-bits − 1)`. Compute it from the host-bit pattern (all 1s), not by guessing the last octet.
- Part B problem 5 (`10.5.0.10/29`): a `/29` has 8 addresses (network + 6 usable + broadcast). Locate the network address by zeroing the last 3 bits of the last octet; do not assume the given address is itself the network address.
- Calculator-tool selection bias: different subnet calculators use different bit-allocation conventions (some show "Wildcard Mask"; some hide the broadcast row by default). Pick one calculator and stick with it for the whole lab so the diff-trace stays consistent.
- The Part B private-address ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) are the RFC 1918 ranges that NAT (network address translation) maps to public addresses; the lab does not exercise NAT itself, but the address provenance is the reason these ranges show up.
- Out-of-scope layer reminder: this lab is at the IP / network layer. Transport-layer security (TLS, per K&R §8.6) sits two layers above and is not exercised here; do not let a `/N` prefix confuse you into looking for a TLS handshake — there is none in pencil-and-paper subnetting.

## References

- K&R 8e, §4.3.2 (IPv4 Addressing — subnet mask, CIDR, longest prefix matching, DHCP / Dynamic Host Configuration Protocol)
- K&R 8e, §4.3.3 (Network Address Translation — NAT, NAT translation table, private-address ranges)
- Concept Notes: CIDR & Subnet Mask Notation; Address Aggregation & Longest-Prefix Match
- RFC 4632 — Classless Inter-Domain Routing (CIDR): <https://www.rfc-editor.org/rfc/rfc4632.html>
- RFC 1918 — Address Allocation for Private Internets: <https://www.rfc-editor.org/rfc/rfc1918.html>
- Lecture 16 (00:12:13–00:21:04) — DHCP + CIDR + ISP block prefix + subnetting + aggregation

<!-- citations-v1.1
- K&R 8e §4.3.2 (IPv4 Addressing — subnet mask + CIDR + longest prefix matching + DHCP) [sha256:e2b1ffaa01fe] 2026-05-26
- K&R 8e §4.3.3 (Network Address Translation) [sha256:2f566e37905a] 2026-05-26
- Lecture16 00:12:13-00:21:04 (DHCP + CIDR + ISP block prefix + subnetting + aggregation) [sha256:e16596c2cb68] 2026-05-26
- RFC 4632 §3 (Classless Inter-Domain Routing — basic concept) [sha256:4c49aeb6bb15] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 9 Plan 09-02 enrichment per NET-02*
