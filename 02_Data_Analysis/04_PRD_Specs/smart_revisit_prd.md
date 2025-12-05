# 📄 Product Requirements Document: Smart Revisit Module
**Status:** Final | **Target Release:** Q4 2025 | **Owner:** Sai Kishan

## 1. Problem Statement
Learners returning to Khan Academy often lose context. Our data shows a **15% drop in efficiency** during summer months due to "context switching" costs. The current "Continue Learning" button is insufficient because it treats all return sessions the same, regardless of whether the user was struggling or succeeding.

## 2. User Stories
| Persona | Problem | Solution |
| :--- | :--- | :--- |
| **Ava (High Schooler)** | "I forgot where I stopped in the video." | **Resume at Timestamp:** Links directly to the last watched second. |
| **Ravi (Adult Upskiller)** | "I kept failing this quiz last time." | **Review Key Concepts:** Suggests a lower-difficulty review before re-attempting. |

## 3. Functional Requirements
### 3.1 The "Smart Chip" Logic
The logic engine must query the `user_activity_daily` table to determine the chip type:

* **IF** `accuracy_rate` < 50% **AND** `attempts` > 2:
    * **DISPLAY:** "Review Key Concepts" (Link to prerequisite video).
* **IF** `accuracy_rate` > 80%:
    * **DISPLAY:** "Next Logical Step" (Link to next unit).
* **ELSE:**
    * **DISPLAY:** "Resume" (Standard timestamp link).

### 3.2 Technical Constraints (Engineering Notes)
* **Latency:** The "Smart Chip" query must execute in < 200ms to avoid blocking the dashboard load.
* **Fallback:** If Redis cache is empty, default to standard "Resume" behavior.

## 4. Success Metrics (The ILV Framework)
* **Primary (North Star):** Interactive Learning Velocity (ILV).
    * *Goal:* Increase by 15% YoY.
* **Counter Metric:** Learning Stress Index (LSI).
    * *Guardrail:* Maintain < 10%.
* **Feature Metric:** Revisit Click-Through Rate (CTR).
    * *Goal:* > 45% for returning users.

## 5. Risks & Mitigation
* **Risk:** Users might feel "judged" by the "Review Key Concepts" suggestion.
* **Mitigation:** Use encouraging copy (e.g., "Let's refresh this concept" instead of "You failed").
