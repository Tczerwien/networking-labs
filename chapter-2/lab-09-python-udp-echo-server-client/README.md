---
lab-id: lab-09-python-udp-echo-server-client
plan-source: _MASTER-PLAN/phase-02-application-layer/03-ApplicationLayer_deliverables.md
concept-notes: ["Sockets — UDP vs TCP", "Datagram-Oriented Communication"]
enrichment_status: pending
---

# Lab 09 — Python UDP Echo Server and Client

## Objective

Build the simplest possible network application from the socket primitives up: a UDP echo server and a matching client in Python. Capture the resulting traffic on the loopback interface and inspect the datagram structure in Wireshark.

## Why this lab exists

- **Reinforces Concept Notes:** Sockets — UDP vs TCP; Datagram-Oriented Communication
- **K&R sections covered:** §2.7 (Socket Programming: Creating Network Applications), §2.7.1 (Socket Programming with UDP)
- **Decision Gate 1 connection:** Indirect prep — Decision Gate 1 demos a Wireshark capture across the layers; the UDP datagrams produced by this lab give a maximally simple application-layer-over-transport-layer dissection (no handshake, no teardown, no retransmission) that is the cleanest possible reference point for the gate demo.

This lab makes the host-process identifier concrete by binding a UDP socket to `127.0.0.1:9999` and exchanging datagrams against it. K&R §2.7.1 names the addressing model the learner exercises in this lab.

## Prerequisites

Verify each tool works before starting:

- [ ] `python3 --version`
- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `ss -h` (verify `iproute2` is installed for port-binding checks)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1.5 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

1. Open assets/udp_echo_server.py. Edit the file to implement the body per the comment scaffold.
2. Open assets/udp_echo_client.py. Edit the file to implement the body per the comment scaffold.
3. Open Wireshark on the loopback interface (`lo`). Apply the display filter `udp.port == 9999` and start a capture.
4. Run `python3 assets/udp_echo_server.py` in terminal 1. Verify the process binds without error.
5. Run `python3 assets/udp_echo_client.py` in terminal 2. Note the reply printed by the client. Inspect the server's stdout in terminal 1.
6. Capture the traffic until both client and server have finished exchanging, then end the capture. Save the capture as `assets/01-udp-single.pcapng`.
7. Inspect the captured datagrams in the dissector pane. Note the source port, destination port, payload length, and the UDP checksum field for each datagram.
8. Edit `assets/udp_echo_client.py` to send 5 messages in a loop instead of a single message. Save the file.
9. Open Wireshark again on the loopback interface. Apply the same display filter and start a fresh capture.
10. Run `python3 assets/udp_echo_server.py` in terminal 1.
11. Run `python3 assets/udp_echo_client.py` in terminal 2. Capture the traffic for the full second run, then end the capture. Save the capture as `assets/02-udp-loop.pcapng`.
12. Inspect the capture. Note the total datagram count and any datagrams that look like connection setup or teardown.

## Constraints

_Per Principle 7 — write the code yourself. Mode 2 (tutor) is fine if you get stuck on syntax. Mode 4 (collaborator) is **not** fine — this is a learning exercise, not a project._

## What to capture

- [ ] Final `udp_echo_server.py` committed at `assets/udp_echo_server.py`
- [ ] Final `udp_echo_client.py` committed at `assets/udp_echo_client.py`
- [ ] Single-message UDP capture saved as `assets/01-udp-single.pcapng`
- [ ] Five-message-loop UDP capture saved as `assets/02-udp-loop.pcapng`
- [ ] Dissector-pane screenshot of one UDP datagram with all layers expanded: save as `assets/03-udp-dissector.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you check that port 9999 is free before starting the server? `ss -unl | grep 9999` shows whether anything is already bound.
- Did you bind the server to `127.0.0.1` (loopback only) and not to `0.0.0.0` (all interfaces)? The capture filter and `lo` interface assumption depend on the bind address.
- Did the client send `bytes` and not `str`? Python's `socket.sendto()` requires bytes; pass `b"hello, world"` or `"hello, world".encode()`, not the bare string.
- Did your server forget the receive-loop guard and exit after one datagram? The server's "loop forever" comment is a hint, not optional.
- Did you forget to flush the server's stdout? On some terminals `print()` buffers output until exit; pass `flush=True` if the server output appears only after Ctrl-C.

## References

- K&R, §2.7 (Socket Programming: Creating Network Applications), §2.7.1 (Socket Programming with UDP)
- Concept Notes: Sockets — UDP vs TCP; Datagram-Oriented Communication
- RFC 8085 — UDP Usage Guidelines: <https://www.rfc-editor.org/rfc/rfc8085.html>
- Python `socket` module reference: <https://docs.python.org/3/library/socket.html>

<!-- citations-v1.1
- K&R 8e §2.7.1 (Socket Programming with UDP) [sha256:980ae432d642] 2026-05-25
- Lecture6 00:14:00-00:50:00 (Datagram socket vs stream socket) [sha256:434d8c342d5b] 2026-05-25
- RFC 8085 §3 (UDP Usage Guidelines — Overview of UDP) [sha256:64d3c95953e6] 2026-05-25
- Python docs library/socket §socket.socket [sha256:6030aee0626d] 2026-05-25
<!-- /citations-v1.1 -->

*Last updated: 2026-05-25 — Phase 8 Plan 08-02 enrichment per NET-01*
