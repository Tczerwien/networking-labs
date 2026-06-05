# Lab 03 — Wireshark Encapsulation — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark --version`, `tcpdump --version`, `curl --version`)
- [ ] `groups | grep -q wireshark` confirms this account is in the `wireshark` capture group
- [ ] `ip route get 1.1.1.1` returns a valid egress interface
- [ ] `assets/` directory present for the capture, the curl output, and the dissector screenshot

> Egress interface (the one carrying the default route, captured on in Steps 2-4):

> 

> `neverssl.com` resolved IP (substitute for `<neverssl-ip>` in the capture and display filters):

> 

---

## Predict before you run

Before capturing, list the four layers you expect the dissector to break this HTTP GET packet into, from the link layer up to the application. Which layer do you expect to carry the source and destination MAC, and which the source and destination port?

> 

---

## Capture summary

A single-glance record of the capture session. Fill each cell from the matching step.

| Item                              | Value (fill in) | Source step | Captured to                          |
|-----------------------------------|-----------------|-------------|--------------------------------------|
| Egress interface captured on      |                 | Step 1      | n/a                                  |
| Capture filter applied (if any)   |                 | Step 2      | n/a                                  |
| curl exit / response status line  |                 | Step 3      | `assets/03-neverssl-curl.txt`        |
| Capture file saved                |                 | Step 5      | `assets/01-encapsulation.pcapng`     |
| Display filter applied            |                 | Step 6      | n/a                                  |
| HTTP GET packet number inspected  |                 | Step 6      | `assets/02-dissector-all-layers.png` |

---

## Step-by-step record

### Step 1 — Run `ip route get` to find the egress interface

**Command:**

```bash
ip route get 1.1.1.1
```

**Output:**

```text

```

**What I observe:**

> Egress interface name the Wireshark capture will attach to:

---

### Step 2 — Open Wireshark and start an unfiltered capture on that interface

**Command:**

```text
Open Wireshark, select the interface from Step 1, start capture with no capture filter applied.
```

**Output:**

```text

```

**What I observe:**

> Interface selected in Wireshark and whether packets begin appearing once capture starts:

---

### Step 3 — Run `curl` to generate the HTTP request traffic

**Command:**

```bash
curl http://neverssl.com 2>&1 | tee assets/03-neverssl-curl.txt
```

**Capture to:** `assets/03-neverssl-curl.txt`

**Output:**

```text

```

**What I observe:**

> Response status line and any redirect behaviour curl reports for `neverssl.com`:

---

### Step 4 — Capture the request, then stop the capture

**Command:**

```text
Let the capture run for the duration of the curl request, then stop the capture in Wireshark.
```

**Output:**

```text

```

**What I observe:**

> Approximate number of packets captured during the request window:

---

### Step 5 — Save the capture

**Command:**

```text
Save the capture as assets/01-encapsulation.pcapng (File > Save As, pcapng format).
```

**Capture to:** `assets/01-encapsulation.pcapng`

**Output:**

```text

```

**What I observe:**

> Saved capture file name and on-disk size:

---

### Step 6 — Apply the display filter and inspect the first HTTP GET packet

**Command:**

```text
Display filter (Wireshark syntax): http and ip.addr == <neverssl-ip>
Select the first HTTP GET packet and open it in the dissector pane.
```

**Capture to:** `assets/02-dissector-all-layers.png` (all four layers expanded)

**Output:**

```text

```

**What I observe:**

> Packet number of the first HTTP GET after the filter, and how many packets remain visible once the filter is applied:

---

### Step 7 — Inspect each layer in the dissector and record its header fields

**Command:**

```text
In the dissector pane, expand Ethernet, then IP, then TCP, then HTTP in turn.
Record the observed field values in the Per-layer header field interpretation table below.
```

**Output:**

```text

```

**What I observe:**

> Which dissector layer carries the MAC addresses, which carries the IP addresses, which carries the ports, and which carries the request method:

#### Per-layer header field interpretation

Fill the **Observed value** and **What it identifies** cells from the dissector for the chosen HTTP GET packet.

| Layer    | Field                | Observed value | What it identifies |
|----------|----------------------|----------------|--------------------|
| Ethernet | Source MAC           |                |                    |
| Ethernet | Destination MAC      |                |                    |
| IP       | Source IP            |                |                    |
| IP       | Destination IP       |                |                    |
| IP       | Time-to-live (TTL)   |                |                    |
| IP       | Protocol             |                |                    |
| TCP      | Source port          |                |                    |
| TCP      | Destination port     |                |                    |
| TCP      | Flags                |                |                    |
| HTTP     | Method               |                |                    |
| HTTP     | Host header          |                |                    |

---

### Step 8 — Explain each header field in your own words

**Command:**

```text
For each row in the table above, write a one-sentence explanation of what the field does, in your own words.
```

**Output:**

```text

```

**What I observe:**

> The field whose purpose was least obvious before opening the dissector, and what made it clear:

---

### Step 9 — Note any ARP traffic in the capture, separately from the HTTP analysis

**Command:**

```text
Apply the display filter: arp
Inspect any link-layer ARP exchanges visible in the capture window.
```

**Output:**

```text

```

**What I observe:**

> ARP packets present in the capture (request / reply), and which addresses they carry — recorded separately from the HTTP analysis above:

---

## Analysis questions

**Question 1:** Walking the dissector pane from the top frame down to the HTTP payload, which layer wraps which? Describe the nesting order you saw and what each layer adds around the one above it.

> 

**Question 2:** The MAC addresses in the Ethernet header and the IP addresses in the IP header describe two different things about where this packet is going. Compare the destination MAC against the destination IP you recorded — do they point at the same machine? What does that tell you about how the packet reaches `neverssl.com`?

> 

**Question 3:** The TCP destination port and the HTTP method both appear in this single packet. What does each one tell a receiver, and why do both need to be present in the same packet?

> 

**Question 4:** If ARP traffic appeared in your capture, why might it show up alongside an HTTP request that targets a host out on the public Internet? Tie your answer to the addresses you recorded in Step 9.

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

**This lab is the preliminary version of Decision Gate 1.** The full gate (after Phase 03) asks you to open a Wireshark capture cold and explain every header field across the Ethernet / IP / TCP / HTTP layers from scratch.

**Of the eleven fields in the per-layer table, which could you explain right now without looking at notes, and which still need another pass?**

> 

**Pick one field from each layer (Ethernet, IP, TCP, HTTP). Could you point a peer at it in the dissector and say what it identifies in under a minute?**

> 

**What would you need to add to be ready for the full Gate 1 captures (lab-11, lab-12, lab-13)?**

> 

*Last updated: 2026-06-05*
