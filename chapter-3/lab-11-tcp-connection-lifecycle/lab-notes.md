# Lab 11 — TCP Connection Lifecycle — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark`, `tcpdump`, `curl`, `ss`)
- [ ] `wireshark` group membership confirmed (`groups | grep -q wireshark`)
- [ ] Egress interface for the route to `1.1.1.1` identified and named below (from Step 1)
- [ ] Wireshark capture started on that interface BEFORE the `curl` runs (Steps 2-3)
- [ ] `assets/` directory present for the pcapng, screenshot, and command outputs

> Egress interface (the one carrying the route to `1.1.1.1`):

> 

> Destination IP that `curl -v` actually resolved for `example.com` (from Step 4):

> 

---

## Predict before you run

Before you start the capture, write down how many distinct segments you expect to see open the connection, and how many you expect to see close it. Commit a number to each so Steps 5, 7, and 8 can confirm or correct it.

> Segments expected to OPEN the connection:

> 

> Segments expected to CLOSE the connection:

> 

---

## Capture summary — fill from Steps 5, 7, 9-13

One table for the lifecycle at a glance. Fill each cell from the matching step's output; leave a cell blank only if that phase produced nothing to record and note why.

| Lifecycle phase            | What to record                                  | Source step | Captured to                              |
|----------------------------|-------------------------------------------------|-------------|------------------------------------------|
| Connection open            | Flags + seq/ack on the first three segments     | Step 5      | `assets/01-tcp-lifecycle.pcapng`         |
| Mid-conversation segment   | The 11 header fields (see layer table below)    | Step 6      | `assets/01-tcp-dissector.png`            |
| Connection close           | Flags on the closing segments + their count     | Step 7      | `assets/01-tcp-lifecycle.pcapng`         |
| Socket state (general)     | The connection-state column from `ss -t`        | Step 9      | `assets/ss-output.txt`                   |
| Socket state (time-wait)   | Entries present immediately vs. after 30s       | Step 11     | `assets/ss-time-wait-*.txt`              |
| Socket state (established) | The new column `-p` adds vs. `ss -t`                    | Step 13     | n/a                                      |

---

## Per-layer header field interpretation — fill from Step 6

Pick ONE mid-conversation TCP segment in the dissector pane (after the opening segments, before the closing segments) and expand every layer. Record each field's observed value and, in your own words, what that field identifies.

| Layer | Field | Observed value | What it identifies |
|-------|-------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| TCP | Source port |  |  |
| TCP | Destination port |  |  |
| TCP | Sequence number |  |  |
| TCP | Acknowledgment number |  |  |
| TCP | Flags (SYN/ACK/FIN/RST/PSH/URG/CWR/ECE) |  |  |
| TCP | Window size |  |  |
| TCP | Checksum |  |  |
| TCP | Options (MSS / WScale / SACK) |  |  |

---

## Step-by-step record

### Step 1 — Run `ip route get` to find the egress interface

**Command:**

```bash
ip route get 1.1.1.1
```

**What I observe:**

> Egress interface name the route uses:

---

### Step 2 — Open Wireshark and start the capture on that interface

**Command:**

```text
Open Wireshark → select the interface from Step 1 →
apply capture filter:  host example.com  →  start capture
```

**What I observe:**

> Interface selected and capture filter applied (confirm capture is running before continuing):

---

### Step 3 — Run the `curl` request while the capture is live

**Command:**

```bash
curl -v https://example.com 2>&1 | tee assets/curl-output.txt
```

**Capture to:** `assets/curl-output.txt`

**Output:**

```text

```

**What I observe:**

> Destination IP that `curl -v` reported connecting to, and whether the request completed:

---

### Step 4 — Save the capture and apply the display filter

**Command:**

```text
Save capture as:  assets/01-tcp-lifecycle.pcapng
Read the destination IP from the curl -v output, then in Wireshark apply:
  tcp and ip.addr == <that-ip>
```

**Capture to:** `assets/01-tcp-lifecycle.pcapng`

**What I observe:**

