# Lab 07 — DNS Resolution Trace — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark --version`, `tcpdump --version`, `dig --version`, `host --help`)
- [ ] `groups | grep -q wireshark` succeeds (capture group membership confirmed)
- [ ] `assets/` directory present for the captured `dig` outputs, the `.pcapng`, and the screenshots
- [ ] Egress interface (the one carrying the route to `1.1.1.1`) identified and named below — the Wireshark capture in Step 12 attaches to it

> Egress interface name (from Step 1):

> 

> Capture filter to apply (BPF): `udp port 53 or tcp port 53`

> Display filter to apply (Wireshark): `dns`

---

## Predict before you run

Before pointing `dig` at three different public resolvers in Steps 13-15, what do you expect to differ across them, and what do you expect to stay the same? Write your prediction now, then check it against the captured outputs.

> 

---

## Record-type capture summary — fill from Steps 5-10

One row per record-type query. Fill each cell from the matching step's answer section. Leave a cell blank if that query returned no record of that type.

| Step | Query                    | Record type | Answer-section record(s) (fill in) | Captured to                    |
|------|--------------------------|-------------|------------------------------------|--------------------------------|
| 5    | `dig A google.com`       | A           |                                    | `assets/04-dig-A.txt`          |
| 6    | `dig AAAA google.com`    | AAAA        |                                    | `assets/05-dig-AAAA.txt`       |
| 7    | `dig MX gmail.com`       | MX          |                                    | `assets/06-dig-MX.txt`         |
| 8    | `dig NS google.com`      | NS          |                                    | `assets/07-dig-NS.txt`         |
| 9    | `dig TXT google.com`     | TXT         |                                    | `assets/08-dig-TXT.txt`        |
| 10   | `dig CNAME www.google.com` | CNAME     |                                    | `assets/09-dig-CNAME.txt`      |

---

## Resolver comparison — fill from Steps 13-15

One row per resolver. Fill each cell from the matching capture/output. These rows feed Analysis Question 3.

| Resolver       | Query time (fill in) | Answer value(s) (fill in) | TTL (fill in) | Captured to                       |
|----------------|----------------------|---------------------------|---------------|-----------------------------------|
| `8.8.8.8`      |                      |                           |               | `assets/11-dig-google-dns.txt`    |
| `1.1.1.1`      |                      |                           |               | `assets/12-dig-cloudflare.txt`    |
| `9.9.9.9`      |                      |                           |               | `assets/13-dig-quad9.txt`         |

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

> Egress interface name the route to `1.1.1.1` leaves by:

---

### Step 2 — Run a default `dig` query

**Command:**

```bash
dig google.com 2>&1 | tee assets/01-dig-default.txt
```

**Capture to:** `assets/01-dig-default.txt`

**Output:**

```text

```

**What I observe:**

> Answer section, authority section, additional section, query time, and the resolver named in the `;; SERVER:` line:

---

### Step 3 — Run `dig +short` and compare against the default

**Command:**

```bash
dig +short google.com 2>&1 | tee assets/02-dig-short.txt
```

**Capture to:** `assets/02-dig-short.txt`

**Output:**

```text

```

**What I observe:**

> Which sections of the Step 2 default response are absent here:

---

### Step 4 — Run `dig +noall +answer` and compare against the default

**Command:**

```bash
dig +noall +answer google.com 2>&1 | tee assets/03-dig-answer-only.txt
```

**Capture to:** `assets/03-dig-answer-only.txt`

**Output:**

```text

```

**What I observe:**

> Which sections are kept and which are dropped versus the Step 2 default response:

---

### Step 5 — Run an `A`-record query

**Command:**

```bash
dig A google.com 2>&1 | tee assets/04-dig-A.txt
```

**Capture to:** `assets/04-dig-A.txt`

**Output:**

```text

```

**What I observe:**

> Each record in the answer section (name, TTL, class, type, value):

---

### Step 6 — Run an `AAAA`-record query

**Command:**

```bash
dig AAAA google.com 2>&1 | tee assets/05-dig-AAAA.txt
```

**Capture to:** `assets/05-dig-AAAA.txt`

**Output:**

```text

```

**What I observe:**

> Each record in the answer section (name, TTL, class, type, value):

---

### Step 7 — Run an `MX`-record query

**Command:**

```bash
dig MX gmail.com 2>&1 | tee assets/06-dig-MX.txt
```

**Capture to:** `assets/06-dig-MX.txt`

**Output:**

```text

```

**What I observe:**

> Each record in the answer section, including the preference value on each:

---

### Step 8 — Run an `NS`-record query

**Command:**

```bash
dig NS google.com 2>&1 | tee assets/07-dig-NS.txt
```

**Capture to:** `assets/07-dig-NS.txt`

**Output:**

```text

```

**What I observe:**

> Each record in the answer section (name, TTL, class, type, value):

---

### Step 9 — Run a `TXT`-record query

**Command:**

```bash
dig TXT google.com 2>&1 | tee assets/08-dig-TXT.txt
```

**Capture to:** `assets/08-dig-TXT.txt`

**Output:**

```text

```

**What I observe:**

> Each record in the answer section (name, TTL, class, type, value):

---

### Step 10 — Run a `CNAME`-record query

**Command:**

```bash
dig CNAME www.google.com 2>&1 | tee assets/09-dig-CNAME.txt
```

**Capture to:** `assets/09-dig-CNAME.txt`

**Output:**

```text

```

**What I observe:**

> Each record in the answer section (name, TTL, class, type, value):

---

### Step 11 — Run `dig +trace` over the hierarchy

**Command:**

