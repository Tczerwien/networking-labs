---
lab-id: lab-13-icmp-and-traceroute-internals
plan-source: _MASTER-PLAN/phase-03-transport-network-layers/03-TransportNetworkLayers_deliverables.md
concept-notes: ["ICMP — Echo Request/Reply and Time Exceeded", "TTL & Hop-by-Hop Forwarding"]
enrichment_status: pending
---

# Lab 13 — ICMP & Traceroute Internals

## Objective

Capture ICMP traffic from three different tools (`ping`, `traceroute`, `mtr`) and decode the ICMP message bytes end-to-end. Inspect the embedded original packet inside an ICMP Time Exceeded message and note the time-to-live (TTL) value visible in the embedded IP datagram header.

## Why this lab exists

- **Reinforces Concept Notes:** ICMP — Echo Request/Reply and Time Exceeded; TTL & Hop-by-Hop Forwarding
- **K&R sections covered:** ICMP (Ch 5); IPv4 Datagram Format (Ch 4)
- **Decision Gate 1 connection:** Direct prep — Decision Gate 1 asks you to walk through every header field across the layers; this lab adds the ICMP-layer dissection (type, code, identifier, sequence number) and the IP-layer TTL field that the gate's traceroute follow-up question exercises.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `traceroute --version`
- [ ] `mtr --version`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `icmp`

**Display filter (Wireshark syntax):** `icmp`

1. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark captures in steps 2, 5, 8, and 11 attach to this interface.
2. Open Wireshark on the interface from step 1. Apply the capture filter `icmp` and start a capture.
3. Run `ping -c 4 8.8.8.8` in a terminal. Capture the traffic for the duration of the run, then stop the capture in Wireshark.
4. Save the capture as `assets/01-ping.pcapng`. Inspect the ICMP packets in the capture. Note the type and code fields of the outbound packets and of the inbound packets, and note the sequence number field across the 4 ping iterations.
5. Open Wireshark for a fresh capture on the interface from step 1 (filter `icmp`).
6. Run `traceroute google.com` in a terminal. Capture the traffic for the duration of the run, then stop the capture.
7. Save the capture as `assets/02-traceroute-udp.pcapng`.
8. Open Wireshark for another fresh capture on the same interface (filter `icmp`).
9. Run `traceroute -I google.com` in a terminal. Capture the traffic for the duration of the run, then stop the capture.
10. Save the capture as `assets/03-traceroute-icmp.pcapng`.
11. Compare the two traceroute captures from steps 7 and 10. Note any differences in the captured packets (outbound packet types, inbound packet types, packet counts).
12. Open the capture from step 10 in Wireshark. Apply the display filter `icmp.type == 11`. Inspect each filtered packet in the dissector pane. Note (a) the source IP of the responding router, (b) the original packet embedded in the ICMP error, and (c) the time-to-live (TTL) value visible in that embedded packet header.
13. Note the final ICMP packet in the traceroute capture (the packet that signals "we've reached the destination, stop probing"). Record the type, code, and source IP in `lab-notes.md`.
14. Open Wireshark for one more fresh capture on the same interface (filter `icmp`).
15. Run `mtr -c 30 8.8.8.8` in a terminal. Capture the traffic for the duration of the run, then stop the capture.
16. Save the capture as `assets/04-mtr.pcapng`. Note the per-hop loss-percentage column in the `mtr` terminal output.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| IP | time-to-live (TTL) |  |  |
| IP | Protocol (= 1 for ICMP) |  |  |
| ICMP | Type |  |  |
| ICMP | Code |  |  |
| ICMP | Checksum |  |  |
| ICMP | Identifier |  |  |
| ICMP | Sequence number |  |  |

## What to capture

- [ ] `ping` capture saved as `assets/01-ping.pcapng`
- [ ] Default-traceroute (UDP probes) capture saved as `assets/02-traceroute-udp.pcapng`
- [ ] Forced-ICMP-traceroute capture saved as `assets/03-traceroute-icmp.pcapng`
- [ ] `mtr` capture saved as `assets/04-mtr.pcapng`
- [ ] `mtr` terminal screenshot saved as `assets/04-mtr-stdout.png`
- [ ] Dissector-pane screenshot of one Time Exceeded packet with embedded IP header expanded: save as `assets/03-time-exceeded-dissector.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Did you use the capture filter `icmp` rather than a wider filter that includes UDP probes? The lab teaches via ICMP responses; the absence of outbound UDP probes from the default `traceroute` capture is part of the discovery (compare the step-7 capture against the step-10 capture).
- Did you confirm that the default `traceroute` on Pop!_OS uses UDP probes rather than ICMP probes? `man traceroute` confirms; the `-I` flag forces ICMP.
- Did some intermediate hops never respond? Some routers do not generate ICMP errors (silent hops); note them as `* * *` rows in the `traceroute` output rather than treating their absence as a tool failure.
- Did ICMP rate-limiting by an intermediate router affect your capture? Re-running step 6 or step 9 may produce different per-hop response patterns.
- Did you confuse the `mtr` aggregated loss-percentage column with per-probe semantics? `mtr` reports the loss percentage observed across the 30 probes, not per individual probe.

## References

- K&R, ICMP (Ch 5); IPv4 Datagram Format (Ch 4)
- Concept Notes: ICMP — Echo Request/Reply and Time Exceeded; TTL & Hop-by-Hop Forwarding
- RFC 792 — Internet Control Message Protocol: <https://www.rfc-editor.org/rfc/rfc792>
- IANA ICMP Type Numbers registry: <https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml>
- `man traceroute`, `man mtr` — tool documentation (Pop!_OS packages `traceroute` and `mtr`)

<!-- citations-v1.1
- K&R 8e §5.6 (ICMP: The Internet Control Message Protocol) [sha256:612acafb7bc6] 2026-05-26
- K&R 8e §4.3.1 (IPv4 Datagram Format) [sha256:e01e1ba1c743] 2026-05-26
- Lecture15 00:39:11-00:42:00 (TTL decrement at hops + IP datagram format walkthrough) [sha256:014fff28af79] 2026-05-26
- IANA ICMP Parameters (ICMP Type Numbers registry) [sha256:cd378ef7547a] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 9 Plan 09-01 enrichment per NET-02*
