# Lab 01 — Network Edge Mapping — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

Confirm each item before running any procedure step.

- [ ] All prerequisite tools verified per README (`hostname`, `ip`, `resolvectl`, `ethtool`, `curl`; `iw` for wireless)
- [ ] `assets/` directory present to receive the captured command outputs
- [ ] You can run `ping` against an external host from this machine (not blocked by a captive portal)
- [ ] Active interface — the one carrying your default route — identified and named below

**Active context (capture before you start):**

> Machine / OS this lab runs on:

> Network you are attached to (home / campus / hotspot / other), in one phrase:

> Wired or wireless for the active interface:

---

## Predict before you run

Commit these predictions in writing first; you will check them against the captured outputs.

> Access-network type you expect this host sits behind, and the single piece of evidence you most expect to confirm it:

> Whether you expect the round-trip time to the gateway or to a public host to be larger, and your reasoning:

---

## Capture summary

One row per step that writes an artifact. Fill the right column as you complete each step.

| Step | Source command            | Captured to                  | Captured? (y/n) |
|------|---------------------------|------------------------------|-----------------|
| 1    | `hostname`                | n/a (recorded inline)        |                 |
| 2    | `ip a`                    | `assets/02-ip-a.txt`         |                 |
| 3    | `ip route`                | `assets/03-ip-route.txt`     |                 |
| 4    | `resolvectl status`       | `assets/04-resolvers.txt`    |                 |
| 5    | `ethtool <wired-iface>`   | `assets/05-ethtool.txt`      |                 |
| 6    | `iw dev <iface> link`     | `assets/06-iw-link.txt`      |                 |
| 7    | `curl ifconfig.me`        | `assets/07-public-ip.txt`    |                 |
| 8    | n/a (reasoning step)      | n/a                          |                 |
| 9    | `ping -c 4 <gateway>`     | `assets/09-ping-gateway.txt` |                 |
| 10   | `ping -c 4 8.8.8.8`       | `assets/10-ping-public.txt`  |                 |

---

## Step-by-step record

### Step 1 — Run `hostname`

**Command:**

```bash
hostname
```

**Output:**

```text

```

**What I observe:**

> Configured hostname of this end system:

---

### Step 2 — Capture `ip a`

**Command:**

```bash
ip a | tee assets/02-ip-a.txt
```

**Capture to:** `assets/02-ip-a.txt`

**Output:**

```text

```

**What I observe:**

> Every network interface present (by name):

> For each interface — its MAC address:

> For each interface — its assigned IPv4 address(es):

> For each interface — its assigned IPv6 address(es):

---

### Step 3 — Capture `ip route`

**Command:**

```bash
ip route | tee assets/03-ip-route.txt
```

**Capture to:** `assets/03-ip-route.txt`

**Output:**

```text

```

**What I observe:**

> Default-gateway IP address:

> Egress interface name carrying the default route:

---

### Step 4 — Capture the DNS resolver state

**Command:**

```bash
resolvectl status | tee assets/04-resolvers.txt
# fallback if resolvectl is unavailable:
cat /etc/resolv.conf | tee assets/04-resolvers.txt
```

**Capture to:** `assets/04-resolvers.txt`

**Output:**

```text

```

**What I observe:**

> Configured DNS resolver(s) for this host:

> Which command (the `resolvectl` form or the `/etc/resolv.conf` fallback) produced this output:

---

### Step 5 — Inspect wired link speed with `ethtool`

Use the wired interface name you identified in Step 2.

**Command:**

```bash
ethtool <wired-iface> | tee assets/05-ethtool.txt
```

**Capture to:** `assets/05-ethtool.txt`

**Output:**

```text

```

**What I observe:**

> Wired interface name passed to `ethtool`:

> Link speed reported for that interface:

> If `ethtool` reported `Unknown!` or an error, note that here and which interface it was:

---

### Step 6 — Inspect wireless link rate with `iw`

