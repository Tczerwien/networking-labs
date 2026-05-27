---
lab-id: lab-04-delay-and-throughput-calculations
plan-source: _MASTER-PLAN/phase-01-networking-foundations/03-NetworkingFoundation_deliverables.md
concept-notes: ["Performance — The Four Components Of Delay", "Performance — Loss & Throughput"]
enrichment_status: pending
---

# Lab 04 — Quantify Your Connection: Delay & Throughput

## Objective

Measure round-trip time and end-to-end throughput on your connection, then hand-compute the transmission-delay, propagation-delay, and loss-rate formulas from K&R §1.4 against those measurements — converting vague intuition into numbers and the formulas that explain them.

## Why this lab exists

- **Reinforces Concept Notes:** 6 (Performance — The Four Components Of Delay), 7 (Performance — Loss & Throughput).
- **K&R sections covered:** §1.4.1 (Overview of Delay in Packet-Switched Networks — nodal processing, queuing, transmission `L/R`, propagation `d/s`), §1.4.4 (Throughput in Computer Networks — instantaneous + average throughput, bottleneck link `min{R_s, R_c}`).
- **Decision Gate 1 connection:** Indirect prep — Gate 1 demos protocol-stack encapsulation in Wireshark; an understanding of the four delay components and the bottleneck-link argument lets you reason about WHY a captured exchange takes as long as it does, not just WHAT layers are involved.

The four delay components separate into ones that scale with packet size (transmission `L/R`), ones that scale with link length and signal speed (propagation `d/s`), and ones that scale with queue occupancy (nodal processing and queuing). The lab asks you to measure round-trip time per host with `ping`, measure end-to-end throughput with a web speedtest, and then hand-compute each formula against your own numbers — so the math is anchored to a connection you can name, not an abstract textbook example.

## Prerequisites

Verify each tool works before starting:

