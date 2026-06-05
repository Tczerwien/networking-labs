# Lab 08 — SMTP Over Telnet — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`telnet`, `wireshark`, `tcpdump`, `nc`)
- [ ] `groups | grep -q wireshark` passes (capture works without sudo)
- [ ] Setup path chosen and committed to for the whole procedure (A — local Postfix, or B — Mailtrap sandbox)
- [ ] If path A: Postfix active and bound on port 25 (`sudo systemctl status postfix`, `ss -tlnp | grep :25`)
- [ ] If path B: Mailtrap free tier confirmed at <https://mailtrap.io/pricing>, credentials noted, host reachable (`nc -vz <host> <port>`)
- [ ] `assets/` directory present for the capture, transcript, and screenshots

> Setup path chosen (A or B):

> 

> Server endpoint in use (host : port):

> 

---

## Predict before you run

Before you start the capture, what do you expect to see in the Wireshark dissector pane for an SMTP command line, given that SMTP is described in the README as a cleartext application protocol? Note your expectation now so you can check it against Step 15.

> 

---

## Capture summary

Fill one row per SMTP request/reply pair as you walk the capture in Steps 12-13. Use the dissector pane and Follow-TCP-Stream view.

| Telnet command sent | Server status code | Server reply text | Captured packet # |
|---------------------|--------------------|-------------------|-------------------|
| (server greeting)   |                    |                   |                   |
| `HELO`              |                    |                   |                   |
| `MAIL FROM`         |                    |                   |                   |
| `RCPT TO`           |                    |                   |                   |
| `DATA`              |                    |                   |                   |
| (message + `.`)     |                    |                   |                   |
| `QUIT`              |                    |                   |                   |

---

## Step-by-step record

### Step 1 — Note the egress interface for the SMTP endpoint

**Command:**

```bash
ip route get 127.0.0.1
# path B:
ip route get <mailtrap-host>
```

**Output:**

```text

```

**What I observe:**

> Egress interface the capture in Step 2 must attach to:

---

### Step 2 — Open Wireshark on that interface and start the capture

**Command:**

```text
Open Wireshark, select the interface from Step 1,
apply the capture filter, and start capturing.
Capture filter (BPF): tcp port 25 or tcp port 587 or tcp port 2525
```

**Output:**

```text

```

**What I observe:**

> Interface selected and capture-filter string applied:

---

### Step 3 — Open the telnet connection and read the greeting

**Command:**

```bash
telnet localhost 25
# path B:
telnet <mailtrap-host> <mailtrap-port>
```

**Output:**

```text

```

**What I observe:**

> First server reply line (status code + message):

---

### Step 4 — Send the HELO command

**Command:**

```text
HELO mydomain.local
```

**Output:**

```text

```

**What I observe:**

> Server reply to HELO (status code + message):

---

### Step 5 — Send the MAIL FROM command

**Command:**

```text
MAIL FROM:<test@mydomain.local>
```

**Output:**

```text

```

**What I observe:**

> Server reply to MAIL FROM (status code + message):

---

### Step 6 — Send the RCPT TO command

**Command:**

```text
RCPT TO:<test@mydomain.local>
# path B:
RCPT TO:<your-mailtrap-test-address>
```

**Output:**

```text

```

**What I observe:**

> Server reply to RCPT TO (status code + message):

---

### Step 7 — Send the DATA command

**Command:**

```text
DATA
```

**Output:**

```text

```

**What I observe:**

> Server reply to DATA (status code + message), and what it instructs you to do next:

---

### Step 8 — Send the message body and the end-of-data terminator

**Command:**

```text
Subject: Test message from telnet
<blank line>
This is a test message I sent by hand via telnet.
.
```

**Output:**

```text

```

**What I observe:**

> Server reply after the lone `.` line (status code + message), and any queue/accept token in it:

---

### Step 9 — Send QUIT and confirm the connection closes

**Command:**

```text
QUIT
```

**Output:**

```text

```

**What I observe:**

> Server reply to QUIT (status code + message) and the connection-close state of the terminal:

---

### Step 10 — End the capture and save the pcapng

**Command:**

