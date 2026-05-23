# Lab 01 — Network Edge Mapping

## Objective

Map your local host's network identity. Concretely answer: what am I, where am I, who do I talk to first?

## Why this lab exists

- **Reinforces Concept Notes:** 1, 2, 3
- **K&R sections covered:** 1.2 (Network edge)
- **Decision Gate 1 connection:** Indirect prep. Builds the foundation for naming end systems and identifying the access network, which Gate 1 layering questions assume.

## Prerequisites

Verify each tool works before starting:

- [ ] `hostname`
- [ ] `ip a`
- [ ] `ip route`
- [ ] `resolvectl status` (or `cat /etc/resolv.conf`)
- [ ] `ethtool --version` (wired) or `iw --version` (wireless)
- [ ] `curl --version`
- [ ] `ping -c 1 127.0.0.1`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1.5 hrs.

## Procedure

1. **Identify hostname.** Command: `hostname`.
2. **List interfaces and MAC addresses.** Command: `ip a`.
3. **Read your IPv4 address(es)** from the `ip a` output for each active interface.
4. **Identify default gateway.** Command: `ip route`.
5. **Identify DNS server(s).** Command: `resolvectl status` (or `cat /etc/resolv.conf`).
6. **Identify link speed of the active interface.** For wired: `ethtool <iface>`. For wireless: `iw dev <iface> link`.
7. **Identify your public IP.** Command: `curl ifconfig.me` (or `curl ipinfo.io/ip`).
8. **Classify your access network type** (DSL / Cable / Fiber / Mobile hotspot). Cite the evidence you used.
9. **Ping your gateway.** Command: `ping -c 4 <gateway-ip>`. Record round-trip times.
10. **Ping a public anycast resolver.** Command: `ping -c 4 8.8.8.8`. Record round-trip times.

## What to capture

- [ ] Screenshot: `ip a` output → save as `assets/01-ip-a.png`
- [ ] Screenshot: `ip route` output → save as `assets/01-ip-route.png`
- [ ] Text output: public IP curl result → paste into lab-notes
- [ ] Text output: ping results (min/avg/max RTT to gateway and to 8.8.8.8) → paste into lab-notes

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- `ip a` shows nothing useful → you're not connected to a network. Connect to wifi or plug in, then re-run.
- `ethtool` permission denied → try `sudo ethtool <iface>`.

## References

- K&R, Section 1.2 (Network edge)
- Concept Notes 1, 2, 3
