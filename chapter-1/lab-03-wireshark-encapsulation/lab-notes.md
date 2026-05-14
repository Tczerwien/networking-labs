# Lab 03 — Wireshark Encapsulation — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README
- [ ] Connected to network (wifi or wired)
- [ ] Confirmed wireshark group membership (`groups | grep wireshark`)
- [ ] Logged out and back in after wireshark group membership change (if applicable)

---

## Step-by-step record

### Step 1 — Open Wireshark, pick active interface

**Interface chosen:**

> 

---

### Step 2 — Start capture (no filter)

**Capture start time:**

> 

---

### Step 3 — Generate plain-HTTP traffic

**Command:**

```bash
curl http://neverssl.com
```

**Curl output:**

```text

```

**Resolved IP of neverssl.com (from curl output or `dig neverssl.com`):**

> 

---

### Step 4 — Apply Wireshark filter

**Filter:**

```text
http and ip.addr == <neverssl-ip>
```

**How many packets matched:**

> 

---

### Step 5 — Pick one HTTP GET packet, expand all layers

**Frame number selected:**

> 

**Screenshot:**

![Wireshark dissector — all 4 layers expanded](./assets/03-wireshark-all-layers.png)

---

### Step 6 — Header field decode

#### Ethernet

| Field | Value | What it does (my words) |
|-------|-------|--------------------------|
| Source MAC |  |  |
| Destination MAC |  |  |
| EtherType |  |  |

#### IP (v4)

| Field | Value | What it does (my words) |
|-------|-------|--------------------------|
| Source IP |  |  |
| Destination IP |  |  |
| TTL |  |  |
| Protocol number |  |  |
| Total length |  |  |

#### TCP

| Field | Value | What it does (my words) |
|-------|-------|--------------------------|
| Source port |  |  |
| Destination port |  |  |
| Sequence number |  |  |
| Ack number |  |  |
| Flags (SYN/ACK/PSH/FIN) |  |  |
| Window size |  |  |

#### HTTP

| Field | Value | What it does (my words) |
|-------|-------|--------------------------|
| Request line (method / path / version) |  |  |
| Host header |  |  |
| User-Agent header |  |  |
| Accept header |  |  |

---

### Step 7 — Save capture

- [ ] Saved to `assets/03-encapsulation.pcapng`

---

## Analysis questions

**Question 1:** For each of the ~20 header fields above, the one-sentence explanation is filled in. Anything that surprised me about a field's purpose or default value:

> 

**Question 2:** Did I see any ARP traffic during the capture? What is it doing? (1 sentence — deep ARP comes in Phase 04+.)

> 

**Question 3:** If I removed any one header field, what would break and at what layer? Pick one field from each of Ethernet / IP / TCP / HTTP.

> 

**Question 4:** Where does encapsulation "end" on my host's side? Which layer hands the frame to the wire?

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

This lab IS the preliminary version of Gate 1.

**Could I redo this lab from scratch — no notes, no spec, just the goal — and produce the same decode?**

> 

**Could I demo this lab's key finding in 60 seconds to a peer?**

> 
