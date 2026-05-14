# Lab 02 — Traceroute Deep Dive

## Objective

Make ISP hierarchy and core routing visible. Trace packet paths to multiple destinations and decode the topology.

## Why this lab exists

- **Reinforces Concept Notes:** 5 (especially), 6 (delay components visible in latency jumps)
- **K&R sections covered:** 1.3 (Network core)
- **Decision Gate 1 connection:** Indirect prep. Builds the mental model of tiered ISPs and packet-switched paths that Gate 1 routing questions depend on.

## Prerequisites

Verify each tool works before starting:

- [ ] `traceroute --version` (or `mtr --version`)
- [ ] `whois --version`
- [ ] `ping -c 1 1.1.1.1` (confirm Internet reachable)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

2 hrs.

## Procedure

1. **Trace to a near destination.** Pick `cloudflare.com` or your ISP's website. Command: `traceroute cloudflare.com` (or `mtr -r -c 30 cloudflare.com` for cleaner output).
2. **Trace to a far US destination.** Pick `amazon.com` or `microsoft.com`. Command: `traceroute amazon.com` (or `mtr -r -c 30 amazon.com`).
3. **Trace to an international destination.** Pick `bbc.co.uk`, `nikkei.com`, or `lemonde.fr`. Command: `traceroute bbc.co.uk` (or `mtr -r -c 30 bbc.co.uk`).
4. **Capture each full output.** For each trace, identify:
    - First 1–3 hops (your local network and ISP entry)
    - Hops where latency jumps significantly (long-haul or transcontinental links)
    - Last hops (destination's network)
5. **ASN lookups.** Pick 5–10 interesting hop IPs across the three traces. Look up ASN and AS owner with `whois <ip>` or via [bgp.tools](https://bgp.tools/).

## What to capture

- [ ] Three full traceroute outputs → paste into lab-notes (or screenshots → `assets/02-trace-near.png`, `assets/02-trace-far-us.png`, `assets/02-trace-intl.png`)
- [ ] ASN lookups for ≥5 hops across the three traces → paste into lab-notes
- [ ] Optional: hand-drawn or ASCII-art diagram of the path through tiers → `assets/02-topology.png` or pasted into lab-notes

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/` or in lab-notes
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- `* * *` for many hops → many routers don't respond to traceroute probes (firewall policy). Try `traceroute -T` (TCP-based) or `mtr -r -c 30`.
- Many stars beyond hop 2 → your ISP may have aggressive ICMP filtering. Note this; it's itself an observation.

## References

- K&R, Section 1.3 (Network core)
- Concept Notes 5, 6
- [bgp.tools](https://bgp.tools/)
