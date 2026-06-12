# ☁️ AWS Core Services Guide

> A beginner-friendly summary of **Route 53**, **EC2 Pricing**, and **S3 Storage Classes** — explained simply and clearly.

---

## 🗂️ Table of Contents

- [🌐 Route 53 — Routing Policies](#-route-53--routing-policies)
- [💻 EC2 — Pricing Models](#-ec2--pricing-models)
- [🗄️ S3 — Storage Classes](#-s3--storage-classes)
- [📋 Full Summary](#-full-summary)

---

## 🌐 Route 53 — Routing Policies

> **What is it?** Think of Route 53 like a **GPS for the internet**. When someone types your website URL, Route 53 decides *which server* to send them to — and it can make smart decisions based on speed, location, health, and more.

> 🧠 **Memory Trick:** Route 53 = Internet Traffic Cop 🚦 — it stands at the intersection and points visitors to the right server based on rules you set.

| # | Policy | Simple Explanation | Use When... |
|---|--------|--------------------|-------------|
| 01 | ➡️ **Simple** | One domain → One server | Just starting out |
| 02 | ⚖️ **Weighted** | Split traffic by % (e.g. 90% / 10%) | A/B testing new features |
| 03 | ⚡ **Latency** | Sends user to fastest server automatically | You have global users |
| 04 | 🔁 **Failover** | Primary down? Switch to backup automatically | You need high availability |
| 05 | 🗺️ **Geolocation** | Route by user's country | Different content per region |
| 06 | 📍 **Geoproximity** | Route by resource location + bias control | Fine-tuned regional control |
| 07 | 🖥️ **IP-Based** | Route based on user's IP address | ISP-specific routing |
| 08 | 🎲 **Multi-Value** | Returns up to 8 healthy servers at random | Simple load distribution |

> 💡 **Quick Decision Guide:**
> - Need backup? → **Failover**
> - Testing new features? → **Weighted**
> - Global users? → **Latency**
> - Different content per country? → **Geolocation**
> - Just starting out? → **Simple**

---

## 💻 EC2 — Pricing Models

> **What is it?** EC2 is AWS's virtual servers (computers in the cloud). AWS gives you **5 different ways to pay** — each suited to different situations. Choosing the right one can save you **up to 90%** on your bill.

> 🧠 **Memory Trick — Think of renting a car:**
> - 🚗 **On-Demand** = daily rental
> - 📅 **Reserved** = yearly lease
> - 🎲 **Spot** = standby seat (cheap but can be cancelled)
> - 💳 **Savings Plan** = loyalty card
> - 🏠 **Dedicated** = private chauffeur

| Model | Simple Explanation | Max Savings | Commitment | Interruptible? |
|-------|--------------------|:-----------:|:----------:|:--------------:|
| 🔓 **On-Demand** | Pay per second, no contract | — | None | No |
| 📅 **Reserved Instances** | 1–3 year commitment for big discount | Up to 72% | 1–3 years | No |
| ⚡ **Spot Instances** | Buy unused AWS capacity at huge discount | Up to 90% | None | ⚠️ Yes |
| 💳 **Savings Plans** | Flexible $/hour commitment across services | Up to 72% | 1–3 years | No |
| 🏠 **Dedicated Hosts** | Your own physical server | Varies | Optional | No |

> 💡 **Best Strategy:**
> Start with **On-Demand** for 2–3 months to understand your usage.
> Then switch to **Savings Plans or Reserved** for steady workloads.
> Use **Spot** for background batch jobs to save maximum money.

---

## 🗄️ S3 — Storage Classes

> **What is it?** Amazon S3 is cloud file storage with **7 storage classes** — think of them like a **temperature scale from 🔥 hot to ❄️ frozen**. The "hotter" the data (frequently accessed), the more you pay. The "colder" (rarely accessed), the cheaper — but slower to retrieve.

> 🧠 **Memory Trick — The Temperature Scale:**
>
> 🔥 Standard → 🌡️ Intelligent-Tiering → 🌤️ Standard-IA → ☁️ One Zone-IA → 🧊 Glacier Instant → ❄️ Glacier Flexible → 🥶 Deep Archive
>
> *Colder = Cheaper storage cost, but longer retrieval time*

### Lifecycle Timeline

```
Day 0          Day 30         Day 90         Day 365
  |              |              |              |
🔥 Standard → 🌤️ Std-IA → 🧊 Glacier → ❄️ Deep Archive
```

| Class | Simple Explanation | Retrieval Speed | Approx. Cost |
|-------|--------------------|:---------------:|:------------:|
| 🔥 **Standard** | Always-on, active data | Instant | 💰💰💰 |
| 🤖 **Intelligent-Tiering** | Auto-optimizes cost | Instant | 💰💰 |
| 🌤️ **Standard-IA** | Infrequent access, retrieval fee applies | Instant | 💰💰 |
| ☁️ **One Zone-IA** | Single AZ, lower cost, non-critical files | Instant | 💰 |
| 🧊 **Glacier Instant** | Archive with instant retrieval | Milliseconds | 💰 |
| ❄️ **Glacier Flexible** | Cold archive, access 1–2x per year | 1 min – 12 hrs | 💰 |
| 🥶 **Deep Archive** | Frozen, legal/compliance data (~$0.001/GB) | 12 – 48 hrs | 💰 cheapest |

> 💡 **Not sure which to use?**
> Use **Intelligent-Tiering** — AWS handles optimization automatically. Only manually pick a class when you *know* your access patterns precisely.

---

## 📋 Full Summary

### 🎯 The 3-Second Rule: What Each Service Does

| Service | What It Does |
|---------|-------------|
| 🌐 Route 53 | Directs traffic to servers |
| 💻 EC2 | The servers themselves |
| 🗄️ S3 | Stores files & data |

### 🔗 How These 3 Services Work Together

```
User visits website
        ↓
  🌐 Route 53
  (directs to nearest/fastest server)
        ↓
    💻 EC2
  (runs your application code)
        ↓
     🗄️ S3
  (stores files and data)
```

> 🚀 This trio forms the **backbone of most AWS-powered applications!**

---

*☁️ AWS Learning Guide · Built for learners · 2026*
