# 🎓 Khan Academy: Smart Revisit & Learning Velocity Optimization
**Stanford Accelerated Product Management Capstone (Group C)**

![Role](https://img.shields.io/badge/Role-Product_Manager-blue) ![Focus](https://img.shields.io/badge/Focus-Data_Strategy_%7C_UX-orange) ![Status](https://img.shields.io/badge/Status-Completed-success)

## 🚀 Executive Summary
Learners on Khan Academy suffer from **friction upon return**. They lose context, leading to drop-offs. This project introduces **"Smart Revisit,"** a feature that uses historical session data to personalize the "Resume Learning" experience.

We validated this through user research (N=5) and defined a new North Star Metric framework: **Interactive Learning Velocity (ILV)** paired with a counter-metric, **Learning Stress Index (LSI)**, to ensure retention doesn't come at the cost of user burnout.

---

## 🧐 The Problem: "Where was I?"
* **User Pain Point:** "Learners lose focus because Khan Academy makes it hard to revisit specific content or pick up where they left off."
* **Data Insight:** Our analysis showed a **15% decline in problem-solving efficiency** during summer months, indicating a need for better context retention.
* **The Gap:** Existing "Continue Learning" options were static and didn't account for *how* a user performed in the previous session.

## 🛠️ The Solution: Smart Revisit Module
We designed a contextual entry point that surfaces personalized "Revisit" content based on prior performance.

### Logic Flow (The "Data" Behind the Feature)
```mermaid
graph TD;
    A[User Returns to Dashboard] --> B{Check Last Session Data};
    B -- "Low Accuracy (<50%)" --> C[Recommend: Review Key Concepts];
    B -- "High Accuracy (>80%)" --> D[Recommend: Next Logical Step];
    B -- Abandoned Session --> E[Recommend: Resume at Timestamp];
    C --> F[User Clicks Smart Chip];
    F --> G[Increase Session Depth +10% KR];
