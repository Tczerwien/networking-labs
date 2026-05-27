---
lab-id: lab-01-network-edge-mapping
plan-source: _MASTER-PLAN/phase-01-networking-foundations/03-NetworkingFoundation_deliverables.md
concept-notes: ["What Is the Internet", "What Is a Protocol", "Network Edge, Access Networks, Physical Media"]
enrichment_status: pending
---

# Lab 01 — Network Edge Mapping

## Objective

Map your end system's local network identity and the reachability from it through the default gateway to the public Internet.

## Why this lab exists

- **Reinforces Concept Notes:** 1, 2, 3
- **K&R sections covered:** §1.1, §1.1.1, §1.1.3, §1.2, §1.2.1
- **Decision Gate 1 connection:** Indirect prep — Decision Gate 1 walks every header field across the protocol layers in Wireshark; this lab establishes the physical and logical identifiers (interface, MAC, IPv4, gateway, DNS, public IP) that those header fields refer to.

## Prerequisites

Verify each tool works before starting:

- [ ] `hostname --version`
- [ ] `ip -V`
- [ ] `resolvectl --version` (or confirm `/etc/resolv.conf` is readable)
- [ ] `ethtool --version`
- [ ] `curl --version`

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

1. Run `hostname` and note the configured hostname of the end system in `lab-notes.md`.
2. Run `ip a` and capture the output to `assets/02-ip-a.txt`. Note every network interface present, including each interface's MAC address and any assigned IPv4 and IPv6 addresses in `lab-notes.md`.
3. Run `ip route` and capture the output to `assets/03-ip-route.txt`. Note the default-gateway IP address and the egress interface name in `lab-notes.md`.
4. Run `resolvectl status` (or `cat /etc/resolv.conf` if `resolvectl` is unavailable) and capture the output to `assets/04-resolvers.txt`. Note the configured DNS resolvers in `lab-notes.md`.
5. Run `ethtool <wired-iface>` for any wired interface listed in step 2 and capture the output to `assets/05-ethtool.txt`. Note the reported link speed in `lab-notes.md`.
6. Run `iw dev` to discover any wireless interface name. For each wireless interface, run `iw dev <wireless-iface> link` and capture the output to `assets/06-iw-link.txt`. Note the reported link rate in `lab-notes.md`.
7. Run `curl ifconfig.me` (or `curl ipinfo.io/ip` as an alternative) and capture the output to `assets/07-public-ip.txt`. Note the host's public IP address in `lab-notes.md`.
8. Note in `lab-notes.md` which access-network type the evidence from steps 1-7 supports, and cite the specific outputs that back the determination.
9. Run `ping -c 4 <gateway-from-step-3>` and capture the output to `assets/09-ping-gateway.txt`. Note the min/avg/max round-trip times in `lab-notes.md`.
10. Run `ping -c 4 8.8.8.8` and capture the output to `assets/10-ping-public.txt`. Note the min/avg/max round-trip times in `lab-notes.md`.

## What to capture

- [ ] Hostname recorded in `lab-notes.md`
- [ ] `ip a` output saved as `assets/02-ip-a.txt`
- [ ] `ip route` output saved as `assets/03-ip-route.txt`
- [ ] DNS-resolver output saved as `assets/04-resolvers.txt`
- [ ] `ethtool` output saved as `assets/05-ethtool.txt`
- [ ] `iw dev` link output saved as `assets/06-iw-link.txt`
- [ ] Public-IP output saved as `assets/07-public-ip.txt`
- [ ] Gateway ping output saved as `assets/09-ping-gateway.txt`
- [ ] Public-host ping output saved as `assets/10-ping-public.txt`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify each prerequisite tool runs cleanly before starting?
- `ethtool` may report `Unknown! (255)` for the wireless interface — use `iw dev <iface> link` for wireless link rates.
- `iw dev <iface> link` requires the wireless interface name; run `iw dev` (with no arguments) first to discover it.
- `curl ifconfig.me` may be blocked or rewritten on captive-portal networks; switch to `curl ipinfo.io/ip` if the response looks like an HTML login page.
- `resolvectl` may not be present on older Debian-based systems; fall back to `cat /etc/resolv.conf` and continue.

## References

- K&R, Section 1.2.1 (Access Networks)
- K&R, Section 1.1.1 (A Nuts-and-Bolts Description of the Internet)
- Concept Notes 1, 2, 3
- Lecture 2 (Data Communications) — access-networks walkthrough

<!-- citations-v1.1
- K&R 8e §1.2.1 (Access Networks) [sha256:ef9fa4365abf] 2026-05-26
- K&R 8e §1.1.1 (A Nuts-and-Bolts Description of the Internet) [sha256:de742306a47d] 2026-05-26
- Lecture2 00:04:00-00:10:00 (Access networks walkthrough — DSL, cable, fiber, wireless) [sha256:fa8e46679d47] 2026-05-26
<!-- /citations-v1.1 -->

*Last updated: 2026-05-26 — Phase 10 Plan 10-01 enrichment per NET-03*
