# Lab 01 — Network Edge Mapping — Lab Notes

**Date started:** _____
**Date completed:** _____
**Time spent:** _____
**Status:** Draft

---

## Setup verification

- [ ] All prerequisite tools verified per README
- [ ] Connected to network (wifi or wired)
- [ ] Active interface identified (note which one below)

> Active interface:

---

## Step-by-step record

### Step 1 — Identify hostname

**Command:**

```bash
hostname
```

**Output:**

```text

```

**What I observe:**

> 

---

### Step 2 — List interfaces and MAC addresses

**Command:**

```bash
ip a
```

**Output:**

```text

```

**Screenshot:**

![ip a output](./assets/01-ip-a.png)

**What I observe:**

> 

---

### Step 3 — Read IPv4 address(es)

**Address(es) found:**

> 

**Which interface they belong to:**

> 

---

### Step 4 — Identify default gateway

**Command:**

```bash
ip route
```

**Output:**

```text

```

**Screenshot:**

![ip route output](./assets/01-ip-route.png)

**Gateway IP:**

> 

---

### Step 5 — Identify DNS server(s)

**Command:**

```bash
resolvectl status
```

**Output:**

```text

```

**DNS server(s):**

> 

---

### Step 6 — Identify link speed of active interface

**Command:**

```bash

```

**Output:**

```text

```

**Link speed:**

> 

---

### Step 7 — Identify public IP

**Command:**

```bash
curl ifconfig.me
```

**Output:**

```text

```

**Public IP:**

> 

---

### Step 8 — Classify access network type

**My classification (DSL / Cable / Fiber / Mobile hotspot):**

> 

**Evidence I used:**

> 

---

### Step 9 — Ping gateway

**Command:**

```bash
ping -c 4 <gateway-ip>
```

**Output:**

```text

```

**RTT min / avg / max:**

> 

---

### Step 10 — Ping 8.8.8.8

**Command:**

```bash
ping -c 4 8.8.8.8
```

**Output:**

```text

```

**RTT min / avg / max:**

> 

---

## Analysis questions

**Question 1:** What does this tell me about how my host fits into the broader Internet?

> 

**Question 2:** Why is my public IP different from my interface IP? What's between them?

> 

**Question 3:** What's the latency difference between gateway and 8.8.8.8? What does it imply about each hop?

> 

**Question 4:** Which piece of information identifies my host on the local link, and which identifies it on the public Internet?

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
