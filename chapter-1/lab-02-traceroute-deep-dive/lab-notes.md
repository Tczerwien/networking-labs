# Lab 02 — Traceroute Deep Dive — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README
- [ ] Connected to network (wifi or wired)
- [ ] Chose which tool to use (`traceroute` or `mtr`)

> Tool used:

---

## Step-by-step record

### Step 1 — Trace to near destination

**Target host:**

> 

**Command:**

```bash

```

**Output:**

```text

```

**First 1–3 hops (local network / ISP entry):**

> 

**Hops with significant latency jumps:**

> 

**Last hops (destination network):**

> 

---

### Step 2 — Trace to far US destination

**Target host:**

> 

**Command:**

```bash

```

**Output:**

```text

```

**First 1–3 hops:**

> 

**Hops with significant latency jumps:**

> 

**Last hops:**

> 

---

### Step 3 — Trace to international destination

**Target host:**

> 

**Command:**

```bash

```

**Output:**

```text

```

**First 1–3 hops:**

> 

**Hops with significant latency jumps:**

> 

**Last hops:**

> 

---

### Step 4 — ASN lookups

For 5–10 interesting hop IPs across the three traces, look up the AS number and owner. Use `whois <ip>` or [bgp.tools](https://bgp.tools/).

| Hop IP | Source trace | ASN | AS owner | Notes |
|--------|--------------|-----|----------|-------|
|        |              |     |          |       |
|        |              |     |          |       |
|        |              |     |          |       |
|        |              |     |          |       |
|        |              |     |          |       |

---

### Step 5 — Topology sketch (optional)

> 

---

## Analysis questions

**Question 1 — near destination:** What story does the near trace tell about the path? (1 paragraph)

> 

**Question 2 — far US destination:** What story does the far US trace tell about the path? (1 paragraph)

> 

**Question 3 — international destination:** What story does the international trace tell about the path? (1 paragraph)

> 

**Question 4:** Which hops appeared to cross a Tier 1 backbone? Cite ASN evidence.

> 

**Question 5:** Where did latency jump most sharply? Why (geography, peering, congestion)?

> 

**Question 6:** Where did probes time out (`* * *`)? What does that suggest about those routers?

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
