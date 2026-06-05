# Lab 13 — ICMP & Traceroute Internals — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark`, `tcpdump`, `traceroute`, `mtr`)
- [ ] `groups | grep -q wireshark` confirms capture group membership
- [ ] Egress interface (the one carrying the route to `1.1.1.1`) identified and named below
- [ ] Capture filter `icmp` and display filter `icmp` ready to apply
- [ ] `assets/` directory present for the `.pcapng` captures and screenshots

> Egress interface name (from Step 1):

> 

---

## Predict before you run

Before capturing anything, the default `traceroute` and the `-I` variant send different probe packets. Which transport does each use, and what do you expect to see (or not see) under a capture filter of `icmp`?

> 

---

## Capture summary

One row per saved capture. Fill each cell from the matching step as you go.

| Capture file                        | Tool / command            | Source step | Saved? | Notes (fill in) |
|-------------------------------------|---------------------------|-------------|--------|-----------------|
| `assets/01-ping.pcapng`             | `ping -c 4 8.8.8.8`       | Step 4      |        |                 |
| `assets/02-traceroute-udp.pcapng`   | `traceroute google.com`   | Step 7      |        |                 |
| `assets/03-traceroute-icmp.pcapng`  | `traceroute -I google.com`| Step 10     |        |                 |
| `assets/04-mtr.pcapng`              | `mtr -c 30 8.8.8.8`       | Step 16     |        |                 |

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

> Egress interface name that the steps-2/5/8/11 captures attach to:

---

### Step 2 — Open Wireshark and start the `icmp` capture

**Command:**

```bash
# Open Wireshark on the interface from Step 1, apply capture filter `icmp`, start capture
wireshark
```

**Output:**

```text

```

**What I observe:**

> Capture filter applied and the interface the capture is bound to:

---

### Step 3 — Run `ping` and stop the capture

**Command:**

```bash
ping -c 4 8.8.8.8
```

**Output:**

```text

```

**What I observe:**

> Number of ICMP packets captured during the ping run:

---

### Step 4 — Save the ping capture and inspect the ICMP fields

**Command:**

```bash
# Save the capture as assets/01-ping.pcapng, then inspect the ICMP packets in Wireshark
```

**Capture to:** `assets/01-ping.pcapng`

**Output:**

```text

```

**What I observe:**

> Type and code field of the outbound packets:

> Type and code field of the inbound packets:

> Sequence-number field across the 4 ping iterations:

---

### Step 5 — Open a fresh capture for the default traceroute

**Command:**

```bash
# Open Wireshark for a fresh capture on the interface from Step 1, filter `icmp`
wireshark
```

**Output:**

```text

```

**What I observe:**

> Capture filter and interface confirmed for this fresh capture:

---

### Step 6 — Run the default `traceroute` and stop the capture

**Command:**

```bash
traceroute google.com
```

**Output:**

```text

```

**What I observe:**

> Hops printed in the terminal, including any `* * *` (silent) rows:

---

### Step 7 — Save the default-traceroute capture

**Command:**

```bash
# Save the capture as assets/02-traceroute-udp.pcapng
```

**Capture to:** `assets/02-traceroute-udp.pcapng`

**Output:**

```text

```

**What I observe:**

> ICMP packets present in this capture (counts of outbound vs inbound under the `icmp` filter):

---

### Step 8 — Open another fresh capture for the forced-ICMP traceroute

**Command:**

```bash
# Open Wireshark for another fresh capture on the same interface, filter `icmp`
wireshark
```

**Output:**

```text

```

**What I observe:**

> Capture filter and interface confirmed for this fresh capture:

---

### Step 9 — Run `traceroute -I` and stop the capture

**Command:**

```bash
traceroute -I google.com
```

**Output:**

```text

```

**What I observe:**

> Hops printed in the terminal, including any `* * *` (silent) rows:

---

### Step 10 — Save the forced-ICMP-traceroute capture

**Command:**

```bash
# Save the capture as assets/03-traceroute-icmp.pcapng
```

**Capture to:** `assets/03-traceroute-icmp.pcapng`

**Output:**

```text

```

**What I observe:**

> ICMP packets present in this capture (counts of outbound vs inbound under the `icmp` filter):

---

### Step 11 — Compare the two traceroute captures

**Command:**

