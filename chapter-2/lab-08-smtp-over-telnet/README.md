---
lab-id: lab-08-smtp-over-telnet
plan-source: _MASTER-PLAN/phase-02-application-layer/03-ApplicationLayer_deliverables.md
concept-notes: ["SMTP — Mail Server Architecture", "Cleartext Application Protocols"]
enrichment_status: pending
---

# Lab 08 — SMTP Over Telnet

## Objective

Drive a mail-sending exchange against an SMTP server by typing the protocol commands manually over telnet. Capture the entire conversation in Wireshark and inspect the cleartext bytes on the wire.

## Why this lab exists

- **Reinforces Concept Notes:** SMTP — Mail Server Architecture; Cleartext Application Protocols
- **K&R sections covered:** §2.3 (Electronic Mail in the Internet), §2.3.1 (SMTP)
- **Decision Gate 1 connection:** Indirect prep — Decision Gate 1 demos a Wireshark capture across the layers; SMTP is a cleartext application protocol that produces highly legible bytes in the dissector pane, which makes the application-layer dissection unambiguous compared with TLS-wrapped HTTP traffic.

## Prerequisites

Verify each tool works before starting:

- [ ] `telnet --version` (Debian/Pop!_OS package is `telnet`; the GNU inetutils variant works)
- [ ] `wireshark --version`
- [ ] `tcpdump --version`
- [ ] `groups | grep -q wireshark`
- [ ] `nc -h` (netcat-openbsd; useful as a fallback for telnet)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1 hr.

## Procedure

<!-- v1.1: every step opens with one of: Run / Open / Edit / Verify / Capture / Save / Compare / Note / Inspect / Apply / Restart / Check. -->

**Capture filter (BPF syntax):** `tcp port 25 or tcp port 587 or tcp port 2525`

**Display filter (Wireshark syntax):** `smtp or tcp.port == 25 or tcp.port == 587 or tcp.port == 2525`

This lab supports two setup paths. Pick ONE before starting and stay on that path for the entire procedure.

**Setup path A — Local Postfix install (no external account required):**

1. Run `sudo apt install -y postfix`. When prompted by debconf, pick "Local only" (or "Internet Site" if that is the only option presented).
2. Run `sudo systemctl status postfix` and verify the service is active.
3. Run `ss -tlnp | grep :25` and verify port 25 is bound on localhost.

