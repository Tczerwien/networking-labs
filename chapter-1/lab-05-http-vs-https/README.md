# Lab 05 — HTTP vs HTTPS

## Objective

Demonstrate the security difference between encrypted and unencrypted application traffic in Wireshark, on real packets.

## Why this lab exists

- **Reinforces Concept Notes:** 9 (security primitives), 8 (layering — TLS sits between TCP and HTTP)
- **K&R sections covered:** 1.6 (Networks under attack)
- **Decision Gate 1 connection:** Indirect prep. Sharpens the layering model from Lab 03 by inserting TLS between TCP and HTTP and observing what each layer exposes.

## Prerequisites

Verify each tool works before starting:

- [ ] `wireshark --version`
- [ ] `groups | grep wireshark`
- [ ] `curl --version`
- [ ] `curl -sI http://neverssl.com` (confirms plain HTTP reachable)
- [ ] `curl -sI https://wikipedia.org` (confirms HTTPS reachable)

If any fail, fix per Phase 00 install notes before continuing.

## Estimated time

1.5 hrs.

## Procedure

1. **Start a Wireshark capture** on your active interface.
2. **HTTP request.** Command: `curl -v http://neverssl.com`. Capture the full conversation.
3. **HTTPS request.** Command: `curl -v https://wikipedia.org`. Capture the full conversation.
4. **Stop capture.** Save as `assets/05-http-vs-https.pcapng`.
5. **HTTP analysis** — apply filter `http`. Identify:
    - Request method
    - URL
    - Host header
    - Response status
    - Response body
   Confirm: everything is readable.
6. **HTTPS analysis** — apply filter `tls`. Identify:
    - TLS handshake packets (ClientHello, ServerHello, Certificate, etc.)
    - The point at which the conversation switches from handshake to encrypted Application Data
    - Confirm: HTTP method, URL, and body are NOT visible in any TLS Application Data packet.

## What to capture

- [ ] Screenshot: HTTP packet fully readable → `assets/05-http-readable.png`
- [ ] Screenshot: HTTPS encrypted Application Data unreadable → `assets/05-https-encrypted.png`
- [ ] `.pcapng` file → `assets/05-http-vs-https.pcapng`

## Deliverable checklist

The lab is done when:

- [ ] All procedure steps executed
- [ ] All "What to capture" items present in `assets/`
- [ ] All analysis questions in lab-notes answered in my own words
- [ ] Reflection section completed
- [ ] Status field in lab-notes set to "Complete"

## Common pitfalls

- neverssl.com redirected to HTTPS (HSTS) → see Lab 03 pitfall.
- TLS handshake packets don't appear → wrong filter; try `tls or tcp.port == 443`.

## References

- K&R, Section 1.6 (Networks under attack)
- Concept Notes 8, 9
- [neverssl.com](http://neverssl.com)
- [wikipedia.org](https://wikipedia.org)
