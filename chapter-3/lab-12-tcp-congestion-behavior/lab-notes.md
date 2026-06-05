# Lab 12 — TCP Congestion Behavior — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark`, `tcpdump`, `iperf3`, `groups | grep wireshark`)
- [ ] Wireshark group membership confirmed (`groups | grep -q wireshark`) before any capture
- [ ] Egress interface (the one carrying your default route) identified and named below — the capture in Step 4 attaches to it
- [ ] iperf3 server selected from the list (host, port, region/limit notes) recorded below
- [ ] Kernel-default congestion-control variant recorded below (`sysctl net.ipv4.tcp_congestion_control`)
- [ ] `assets/` directory present for the captures, screenshots, and stdout

> Egress interface name:

> 

> iperf3 server (host / port / region / limit notes):

> 

> Kernel-default congestion-control variant:

> 

---

## Predict before you run

Before running the transfer, what shape do you expect the sequence-number-vs-time curve to take over the opening RTTs of the connection, and why?

> 

Before inspecting the SYN, do you expect the Window Scale option to be present on this connection? What is the consequence for the effective receive window either way?

> 

---

## Capture summary

A single-glance summary of the conversation. Fill each Value cell from the matching step.

| Item                                  | Value (fill in) | Source step | Captured to                          |
|---------------------------------------|-----------------|-------------|--------------------------------------|
| Egress interface                      |                 | Step 3      | n/a                                  |
| iperf3 server endpoint                |                 | Step 2      | `assets/00-iperf3-server-list.png`   |
| Per-second throughput (iperf3 stdout) |                 | Step 7      | `assets/iperf3-stdout.txt`           |
| Total throughput (iperf3 stdout)      |                 | Step 7      | `assets/iperf3-stdout.txt`           |
| Window Scale shift count (client SYN) |                 | Step 12     | `assets/01-iperf3.pcapng`            |
| Advertised window (mid-exchange ACK)  |                 | Step 13     | `assets/01-iperf3.pcapng`            |
| Effective window (advertised × 2^shift)|                | Step 14     | `assets/01-iperf3.pcapng`            |

---

## Step-by-step record

### Step 1 — Install iperf3 and confirm the version

**Command:**

```bash
sudo apt install -y iperf3
iperf3 --version
```

**Output:**

```text

```

**What I observe:**

> iperf3 version reported by the install:

---

### Step 2 — Open the server list and note one distant server

**Command:**

```bash
xdg-open https://iperf3serverlist.net
```

**Capture to:** `assets/00-iperf3-server-list.png`

**Output:**

```text

```

**What I observe:**

> Chosen server host, port (if non-default), and any region/limit notes:

---

### Step 3 — Identify the egress interface for the capture

**Command:**

```bash
ip route get 1.1.1.1
```

**Output:**

```text

```

**What I observe:**

> Egress interface name (the one Wireshark attaches to in Step 4):

---

### Step 4 — Open Wireshark on the interface and start a filtered capture

**Command:**

```text
Wireshark → select the interface from Step 3 → Capture filter:
host <iperf3-server-hostname> and tcp port 5201
→ start capture
```

**Output:**

```text

```

**What I observe:**

> Interface selected and the exact capture filter applied (with the real server hostname substituted):

---

### Step 5 — Run the 30-second iperf3 transfer and capture the traffic

**Command:**

```bash
iperf3 -c <server-from-step-2> -t 30 -i 1 2>&1 | tee assets/iperf3-stdout.txt
```

**Output:**

```text

```

**What I observe:**

> Whether the transfer ran to completion and the capture covered its full duration:

---

### Step 6 — Save the capture

**Command:**

```text
Wireshark → File → Save As → assets/01-iperf3.pcapng
```

**Output:**

```text

```

**What I observe:**

> Capture saved, and the packet count it contains:

---

### Step 7 — Note the throughput values from the iperf3 stdout

**Command:**

```bash
cat assets/iperf3-stdout.txt
```

**Output:**

```text

```

**What I observe:**

> Per-second throughput values across the run, and the total throughput reported at the end:

---

### Step 8 — Open and inspect the Time Sequence (Stevens) graph

**Command:**

```text
Wireshark → Statistics → TCP Stream Graphs → Time Sequence (Stevens)
```

**Capture to:** `assets/02-time-seq.png`

**Output:**

```text

```

**What I observe:**

> Overall shape of the sequence-number-vs-time curve across the whole conversation:

---

### Step 9 — Inspect the opening RTTs in the Time Sequence graph

