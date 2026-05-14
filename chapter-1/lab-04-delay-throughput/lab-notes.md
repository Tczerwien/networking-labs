# Lab 04 — Delay & Throughput Calculations — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README
- [ ] Connected to network (wifi or wired)
- [ ] Picked which distant host I will use, and noted its approximate distance from me

> Distant host:
> Approximate distance (km):

---

## Step-by-step record

### Step 1 — RTT to gateway

**Command:**

```bash
ping -c 20 <gateway>
```

**Output:**

```text

```

**min / avg / max (ms):**

> 

---

### Step 2 — RTT to 8.8.8.8

**Command:**

```bash
ping -c 20 8.8.8.8
```

**Output:**

```text

```

**min / avg / max (ms):**

> 

---

### Step 3 — RTT to distant host

**Command:**

```bash
ping -c 20 <distant_host>
```

**Output:**

```text

```

**min / avg / max (ms):**

> 

---

### Step 4 — Throughput

**Service used (speedtest.net / fast.com):**

> 

**Screenshot:**

![Speedtest result](./assets/04-speedtest.png)

**Download (Mbps):**

> 

**Upload (Mbps):**

> 

---

### Step 5 — Calculation A: 1 MB transmission delay

**Bits in 1 MB:** 8,388,608

**My download bandwidth (bps):**

> 

**Formula:**

```text
transmission_delay = file_size_bits / bandwidth_bps
```

**Work:**

> 

**Result (seconds):**

> 

---

### Step 6 — Calculation B: 1500-byte packet on 1 Gbps

**Packet size (bits):**

> 

**Bandwidth:** 1,000,000,000 bps

**Formula:**

```text
transmission_delay = packet_size_bits / bandwidth_bps
```

**Work:**

> 

**Result (seconds / microseconds):**

> 

---

### Step 7 — Calculation C: propagation delay vs measured RTT

**Distance to host (one-way, m):**

> 

**Signal speed in fiber:** 2 × 10⁸ m/s

**Formula:**

```text
propagation_delay_one_way = distance_m / signal_speed_mps
propagation_only_rtt    = 2 × propagation_delay_one_way
```

**Work:**

> 

**Theoretical propagation-only RTT (ms):**

> 

**Measured RTT (avg) to that host (ms):**

> 

**Gap (measured − theoretical, ms):**

> 

**Where the gap likely lives (queuing / processing / transmission):**

> 

---

### Step 8 — Loss

**Did natural pings show loss? If yes, rate:**

> 

**If no, simulated stress test command:**

```bash
ping -c 100 -i 0.01 -s 1000 <host>
```

**Output:**

```text

```

**Loss rate observed:**

> 

---

## Analysis questions

**Question 1 — Measurements table.** Fill in once everything above is done.

| Host | RTT min (ms) | RTT avg (ms) | RTT max (ms) |
|------|--------------|--------------|--------------|
| Gateway |  |  |  |
| 8.8.8.8 |  |  |  |
| Distant host |  |  |  |

| Throughput | Mbps |
|------------|------|
| Download |  |
| Upload |  |

**Question 2:** All calculations above show formulas, not just final numbers. Is there a step where I had to make an assumption (e.g., "I treated 1 MB as 8,388,608 bits, not 8,000,000 bits, because...")? Note it here.

> 

**Question 3:** For my distant host: measured RTT vs theoretical propagation-only RTT. What accounts for the gap?

> 

**Question 4:** If my download throughput is X Mbps, can I receive Y simultaneous video streams of Z Mbps? Show reasoning.

> 

**Question 5:** Which delay component am I most surprised by — and why?

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

**Which Decision Gate 1 question does this lab prepare me for?**

> 

**Could I demo this lab's key finding in 60 seconds to a peer?**

> 
