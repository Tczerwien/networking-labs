---
lab-id: lab-11-tcp-connection-lifecycle
plan-source: _MASTER-PLAN/phase-03-transport-network-layers/03-TransportNetworkLayers_deliverables.md
concept-notes: ["TCP — Segment, Seq/ACK, Connection Management", "TCP — Flow Control, Reliable Transfer, & Production Tunables"]
enrichment_status: pending
---

# Lab 11 — TCP Connection Lifecycle

## Objective

Capture one complete TCP conversation at the byte level and decode its full lifecycle. Inspect the segments that open the conversation, the segments that carry application data, and the segments that close the conversation; annotate the 11 main fields of one mid-conversation TCP segment from the dissector pane.

## Why this lab exists

- **Reinforces Concept Notes:** TCP — Segment, Seq/ACK, Connection Management; TCP — Flow Control, Reliable Transfer, & Production Tunables
- **K&R sections covered:** §3.5.2 (TCP Segment Structure), §3.5.6 (TCP Connection Management)
- **Decision Gate 1 connection:** Direct prep — Decision Gate 1 asks you to open a Wireshark capture and explain every header field across the layers; this lab exercises the transport-layer-segment dissection (11 TCP header fields) that the gate demos.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `curl --version`
- [ ] `ss --version`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1.25 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `host example.com`

**Display filter (Wireshark syntax):** `tcp and ip.addr == <target-ip>`

1. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark capture in step 2 attaches to this interface.
2. Open Wireshark on the interface from step 1. Apply the capture filter above and start a capture.
3. Run `curl -v https://example.com 2>&1 | tee assets/curl-output.txt`. Capture the traffic for the duration of the request, then stop the capture in Wireshark.
4. Save the capture as `assets/01-tcp-lifecycle.pcapng`. Note the destination IP from the `curl -v` output, then apply the display filter `tcp and ip.addr == <that-ip>` in Wireshark.
5. Inspect the first three TCP segments in the capture. Note the flags set on each segment and the sequence and acknowledgment number values for each.
6. Inspect one TCP segment from the middle of the data exchange (after the connection-opening segments and before the connection-closing segments). Note all 11 main header fields visible in the dissector pane and fill in the `### Per-layer header field interpretation` table below in your `lab-notes.md`.
7. Inspect the final TCP segments of the conversation. Note the flags set on the closing segments and the count of closing segments observed.
8. Compare the closing-segment count from step 7 with the count described in K&R §3.5.6 for the canonical TCP teardown. Note any variation.
9. Run `ss -t`. Note the connection state column.
10. Run `ss -t state established`. Note which entries appear.
11. Run `ss -t state time-wait` immediately after the `curl` returns. Save the output as `assets/ss-time-wait-immediate.txt`. Run the same command again 30 seconds later and save as `assets/ss-time-wait-after-30s.txt`. Compare the two outputs.
12. Run `ss -t state close-wait`. Note which entries appear.
13. Run `ss -tnp state established`. Note the additional column compared to step 10.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| TCP | Source port |  |  |
| TCP | Destination port |  |  |
| TCP | Sequence number |  |  |
| TCP | Acknowledgment number |  |  |
| TCP | Flags (SYN/ACK/FIN/RST/PSH/URG/CWR/ECE) |  |  |
| TCP | Window size |  |  |
| TCP | Checksum |  |  |
| TCP | Options (MSS / WScale / SACK) |  |  |

## What to capture

- [ ] Packet capture saved as `assets/01-tcp-lifecycle.pcapng`
- [ ] curl verbose output saved as `assets/curl-output.txt`
- [ ] `ss -t` output saved as `assets/ss-output.txt`
- [ ] `ss -t state time-wait` output (immediate) saved as `assets/ss-time-wait-immediate.txt`
- [ ] `ss -t state time-wait` output (after 30 seconds) saved as `assets/ss-time-wait-after-30s.txt`
- [ ] Dissector-pane screenshot of the mid-conversation segment with all layers expanded: save as `assets/01-tcp-dissector.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Did your capture filter actually match the traffic you intended to see? `example.com` resolves to a different IP across DNS queries; filter by hostname (BPF `host example.com`) when in doubt, then refine the display filter using the IP that `curl -v` actually resolved.
- Did you start the Wireshark capture BEFORE running `curl`? If the capture starts late, the connection-opening segments will not appear in the trace.
- Did you pick a single mid-conversation segment from the dissector pane before annotating the 11 fields, instead of trying to interpret the whole stream at once?
- The ECE / CWR flag bits in the TCP `Flags` field are rare and may not appear in a vanilla example.com capture — note their absence (or presence) explicitly rather than skipping them.
- `ss -t state close-wait` often shows nothing on a healthy machine — note variations across re-runs in your `lab-notes.md` rather than treating zero output as a failed step.

## References

- K&R, §3.5.2 (TCP Segment Structure), §3.5.6 (TCP Connection Management)
- Concept Notes: TCP — Segment, Seq/ACK, Connection Management; TCP — Flow Control, Reliable Transfer, & Production Tunables
- RFC 9293 — Transmission Control Protocol: <https://www.rfc-editor.org/rfc/rfc9293.html>
- `man ss` — socket statistics utility (Pop!_OS package `iproute2`)

<!-- citations-v1.1
- K&R 8e §3.5.2 (TCP Segment Structure) [sha256:6b83c5b3362c] 2026-05-26
- K&R 8e §3.5.6 (TCP Connection Management) [sha256:2e3242aeec3d] 2026-05-26
- Lecture11 01:02:57-01:12:48 (Three-way handshake walkthrough) [sha256:41436a071f84] 2026-05-26
- RFC 9293 §3.5 (Establishing a Connection: SYN/SYN-ACK/ACK) [sha256:d333e195a9bf] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 9 Plan 09-01 enrichment per NET-02*
