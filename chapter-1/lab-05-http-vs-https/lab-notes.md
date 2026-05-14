# Lab 05 — HTTP vs HTTPS — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README
- [ ] Connected to network (wifi or wired)
- [ ] Confirmed wireshark group membership

---

## Step-by-step record

### Step 1 — Start Wireshark capture

**Interface chosen:**

> 

**Capture start time:**

> 

---

### Step 2 — HTTP request

**Command:**

```bash
curl -v http://neverssl.com
```

**Curl output:**

```text

```

---

### Step 3 — HTTPS request

**Command:**

```bash
curl -v https://wikipedia.org
```

**Curl output:**

```text

```

---

### Step 4 — Stop and save capture

- [ ] Saved to `assets/05-http-vs-https.pcapng`

---

### Step 5 — HTTP analysis (filter `http`)

**Filter applied:**

```text
http
```

**Screenshot:**

![HTTP packet — fully readable](./assets/05-http-readable.png)

| Item | Value observed in Wireshark |
|------|------------------------------|
| Request method |  |
| URL |  |
| Host header |  |
| Response status |  |
| Response body (first ~80 chars) |  |

**Confirmation that everything was readable:**

> 

---

### Step 6 — HTTPS analysis (filter `tls`)

**Filter applied:**

```text
tls
```

**Screenshot:**

![HTTPS — encrypted Application Data unreadable](./assets/05-https-encrypted.png)

#### TLS handshake packets observed

| Frame # | Handshake message type (ClientHello / ServerHello / Certificate / etc.) | Notes |
|---------|--------------------------------------------------------------------------|-------|
|         |                                                                          |       |
|         |                                                                          |       |
|         |                                                                          |       |
|         |                                                                          |       |

**Frame at which conversation switches to encrypted Application Data:**

> 

**Confirmation that HTTP method / URL / body are NOT visible in any Application Data packet:**

> 

---

## Analysis questions

**Question 1a — sniffer on coffee-shop wifi, HTTP:** What can they see / steal / modify?

> 

**Question 1b — sniffer on coffee-shop wifi, HTTPS:** What can they still see (destination IP, SNI, traffic timing, packet sizes)? What is hidden?

> 

**Question 2:** Why does TLS happen below HTTP but above TCP? What would break if we put it elsewhere?

> 

**Question 3:** What is SNI and why is it controversial?

> 

**Question 4:** Looking at the same conversation, which fields are visible in both HTTP and HTTPS captures, and which only in HTTP?

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

**Which Decision Gate 1 question does this lab prepare me for?**

> 

**Could I demo this lab's key finding in 60 seconds to a peer?**

> 