**Command:**

```text
Wireshark → Time Sequence (Stevens) → zoom into the first few RTTs of the connection
```

**Output:**

```text

```

**What I observe:**

> Shape of the sequence-number-vs-time curve over the opening portion of the conversation:

---

### Step 10 — Open and inspect the Throughput graph

**Command:**

```text
Wireshark → Statistics → TCP Stream Graphs → Throughput
```

**Capture to:** `assets/03-throughput.png`

**Output:**

```text

```

**What I observe:**

> How throughput varies over the lifetime of the connection in the graph:

---

### Step 11 — Open and inspect the Window Scaling graph

**Command:**

```text
Wireshark → Statistics → TCP Stream Graphs → Window Scaling
```

**Capture to:** `assets/04-window-scaling.png`

**Output:**

```text

```

**What I observe:**

> How the advertised window tracks over the connection in the graph:

---

### Step 12 — Find the client SYN and inspect its TCP Options

**Command:**

```text
Wireshark → Display filter: tcp.flags.syn == 1 and tcp.flags.ack == 0
→ select the client SYN → expand TCP → Options in the dissector pane
```

**Output:**

```text

```

**What I observe:**

> Window Scale option shift count in the client SYN (or its absence):

---

### Step 13 — Find a mid-exchange ACK and inspect its TCP header

**Command:**

```text
Wireshark → Display filter: tcp.flags.ack == 1 and tcp.port == 5201
→ select an ACK well into the data exchange → expand TCP in the dissector pane
```

**Output:**

```text

```

**What I observe:**

> Advertised window value carried in that segment:

---

### Step 14 — Compute the effective receive window

**Command:**

```text
No new command — compute from Steps 12 and 13:
effective window = advertised window × 2^(Window Scale shift count)
```

**Output:**

```text

```

**What I observe:**

> Effective window value and the arithmetic that produced it:

---

### Step 15 — (Optional) Repeat the capture under 1% emulated loss

**Command:**

```bash
sudo tc qdisc add dev <interface> root netem loss 1%
# repeat Steps 4-6, saving the capture as assets/05-iperf3-with-loss.pcapng
sudo tc qdisc del dev <interface> root
```

**Output:**

```text

```

**What I observe:**

> How the sequence-number-vs-time and throughput graphs under loss differ from the loss-free run:

---

## Per-layer header field interpretation

Pick one representative data segment from the capture and read its dissector pane top to bottom. Fill the Observed value cell from that segment, and state in your own words what each field identifies.

| Layer    | Field                                | Observed value | What it identifies |
|----------|--------------------------------------|----------------|--------------------|
| Ethernet | Source MAC                           |                |                    |
| Ethernet | Destination MAC                      |                |                    |
| IP       | Source IP                            |                |                    |
| IP       | Destination IP                       |                |                    |
| TCP      | Source port                          |                |                    |
| TCP      | Destination port                     |                |                    |
| TCP      | Sequence number                      |                |                    |
| TCP      | Acknowledgment number                |                |                    |
| TCP      | Flags                                |                |                    |
| TCP      | Window size (advertised)             |                |                    |
| TCP      | Options — Window Scale (shift count) |                |                    |

---

## Analysis questions

**Question 1:** Looking at the opening RTTs you inspected in Step 9, how does the rate at which the sequence number climbs change as the connection gets older, and which phase of TCP congestion control does each portion of that curve correspond to?

> 

**Question 2:** Relate the per-second throughput numbers from the iperf3 stdout (Step 7) to the slope of the Time Sequence graph (Steps 8-9) and the Throughput graph (Step 10). Where do they agree, and where does the one tell you something the other does not?

> 

**Question 3:** Using the advertised window (Step 13), the Window Scale shift count (Step 12), and the effective window you computed (Step 14), explain what would have been mis-read about this connection's receive window if the Window Scale option had been ignored.

> 

**Question 4:** Compare the congestion-control variant you recorded in Setup with the textbook AIMD (Reno) behavior. Where does the shape of the curve you observed match the textbook account, and where does it depart from it?

> 

**Question 5 (if you ran Step 15):** Contrast the loss-free capture with the 1%-loss capture. What changed in the sequence-number-vs-time curve and the throughput, and which TCP mechanism accounts for the change?

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

**Walking the per-layer table top to bottom, which field would you point to first when asked to explain the TCP segment at the gate, and how would you tie the Window Scale option to the effective receive window?**

> 

**Could I demo this lab's key finding — the congestion-control shape and the effective-window calculation — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