```bash
# Compare assets/02-traceroute-udp.pcapng (Step 7) against assets/03-traceroute-icmp.pcapng (Step 10)
```

**Output:**

```text

```

**What I observe:**

> Differences in outbound packet types between the two captures:

> Differences in inbound packet types between the two captures:

> Difference in total captured packet counts between the two captures:

---

### Step 12 — Inspect the Time Exceeded packets in the dissector

**Command:**

```bash
# Open assets/03-traceroute-icmp.pcapng in Wireshark, apply display filter `icmp.type == 11`
```

**Display filter:** `icmp.type == 11`

**Capture to:** `assets/03-time-exceeded-dissector.png`

**Output:**

```text

```

**What I observe:**

> Source IP of the responding router for a filtered packet:

> The original packet embedded inside the ICMP error (which protocol / addresses it carries):

> time-to-live (TTL) value visible in that embedded packet's IP header:

---

### Step 13 — Note the final ICMP packet that signals arrival

**Command:**

```bash
# In the same capture, locate the final ICMP packet that signals the destination was reached
```

**Output:**

```text

```

**What I observe:**

> Type field of the final ICMP packet:

> Code field of the final ICMP packet:

> Source IP of the final ICMP packet:

---

### Step 14 — Open one more fresh capture for `mtr`

**Command:**

```bash
# Open Wireshark for one more fresh capture on the same interface, filter `icmp`
wireshark
```

**Output:**

```text

```

**What I observe:**

> Capture filter and interface confirmed for this fresh capture:

---

### Step 15 — Run `mtr` and stop the capture

**Command:**

```bash
mtr -c 30 8.8.8.8
```

**Output:**

```text

```

**What I observe:**

> Per-hop rows shown in the `mtr` terminal display while it runs:

---

### Step 16 — Save the `mtr` capture and read the loss column

**Command:**

```bash
# Save the capture as assets/04-mtr.pcapng; screenshot the mtr terminal as assets/04-mtr-stdout.png
```

**Capture to:** `assets/04-mtr.pcapng` and `assets/04-mtr-stdout.png`

**Output:**

```text

```

**What I observe:**

> Per-hop loss-percentage column values from the `mtr` terminal output:

---

## Per-layer header field interpretation

Pick one ICMP packet from a saved capture (a Time Exceeded packet from Step 12 makes a rich example). Expand each layer in the dissector pane and fill in the observed value and what that field identifies. Leave a row blank only if the chosen packet does not carry that field, and note which packet you used.

> Packet chosen (capture file + frame number):

> 

| Layer    | Field                    | Observed value | What it identifies |
|----------|--------------------------|----------------|--------------------|
| Ethernet | Source MAC               |                |                    |
| Ethernet | Destination MAC          |                |                    |
| IP       | Source IP                |                |                    |
| IP       | Destination IP           |                |                    |
| IP       | time-to-live (TTL)       |                |                    |
| IP       | Protocol (= 1 for ICMP)  |                |                    |
| ICMP     | Type                     |                |                    |
| ICMP     | Code                     |                |                    |
| ICMP     | Checksum                 |                |                    |
| ICMP     | Identifier               |                |                    |
| ICMP     | Sequence number          |                |                    |

---

## Analysis questions

**Question 1:** Looking at your ping capture (Step 4), how do the type/code values on the outbound packets relate to the type/code values on the inbound packets, and what does each pair tell you about who is asking and who is answering?

> 

**Question 2:** Your two traceroute captures (Steps 7 and 10) were taken under the same `icmp` capture filter, yet they differ. From what you observed, what does that difference reveal about how each traceroute mode probes the path?

> 

**Question 3:** Inside the Step-12 Time Exceeded message, the responding router echoed back part of your original packet. Why would a router include that embedded fragment, and how does the TTL value you read there connect to why that particular router was the one to respond?

> 

**Question 4:** Compare what `mtr` reports in its loss-percentage column (Step 16) against the `* * *` rows you may have seen in the plain `traceroute` runs. What might explain a non-zero loss figure for an intermediate hop without the destination itself being unreachable?

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

**Walk the ICMP-layer fields (type, code, identifier, sequence number) and the IP-layer TTL field as you would at the gate — which one would you point to first to prove a packet is a Time Exceeded error, and why?**

> 

**Could I demo this lab's key finding — the embedded packet and its TTL inside a Time Exceeded message — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
