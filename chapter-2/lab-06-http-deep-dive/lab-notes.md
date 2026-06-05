# Lab 06 — HTTP Deep Dive — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README (`wireshark`, `tcpdump`, `curl`, `dig`)
- [ ] `groups | grep -q wireshark` succeeds (capture works without sudo)
- [ ] Egress interface for `1.1.1.1` identified and named below (from Step 1)
- [ ] Capture filter `host neverssl.com or host example.com or host httpbin.org` ready to apply
- [ ] Display filter `http` ready to apply
- [ ] `assets/` directory present for the captures, screenshots, and `curl` transcripts

> Egress interface the Wireshark capture attaches to:

> 

---

## Predict before you run

Before running any command, which of the four `curl` targets (`neverssl.com`, `example.com`, `httpbin.org`) do you expect to expose readable application-layer bytes in the Wireshark dissector pane, and why?

> 

---

## Capture summary

One row per saved capture. Fill each cell from the matching step after you stop the capture.

| Capture file | Driven by (command) | Connections opened | Request/response pairs |
|--------------|---------------------|--------------------|------------------------|
| `assets/01-http-capture.pcapng` | Step 3 — `curl -v http://neverssl.com` | | |
| `assets/02-persistent.pcapng` | Step 7 — `curl -v http://example.com http://example.com` | | |
| `assets/03-http10.pcapng` | Step 8 — `curl -v --http1.0 http://example.com http://example.com` | | |

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

> Egress interface name the capture in Step 2 attaches to:

---

### Step 2 — Open Wireshark and start a filtered capture

**Command:**

```text
Open Wireshark on the interface from Step 1.
Capture filter: host neverssl.com or host example.com or host httpbin.org
Start the capture.
```

**Output:**

```text

```

**What I observe:**

> Interface selected and capture-filter string applied:

---

### Step 3 — Run `curl` against the plain-HTTP endpoint

**Command:**

```bash
curl -v http://neverssl.com 2>&1 | tee assets/neverssl-curl.txt
```

**Output:**

```text

```

**What I observe:**

> Request method and target URL `curl` reported on the verbose request line:

---

### Step 4 — Save the capture and apply the display filter

**Command:**

```text
Stop the capture in Wireshark.
Save as: assets/01-http-capture.pcapng
Apply display filter: http
```

**Output:**

```text

```

**What I observe:**

> Number of packets remaining after the `http` display filter is applied:

---

### Step 5 — Inspect the HTTP request packet in the dissector

**Command:**

```text
Select the first HTTP request packet.
Expand the HTTP layer in the dissector pane.
```

**Output:**

```text

```

**What I observe:**

> Request line (method, request-target, HTTP version):

> Every request header present (Host, User-Agent, Accept, and any others):

---

### Step 6 — Inspect the HTTP response packet in the dissector

**Command:**

```text
Select the HTTP response packet that pairs with the Step 5 request.
Expand the HTTP layer in the dissector pane.
```

**Output:**

```text

```

**What I observe:**

> Status line (HTTP version, status code, reason phrase):

> Every response header present (Content-Type, Content-Length, Date, Server, and any others):

> Byte offset where the message body begins relative to the headers:

---

### Step 7 — Run a two-URL `curl` over a persistent connection

**Command:**

```bash
curl -v http://example.com http://example.com 2>&1 | tee assets/example-persistent.txt
```

Start a fresh capture before running, then save as `assets/02-persistent.pcapng`.

**Output:**

```text

```

**What I observe:**

> Count of TCP connection-setup groups, teardown groups, and HTTP request/response pairs in this capture:

---

### Step 8 — Compare the persistent capture with an HTTP/1.0 run

**Command:**

```bash
curl -v --http1.0 http://example.com http://example.com 2>&1 | tee assets/example-http10.txt
```

Capture this second invocation as `assets/03-http10.pcapng`.

**Output:**

```text

```

**What I observe:**

> Connection-setup count, teardown count, and request/response pair count for the HTTP/1.0 capture, set beside the same three counts from Step 7:

---

### Step 9 — Run `curl` to set a cookie

**Command:**

```bash
curl -v -c assets/cookies.txt https://httpbin.org/cookies/set?session=abc123 2>&1 | tee assets/cookies-set.txt
```

**Output:**

```text

```

**What I observe:**

> Response header in the verbose output that affects subsequent requests:

---

### Step 10 — Run `curl` sending the stored cookie

**Command:**

```bash
curl -v -b assets/cookies.txt https://httpbin.org/cookies 2>&1 | tee assets/cookies-send.txt
```

**Output:**

```text

```

**What I observe:**

> Request header the client sent this time that was absent in Step 9:

---

### Step 11 — Run a `HEAD` request to read cache-validator headers

**Command:**

```bash
curl -v -I https://example.com 2>&1 | tee assets/cache-headers.txt
```

**Output:**

```text

```

**What I observe:**

> Value of `ETag` and value of `Last-Modified` (note "absent" for either that is not present):

---

### Step 12 — Run a conditional `GET` with the captured ETag

**Command:**

```bash
curl -v -H 'If-None-Match: <etag-from-step-11>' https://example.com 2>&1 | tee assets/cache-revalidate.txt
```

Substitute the `ETag` value you captured in Step 11.

**Output:**

```text

```

**What I observe:**

> Status code on the response line for the conditional request:

---

## Per-layer header field interpretation

Pick one packet from the Step 4 capture (`assets/01-http-capture.pcapng`), expand every layer in the dissector pane, and fill one row per field. Leave "Observed value" and "What it identifies" for your own reading of the packet.

| Layer | Field | Observed value | What it identifies |
|-------|-------|----------------|--------------------|
| Ethernet | Source MAC | | |
| Ethernet | Destination MAC | | |
| IP | Source IP | | |
| IP | Destination IP | | |
| TCP | Source port | | |
| TCP | Destination port | | |
| TCP | Flags | | |
| HTTP | Request method or status code | | |
| HTTP | Host (request) or Content-Type (response) | | |

---

## Analysis questions

**Question 1:** Compare the byte offset you recorded in Step 6 with the header lines above it. What in the message format separates the headers from the body, and how does the dissector mark that boundary?

> 

**Question 2:** Set the three counts from Step 7 beside the three counts from Step 8. What does the difference in connection-setup groups tell you about how the persistent and HTTP/1.0 runs handled the two requests?

> 

**Question 3:** Trace the cookie across Steps 9 and 10. Which header carried the cookie from the server, which header carried it back from the client, and what does that round-trip let the server do that a single request could not?

> 

**Question 4:** Compare the status code you recorded in Step 12 against the one from an unconditional request in Step 11. What did the server's response to `If-None-Match` let the client avoid re-transferring?

> 

**Question 5:** For the four `curl` runs, contrast what the dissector pane shows at the application layer for the `neverssl.com` traffic versus the `httpbin.org` and `example.com` traffic. What accounts for the difference in what you can read?

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

**Walking down the dissector pane from Ethernet to HTTP, which field at each layer would you point to first to explain what the packet is, and why that one?**

> 

**Could I demo this lab's key finding — explaining every header field across the layers for one HTTP packet — in 60 seconds to a peer?**

> 

*Last updated: 2026-06-05*
