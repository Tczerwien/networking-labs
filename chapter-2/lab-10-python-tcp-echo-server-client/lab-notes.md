# Lab 10 — Python TCP Echo Server and Client — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`python3`, `wireshark`, `tcpdump`, `wireshark` group membership, `ss`)
- [ ] `assets/` directory present for the server/client sources, the capture, and the screenshots
- [ ] Port 9998 confirmed free before starting the server (`ss -tlnp | grep 9998` returns nothing)
- [ ] Lab 09's `assets/01-udp-single.pcapng` present and accessible for the Step 9 comparison

> Loopback interface name as it appears in Wireshark's interface list:

> 

> Python version in use (`python3 --version`):

> 

---

## Predict before you run

Before capturing anything, write down how many packets you expect on the wire for a single client connect → one echo exchange → disconnect, and why.

> 

Before running, predict whether you expect more packets in this TCP exchange or in the Lab 09 UDP exchange, and name the reason you expect that.

> 

---

## Transport-layer field decode — fill from Step 8

Inspect the dissector pane for the first packet of the connection (Step 8) and the data-bearing segment (Step 7). Read each field off the dissector and record both the value you see and, in your own words, what that field tells you about the segment. Leave the value cells until you have run the capture.

| Layer            | Field                          | Observed value | What it identifies |
|------------------|--------------------------------|----------------|--------------------|
| Link (Ethernet)  | Source / destination MAC       |                | which link-layer endpoints framed this segment |
| Network (IPv4)   | Source address                 |                | which host originated the segment |
| Network (IPv4)   | Destination address            |                | which host the segment is bound for |
| Network (IPv4)   | Protocol field                 |                | which transport protocol the payload uses |
| Transport (TCP)  | Source port                    |                | the client-side endpoint of this connection |
| Transport (TCP)  | Destination port               |                | the server-side endpoint of this connection |
| Transport (TCP)  | Sequence number                |                | the byte-stream position this segment carries |
| Transport (TCP)  | Acknowledgment number          |                | the next byte this side expects to receive |
| Transport (TCP)  | Flags                          |                | the role of this segment in the connection |
| Application      | Payload bytes (data segment)   |                | the echoed message carried over the stream |

---

## Step-by-step record

### Step 1 — Edit `tcp_echo_server.py` to implement the server body

**Command:**

```bash
$EDITOR assets/tcp_echo_server.py
```

**Capture to:** `assets/tcp_echo_server.py`

**Output:**

```text

```

**What I observe:**

> The socket calls I used and the order I placed them in (binding, listening, accepting, receiving, sending, closing):

---

### Step 2 — Edit `tcp_echo_client.py` to implement the client body

**Command:**

```bash
$EDITOR assets/tcp_echo_client.py
```

**Capture to:** `assets/tcp_echo_client.py`

**Output:**

```text

```

**What I observe:**

> The socket calls I used on the client side and the type the message was sent as:

---

### Step 3 — Open Wireshark on `lo`, apply the filter, and start the capture

**Command:**

```text
Wireshark → select interface `lo` → display filter: tcp.port == 9998 → Start
```

**What I observe:**

> Interface selected and the display filter as entered:

---

### Step 4 — Run the server and verify the listening socket

**Command:**

```bash
# terminal 1
python3 assets/tcp_echo_server.py
# terminal 1 (separate shell)
ss -tlnp | grep 9998
```

**Output:**

```text

```

**What I observe:**

> Whether the process bound without error, and the socket state reported for port 9998:

---

### Step 5 — Run the client and read both sides of the exchange

**Command:**

```bash
# terminal 2
python3 assets/tcp_echo_client.py
```

**Output:**

```text

```

**What I observe:**

> The reply printed by the client and what the server printed to its stdout in terminal 1:

---

### Step 6 — End the capture and save it

**Command:**

```text
Wireshark → Stop capture → File → Save As → assets/01-tcp-exchange.pcapng
```

**Capture to:** `assets/01-tcp-exchange.pcapng`

**Output:**

```text

```

**What I observe:**

> Total number of packets Wireshark captured under the filter:

---

### Step 7 — Inspect the capture and classify the packets by phase

**Command:**

```text
Wireshark → packet list → read the TCP flag column for each packet
```

**Output:**

```text

```

**What I observe:**

> The packets that appear before any application data is exchanged, and the flags on each:

> The packet(s) that carry the application data:

> The packets that close the connection, and the flags on each:

---

### Step 8 — Inspect the dissector pane for the first packet of the connection

**Command:**

```text
Wireshark → select the first packet → expand the dissector tree → read the TCP layer
```

**Capture to:** `assets/02-tcp-dissector.png`

**Output:**

```text

```

**What I observe:**

> Source port, destination port, sequence number, acknowledgment number, and flags for this first packet (also recorded in the field-decode table above):

---

### Step 9 — Compare side-by-side with Lab 09's UDP capture

**Command:**

```text
Wireshark → open assets/01-udp-single.pcapng (Lab 09) alongside assets/01-tcp-exchange.pcapng
```

**Capture to:** `assets/03-udp-vs-tcp-compare.png`

**Output:**

```text

```

**What I observe:**

> Total packet count in each capture, and which packet types are present in one but not the other:

---

## Analysis questions

**Question 1:** Looking at the packets you classified in Step 7, which exchange happens before any application bytes move, and what does the flag pattern on those leading packets tell you about what the two sides agree on first?

> 

**Question 2:** In Step 5 the server returned the same message the client sent. Trace that message through your capture: which packet(s) carry it, and how do the sequence and acknowledgment numbers on the surrounding segments account for those bytes?

> 

**Question 3:** From the side-by-side comparison in Step 9, account for the difference in packet count between the UDP and TCP captures. Which packets in the TCP capture have no counterpart in the UDP capture, and what work are they doing?

> 

**Question 4:** The README distinguishes a welcoming socket from a connection socket. From what you saw on the wire and in the server's stdout, which socket does each phase of the exchange (connection setup, data transfer, teardown) belong to?

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

**At Gate 1 you must explain every transport-layer header field in a live capture. Using your field-decode table, which TCP fields would you point to first to prove a packet is connection setup versus data versus teardown?**

> 

**Could I demo this lab's key finding — the on-wire difference between TCP and UDP — in 60 seconds to a peer?**

> 

---

*Last updated: 2026-06-05*
