# Lab 02 — Traceroute Deep Dive — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`traceroute`, `mtr`, `whois`, `curl`)
- [ ] Browser available and `https://bgp.tools/` reachable
- [ ] `assets/` directory present for the captured command outputs
- [ ] Three destinations chosen and named below (near / far / international)

> Near-destination host (inside your ISP, or `cloudflare.com`):

> 

> Far-destination host (opposite coast or major cloud provider):

> 

> International-destination host (another continent):

> 

---

## Predict before you run

Before running any command, which of the three paths do you expect to have the most hops, and which the highest round-trip time to its final hop? Commit a guess for each.

> Most hops (which path, and why):

> 

> Highest final-hop round-trip time (which path, and why):

> 

---

## Path summary — fill from Steps 1-4

A single-glance comparison across the three paths. Fill each Value cell from the matching capture.

| Path                  | Destination (fill in) | Hop count | Final-hop avg RTT | First `* * *` hop (if any) | Captured to                              |
|-----------------------|-----------------------|-----------|-------------------|----------------------------|------------------------------------------|
| Near                  |                       |           |                   |                            | `assets/01-traceroute-near.txt`          |
| Far                   |                       |           |                   |                            | `assets/02-traceroute-far.txt`           |
| International         |                       |           |                   |                            | `assets/03-traceroute-international.txt`  |
| Far (`mtr`)           |                       |           |                   |                            | `assets/04-mtr.txt`                       |

---

## Step-by-step record

### Step 1 — Run `traceroute` to the near destination

**Command:**

```bash
traceroute <near-destination> | tee assets/01-traceroute-near.txt
```

**Capture to:** `assets/01-traceroute-near.txt`

**Output:**

```text

```

**What I observe:**

> The IP address and any hostname of every hop, in order:

---

### Step 2 — Run `traceroute` to the far destination

**Command:**

```bash
traceroute <far-destination> | tee assets/02-traceroute-far.txt
```

**Capture to:** `assets/02-traceroute-far.txt`

**Output:**

```text

```

**What I observe:**

> The hop number(s) where the round-trip time changes sharply relative to the previous hop (record the hop, not yet the cause):

---

### Step 3 — Run `traceroute` to the international destination

**Command:**

```bash
traceroute <international-destination> | tee assets/03-traceroute-international.txt
```

**Capture to:** `assets/03-traceroute-international.txt`

**Output:**

```text

```

**What I observe:**

> The hop number(s) where the round-trip time changes sharply relative to the previous hop:

---

### Step 4 — Run `mtr` against the far destination

**Command:**

```bash
mtr -r -c 30 <far-destination> | tee assets/04-mtr.txt
# add sudo if mtr reports a raw-socket permission error
```

**Capture to:** `assets/04-mtr.txt`

**Output:**

```text

```

**What I observe:**

> The per-hop loss percentage and average round-trip time for each hop:

---

### Step 5 — Run `whois` on the interesting hop IPs

**Command:**

```bash
whois <ip>
# repeat for 5-10 hop IPs: hops at RTT jumps, hops with transit-looking hostnames
```

**What I observe:**

> For each looked-up hop IP, the ASN and AS owner:

> 

> Hop IP 1 — ASN / AS owner:

> 

> Hop IP 2 — ASN / AS owner:

> 

> Hop IP 3 — ASN / AS owner:

> 

> Hop IP 4 — ASN / AS owner:

> 

> Hop IP 5 — ASN / AS owner:

> 

> (Add rows for any further hop IPs looked up:)

> 

---

### Step 6 — Inspect the AS path on bgp.tools

No new command for this step; open `https://bgp.tools/` and search one far-destination hop IP from Step 5.

**What I observe:**

> The sequence of AS numbers between your starting hop and the destination AS:

---

## Analysis questions

**Question 1:** Compare the near, far, and international traceroutes you captured in Steps 1-3. How does hop count track with the geographic distance to each destination, and where in each output do you see the evidence?

> 

**Question 2:** Look at the `mtr` report from Step 4 alongside the single-run far traceroute from Step 2. What does running 30 probes per hop reveal about a hop's round-trip time and loss that one pass does not, and which hops change character between the two views?

> 

**Question 3:** Using the ASNs from Step 5 and the AS path from Step 6, describe the boundaries where one operator's network hands the packet to another along the far path. Which hop IPs sit at those handoffs, and what in the `whois` output marks the boundary?

> 

**Question 4:** For any hop that appeared as `* * *` in your captures, what does that line tell you and what does it withhold? How does its presence affect your reading of the hop count and the per-hop RTTs around it?

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

**At Gate 1 you walk every header field in a single packet; here you walked the sequence of switches a packet visits. How does the destination IP in the Network-layer header relate to the hop-by-hop path you recorded?**

> 

**Could I demo this lab's key finding — one path through the AS tiers — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
