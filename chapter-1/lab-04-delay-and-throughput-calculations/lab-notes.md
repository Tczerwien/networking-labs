# Lab 04 — Quantify Your Connection: Delay & Throughput — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`ping`, `ip route`, a browser for speedtest.net or fast.com, calculator/pen-and-paper)
- [ ] `ping -c 1 127.0.0.1` succeeds (iputils-ping present)
- [ ] One distant host (another continent) pre-selected for the third ping target, named below before starting
- [ ] Speedtest tool chosen (speedtest.net OR fast.com) and committed to for the whole lab
- [ ] `assets/` directory present for the captured ping outputs and speedtest screenshot

> Default gateway IP (from `ip route`, the address after `default via`):

> 

> Pre-selected distant host (hostname or IP, and roughly where it is):

> 

> Speedtest tool chosen for this run (speedtest.net or fast.com):

> 

---

## Predict before you run

Before running any command, rank the three ping targets — your gateway, `8.8.8.8`, and your distant host — from lowest to highest round-trip time you expect, and say what physical fact about each path drives your ranking.

> 

---

## Measurement summary — fill from Steps 1–2

A single-glance record of what you measured. Fill each Value cell from the matching step's output.

| Measurement                          | Value (fill in) | Source command                    | Captured to                       |
|--------------------------------------|-----------------|-----------------------------------|-----------------------------------|
| Gateway RTT — min / avg / max (ms)   |                 | `ping -c 20 <gateway>`            | `assets/01-ping-gateway.txt`      |
| 8.8.8.8 RTT — min / avg / max (ms)   |                 | `ping -c 20 8.8.8.8`              | `assets/02-ping-8.8.8.8.txt`      |
| Distant-host RTT — min / avg / max (ms) |              | `ping -c 20 <distant-host>`       | `assets/03-ping-distant.txt`      |
| Download bandwidth (Mbps)            |                 | speedtest.net / fast.com          | `assets/04-speedtest.png`         |
| Upload bandwidth (Mbps)              |                 | speedtest.net / fast.com          | `assets/04-speedtest.png`         |
| Packet loss seen on any ping? (which / %) |            | the three `ping` runs             | n/a                               |

---

## Step-by-step record

### Step 1 — Run the measurement commands (ping each host, run one speedtest)

**Command:**

```bash
ip route
ping -c 20 <default-gateway-from-ip-route> | tee assets/01-ping-gateway.txt
ping -c 20 8.8.8.8 | tee assets/02-ping-8.8.8.8.txt
ping -c 20 <distant-host> | tee assets/03-ping-distant.txt
# then open speedtest.net (or fast.com) in a browser, run one test,
# and screenshot the final result page as assets/04-speedtest.png
```

**Output:**

```text

```

**What I observe:**

> Default-gateway IP returned by `ip route` (the address after `default via`):

> Min / avg / max round-trip time reported for the gateway, `8.8.8.8`, and the distant host (one line each, in ms):

> Download and upload bandwidth from the speedtest result page (in Mbps):

> Packets transmitted / received / lost on each of the three ping runs:

---

### Step 2 — Note the measurements in the summary table per the source schema

No new command for this step; transcribe from the Step 1 output and the speedtest screenshot into the `## Measurement summary` table above, then answer the caveat prompt.

**What I observe:**

> Per K&R §1.4.4, the single bandwidth number the speedtest reports represents the path's bottleneck link `min{R_s, R_c}` — state which end of the path (your access link or the server side) you believe is the bottleneck for your run, and what in your measurements points there:

> 

---

### Step 3 — Verify the calculation formulas by hand-computing each Problem Set prompt

No new shell command; this step is hand-computation. For each prompt below show work as `formula → substituted values → units → result`. Carry the binary value `1 MB = 8,388,608 bits` verbatim; use the textbook fiber signal speed `2×10⁸ m/s`; do not substitute `c`.

**3a — Transmission delay of a 1 MB file (8,388,608 bits) at your measured download bandwidth:**

> Formula → substituted values → units → result:

> 

**3b — Transmission delay of a 1500-byte packet on a 1 Gbps link:**

> Formula → substituted values → units → result:

> 

**3c — One-way propagation delay for a 1500 km path at `2×10⁸ m/s`, then the round-trip propagation delay (×2) for comparison to a measured ping RTT:**

> Formula → substituted values → units → result (one-way, then round-trip):

> 

**3d — Loss rate:** if any ping in Step 1 showed loss, compute the loss rate from its packets-transmitted vs packets-received. If none showed loss, run the simulation below and compute the loss rate from its result either way.

```bash
ping -c 100 -i 0.01 -s 1000 <host>
```

> Packets transmitted / received on the run used, and the loss rate as a percentage with the formula shown:

> 

---

### Step 4 — Compare measured RTT against theoretical propagation-only RTT for one host

No new command; reason from your Step 1 RTT and your Step 3c round-trip propagation figure for the same host.

**What I observe:**

> The host chosen for this comparison, its measured avg RTT (ms), and its round-trip propagation-only figure from 3c (ms):

> The numeric difference between measured RTT and propagation-only RTT, and which of the remaining three delay components (nodal processing, queuing, transmission `L/R`) per K&R §1.4.1 you attribute that gap to:

> 

---

## Analysis questions

**Question 1:** Across your three ping targets, how does the avg RTT change from the gateway outward to the distant host, and which of the four delay components from K&R §1.4.1 best accounts for the largest jump you see?

> 

**Question 2:** Compare the transmission delay you computed in 3a (1 MB at your download bandwidth) with the round-trip propagation delay you computed in 3c. For a transfer of that file to your distant host, which of the two would dominate the total time, and what does that tell you about when bandwidth matters versus when distance matters?

> 

**Question 3:** Your speedtest reported one bandwidth number for the whole path. Using the bottleneck-link idea `min{R_s, R_c}` from K&R §1.4.4, explain what that single number does and does not let you conclude about any individual link along the path.

> 

**Question 4:** Did your loss simulation in 3d actually induce loss on your link? Whether it did or not, what does the outcome tell you about the health and headroom of the path you tested?

> 

---

## Reflection

**What did I learn that I won't find in the textbook?**

> 

**What would I tell someone starting this lab tomorrow?**

> 

**Where did my mental model break? (List the moment you said "wait, that's not what I expected.")**

> 

---

## Decision Gate 1 connection

**How does understanding the four delay components prepare me to reason about a captured exchange at Decision Gate 1?**

> 

**For a packet exchange I will open in Wireshark at Gate 1, which delay component would a timestamp gap between two frames most likely reflect, and how would I argue that from the numbers I measured here?**

> 

**Could I demo this lab's key finding — measured RTT versus the propagation-only floor — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