> Number of segments remaining after the display filter is applied:

---

### Step 5 — Inspect the first three TCP segments

**Command:**

```text
In the filtered Wireshark view, select each of the first three TCP segments
in turn and read the Flags, Sequence number, and Acknowledgment number.
```

**Output:**

```text

```

**What I observe:**

> Flags set on each of the first three segments, and the seq/ack value on each:

---

### Step 6 — Inspect one mid-conversation segment and annotate its 11 fields

**Command:**

```text
Select one TCP segment from the middle of the data exchange (after the
opening segments, before the closing segments). Expand every layer in the
dissector pane and screenshot it.
```

**Capture to:** `assets/01-tcp-dissector.png`

**What I observe:**

> Which frame number you chose, and confirmation that all 11 fields in the layer table above are filled from this one segment:

---

### Step 7 — Inspect the final TCP segments of the conversation

**Command:**

```text
In the filtered Wireshark view, select the last TCP segments of the
conversation and read the flags set on each.
```

**Output:**

```text

```

**What I observe:**

> Flags set on the closing segments, and the count of closing segments observed:

---

### Step 8 — Compare your closing-segment count with K&R §3.5.6

**Command:**

```text
No new command. Compare the closing-segment count from Step 7 against the
canonical TCP teardown described in K&R §3.5.6.
```

**What I observe:**

> The teardown count K&R §3.5.6 describes, your observed count from Step 7, and any variation between the two:

---

### Step 9 — Run `ss -t` to read socket connection states

**Command:**

```bash
ss -t | tee assets/ss-output.txt
```

**Capture to:** `assets/ss-output.txt`

**Output:**

```text

```

**What I observe:**

> Values appearing in the connection-state column:

---

### Step 10 — Run `ss -t state established`

**Command:**

```bash
ss -t state established
```

**Output:**

```text

```

**What I observe:**

> Which entries appear under the `established` state filter:

---

### Step 11 — Capture `time-wait` immediately and again after 30 seconds

**Command:**

```bash
# immediately after curl returns:
ss -t state time-wait | tee assets/ss-time-wait-immediate.txt
# wait 30 seconds, then:
ss -t state time-wait | tee assets/ss-time-wait-after-30s.txt
```

**Capture to:** `assets/ss-time-wait-immediate.txt`, `assets/ss-time-wait-after-30s.txt`

**Output:**

```text

```

**What I observe:**

> Entries present in the immediate capture versus the after-30s capture:

---

### Step 12 — Run `ss -t state close-wait`

**Command:**

```bash
ss -t state close-wait
```

**Output:**

```text

```

**What I observe:**

> Which entries appear under the `close-wait` state filter (record across re-runs if it varies):

---

### Step 13 — Run `ss -tnp state established`

**Command:**

```bash
ss -tnp state established
```

**Output:**

```text

```

**What I observe:**

> The additional column present compared with the Step 10 output:

---

## Analysis questions

**Question 1:** Trace the sequence and acknowledgment numbers across the first three segments you captured in Step 5. What relationship do you see between one segment's seq/ack values and the next, and what does that relationship tell you about how the two endpoints agree on where the byte stream begins?

> 

**Question 2:** Look at the flags you recorded on the opening segments (Step 5) versus the closing segments (Step 7). What does each flag combination signal about the state of the connection at that moment?

> 

**Question 3:** Compare your immediate `time-wait` capture with the one taken 30 seconds later (Step 11). What changed between them, and what does that change suggest about how long a closed connection lingers in this state and why?

> 

**Question 4:** Of the 11 fields you annotated in the layer table, which ones change from segment to segment within this one conversation and which stay fixed? What does that split tell you about which fields identify the *connection* versus which fields describe an *individual segment*?

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

**At Gate 1 you must explain every header field across the layers from a live capture. Using the layer table you filled in Step 6, which fields sit at the Link layer, which at the Network layer, and which at the Transport layer — and how would you walk a reviewer through one segment top to bottom?**

> 

**Could I demo this lab's key finding — opening, data, and teardown of one TCP conversation — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
