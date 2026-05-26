---
lab-id: lab-10-python-tcp-echo-server-client
plan-source: _MASTER-PLAN/phase-02-application-layer/03-ApplicationLayer_deliverables.md
concept-notes: ["Sockets — Stream vs Datagram", "TCP Connection Lifecycle"]
enrichment_status: pending
---

# Lab 10 — Python TCP Echo Server and Client

## Objective

Build a Python TCP echo server and client from the socket primitives up. Capture the resulting traffic on the loopback interface and compare the on-wire behavior side-by-side with the UDP capture from Lab 09.

## Why this lab exists

- **Reinforces Concept Notes:** Sockets — Stream vs Datagram; TCP Connection Lifecycle
- **K&R sections covered:** §2.7 (Socket Programming: Creating Network Applications), §2.7.2 (Socket Programming with TCP)
- **Decision Gate 1 connection:** Direct prep — Decision Gate 1 asks you to open a Wireshark capture and explain every header field across the layers; this lab produces a TCP-over-loopback capture whose handshake, data-bearing, and teardown packets are the canonical reference set for the gate demo's transport-layer explanation.

K&R §2.7.2 introduces the welcoming socket on the server side: a single socket that calls `listen()` and `accept()`, and that returns a separate connection socket per accepted client. The welcoming socket persists across many clients; each connection socket handles exactly one client conversation and is closed when that conversation ends. This lab makes the welcoming-socket vs connection-socket distinction concrete in code and visible on the wire.

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

1. Open assets/tcp_echo_server.py. Edit the file to implement the body per the comment scaffold.
2. Open assets/tcp_echo_client.py. Edit the file to implement the body per the comment scaffold.
3. Open Wireshark on the loopback interface (`lo`). Apply the display filter `tcp.port == 9998` and start a capture.
4. Run `python3 assets/tcp_echo_server.py` in terminal 1. Verify the process binds without error. Run `ss -tlnp | grep 9998` and verify port 9998 is in `LISTEN` state.
5. Run `python3 assets/tcp_echo_client.py` in terminal 2. Note the reply printed by the client. Inspect the server's stdout in terminal 1.
6. Capture the traffic until both client and server have finished exchanging, then end the capture. Save the capture as `assets/01-tcp-exchange.pcapng`.
7. Inspect the capture. Note the packets that appear at the start of the connection (before any application data is exchanged), the packets that carry the application data, and the packets that close the connection. Use the TCP flag column in the Wireshark packet list to identify each packet type.
8. Inspect the dissector pane for the first packet of the connection. Note the source port, destination port, sequence number, acknowledgment number, and the flags field.
9. Compare side-by-side with Lab 09's `assets/01-udp-single.pcapng`. Note differences in total packet count and the types of packets present in each capture.

## Constraints

_Per Principle 7 — write the code yourself. Mode 2 (tutor) is fine if you get stuck on syntax. Mode 4 (collaborator) is **not** fine — this is a learning exercise, not a project._

## What to capture

- [ ] Final `tcp_echo_server.py` committed at `assets/tcp_echo_server.py`
- [ ] Final `tcp_echo_client.py` committed at `assets/tcp_echo_client.py`
- [ ] TCP exchange capture saved as `assets/01-tcp-exchange.pcapng`
- [ ] Dissector-pane screenshot of one transport-layer segment with all layers expanded: save as `assets/02-tcp-dissector.png`
- [ ] Side-by-side screenshot of the Lab 09 UDP capture vs the Lab 10 TCP capture (Wireshark packet list, both visible): save as `assets/03-udp-vs-tcp-compare.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you check that port 9998 is free before starting the server? `ss -tlnp | grep 9998` shows whether anything is already bound.
- Did you `listen()` before `accept()` in the server? K&R §2.7.2 names the listening socket the welcoming socket; if `accept()` blocks indefinitely on connection attempts, check the sequence.
- Did you keep the welcoming socket open after `accept()` returned the connection socket? Closing the welcoming socket would prevent the server from accepting any future clients; the welcoming socket is the persistent server-side identity and the connection socket is per-client.
- Did the client send `bytes` and not `str`? Python's `socket.send()` requires bytes; pass `b"hello, world"` or `"hello, world".encode()`, not the bare string.
- Did your server forget to close the connection socket after the per-client loop ended? On loopback this leaks a small amount of state per connection; the leak grows quickly under repeated tests.
- Did you set `SO_REUSEADDR` on the welcoming socket? Without it, a TIME_WAIT-bound port refuses a quick re-bind after the previous run exits; restarting the server within ~60s of a kill then raises a bind-time error.

## References

- K&R, §2.7 (Socket Programming: Creating Network Applications), §2.7.2 (Socket Programming with TCP)
- Concept Notes: Sockets — Stream vs Datagram; TCP Connection Lifecycle
- RFC 9293 — Transmission Control Protocol: <https://www.rfc-editor.org/rfc/rfc9293.html>
- Python `socket` module reference: <https://docs.python.org/3/library/socket.html>

<!-- citations-v1.1
- K&R 8e §2.7.2 (Socket Programming with TCP) [sha256:a456a133151d] 2026-05-25
- Lecture7 00:30:00-00:50:00 (TCP socket programming: listen / accept / connect) [sha256:b3534375580a] 2026-05-25
- RFC 9293 §3.5 (Establishing a Connection) [sha256:d333e195a9bf] 2026-05-25
- Python docs library/socket §socket.listen [sha256:f8bea2435194] 2026-05-25
<!-- /citations-v1.1 -->

*Last updated: 2026-05-25 — Phase 8 Plan 08-02 enrichment per NET-01*
