---
lab-id: lab-03-wireshark-encapsulation
plan-source: _MASTER-PLAN/phase-01-networking-foundations/03-NetworkingFoundation_deliverables.md
concept-notes: ["Layered Protocol Stack & Encapsulation", "What Is a Protocol"]
enrichment_status: pending
---

# Lab 03 — Wireshark Encapsulation

## Objective

Capture a real HTTP request on the wire and decode every layer of the resulting packet, layer by layer, in the Wireshark dissector.

## Why this lab exists

- **Reinforces Concept Notes:** 8 (encapsulation), 2 (protocol)
- **K&R sections covered:** §1.5, §1.5.1, §1.5.2, §1.1.3
- **Decision Gate 1 connection:** This lab is the preliminary version of Decision Gate 1. The full version of Decision Gate 1 happens after Phase 03 (the wireshark labs in chapter-3/4 — lab-11, lab-12, lab-13 — constitute the complete demo subject). If you can open a Wireshark capture and explain every header field across the Ethernet / IP / TCP / HTTP layers from scratch after completing this lab, the preliminary gate passes.

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

**Capture filter (BPF syntax):** `host <neverssl-ip>`

**Display filter (Wireshark syntax):** `http and ip.addr == <neverssl-ip>`

1. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark capture in steps 2-4 attaches to this interface.
2. Open Wireshark on the interface from step 1 and start a capture with no filter applied.
3. Run `curl http://neverssl.com 2>&1 | tee assets/03-neverssl-curl.txt` in a terminal to generate the HTTP request traffic.
4. Capture the traffic for the duration of the request, then stop the capture in Wireshark.
5. Save the capture as `assets/01-encapsulation.pcapng`.
6. Apply the display filter `http and ip.addr == <neverssl-ip>` in Wireshark and inspect the first HTTP GET packet in the dissector pane.
7. Inspect each layer in the dissector pane in turn — Ethernet, IP, TCP, HTTP. Note the header fields observed in each layer in the `### Per-layer header field interpretation` table below.
8. Note in `lab-notes.md` a one-sentence explanation of each header field in your own words.
9. Note any ARP traffic visible in the capture in `lab-notes.md`, separately from the HTTP analysis.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| IP | Time-to-live (TTL) |  |  |
| IP | Protocol |  |  |
| TCP | Source port |  |  |
| TCP | Destination port |  |  |
| TCP | Flags |  |  |
| HTTP | Method |  |  |
| HTTP | Host header |  |  |

## What to capture

- [ ] Packet capture saved as `assets/01-encapsulation.pcapng`
- [ ] `curl` terminal output saved as `assets/03-neverssl-curl.txt`
- [ ] Dissector-pane screenshot with all four layers expanded: save as `assets/02-dissector-all-layers.png`
- [ ] Per-layer header-field table in `lab-notes.md` filled in for the chosen HTTP GET packet

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture? A missing group membership shows up as a capture that starts but stays empty.
- Did you start the capture on the egress interface from step 1? A wrong NIC selection shows up as no HTTP traffic visible in the capture.
- The `http` display filter does not show ARP packets — apply the filter `arp` separately if you want to inspect the link-layer ARP exchanges.
- Wireshark dissector field names follow RFC terminology rather than casual names; the field-name column may not match what `curl -v` prints.
- Captures may include unrelated background traffic from other applications; the display filter `http and ip.addr == <neverssl-ip>` narrows to the lab conversation.
- The `neverssl.com` host is chosen because it serves plain HTTP without redirecting to TLS; lab-05 covers TLS-encrypted traffic separately.

## References

- K&R, Section 1.5.2 (Encapsulation)
- K&R, Section 1.5.1 (Layered Architecture — Internet 5-layer protocol stack)
- K&R, Section 1.1.3 (What Is a Protocol)
- Concept Notes 8, 2
- Lecture 3 (Data Communications) — protocol layering and TCP/IP 5-layer model walkthrough

<!-- citations-v1.1
- K&R 8e §1.5.2 (Encapsulation) [sha256:4c625c9fcf74] 2026-05-26
- K&R 8e §1.5.1 (Layered Architecture — Internet 5-layer protocol stack) [sha256:dbca562c8b0a] 2026-05-26
- Lecture3 00:04:36-00:14:56 (Protocol layering: rationale + TCP/IP 5-layer model walkthrough) [sha256:50abde19020f] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 10 Plan 10-01 enrichment per NET-03*