- [ ] `ping -c 1 127.0.0.1` succeeds (iputils-ping present on Pop!_OS by default; if not, `sudo apt install -y iputils-ping`).
- [ ] A browser with internet access for [speedtest.net](https://www.speedtest.net) or [fast.com](https://fast.com) (either works; pick one and stay with it).
- [ ] Pen and paper or a calculator for the Problem Set hand-computation step.
- [ ] One known distant host (e.g., a server on another continent) for the third ping target. Pick before starting; do not improvise mid-lab.
- [ ] `ip route` (iproute2 — present on Pop!_OS by default) for default-gateway discovery.

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

60–90 min.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

1. Run the measurement commands and capture min/avg/max round-trip time per host plus end-to-end download/upload bandwidth:
   - `ip route` to discover the default gateway IP (the address after `default via`).
   - `ping -c 20 <default-gateway-from-ip-route> | tee assets/01-ping-gateway.txt` (a near-zero-distance baseline against your own router).
   - `ping -c 20 8.8.8.8 | tee assets/02-ping-8.8.8.8.txt` (a public DNS resolver, near baseline for one continental hop).
   - `ping -c 20 <distant-host> | tee assets/03-ping-distant.txt` (a host on another continent; substitute the host you pre-selected in Prerequisites).
   - Open speedtest.net (or fast.com) in a browser and run one test. Screenshot the final result page as `assets/04-speedtest.png`.
2. Note the measurements in `lab-notes.md` per the source schema: one round-trip-time table per host with min/avg/max in milliseconds; download and upload bandwidth in megabits per second from the speedtest; and the aggregated-throughput caveat that the bandwidth number represents the path's bottleneck link `min{R_s, R_c}` per K&R §1.4.4, not any single intermediate link.
3. Verify the calculation formulas by hand-computing each prompt in the `## Problem Set` section below: transmission delay for a 1 MB file at your measured download bandwidth, transmission delay for a 1500-byte packet on a 1 Gbps link, propagation delay for a 1500 km distance assuming 2×10⁸ m/s fiber signal speed, and the loss-rate calculation. Note your work in `lab-notes.md` with explicit show-work (formula → substituted values → units → result), not just the final number.
4. Compare measured round-trip time against the theoretical propagation-only round-trip time for one host. Note the difference in `lab-notes.md` and trace it to the queuing, processing, and transmission delay components per K&R §1.4.1.

## Problem Set

3. **Calculations:**
   - For a 1 MB file (8,388,608 bits) at your measured download bandwidth: what's the **transmission delay**?
   - For a packet on a 1 Gbps link: what's the transmission delay of a 1500-byte packet?
   - Given your RTT to a host 1500 km away, calculate the **propagation delay** (assume signal speed ~2×10⁸ m/s in fiber). Compare to your measured RTT — is the rest queuing/processing/transmission?
4. **Loss:** if any of your pings showed packet loss, calculate the loss rate. If none showed loss, simulate it: `ping -c 100 -i 0.01 -s 1000 <host>` and see if you can saturate enough to lose any.

## What to capture

- [ ] Gateway ping output: save as `assets/01-ping-gateway.txt`
- [ ] 8.8.8.8 ping output: save as `assets/02-ping-8.8.8.8.txt`
- [ ] Distant-host ping output: save as `assets/03-ping-distant.txt`
- [ ] Speedtest result-page screenshot: save as `assets/04-speedtest.png`
- [ ] Explicit show-work for all four Problem Set prompts in `lab-notes.md` (formula → substituted values → units → result)

## Deliverable checklist

The lab is done when:

- [ ] All three ping output files present in `assets/`
- [ ] Speedtest screenshot present in `assets/`
- [ ] Problem Set calculations completed with explicit show-work in `lab-notes.md`
- [ ] Comparison paragraph (measured round-trip time vs theoretical propagation-only round-trip time) completed in `lab-notes.md`
- [ ] Reflection section completed and Status field in `lab-notes.md` set to "Complete"

## Common pitfalls

- `ping -c 20` blocks for 20+ seconds per host on a slow link (one ping per second by default); budget 60–90 seconds for the three sequential pings.
- speedtest.net and fast.com pick different test servers and may report substantially different bandwidth numbers — pick one and stay with it for both the measurement step and any re-runs, otherwise the bottleneck-link comparison is muddled.
- The 2×10⁸ m/s signal-speed assumption is the K&R §1.4.1 textbook value for fiber (~2/3 c); copper and wireless segments diverge from this. Use the textbook value for the Problem Set; do not substitute c (3×10⁸ m/s).
- Loss simulation may not actually induce loss on a healthy link — the source acknowledges this; the `ping -c 100 -i 0.01 -s 1000 <host>` command is the attempt, not a guaranteed outcome. Note the outcome (whether loss occurred or not) and the loss rate either way.
- Unit conversion: `1 MB = 8,388,608 bits = 8 × 1024² bits` (binary), not `8 × 10⁶` (decimal). The Problem Set spells out the binary value; carry it verbatim through your formula.
- The propagation-delay formula `d / (2×10⁸ m/s)` gives one-way delay. Multiply by 2 for the round-trip comparison to your measured ping RTT, otherwise the comparison is off by a factor of 2.

## References

- K&R 8e, §1.4.1 (Overview of Delay in Packet-Switched Networks — nodal processing, queuing, transmission delay `L/R`, propagation delay `d/s`)
- K&R 8e, §1.4.4 (Throughput in Computer Networks — instantaneous + average throughput, bottleneck link `min{R_s, R_c}`)
- Concept Notes: Performance — The Four Components Of Delay; Performance — Loss & Throughput
- Data Communications Lecture 2 (00:33:00–00:42:00) — Transmission delay vs propagation delay + caravan analogy
- Data Communications Lecture 2 (00:58:36–01:01:13) — Throughput + bottleneck bandwidth

<!-- citations-v1.1
- K&R 8e §1.4.1 (Overview of Delay in Packet-Switched Networks) [sha256:a7db00014979] 2026-05-27
- K&R 8e §1.4.4 (Throughput in Computer Networks) [sha256:60739348b0e4] 2026-05-27
- Lecture2 00:33:00-00:42:00 (Transmission delay vs propagation delay + caravan analogy) [sha256:809dc46b6a4f] 2026-05-27
- Lecture2 00:58:36-01:01:13 (Throughput + bottleneck bandwidth) [sha256:53ab57ac1078] 2026-05-27
<!-- /citations-v1.1 -->

*Last updated: 2026-05-27 — Phase 10 Plan 10-02 enrichment per NET-03*
