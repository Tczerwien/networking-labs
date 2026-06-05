# Lab 14 — IP Subnetting Drills — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`sipcalc --version`, or a bookmarked subnet-calculator URL)
- [ ] Pen and paper (or stylus + tablet) ready — the by-hand-first work happens off-screen
- [ ] `lab-notes.md` open with Part A / Part B / Part C stubs in place
- [ ] One verification calculator chosen and committed to for the whole lab (so the diff-trace stays consistent)
- [ ] `assets/` directory present for the scanned hand-work and verification screenshots

> Verification tool chosen (binary name or calculator URL):

> 

> Convention this calculator uses for the broadcast / wildcard rows (so you can read its output correctly):

> 

---

## Predict before you run

Before doing any arithmetic, write the rule you will apply to get usable-host count from a `/N` prefix, in your own words:

> 

For the Part C design, before allocating anything: in what order will you place the four subnets into the `10.0.0.0/16` block, and why that order?

> 

---

## Drill record — fill from your hand-work

A single-glance answer card. Solve each problem on paper FIRST, then transcribe your hand-derived result into the matching cell. Leave every value cell blank until you have committed a by-hand answer to it.

### Part A — Notation conversion

| # | Given prefix       | Subnet mask (your answer) | Usable hosts (your answer) |
|---|--------------------|---------------------------|----------------------------|
| 1 | `192.168.1.0/24`   |                           |                            |
| 2 | `10.0.0.0/16`      |                           |                            |
| 3 | `172.16.0.0/12`    |                           |                            |
| 4 | `192.168.50.128/25`|                           |                            |
| 5 | `10.20.30.0/30`    |                           |                            |

### Part B — Address decomposition

| # | Given address      | Network address | Broadcast address | Host range |
|---|--------------------|-----------------|-------------------|------------|
| 1 | `192.168.5.45/24`  |                 |                   |            |
| 2 | `10.10.10.130/25`  |                 |                   |            |
| 3 | `172.16.20.50/22`  |                 |                   |            |
| 4 | `192.168.100.200/27`|                |                   |            |
| 5 | `10.5.0.10/29`     |                 |                   |            |

### Part C — Subnet design (from `10.0.0.0/16`)

| Subnet | Required hosts | Network address | Mask (CIDR) | Broadcast | Host range |
|--------|----------------|-----------------|-------------|-----------|------------|
| A      | 500            |                 |             |           |            |
| B      | 200            |                 |             |           |            |
| C      | 50             |                 |             |           |            |
| D      | 4              |                 |             |           |            |

---

## Step-by-step record

### Step 1 — Open `lab-notes.md` and set up the three Part sections

No command for this step. Create the "Part A — Notation conversion", "Part B — Address decomposition", and "Part C — Subnet design" sections (above) and confirm each problem has a blank slot waiting.

**What I observe:**

> Sections present and every problem slot blank before any solving (yes / no):

---

### Step 2 — Note your by-hand solutions for all 11 problems

No command for this step — this is the pencil-and-paper work. Solve Part A (5), Part B (5), and Part C (1) with the bit-level work shown, then transcribe each result into the Drill-record tables above. Scan or photograph the worked paper.

**Capture to:** `assets/01-hand-solutions.pdf` (or `.jpg`)

**What I observe:**

> For each Part, the bit-pattern step that converts the prefix into the answer (host bits, mask octets, network/broadcast boundary):

> Where the Part C allocation forced a tradeoff (a subnet rounded up to the next prefix to cover its host count):

---

### Step 3 — Verify each Part A and Part B problem through the calculator

Run each given prefix/address through your chosen calculator AFTER you have a hand answer for it. With `sipcalc` the invocation is below; with a web calculator, paste the same prefix string.

**Command:**

```bash
sipcalc 192.168.1.0/24
sipcalc 10.0.0.0/16
sipcalc 172.16.0.0/12
sipcalc 192.168.50.128/25
sipcalc 10.20.30.0/30
sipcalc 192.168.5.45/24
sipcalc 10.10.10.130/25
sipcalc 172.16.20.50/22
sipcalc 192.168.100.200/27
sipcalc 10.5.0.10/29
```

**Capture to:** `assets/02-calculator-verification.png`

**Output:**

```text

```

**What I observe:**

> The calculator's field labels and which one maps to each column in your Drill-record table (network / broadcast / host range / usable count):

---

### Step 4 — Compare calculator output against your hand answers and trace any discrepancy

For every problem, set the calculator's reported values beside your hand-derived values. Where they match, mark it. Where they differ, find the bit-level step where your reasoning diverged.

**What I observe:**

> Which problems matched on the first pass and which did not:

> For each mismatch, the specific bit-level step where the hand answer and the calculator parted ways:

> The reasoning error behind each mismatch, stated as a rule you would now apply differently:

---

## Analysis questions

**Question 1:** Across the five Part A prefixes, how does the usable-host count change as the prefix length grows, and what in the bit layout of the mask explains that relationship?

> 

**Question 2:** In Part B, which problems gave a network address different from the address you were handed, and what about those prefixes made the given address sit somewhere other than the network boundary?

> 

**Question 3:** In your Part C design, account for the address space between the largest subnet you allocated and the `10.0.0.0/16` block size — how much of the block did the four subnets consume, and what is left?

> 

**Question 4:** For any discrepancy you traced in Step 4, was the error in the host-bit count, the boundary arithmetic, or the calculator's display convention? Categorize each one.

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

## Decision Gate 2 connection

**Which Decision Gate 2 question does this lab prepare me for?**

> 

**Given only an address and its mask from an incident report, which fields here (network, broadcast, host range, usable count) would you derive in your head to decide whether two hosts share a subnet — and which Part of this lab drilled that move?**

> 

**Could I demo this lab's key finding — converting a prefix and decomposing an address by hand — in 60 seconds to a peer, without a calculator?**

> 

*Last updated: 2026-06-05*
