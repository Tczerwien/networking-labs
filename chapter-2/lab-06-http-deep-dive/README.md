---
lab-id: lab-06-http-deep-dive
plan-source: _MASTER-PLAN/phase-02-application-layer/03-ApplicationLayer_deliverables.md
concept-notes: ["Web & HTTP — Overview, Connections, Message Format", "HTTP — Cookies, Caching, Conditional GET"]
enrichment_status: pending
---

# Lab 06 — HTTP Deep Dive

## Objective

Capture HTTP traffic at the byte level and decode request/response message format. Drive `curl` through three behavioural variations (persistent vs non-persistent connections, cookies, caching) and inspect each variation in the Wireshark dissector.

## Why this lab exists

- **Reinforces Concept Notes:** Web & HTTP — Overview, Connections, Message Format; HTTP — Cookies, Caching, Conditional GET
- **K&R sections covered:** §2.2.1 (HTTP Overview), §2.2.2 (Non-Persistent and Persistent Connections), §2.2.3 (Message Format), §2.2.4 (Cookies), §2.2.5 (Web Caching)
- **Decision Gate 1 connection:** Direct prep — Decision Gate 1 asks you to open a Wireshark capture and explain every header field across the layers; this lab exercises HTTP-at-the-top-of-the-stack dissection that the gate demos with HTTP traffic.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `curl --version`
- [ ] `dig --version` (verify `dig` is installed even though this lab does not use it directly; lab-07 needs it)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `host neverssl.com or host example.com or host httpbin.org`

**Display filter (Wireshark syntax):** `http`

1. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark capture in step 2 attaches to this interface.
2. Open Wireshark on the interface from step 1. Apply the capture filter above and start a capture.
3. Run `curl -v http://neverssl.com 2>&1 | tee assets/neverssl-curl.txt`. Capture the traffic for the duration of the request, then stop the capture in Wireshark.
4. Save the capture as `assets/01-http-capture.pcapng`. Apply the display filter `http` in Wireshark.
5. Inspect the first HTTP request packet in the dissector pane. Note the request line and every request header (Host, User-Agent, Accept, and any others present) in your lab-notes.
6. Inspect the corresponding HTTP response packet. Note the status line and every response header (Content-Type, Content-Length, Date, Server, and any others present). Note the byte offset where the message body begins relative to the headers.
7. Run `curl -v http://example.com http://example.com 2>&1 | tee assets/example-persistent.txt` while a fresh capture is active. Save the capture as `assets/02-persistent.pcapng`.
8. Compare the persistent-connection capture from step 7 with the output of `curl -v --http1.0 http://example.com http://example.com 2>&1 | tee assets/example-http10.txt`. Capture the second invocation as `assets/03-http10.pcapng`. Note the three-way handshake count, FIN packet count, and HTTP request/response pair count in each capture.
9. Run `curl -v -c assets/cookies.txt https://httpbin.org/cookies/set?session=abc123 2>&1 | tee assets/cookies-set.txt`. Inspect the response headers in the curl verbose output. Note any header that affects subsequent requests.
10. Run `curl -v -b assets/cookies.txt https://httpbin.org/cookies 2>&1 | tee assets/cookies-send.txt`. Inspect the request headers. Note which header was sent by the client this time.
11. Run `curl -v -I https://example.com 2>&1 | tee assets/cache-headers.txt`. Note the values of `ETag` and `Last-Modified` (if present) in the response.
12. Run `curl -v -H 'If-None-Match: <etag-from-step-11>' https://example.com 2>&1 | tee assets/cache-revalidate.txt` substituting the ETag value captured in step 11. Note the status code in the response line.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| TCP | Source port |  |  |
| TCP | Destination port |  |  |
| TCP | Flags |  |  |
| HTTP | Request method or status code |  |  |
| HTTP | Host (request) or Content-Type (response) |  |  |

## What to capture

- [ ] Packet capture saved as `assets/01-http-capture.pcapng`
- [ ] Persistent-connection capture saved as `assets/02-persistent.pcapng`
- [ ] HTTP/1.0 capture saved as `assets/03-http10.pcapng`
- [ ] curl verbose output saved as `assets/neverssl-curl.txt`
- [ ] curl verbose output saved as `assets/example-persistent.txt`
- [ ] curl verbose output saved as `assets/example-http10.txt`
- [ ] Cookies set output saved as `assets/cookies-set.txt`
- [ ] Cookies send output saved as `assets/cookies-send.txt`
- [ ] Cache headers output saved as `assets/cache-headers.txt`
- [ ] Cache revalidation output saved as `assets/cache-revalidate.txt`
- [ ] Dissector-pane screenshot with all layers expanded: save as `assets/01-http-dissector.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Did your capture filter actually match the traffic you intended to see? `neverssl.com` may resolve to a different IP than the one you saw last time — filter by hostname or by both directions of the TCP stream rather than by a single IP.
- Did you stop each capture before exporting, or did you let it grow unboundedly across the four `curl` runs in steps 3, 7, 8?
- Did you pick a single packet from the conversation before expanding the dissector pane, instead of trying to interpret the whole stream at once?
- Did you use `--http1.0` (two dashes, no space) and not `-http1.0`? curl silently ignores unknown short flags.
- The `neverssl.com` domain in step 3 deliberately serves plain HTTP (no TLS) so that the application-layer bytes are visible in the dissector pane; the `httpbin.org` and `example.com` end systems in steps 9-12 use TLS and the dissector pane will show encrypted application-layer bytes for those captures.

## References

- K&R, §2.2.1 (HTTP Overview), §2.2.2 (Non-Persistent and Persistent Connections), §2.2.3 (HTTP Message Format), §2.2.4 (Cookies), §2.2.5 (Web Caching)
- Concept Notes: Web & HTTP — Overview, Connections, Message Format; HTTP — Cookies, Caching, Conditional GET
- RFC 9110 — HTTP Semantics: <https://www.rfc-editor.org/rfc/rfc9110.html>
- MDN HTTP Headers reference: <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers>

<!-- citations-v1.1
- K&R 8e §2.2.1 (HTTP Overview) [sha256:130369a42bdc] 2026-05-25
- K&R 8e §2.2.2 (Non-Persistent and Persistent Connections) [sha256:f51abe396104] 2026-05-25
- Lecture5 00:13:24-00:14:08 (Wireshark protocol-stack walkthrough showing HTTP at top of stack) [sha256:1207a4c76e6a] 2026-05-25
- RFC 9110 §15.4.1 (200 OK) [sha256:3dc2267924d0] 2026-05-25
<!-- /citations-v1.1 -->

*Last updated: 2026-05-25 — Phase 8 Plan 08-02 enrichment per NET-01 (lab-06 D-06 trip-wire)*
