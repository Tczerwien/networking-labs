# Lab 03 — Wireshark Encapsulation

## Objective

Make encapsulation visible. Capture a real packet and decode every layer's header by hand.

## Why this lab exists

- **Reinforces Concept Notes:** 8 (encapsulation), 2 (protocol)
- **K&R sections covered:** 1.5 (Protocol layers)
- **Decision Gate 1 connection:** This lab is the preliminary version of Gate 1. If you can do this from scratch, the preliminary gate passes.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `groups | grep wireshark` (confirms you're in the wireshark group)
- [ ] `curl --version`
- [ ] `ping -c 1 neverssl.com`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

2 hrs.

## Procedure

1. **Open Wireshark.** Pick the active interface (wifi or wired NIC).
2. **Start a capture with no filter.**
3. **Generate plain-HTTP traffic.** In a terminal: `curl http://neverssl.com`. neverssl.com is designed to stay on plain HTTP. Stop the capture after the response completes.
4. **Filter to the conversation.** In Wireshark, apply: `http and ip.addr == <neverssl-ip>`.
5. **Pick one HTTP GET packet.** Expand each layer in the dissector pane:
    - **Ethernet:** source MAC, destination MAC, EtherType
    - **IP (v4):** source IP, destination IP, TTL, protocol number, total length
    - **TCP:** source port, destination port, sequence number, ack number, flags (SYN, ACK, PSH, FIN), window size
    - **HTTP:** request line (method, path, version), headers (Host, User-Agent, Accept)
6. **For each header field, write 1 sentence in your own words on what it does** (in lab-notes).
7. **Save the capture.** Save to `assets/03-encapsulation.pcapng`.

## What to capture

- [ ] Screenshot: Wireshark dissector with all 4 layers expanded → `assets/03-wireshark-all-layers.png`
- [ ] `.pcapng` capture → `assets/03-encapsulation.pcapng`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Wireshark won't capture → not in `wireshark` group. `groups | grep wireshark`. If missing: `sudo usermod -aG wireshark $USER`, then log out and log back in.
- neverssl.com redirected to HTTPS → some clients have HSTS preloads forcing HTTPS. Try a different plain-HTTP target or use curl with `--no-alpn`.

## References

- K&R, Section 1.5 (Protocol layers)
- Concept Notes 2, 8
- [neverssl.com](http://neverssl.com)
