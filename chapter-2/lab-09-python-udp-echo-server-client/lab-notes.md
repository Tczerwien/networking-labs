# Lab 09 — Python UDP Echo Server and Client — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`python3`, `wireshark`, `tcpdump`, `wireshark`-group membership, `ss`)
- [ ] Port 9999 confirmed free before starting the server (`ss -unl | grep 9999`)
- [ ] Loopback interface (`lo`) identified as the capture target
- [ ] `assets/` directory present for the two captures, the dissector screenshot, and the two source files

> Loopback interface name and current state:

> 

> Result of the port-9999 free-check:

> 

---

## Predict before you run

Before writing or running anything, what do you expect a UDP datagram exchange to look like on the wire — how many packets, and in what order — compared with a connection-oriented exchange? Record the prediction now so you can check it against Steps 7 and 12.

> 

---

## Datagram capture summary — fill from Steps 6-12

One row per capture run. Fill each cell from the matching step's dissector inspection.

| Capture                          | Datagram count | Client→server port pair | Server→client port pair | Captured to                  |
|----------------------------------|----------------|-------------------------|-------------------------|------------------------------|
| Single message (Steps 4-7)       |                |                         |                         | `assets/01-udp-single.pcapng`|
| Five-message loop (Steps 10-12)  |                |                         |                         | `assets/02-udp-loop.pcapng`  |

---

## Per-layer field interpretation — fill from Step 7

Pick one datagram from the single-message capture and expand every layer in the dissector pane. For each row, read the Observed value from the dissector and write, in your own words, what that field identifies.

| Layer       | Field                     | Observed value | What it identifies |
|-------------|---------------------------|----------------|--------------------|
| Frame       | Capture length (bytes)    |                |                    |
| Ethernet/Loopback | Encapsulation type  |                |                    |
| IPv4        | Source address            |                |                    |
| IPv4        | Destination address       |                |                    |
| IPv4        | Protocol number           |                |                    |
| UDP         | Source port               |                |                    |
| UDP         | Destination port          |                |                    |
| UDP         | Length                    |                |                    |
| UDP         | Checksum                  |                |                    |
| Data        | Payload bytes             |                |                    |

---

## Step-by-step record

### Step 1 — Edit `udp_echo_server.py` to implement the server body

**Command:**

```bash
${EDITOR:-nano} assets/udp_echo_server.py
```

**Capture to:** `assets/udp_echo_server.py`

**Output:**

```text

```

**What I observe:**

> Address and port the server binds to, and the call it blocks on while waiting:

---

### Step 2 — Edit `udp_echo_client.py` to implement the client body

**Command:**

```bash
${EDITOR:-nano} assets/udp_echo_client.py
```

**Capture to:** `assets/udp_echo_client.py`

**Output:**

```text

```

**What I observe:**

> Destination address/port the client sends to, and the type the payload is passed as:

---

### Step 3 — Open Wireshark on `lo`, apply the filter, and start the first capture

**Command:**

```bash
wireshark -i lo -k -f "udp port 9999"
# or open Wireshark, select the lo interface, and set the display filter:
#   udp.port == 9999
```

**Output:**

```text

```

**What I observe:**

> Interface selected and the filter string applied before the capture starts:

---

### Step 4 — Run the server in terminal 1 and verify it binds

**Command:**

```bash
python3 assets/udp_echo_server.py
```

**Output:**

```text

```

**What I observe:**

> Whether the bind succeeded and any startup line the server printed:

---

### Step 5 — Run the client in terminal 2 and read both sides

**Command:**

```bash
python3 assets/udp_echo_client.py
```

**Output:**

```text

```

**What I observe:**

> Reply printed by the client, and the line the server printed on receipt:

---

### Step 6 — End the first capture and save it

**Command:**

```bash
# Stop the Wireshark capture, then:
#   File > Save As > assets/01-udp-single.pcapng
```

**Capture to:** `assets/01-udp-single.pcapng`

**Output:**

```text

```

**What I observe:**

> Number of packets retained in the saved capture after the filter:

---

### Step 7 — Inspect the single-message datagrams in the dissector pane

**Command:**

```bash
# In Wireshark: select a datagram, expand the UDP layer in the detail pane.
# Optional CLI cross-check:
tshark -r assets/01-udp-single.pcapng -V
```

**Output:**

```text

```

**What I observe:**

> For each datagram — source port, destination port, payload length, and UDP checksum value:

> Expand all layers on one datagram and save the dissector screenshot to `assets/03-udp-dissector.png`. Layers visible top to bottom:

---

### Step 8 — Edit the client to send 5 messages in a loop

**Command:**

```bash
${EDITOR:-nano} assets/udp_echo_client.py
```

**Capture to:** `assets/udp_echo_client.py`

**Output:**

```text

```

**What I observe:**

> Change made to turn the single send into a five-iteration loop:

---

### Step 9 — Open Wireshark again and start a fresh capture

**Command:**

```bash
wireshark -i lo -k -f "udp port 9999"
# or open Wireshark, select lo, set display filter:
#   udp.port == 9999
```

**Output:**

```text

```

**What I observe:**

> Confirmation the capture is empty and running before the second run starts:

---

### Step 10 — Run the server again in terminal 1

**Command:**

```bash
python3 assets/udp_echo_server.py
```

**Output:**

```text

```

**What I observe:**

> Source port the server now reports binding to (compare with Step 4):

---

### Step 11 — Run the looping client and save the second capture

**Command:**

```bash
python3 assets/udp_echo_client.py
# Stop the Wireshark capture, then:
#   File > Save As > assets/02-udp-loop.pcapng
```

**Capture to:** `assets/02-udp-loop.pcapng`

**Output:**

```text

```

**What I observe:**

> Replies printed by the client across the five iterations:

---

### Step 12 — Inspect the loop capture for total count and any setup/teardown

**Command:**

```bash
# In Wireshark: read the packet count in the status bar.
# Optional CLI cross-check:
tshark -r assets/02-udp-loop.pcapng | wc -l
```

**Output:**

```text

```

**What I observe:**

> Total datagram count, and whether any packet resembles connection setup or teardown:

---

## Analysis questions

**Question 1:** Look at the source and destination ports across the request and the reply in the single-message capture. Which port stayed fixed across both directions and which one was assigned, and what does each port number tell you about who is addressing whom?

> 

**Question 2:** Compare the datagram count in the five-message loop capture (Step 12) against your Step 11 reply count. What is the relationship between application-level `sendto` calls and packets on the wire, and what does that say about how UDP maps messages to datagrams?

> 

**Question 3:** Revisit the prediction you wrote in "Predict before you run." Did the captures contain any packets beyond the request/reply pairs? What about the absence (or presence) of those packets distinguishes this transport from a connection-oriented one?

> 

**Question 4:** Using the per-layer table, trace one datagram from the outermost layer down to the payload bytes. At which layer does the port appear, at which layer does the IP address appear, and how does that layering let the same host carry many independent conversations at once?

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

**At Gate 1 you explain every header field across the layers of a live capture. Using your per-layer table, which fields here belong to the transport layer versus the network layer, and how would you point to each in the dissector during the demo?**

> 

**Could I demo this lab's key finding — what a bare datagram exchange looks like with no handshake or teardown — in 60 seconds to a peer?**

> 

---

*Last updated: 2026-06-05*
