# Lab 04 — Delay & Throughput Calculations

## Objective

Quantify your connection. Convert vague intuition into measured numbers and the formulas that explain them.

## Why this lab exists

- **Reinforces Concept Notes:** 6, 7
- **K&R sections covered:** 1.4 (Delay, loss, throughput)
- **Decision Gate 1 connection:** Indirect prep. Numeric fluency with delay components and throughput math underpins Gate 1 analysis questions.

## Prerequisites

Verify each tool works before starting:

- [ ] `ping -c 1 8.8.8.8`
- [ ] Browser open to `https://speedtest.net` or `https://fast.com`
- [ ] Calculator / unit-conversion ready (or `python3` / `bc` on hand)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1.5–2 hrs.

## Procedure

1. **RTT to gateway.** Command: `ping -c 20 <gateway>`. Record min/avg/max.
2. **RTT to public anycast.** Command: `ping -c 20 8.8.8.8`. Record min/avg/max.
3. **RTT to a coast-opposite US server (distant host).** Command: `ping -c 20 <distant_host>`. Record min/avg/max.
4. **Throughput.** Open speedtest.net or fast.com. Run a test. Record download and upload bandwidth in Mbps.
5. **Calculation A — 1 MB transmission delay.** For a 1 MB file (8,388,608 bits) at your measured download bandwidth: what is the transmission delay?
6. **Calculation B — 1500-byte packet on 1 Gbps.** For a 1500-byte packet on a 1 Gbps link: what is the transmission delay?
7. **Calculation C — propagation delay vs measured RTT.** Given the RTT to a host ~1500 km away, calculate propagation delay (assume signal ~2×10⁸ m/s in fiber). Compare to measured RTT — is the remainder queuing/processing/transmission?
8. **Loss.** If pings showed loss, calculate loss rate. If none, simulate: `ping -c 100 -i 0.01 -s 1000 <host>`.

## What to capture

- [ ] All ping outputs (text) → paste into lab-notes
- [ ] Speedtest result → screenshot to `assets/04-speedtest.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] All calculations show formulas, not just final numbers
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- "I confuse latency and throughput" → Latency = how long until first bit arrives. Throughput = how many bits/sec arrive once flowing. Freight train analogy: latency is time-to-first-car, throughput is cars-per-minute.
- Speedtest variance: run twice and use the better reading, or note both.

## References

- K&R, Section 1.4 (Delay, loss, throughput)
- Concept Notes 6, 7
