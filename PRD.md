# 📄 Product Requirements Document: Smart Revisit Engine

| Attribute | Details |
| :--- | :--- |
| **Feature Name** | Smart Revisit & Contextual Entry |
| **Status** | 🟢 Shipped (MVP) |
| **Target Persona** | Returning Learners & Adult Upskillers |
| **Product Area** | Core Learner Experience / Retention |
| **Version** | 1.2 (Final) |

---

## 1. Problem Statement
**The "Cold Start" Friction:**
Learners frequently drop off after a break because revisiting specific content feels cumbersome. Without a clear "return path," users waste time searching for where they left off and often abandon their learning goals due to a loss of momentum.

**Data Insight:**
* **60%** of potential churn occurs when a user breaks their daily streak and cannot easily find a re-entry point.
* Adult learners specifically struggle with "forgetting recently missed concepts" and wasting time searching for review material.

---

## 2. Goals & Success Metrics
The primary goal is to **eliminate friction upon return**, translating user intent into immediate learning activity.

| Metric Category | Metric Name | Target (KR) | Why it matters |
| :--- | :--- | :--- | :--- |
| **North Star** | **Interactive Learning Velocity (ILV)** | +15% YoY | Measures speed of skill acquisition balanced by quality. |
| **Adoption** | **Feature Engagement Rate** | 45% CTR | Percentage of returning users clicking the "Smart Revisit" card. |
| **Retention** | **30-Day Retention Rate** | 32% | Measures long-term habit formation for the exposed cohort. |
| **Counter Metric**| **Learning Stress Index (LSI)** | < 10% | Ensures we don't push users into frustration or "rage quits." |

---

## 3. The Solution: "Smart Revisit" Module
A contextual entry point on the learner dashboard that automatically shifts from offering a generic "Welcome" to surfacing personalized **"Revisit" content** based on prior session data.

### 🧠 The Logic Engine (Personalization)
Instead of a static feed, the application uses a **Rule-Based Scoring Engine** to determine the optimal card to show:

1.  **Refresher Mode:** Triggered if `DaysSinceLastVisit > 7`.
2.  **Review Mode:** Triggered if `Accuracy < 60%` OR `StruggleAttempts > 2`.
3.  **Challenge Mode:** Triggered if `Accuracy > 90%` (Flow State).
4.  **Resume Mode:** Default state (Continue exactly where left off).

---

## 4. User Stories & Functional Requirements

### P0: Continue Learning (The Happy Path)
> **As a** Returning Learner (Ava),
> **I want to** instantly resume my last viewed lesson at the exact timestamp,
> **So that** I can continue my progress without losing context.

* **Requirement:** Display a "Welcome Back" card with a thumbnail preview and dynamic CTA (e.g., "Resume at 3:42").
* **Data State:** Retrieves `content_ID`, `timestamp`, and `progress_status` from local storage.

### P1: Revisit Key Concepts (The Recovery Path)
> **As a** Goal-Oriented Learner (Ravi),
> **I want** the system to suggest the most critical, challenging concepts from my past sessions,
> **So that** I can reinforce my understanding efficiently before moving on.

* **Requirement:** If the user struggled previously, replace the "Continue" CTA with a "Review Key Concepts" card.
* **Visuals:** Display specific rationale tags (e.g., "Missed 2x", "Lowest Accuracy Skill").

---

## 5. Technical Implementation (MVP)

### Frontend Architecture
* **Framework:** React + TypeScript + Vite.
* **Styling:** Tailwind CSS for mobile-responsive layout (Mobile-First approach).
* **State Management:** React Query for data fetching; `localStorage` for session persistence (simulating a Redis caching layer for MVP).

### Data Tracking Plan
To calculate the **Interactive Learning Velocity (ILV)**, the app tracks the following signals:
* `skill_progress_updates`
* `interactive_tool_usage`
* `mastery_success_rate`
* `hint_dependency` (captured via the "Confidence Loop" UI).

---

## 6. Risks & Mitigation Strategies

| Risk | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **Low Adoption** | Users ignore the card. | **A/B Test Placement:** Test the card at the top of Feed vs. a modal. Add a "New" tooltip on first exposure. |
| **Inaccurate Recs** | Users lose trust in the "Smart" engine. | **Rule-Based MVP:** Start with strict, transparent rules (e.g., "Because you missed 2 questions") before moving to complex ML models. |
| **Data Privacy** | Leaking user performance data. | **Local Storage & Anonymization:** Ensure all session data is stored using anonymized IDs locally for the MVP. |

---

## 7. Future Roadmap (Post-MVP)
* **v1.5:** Integration of **"Confidence Loop"** (User self-reported sentiment) to refine the algorithm.
* **v2.0:** **Cross-Device Sync** (Transition from LocalStorage to Cloud DB/Supabase).
* **v2.5:** **AI-Generated Flashcards** based on specific "Struggle" topics.
