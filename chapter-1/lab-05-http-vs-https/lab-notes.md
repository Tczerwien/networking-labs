# Lab 05 — HTTP vs HTTPS — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark --version`, `tcpdump --version`, `curl --version`)
- [ ] `groups | grep -q wireshark` succeeds (you are in the `wireshark` group — capture works without sudo)
- [ ] `ip route get 1.1.1.1` returns a valid egress interface
- [ ] Egress / capture interface identified and named below
- [ ] `assets/` directory present for the pcapng, curl logs, and dissector screenshots

> Egress interface the Wireshark capture attaches to (from `ip route get 1.1.1.1`):

> 

> Capture filter applied (BPF): `host neverssl.com or host wikipedia.org`

> Display filters used in Wireshark: `http`, then `tls`

---

## Predict before you run

Before you start the capture, write down what you expect a passive sniffer on this interface to be able to read from the plain-HTTP request to `neverssl.com` versus the HTTPS request to `wikipedia.org`. Name the specific fields you expect to be readable in each case.

> 

---

## Per-layer field interpretation — fill from Steps 6-9

For each row, open the matching packet in the Wireshark dissector pane and record what you actually see. Leave a cell blank only if the field is genuinely absent from that side of the capture (its absence is itself a finding — note it in Step 8). Fill every Observed-value cell from the capture, not from memory.

| Layer | Field | Observed value (HTTP side) | Observed value (HTTPS side) | What it identifies |
|-------|-------|----------------------------|-----------------------------|--------------------|
| TCP | Source port |  |  | |
| TCP | Destination port |  |  | |
| IP | Source IP |  |  | |
| IP | Destination IP |  |  | |
| HTTP | Method |  |  | |
| HTTP | Host header |  |  | |
| HTTP | Response body |  |  | |
| TLS | Record content type |  |  | |
| TLS | Handshake message types (before Application Data) |  |  | |

---

## Step-by-step record

### Step 1 — Run `ip route get 1.1.1.1` and identify the egress interface

**Command:**

```bash
ip route get 1.1.1.1
```

**Output:**

```text

```

**What I observe:**

> Egress interface name the capture will attach to:

---

### Step 2 — Open Wireshark on that interface and start a capture with the capture filter applied

**Command:**

```text
Wireshark → select the interface from Step 1 → set capture filter:
host neverssl.com or host wikipedia.org → start capture
```

**Output:**

```text

```

**What I observe:**

> Interface selected and capture-filter string Wireshark accepted before starting:

---

### Step 3 — Run the plain-HTTP request to generate traffic

**Command:**

```bash
curl -v http://neverssl.com 2>&1 | tee assets/02-neverssl-curl.txt
```

**Capture to:** `assets/02-neverssl-curl.txt`

**Output:**

```text

```

**What I observe:**

> Request line and the response status line `curl -v` printed for the HTTP request:

---

### Step 4 — Run the HTTPS request to generate traffic

**Command:**

```bash
curl -v --http1.1 https://wikipedia.org 2>&1 | tee assets/03-wikipedia-curl.txt
```

**Capture to:** `assets/03-wikipedia-curl.txt`

**Output:**

```text

```

**What I observe:**

> TLS-handshake / negotiated-protocol lines `curl -v` printed for the HTTPS request (lines beginning with `*`):

---

### Step 5 — Stop the capture and save it

**Command:**

```text
Wireshark → Stop capture → File → Save As → assets/01-http-vs-https.pcapng
```

**Capture to:** `assets/01-http-vs-https.pcapng`

**Output:**

```text

```

**What I observe:**

> Approximate packet count captured and the saved filename:

---

### Step 6 — Apply the `http` display filter and inspect the HTTP packets

**Command:**

```text
Wireshark display filter: http
```

**Capture to:** `assets/04-http-dissector.png`

**Output:**

```text

```

**What I observe:**

> Request method, request URL, Host header, response status, and any response-body content readable in the HTTP dissector pane:

---

### Step 7 — Apply the `tls` display filter and inspect the TLS packets

**Command:**

```text
Wireshark display filter: tls
```

**Capture to:** `assets/05-https-dissector.png`

**Output:**

```text

```

**What I observe:**

> Packet types appearing before any encrypted-data packet, and the packet at which the dissector pane transitions from named handshake message types to Application Data:

---

### Step 8 — Verify what is and is not visible in the encrypted Application Data packets

No new command for this step; expand an Application Data packet from Step 7 in the dissector pane and read its fields.

**What I observe:**

> Fields that ARE still visible in the encrypted Application Data packets (across every layer the dissector shows):

> Fields that are NOT visible in those packets (the application-layer fields that were readable in Step 6):

---

### Step 9 — Compare the HTTP and HTTPS sides using the per-layer table

No new command for this step; complete the per-layer field-interpretation table above from Steps 6-8, then write the comparison here.

**What I observe:**

> The layer at which the HTTP and HTTPS captures stop looking alike, and the field(s) that mark that boundary:

---

## Analysis questions

**Question 1:** Walk down the per-layer table from TCP up to the application layer. At which row do the HTTP and HTTPS observed values stop being equivalent in kind, and what does that tell you about which layers TLS leaves untouched?

> 

**Question 2:** In Step 6 you could read the request method, URL, and Host header for the plain-HTTP conversation. For the HTTPS conversation, which of those same items did you find anywhere in the capture, and where (if at all) did each one appear?

> 

**Question 3:** A passive observer on this interface — one who can see every byte but cannot decrypt — learns different things about the two conversations. Based on what you recorded, what can that observer still determine about the HTTPS conversation, and what is now hidden from them?

> 

**Question 4:** The README notes that modern `curl` negotiates TLS 1.3 by default. Compare the handshake message types you recorded in Step 7 against what an older TLS 1.2 walkthrough would describe. What did your capture show, and what does that say about how much of the handshake is itself protected?

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

**Gate 1 asks you to explain every header field across the layers of a capture. Using your per-layer table, which fields can you explain identically for both the HTTP and HTTPS conversations, and at which layer does that shared explanation stop?**

> 

**Could I demo this lab's key finding — what a sniffer sees for HTTP versus HTTPS — in 60 seconds to a peer, pointing at real packets?**

> 

---

*Last updated: 2026-06-05*
