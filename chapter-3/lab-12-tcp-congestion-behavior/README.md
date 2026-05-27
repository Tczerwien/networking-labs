---
lab-id: lab-12-tcp-congestion-behavior
plan-source: _MASTER-PLAN/phase-03-transport-network-layers/03-TransportNetworkLayers_deliverables.md
concept-notes: ["TCP Congestion Control — Slow Start / Congestion Avoidance / AIMD", "Bottleneck Link & Effective Throughput"]
enrichment_status: pending
---

# Lab 12 — TCP Congestion Behavior

## Objective

Drive a 30-second `iperf3` measurement, capture the underlying TCP traffic in Wireshark, and inspect the sequence-number-vs-time and throughput graphs that Wireshark generates from the capture. Note the values of the TCP Window Scale option and the advertised receive window observed in the conversation.

## Why this lab exists

- **Reinforces Concept Notes:** TCP Congestion Control — Slow Start / Congestion Avoidance / AIMD; Bottleneck Link & Effective Throughput
- **K&R sections covered:** Classic TCP Congestion Control; Reliable Data Transfer — fast retransmit on three duplicate ACKs
- **Decision Gate 1 connection:** Direct prep — Decision Gate 1 asks you to walk through every header field across the layers of a Wireshark capture; this lab adds the TCP Window Scale option and the throughput-over-time view that the gate's TCP-congestion follow-up question exercises.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `iperf3 --version` (install in step 1 if missing)
- [ ] `ip route get 1.1.1.1` returns a route (any active default route is sufficient)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1.5 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `host <iperf3-server-hostname> and tcp port 5201`

**Display filter (Wireshark syntax):** `tcp.port == 5201`

1. Run `sudo apt install -y iperf3`. Then run `iperf3 --version` to confirm the install.
2. Open <https://iperf3serverlist.net> in a browser. Note credentials for one geographically distant server (host, port if non-default, any region or limit notes). Save the page screenshot as `assets/00-iperf3-server-list.png`.
3. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark capture in step 4 attaches to this interface.
4. Open Wireshark on the interface from step 3. Apply the capture filter above (substituting the server hostname from step 2) and start a capture.
5. Run `iperf3 -c <server-from-step-2> -t 30 -i 1 2>&1 | tee assets/iperf3-stdout.txt` in a terminal. Capture the traffic for the duration of the run, then stop the capture in Wireshark.
6. Save the capture as `assets/01-iperf3.pcapng`.
7. Note the per-second and the total throughput values from the iperf3 stdout that was written to `assets/iperf3-stdout.txt`. Place the iperf3 stdout in your `lab-notes.md` inside a triple-fenced code block.
8. Open Statistics → TCP Stream Graphs → Time Sequence (Stevens) in Wireshark. Inspect the graph. Save a screenshot as `assets/02-time-seq.png`.
9. Inspect the first few RTTs of the connection in the Time Sequence graph. Note the shape of the sequence-number-vs-time curve over the opening portion of the conversation.
10. Open Statistics → TCP Stream Graphs → Throughput in Wireshark. Inspect the graph. Save a screenshot as `assets/03-throughput.png`.
11. Open Statistics → TCP Stream Graphs → Window Scaling in Wireshark. Inspect the graph. Save a screenshot as `assets/04-window-scaling.png`.
12. Apply the display filter `tcp.flags.syn == 1 and tcp.flags.ack == 0` to find the client-side SYN. Inspect the TCP Options field in the dissector pane. Note the Window Scale option value (the `shift count`) if present.
13. Apply the display filter `tcp.flags.ack == 1 and tcp.port == 5201` to find an ACK segment well into the data exchange. Inspect the TCP header in the dissector pane. Note the advertised window value in that segment.
14. Note the effective window value (= advertised window × 2 raised to the Window Scale shift count from step 12). Record the calculation in `lab-notes.md`.
15. Run `sudo tc qdisc add dev <interface> root netem loss 1%` to introduce 1% artificial loss (optional, advanced — skip if running short on time). Repeat steps 4-6 with capture saved as `assets/05-iperf3-with-loss.pcapng`. Run `sudo tc qdisc del dev <interface> root` afterward to restore normal queueing.

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
| TCP | Flags |  |  |
| TCP | Window size (advertised) |  |  |
| TCP | Options — Window Scale (shift count) |  |  |

## What to capture

- [ ] Packet capture saved as `assets/01-iperf3.pcapng`
- [ ] iperf3 stdout saved as `assets/iperf3-stdout.txt`
- [ ] iperf3 server-list screenshot saved as `assets/00-iperf3-server-list.png`
- [ ] Time Sequence (Stevens) graph screenshot saved as `assets/02-time-seq.png`
- [ ] Throughput graph screenshot saved as `assets/03-throughput.png`
- [ ] Window Scaling graph screenshot saved as `assets/04-window-scaling.png`
- [ ] (Optional) Loss-simulation capture saved as `assets/05-iperf3-with-loss.pcapng`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

> **Pragmatic note:** if iperf3 server is unavailable or too constrained, an alternative is `wget` of a large public file (e.g., a Linux ISO from a fast mirror) and capture that. Same observable behaviors at a less-controlled scale.

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Did you place the iperf3 stdout in your `lab-notes.md` inside a triple-fenced code block (```` ``` ````), not inside inline backticks? The K&R-vocab discipline gate treats fenced blocks as tool-output literal (exempt from drift); inline backticks are treated as prose.
- Did your capture filter use the actual iperf3 server hostname from step 2, not the literal string `<iperf3-server-hostname>`?
- Did the iperf3 server you picked accept connections at all? Many entries on `iperf3serverlist.net` are intermittent — if the test fails immediately, try a second server from the list before falling back to the Pragmatic note path.
- Did you compute the effective window (step 14) as `advertised × 2^shift-count`, or did you forget to apply the shift? The advertised window alone does not represent the effective receive window when the Window Scale option is in effect.
- Linux defaults to TCP CUBIC on Pop!_OS, not the textbook additive-increase, multiplicative-decrease (AIMD) Reno congestion-control variant. Note the kernel-default by running `sysctl net.ipv4.tcp_congestion_control` and recording the output in `lab-notes.md`; the shape of the Time Sequence graph you observe is specific to whichever variant is active.

## References

- K&R, Classic TCP Congestion Control; Reliable Data Transfer (fast retransmit on three duplicate ACKs)
- Concept Notes: TCP Congestion Control — Slow Start / Congestion Avoidance / AIMD; Bottleneck Link & Effective Throughput
- RFC 5681 — TCP Congestion Control: <https://www.rfc-editor.org/rfc/rfc5681.html>
- iperf3 documentation: <https://iperf.fr/iperf-doc.php>
- `man tc-netem` — Linux network emulation utility (for the optional loss-simulation step)

<!-- citations-v1.1
- K&R 8e §3.7.1 (Classic TCP Congestion Control) [sha256:e82e3c12ebfa] 2026-05-26
- K&R 8e §3.5.4 (Reliable Data Transfer — fast retransmit on three duplicate ACKs) [sha256:016e2182f08b] 2026-05-26
- Lecture12 00:34:40-00:41:18 (Congestion collapse + AIMD as solution) [sha256:fa4244dfff84] 2026-05-26
- RFC 5681 §3 (Slow Start and Congestion Avoidance) [sha256:9596b534da14] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 9 Plan 09-01 enrichment per NET-02*