**Setup path B — Public sandbox (Mailtrap free tier — verify free at <https://mailtrap.io/pricing> before signup):**

1. Open <https://mailtrap.io>. Sign up and create a sandbox inbox.
2. Open the inbox SMTP credentials page. Note the host, port, username, and password.
3. Verify reachability with `nc -vz <mailtrap-host> <mailtrap-port>`.

> **Note:** Mailtrap free-tier availability is verified at this README's last-updated date. If signup now requires a credit card or the free tier no longer exists, fall back to Setup path A. Setup path B is preserved here for the case where Mailtrap is accessible.

After your setup path is up, proceed with the capture procedure below.

4. Run `ip route get 127.0.0.1` (path A) or `ip route get <mailtrap-host>` (path B) and note the egress interface. The Wireshark capture in step 5 attaches to this interface (`lo` for path A; the routed interface for path B).
5. Open Wireshark on the interface from step 4. Apply the capture filter above and start a capture.
6. Run `telnet localhost 25` (path A) or `telnet <mailtrap-host> <mailtrap-port>` (path B) in a terminal. Inspect the first server reply.
7. Run `HELO mydomain.local` in the telnet connection. Inspect the server reply (status code + message).
8. Run `MAIL FROM:<test@mydomain.local>` in the telnet connection. Inspect the server reply.
9. Run `RCPT TO:<test@mydomain.local>` (path A) or `RCPT TO:<your-mailtrap-test-address>` (path B). Inspect the server reply.
10. Run `DATA` in the telnet connection. Inspect the server reply.
11. Run the message lines: `Subject: Test message from telnet`, then a blank line, then `This is a test message I sent by hand via telnet.`, then a line containing only `.` (a single period) followed by Enter. Inspect the server reply.
12. Run `QUIT` in the telnet connection. Inspect the server reply and verify the connection closes.
13. Capture the traffic until the connection has closed, then end the capture. Save it as `assets/01-smtp-exchange.pcapng`.
14. Save the full telnet transcript as `assets/02-telnet-transcript.txt` (copy from the terminal scrollback, or re-run under `script -c 'telnet ...' assets/02-telnet-transcript.txt`).
15. Apply the display filter `smtp` in Wireshark. Inspect the first SMTP packet in the dissector pane. Note the request command and the corresponding server reply (status code + message).
16. Inspect each subsequent SMTP packet in turn. Note each server reply (status code + message).
17. Inspect the DATA-phase packets. Note the boundary between the header lines and the body, and the terminator that ends the message.
18. Note the cleartext nature of the SMTP exchange visible in the capture.

### Per-layer header field interpretation

| Layer | Field name | Observed value | What it identifies |
|-------|------------|----------------|--------------------|
| Ethernet | Source MAC |  |  |
| Ethernet | Destination MAC |  |  |
| IP | Source IP |  |  |
| IP | Destination IP |  |  |
| TCP | Source port |  |  |
| TCP | Destination port |  |  |
| TCP | Flags |  |  |
| SMTP | Request command (HELO/MAIL/RCPT/DATA/QUIT) |  |  |
| SMTP | Response status code |  |  |

## What to capture

- [ ] Packet capture saved as `assets/01-smtp-exchange.pcapng`
- [ ] Full telnet transcript saved as `assets/02-telnet-transcript.txt`
- [ ] Dissector-pane screenshot showing one SMTP request/reply pair with all layers expanded: save as `assets/03-smtp-dissector.png`
- [ ] Wireshark "Follow TCP Stream" view of the entire SMTP conversation: save as `assets/04-smtp-stream.txt`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- Did you verify wireshark group membership with `groups | grep wireshark` before starting the capture?
- On path A, did you confirm Postfix is bound to `127.0.0.1` and not to all interfaces? `ss -tlnp | grep :25` shows the bind address explicitly.
- On path B, did you check `https://mailtrap.io/pricing` for free-tier changes before creating an account? If the free tier has been removed or now requires a credit card, switch to path A.
- Did you type the terminator on its own line in step 11? The DATA-phase terminator is a single `.` on a line by itself; if your terminal expanded a paste or appended whitespace, the server will keep waiting and your `QUIT` will look like message body.
- Did you end the Wireshark capture before exporting, or did you let it grow unboundedly across the entire telnet connection?
- Did you read the SMTP status codes left-to-right? Each three-digit code's first digit indicates the broad outcome (1xx info, 2xx success, 3xx intermediate, 4xx transient, 5xx permanent); the remaining digits add detail.

## References

- K&R, §2.3 (Electronic Mail in the Internet), §2.3.1 (SMTP)
- Concept Notes: SMTP — Mail Server Architecture; Cleartext Application Protocols
- RFC 5321 — Simple Mail Transfer Protocol: <https://www.rfc-editor.org/rfc/rfc5321.html>
- IANA Service Name and Transport Protocol Port Number Registry: <https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml>

<!-- citations-v1.1
K&R 8e §2.3.1 (SMTP) [sha256:b72be7ccd691] 2026-05-25
K&R 8e §2.3 (Electronic Mail in the Internet) [sha256:52d66e58fb65] 2026-05-25
RFC 5321 §3.3 (Mail Transactions) [sha256:0958fc2045f2] 2026-05-25
IANA Service Names and Port Numbers (SMTP entries) [sha256:3d199db6dbf6] 2026-05-25
<!-- /citations-v1.1 -->

*Last updated: 2026-05-25 — Phase 8 Plan 08-02 enrichment per NET-01*