```text
Stop the Wireshark capture once the connection has closed,
then File > Save As: assets/01-smtp-exchange.pcapng
```

**Capture to:** `assets/01-smtp-exchange.pcapng`

**Output:**

```text

```

**What I observe:**

> Capture stopped at the right moment, packet count saved, and file path written:

---

### Step 11 — Save the telnet transcript

**Command:**

```bash
# copy from terminal scrollback into assets/02-telnet-transcript.txt
# or re-run under script:
script -c 'telnet localhost 25' assets/02-telnet-transcript.txt
```

**Capture to:** `assets/02-telnet-transcript.txt`

**Output:**

```text

```

**What I observe:**

> Transcript saved, and a check that the lone `.` terminator landed on its own line:

---

### Step 12 — Inspect the first SMTP packet in the dissector pane

**Command:**

```text
Apply the display filter in Wireshark, then select the first SMTP packet.
Display filter: smtp or tcp.port == 25 or tcp.port == 587 or tcp.port == 2525
```

**Output:**

```text

```

**What I observe:**

> First SMTP packet's request command and the matching server reply (status code + message):

---

### Step 13 — Inspect each subsequent SMTP packet in turn

**Command:**

```text
Step through the remaining SMTP packets in the packet list,
reading each request command and its server reply.
```

**Output:**

```text

```

**What I observe:**

> Each server reply in sequence (status code + message), in the order they appear:

---

### Step 14 — Inspect the DATA-phase packets

**Command:**

```text
Select the packets that carry the message after DATA,
and Right-click > Follow > TCP Stream. Save the stream view to
assets/04-smtp-stream.txt
```

**Capture to:** `assets/04-smtp-stream.txt`

**Output:**

```text

```

**What I observe:**

> Boundary between the header lines and the message body, and the byte sequence that terminates the message:

---

### Step 15 — Inspect the dissector pane at the byte level

**Command:**

```text
Expand all protocol layers for one SMTP request/reply packet
and screenshot it to assets/03-smtp-dissector.png
```

**Capture to:** `assets/03-smtp-dissector.png`

**Output:**

```text

```

**What I observe:**

> What is legible at the byte level for each SMTP command and reply in the dissector pane:

---

## Per-layer header field interpretation

Pick one SMTP request/reply packet from your capture and fill every cell from its expanded dissector pane. The "What it identifies" column is your own one-line reading of what that field tells you about the packet.

| Layer    | Field                                       | Observed value | What it identifies |
|----------|---------------------------------------------|----------------|--------------------|
| Ethernet | Source MAC                                  |                |                    |
| Ethernet | Destination MAC                             |                |                    |
| IP       | Source IP                                   |                |                    |
| IP       | Destination IP                              |                |                    |
| TCP      | Source port                                 |                |                    |
| TCP      | Destination port                            |                |                    |
| TCP      | Flags                                       |                |                    |
| SMTP     | Request command (HELO/MAIL/RCPT/DATA/QUIT)  |                |                    |
| SMTP     | Response status code                        |                |                    |

---

## Analysis questions

**Question 1:** Walk the SMTP exchange you captured in order. Which command must succeed before the next one is accepted, and what in the server replies you recorded tells you the server is tracking the state of the transaction?

> 

**Question 2:** Take the three-digit status codes you recorded across Steps 3-9. RFC 5321 §4.2.1 defines a reply code as a single value with a class structure rather than three independent digits. Read your captured codes against that structure — what does the leading digit signal in each case, and where did the codes change as the transaction progressed?

> 

**Question 3:** Compare the bytes you saw in the dissector pane (Step 15) with what an analyst would see if this same login had run over a TLS-wrapped connection. What did the cleartext property let you read directly off the wire, and why does the README call that out as useful for Decision Gate 1?

> 

**Question 4:** Look at the TCP source and destination ports in your per-layer table. Which side of the connection does each port belong to, and how does the destination port relate to the SMTP service you targeted?

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

**Trace one SMTP byte you captured up the stack: name the Ethernet, IP, TCP, and SMTP field that each carry it, using your per-layer table. How would you narrate that path live at Gate 1?**

> 

**Could I demo this lab's key finding — the full cleartext SMTP conversation in the dissector pane — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