Run `iw dev` first with no arguments to discover the wireless interface name, then query its link.

**Command:**

```bash
iw dev
iw dev <wireless-iface> link | tee assets/06-iw-link.txt
```

**Capture to:** `assets/06-iw-link.txt`

**Output:**

```text

```

**What I observe:**

> Wireless interface name discovered by `iw dev`:

> Reported link rate for that wireless interface:

> If no wireless interface exists on this host, note that here:

---

### Step 7 — Find the host's public IP

**Command:**

```bash
curl ifconfig.me | tee assets/07-public-ip.txt
# alternative if the first response looks like an HTML login page:
curl ipinfo.io/ip | tee assets/07-public-ip.txt
```

**Capture to:** `assets/07-public-ip.txt`

**Output:**

```text

```

**What I observe:**

> Public IP address returned for this host:

> Which endpoint (`ifconfig.me` or `ipinfo.io/ip`) returned it:

---

### Step 8 — Determine the access-network type

No new command for this step. Reason from the outputs captured in Steps 1–7.

**What I observe:**

> Access-network type this evidence supports (for example DSL, cable, fiber, cellular/hotspot):

> The specific captured outputs (name the step and what in it) that back this determination:

---

### Step 9 — Ping the gateway

Use the default-gateway IP you recorded in Step 3.

**Command:**

```bash
ping -c 4 <gateway-from-step-3> | tee assets/09-ping-gateway.txt
```

**Capture to:** `assets/09-ping-gateway.txt`

**Output:**

```text

```

**What I observe:**

> Gateway IP address pinged:

> Round-trip time min / avg / max to the gateway:

> Packets transmitted vs. received (loss, if any):

---

### Step 10 — Ping a host beyond the gateway

**Command:**

```bash
ping -c 4 8.8.8.8 | tee assets/10-ping-public.txt
```

**Capture to:** `assets/10-ping-public.txt`

**Output:**

```text

```

**What I observe:**

> Round-trip time min / avg / max to 8.8.8.8:

> Packets transmitted vs. received (loss, if any):

---

## Analysis questions

Answer in your own words, citing the specific captured outputs.

**Question 1:** Set the gateway RTT from Step 9 beside the 8.8.8.8 RTT from Step 10. What is the difference between them, and where in the path from this host to the public Internet does that difference arise? Point to the numbers in both captures that justify your reading.

>

**Question 2:** Relate the public IP from Step 7 to the IPv4 address on your active interface from Step 2. Are they the same value or different? What does that relationship tell you about how packets from this host reach a server on the public Internet?

>

**Question 3:** Step 5 (`ethtool`) and Step 6 (`iw`) report a link figure for a wired and a wireless interface. For the interface that carries your default route, which tool gave the meaningful figure, and what does that say about the medium this host uses at the edge?

>

**Question 4:** Among the identifiers you captured — interface name, MAC, IPv4, gateway, DNS resolver, public IP — which are local to this network segment and which have meaning across the wider Internet? Justify each placement from what you observed.

>

---

## Reflection

**What did I learn that I won't find in the textbook?**

>

**What would I tell someone starting this lab tomorrow?**

>

**Where did my mental model break? (List the moment you said "wait, that's not what I expected.")**

>

---

## Decision Gate 1 connection

Decision Gate 1 is the live test: open a Wireshark capture and explain every header field across the protocol layers. This lab establishes the identifiers those header fields refer to.

**Which identifiers captured here do you expect to reappear as header fields when you open a packet capture at Gate 1, and at which protocol layer would each one sit?**

>

**For the active interface, which identifier names the host on its local segment and which names it to a host on the far side of the gateway? How do you expect that split to map onto two different layers in the Gate 1 capture?**

>

**Could you demo this lab's key finding — the path from this host's local identity out to the public Internet — to a peer in 60 seconds, using only your captured outputs?**

>

*Last updated: 2026-06-05*
