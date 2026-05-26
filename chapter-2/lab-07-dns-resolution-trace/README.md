---
lab-id: lab-07-dns-resolution-trace
plan-source: _MASTER-PLAN/phase-02-application-layer/03-ApplicationLayer_deliverables.md
concept-notes: ["DNS — Hierarchy and Resolution", "DNS Resource Records and TTL"]
enrichment_status: pending
---

# Lab 07 — DNS Resolution Trace

## Objective

Trace DNS resolution from a stub resolver out through the iterative hierarchy and back. Decode the DNS message structure in Wireshark and compare timing and answers across different public resolvers.

## Why this lab exists

- **Reinforces Concept Notes:** DNS — Hierarchy and Resolution; DNS Resource Records and TTL
- **K&R sections covered:** §2.4 (DNS — The Internet's Directory Service), §2.4.2 (Overview of How DNS Works), §2.4.3 (Resource Records and Messages)
- **Decision Gate 1 connection:** Direct prep — Decision Gate 1 asks you to open a Wireshark capture and explain every header field across the layers; this lab exercises DNS-message dissection in the same dissector pane you will use during the gate demo. K&R §2.4.3 introduces the resource record as the four-tuple (Name, Value, Type, TTL); the `dig` output sections in this lab map directly onto that tuple.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `dig --version`
- [ ] `host --help` (verify `bind9-host` is installed for cross-check)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `udp port 53 or tcp port 53`

**Display filter (Wireshark syntax):** `dns`

1. Run `ip route get 1.1.1.1` and note the egress interface name. The Wireshark capture in step 12 attaches to this interface.
2. Run `dig google.com 2>&1 | tee assets/01-dig-default.txt`. Note the answer section, authority section, additional section, query time, and the resolver listed in the server line.
3. Run `dig +short google.com 2>&1 | tee assets/02-dig-short.txt`. Compare the output with step 2 and note which sections of the default response have been stripped.
4. Run `dig +noall +answer google.com 2>&1 | tee assets/03-dig-answer-only.txt`. Note which sections are kept and which are dropped from the default response.
5. Run `dig A google.com 2>&1 | tee assets/04-dig-A.txt`. Note each record in the answer section.
6. Run `dig AAAA google.com 2>&1 | tee assets/05-dig-AAAA.txt`. Note each record in the answer section.
7. Run `dig MX gmail.com 2>&1 | tee assets/06-dig-MX.txt`. Note each record in the answer section.
8. Run `dig NS google.com 2>&1 | tee assets/07-dig-NS.txt`. Note each record in the answer section.
9. Run `dig TXT google.com 2>&1 | tee assets/08-dig-TXT.txt`. Note each record in the answer section.
10. Run `dig CNAME www.google.com 2>&1 | tee assets/09-dig-CNAME.txt`. Note each record in the answer section.
11. Run `dig +trace google.com 2>&1 | tee assets/10-dig-trace.txt`. Note each level of the hierarchy in the output.
12. Open Wireshark on the interface from step 1. Apply the capture filter above and start a capture.
13. Run `dig @8.8.8.8 google.com 2>&1 | tee assets/11-dig-google-dns.txt` while the capture is active.
14. Run `dig @1.1.1.1 google.com 2>&1 | tee assets/12-dig-cloudflare.txt` while the capture is active.
15. Run `dig @9.9.9.9 google.com 2>&1 | tee assets/13-dig-quad9.txt` while the capture is active. Stop the capture after this command completes.
16. Save the capture as `assets/14-dns-resolvers.pcapng`. Apply the display filter `dns` in Wireshark.
17. Inspect the first DNS query packet in the dissector pane. Note the transaction ID, the flags field, the question section, and any record-type indicator.
18. Inspect the corresponding response packet. Note the transaction ID, the flags field, the answer section, the authority section, and the additional section.
19. Compare query times across the three resolver outputs from steps 13-15. Note any differences in answer values and TTL values.
20. Run `dig google.com 2>&1 | tee assets/15-dig-first.txt`. Note the reported query time.
21. Run `dig google.com 2>&1 | tee assets/16-dig-second.txt` immediately after step 20. Compare the query time with step 20.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| UDP | Source port |  |  |
| UDP | Destination port |  |  |
| DNS | Transaction ID |  |  |
| DNS | Flags (QR, RD, RA) |  |  |
| DNS | Questions / Answers / Authority / Additional counts |  |  |

## What to capture

- [ ] Packet capture saved as `assets/14-dns-resolvers.pcapng`
- [ ] dig output for each invocation saved as `assets/NN-dig-*.txt` (16 files total, steps 2-15 + 20-21)
- [ ] Dissector-pane screenshot of one query+response pair with all layers expanded: save as `assets/17-dns-dissector.png`
- [ ] Screenshot of the `+trace` terminal output: save as `assets/18-trace-screenshot.png`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- Did you let the system stub resolver respond from its cache instead of querying the resolver? Run `sudo resolvectl flush-caches` (or `sudo systemd-resolve --flush-caches`) before the cache-observation pair in steps 20-21 if the second query returns suspiciously fast on the first run.
- Did you point `dig` at the resolver you intended? `dig google.com` queries the system-configured resolver; `dig @8.8.8.8 google.com` queries 8.8.8.8 explicitly. The two can disagree on answer values and TTL.
- Did you read `+trace` output bottom-up? `dig +trace` prints each level as it discovers it; the question-answer flow is top-down but the resolution path is built up from the root over multiple sections.
- Did you keep the capture running across all three resolvers in steps 13-15, or did you stop and restart between commands? A single capture file makes the side-by-side comparison cleaner.

## References

- K&R, §2.4 (DNS — The Internet's Directory Service), §2.4.2 (Overview of How DNS Works), §2.4.3 (Resource Records and Messages)
- Concept Notes: DNS — Hierarchy and Resolution; DNS Resource Records and TTL
- RFC 1035 — Domain Names Implementation and Specification: <https://www.rfc-editor.org/rfc/rfc1035.html>
- IANA Root Zone Database: <https://www.iana.org/domains/root/files>

<!-- citations-v1.1
- K&R 8e §2.4.2 (Overview of How DNS Works) [sha256:414e4c097594] 2026-05-25
- K&R 8e §2.4.3 (DNS Records and Messages) [sha256:5fdc3897829f] 2026-05-25
- Lecture5 01:01:00-01:15:30 (DNS Wireshark walkthrough) [sha256:711f568e9e33] 2026-05-25
- RFC 1035 §4.1.1 (DNS Message Format header section) [sha256:9722ede960ea] 2026-05-25
<!-- /citations-v1.1 -->

*Last updated: 2026-05-25 — Phase 8 Plan 08-02 enrichment per NET-01*
