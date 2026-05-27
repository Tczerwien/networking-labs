---
lab-id: lab-05-http-vs-https
plan-source: _MASTER-PLAN/phase-01-networking-foundations/03-NetworkingFoundation_deliverables.md
concept-notes: ["Security Primitives — Threats & Defenses", "Layered Protocol Stack & Encapsulation"]
enrichment_status: pending
---

# Lab 05 — HTTP vs HTTPS

## Objective

Capture one plain HTTP conversation and one HTTPS conversation in a single Wireshark capture and compare what fields remain visible at each layer of the dissector.

## Why this lab exists

- **Reinforces Concept Notes:** 9, 8
- **K&R sections covered:** §1.5, §1.6, §8.6
- **Decision Gate 1 connection:** Indirect prep — Decision Gate 1 walks every header field across the protocol layers; this lab extends that view to the boundary where the TLS sublayer (K&R §8.6) hides the application-layer payload, so the demo-time answer to "what does a sniffer see for HTTPS?" is grounded in a real packet capture rather than memorised.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `curl --version`
- [ ] `ip route get 1.1.1.1` returns a valid egress interface

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `host neverssl.com or host wikipedia.org`

**Display filter (Wireshark syntax):** `http or tls`

1. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark capture in steps 2-5 attaches to this interface.
2. Open Wireshark on the interface from step 1 and start a capture with the capture filter above applied.
3. Run `curl -v http://neverssl.com 2>&1 | tee assets/02-neverssl-curl.txt` in a terminal to generate the plain HTTP traffic.
4. Run `curl -v https://wikipedia.org 2>&1 | tee assets/03-wikipedia-curl.txt` to generate the HTTPS traffic.
5. Capture the traffic for the duration of both requests, then stop the capture in Wireshark. Save the capture as `assets/01-http-vs-https.pcapng`.
6. Apply the display filter `http` in Wireshark. Inspect the HTTP packets in the dissector pane. Note the request method, URL, host header, response status, and any response body content visible in the dissector pane.
7. Apply the display filter `tls` in Wireshark. Inspect the TLS packets in the capture. Note the packet types appearing before any encrypted-data packets, and note the packet at which the dissector pane transitions from named handshake message types to Application Data.
8. Verify the absence of the HTTP method, URL, and body in the encrypted Application Data packets. Note in `lab-notes.md` which fields ARE visible in those encrypted-data packets and which fields are NOT.
9. Compare the HTTP and HTTPS sides of the capture using the table below. Note the comparison writeup in `lab-notes.md`.

### Per-layer header field interpretation

| Layer | Field name | HTTP capture observed | HTTPS capture observed |
|-------|------------|------------------------|-------------------------|
| TCP | Source port |  |  |
| TCP | Destination port |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| HTTP | Method |  |  |
| HTTP | Host header |  |  |
| HTTP | Response body |  |  |
| TLS | Record content type |  |  |
| TLS | Handshake message types (before Application Data) |  |  |

## What to capture

- [ ] Combined packet capture saved as `assets/01-http-vs-https.pcapng`
- [ ] HTTP `curl` terminal output saved as `assets/02-neverssl-curl.txt`
- [ ] HTTPS `curl` terminal output saved as `assets/03-wikipedia-curl.txt`
- [ ] HTTP dissector-pane screenshot saved as `assets/04-http-dissector.png`
- [ ] HTTPS dissector-pane screenshot (Application Data packet expanded) saved as `assets/05-https-dissector.png`
- [ ] Comparison writeup completed in `lab-notes.md`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Modern `curl` negotiates TLS 1.3 by default (since 2018), and TLS 1.3 hides more of the handshake than TLS 1.2; you may see fewer named handshake messages than older walkthroughs describe.
- The `tls` display-filter alias works for both TLS 1.2 and TLS 1.3 packets in Wireshark 3.0+.
- Browsers and curl may negotiate HTTP/2 over TLS; passing `--http1.1` to `curl -v https://wikipedia.org` keeps the request shape directly comparable with the HTTP/1.1 captured against `neverssl.com`.
- Captures may include unrelated TLS-using applications on the same interface; the capture filter `host neverssl.com or host wikipedia.org` restricts to the lab conversation.

## References

- K&R, Section 8.6 (Securing TCP Connections: TLS)
- K&R, Section 1.6 (Networks Under Attack)
- K&R, Section 1.5 (Protocol Layers)
- Concept Notes 9, 8
- RFC 8446 §4 (TLS 1.3 Handshake Protocol) — `https://www.rfc-editor.org/rfc/rfc8446.html#section-4`

<!-- citations-v1.1
- K&R 8e §8.6 (Securing TCP Connections: TLS) [sha256:8a18f23df381] 2026-05-26
- K&R 8e §1.6 (Networks Under Attack) [sha256:9e2778fb5ce2] 2026-05-26
- RFC 8446 §4 (TLS 1.3 Handshake Protocol) [sha256:6b2e5dfb7fdd] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 10 Plan 10-01 enrichment per NET-03*