```bash
dig +trace google.com 2>&1 | tee assets/10-dig-trace.txt
```

**Capture to:** `assets/10-dig-trace.txt`

**What I observe:**

> Each level of the hierarchy the trace passes through, in the order the output lists them:

---

### Step 12 — Open Wireshark and start a capture on the egress interface

**Command:**

```text
Open Wireshark on the interface from Step 1.
Apply capture filter:  udp port 53 or tcp port 53
Start capture.
```

**What I observe:**

> Interface selected and confirmation the capture filter was accepted (no syntax error):

---

### Step 13 — Run `dig @8.8.8.8` while the capture is active

**Command:**

```bash
dig @8.8.8.8 google.com 2>&1 | tee assets/11-dig-google-dns.txt
```

**Capture to:** `assets/11-dig-google-dns.txt`

**Output:**

```text

```

**What I observe:**

> Query time reported and the answer-section value(s) from this resolver:

---

### Step 14 — Run `dig @1.1.1.1` while the capture is active

**Command:**

```bash
dig @1.1.1.1 google.com 2>&1 | tee assets/12-dig-cloudflare.txt
```

**Capture to:** `assets/12-dig-cloudflare.txt`

**Output:**

```text

```

**What I observe:**

> Query time reported and the answer-section value(s) from this resolver:

---

### Step 15 — Run `dig @9.9.9.9` while the capture is active, then stop the capture

**Command:**

```bash
dig @9.9.9.9 google.com 2>&1 | tee assets/13-dig-quad9.txt
# stop the Wireshark capture after this command completes
```

**Capture to:** `assets/13-dig-quad9.txt`

**Output:**

```text

```

**What I observe:**

> Query time reported and the answer-section value(s) from this resolver:

---

### Step 16 — Save the capture and apply the display filter

**Command:**

```text
Save the capture as:  assets/14-dns-resolvers.pcapng
Apply display filter:  dns
```

**What I observe:**

> Confirmation the file saved and the packet count remaining after the `dns` display filter is applied:

---

### Step 17 — Inspect the first DNS query packet in the dissector pane

**Command:**

```text
Select the first DNS query packet.
Expand every layer in the dissector pane.
```

**What I observe:**

> Transaction ID, the flags field, the question section, and the record-type indicator on this query:

---

### Step 18 — Inspect the corresponding DNS response packet

**Command:**

```text
Select the response packet matching the Step 17 query (same transaction ID).
Expand every layer in the dissector pane.
```

**What I observe:**

> Transaction ID, the flags field, the answer section, the authority section, and the additional section on this response:

---

### Step 19 — Compare query times and answers across the three resolvers

No new command for this step; reason from the Steps 13-15 outputs and the captured packets.

**What I observe:**

> Differences in query time, answer value, and TTL across `8.8.8.8`, `1.1.1.1`, and `9.9.9.9`:

---

### Step 20 — Run a first cache-observation query

**Command:**

```bash
dig google.com 2>&1 | tee assets/15-dig-first.txt
```

**Capture to:** `assets/15-dig-first.txt`

**Output:**

```text

```

**What I observe:**

> Query time reported by this first query:

---

### Step 21 — Run the second cache-observation query immediately after

**Command:**

```bash
dig google.com 2>&1 | tee assets/16-dig-second.txt
```

**Capture to:** `assets/16-dig-second.txt`

**Output:**

```text

```

**What I observe:**

> Query time reported by this second query, and how it compares to the Step 20 query time:

---

## Per-layer header field interpretation

Fill this from the query+response pair you expanded in Steps 17-18. One row per field. The **Observed value** is what the dissector pane shows; **What it identifies** is your own one-line account of the field's role.

| Layer    | Field                                                | Observed value (fill in) | What it identifies (fill in) |
|----------|------------------------------------------------------|--------------------------|------------------------------|
| Ethernet | Source MAC                                           |                          |                              |
| Ethernet | Destination MAC                                      |                          |                              |
| IP       | Source IP                                            |                          |                              |
| IP       | Destination IP                                       |                          |                              |
| UDP      | Source port                                          |                          |                              |
| UDP      | Destination port                                     |                          |                              |
| DNS      | Transaction ID                                       |                          |                              |
| DNS      | Flags (QR, RD, RA)                                   |                          |                              |
| DNS      | Questions / Answers / Authority / Additional counts |                          |                              |

---

## Analysis questions

**Question 1:** Compare the default response in Step 2 with the `+short` output in Step 3 and the `+noall +answer` output in Step 4. What does each flag combination change about what `dig` prints, and what is lost when you only keep the answer section?

> 

**Question 2:** Across the record-type queries in Steps 5-10, how does the structure of an answer-section record stay the same, and what does the type-specific value field carry differently for each type you queried? Cite the records you captured.

> 

**Question 3:** Using the resolver-comparison table (Steps 13-15) and the captured packets, what differs and what agrees across the three resolvers? Where the values diverge, what in the outputs explains the divergence?

> 

**Question 4:** Look at the query times you recorded in Steps 20 and 21. What accounts for the relationship between the two times, and which part of the resolution path does that point to?

> 

**Question 5:** Match the fields in your per-layer table to the question+answer flow of the DNS message. How do the transaction ID and the flags field let a resolver pair a response with the query that prompted it?

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

**Decision Gate 1 asks you to open a Wireshark capture and explain every header field across the layers. Walking your per-layer table from Ethernet up to DNS, which field at each layer would you point to first, and why?**

> 

**Could I demo this lab's DNS-message dissection in 60 seconds to a peer, using the saved `assets/14-dns-resolvers.pcapng`?**

> 

*Last updated: 2026-06-05*
