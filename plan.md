# ET AI Hackathon 2026 — Industrial Safety Intelligence Platform

## Execution Plan: Phases, Priorities & Team Split

---

## Vision Statement

> SHELDRA — an autonomous holographic AI safety coach that walks beside every worker, sees what they see, knows what they know, and guides them through every hazard with personalized, adaptive intelligence. Backed by a real-time decision tree engine that learns from every interaction, every sensor, every incident.

---

## Two Primary Pillars (Everything Else Supports These)

| # | Pillar | What It Is | Why It Wins |
|---|--------|------------|-------------|
| **1** | **SHELDRA** — Holographic AI Safety Coach | An adaptive AI avatar that provides real-time guidance, corrective feedback, and personalized training to workers via AR/VR/mobile. Adapts to each worker's profile, learning speed, and experience level. | No other industrial safety system puts an _intelligent, personalized coach_ at the center. Not a dashboard — a relationship. |
| **2** | **Decision Tree Engine** — Automated Hazard Resolution | A real-time decision tree algorithm that ingests sensor data, worker context, and historical incidents to generate step-by-step hazard resolution flow charts. Updates every 5 minutes with new data for continuous accuracy improvement. | Replaces static safety checklists with _living, learning_ decision trees that evolve with every incident. |

> Everything below — Multi-Agent System, Knowledge Graph, Computer Vision, RAG, Digital Twin, Time-Series — exists to **feed and empower** these two pillars.

---

## Team Structure

| Person | Role | Primary Focus (SHELDRA) | Secondary Focus (Decision Tree) |
|--------|------|------------------------|----------------------------------|
| **A** | AI/ML Engineer | SHELDRA core AI (LLM fine-tuning, personalization engine, voice/emotion models), Worker profile learning | Decision tree node expansion logic, accuracy scoring, RL from feedback |
| **B** | Backend/Infrastructure | SHELDRA API, real-time context ingestion, Knowledge Graph for personalization, multi-agent orchestration | Decision tree engine (generation + update pipeline), 5-min refresh cycle, evaluation metrics |
| **C** | Full-Stack / Frontend | SHELDRA 3D holographic avatar UI (Three.js/WebXR), voice I/O, AR overlay wireframes, VR training scene | Decision tree flow chart visualization (interactive DAG), hazard resolution walkthrough UI |

---

## Priority Matrix

| Priority | Category | Components | Effort | Impact |
|----------|----------|------------|--------|--------|
| **P0** | **Primary** | SHELDRA holographic avatar + voice interaction + real-time coaching | High | Highest |
| **P0** | **Primary** | Decision Tree Engine — dynamic generation + 5-min update cycle | High | Highest |
| **P0** | **Supporting** | Worker profile model + personalization engine | Medium | High |
| **P0** | **Supporting** | Real-time context ingestion (vision + IoT → SHELDRA awareness) | Medium | High |
| **P1** | **Supporting** | Multi-Agent System (agents feed SHELDRA's awareness) | High | High |
| **P1** | **Supporting** | Knowledge Graph (worker context, hazard relationships) | Medium | High |
| **P1** | **Supporting** | Decision tree flow chart visualization UI | Medium | High |
| **P1** | **UX** | VR training scenario integration | High | High |
| **P2** | **Supporting** | Computer Vision pipeline (feeds SHELDRA's "eyes") | Medium | Medium |
| **P2** | **Supporting** | Time-series anomaly detection (feeds Decision Tree) | Medium | Medium |
| **P2** | **Supporting** | RAG for SHELDRA's safety knowledge grounding | Medium | High |
| **P2** | **UX** | AR overlay wireframes (HoloLens-style concept) | Medium | Medium |
| **P3** | **Supporting** | Digital Twin (3D spatial context for SHELDRA) | High | Medium |
| **P3** | **Metrics** | Accuracy evaluation dashboard for hazard measures | Medium | Medium |

---

## Phase 0: Foundation (Pre-Hackathon)

| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Set up monorepo (GitHub) | B | 1h | None |
| Configure cloud accounts | B | 1h | None |
| **SHELDRA persona design** — name, voice, visual identity | All | 2h | None |
| Research 3D avatar frameworks (Ready Player Me, Three.js avatars) | C | 2h | None |
| Docker-compose for local infra (Kafka, Neo4j, Qdrant, Redis) | B | 2h | None |
| Frontend scaffold (Next.js + Three.js + WebXR + Tailwind) | C | 2h | None |
| Define API contracts (OpenAPI spec — SHELDRA endpoints first) | B + C | 2h | None |
| Seed Knowledge Graph schema (worker profiles + hazard taxonomy) | B | 2h | Neo4j running |
| Set up CI/CD (GitHub Actions) | B | 1h | Repo ready |
| **Collect safety procedure PDFs for SHELDRA's knowledge base** | A | 2h | None |

**Milestone: SHELDRA avatar renders in browser; Knowledge Graph seeded**

---

## Phase 1: SHELDRA + Decision Tree Core (Day 1)

### 1A — SHELDRA Core AI (P0 — A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Design SHELDRA system prompt + guardrails (safety-critical LLM behavior) | A | 1h |
| Implement worker profile model (experience, learning speed, language, certs) | A | 1.5h |
| Build personalization engine (profile → prompt augmentation → response tuning) | A | 2h |
| Implement SHELDRA response pipeline: Context → Profile → RAG → LLM → Response | A | 2h |
| Voice I/O integration (Web Speech API + ElevenLabs TTS / Whisper STT) | A + C | 2h |
| Implement corrective feedback generation (from CV observations) | A | 1.5h |
| Build SHELDRA emotional awareness (voice tone analysis + stress detection) | A | 2h |

### 1B — SHELDRA Holographic Avatar (P0 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| 3D avatar rendering in Three.js / React Three Fiber | C | 3h |
| Lip-sync animation from TTS audio | C | 1.5h |
| Gesture animation system (pointing, nodding, warning stance) | C | 2h |
| SHELDRA UI overlay (speech bubble, context panel, mini-map) | C | 2h |
| Mobile + desktop responsive layout | C | 1h |
| Ambient mode (idle animations, environmental scanning visualization) | C | 1h |

### 1C — Decision Tree Engine (P0 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Design decision tree data model (JSON schema: nodes, edges, conditions, actions) | B | 1.5h |
| Implement tree generator from rule patterns + KG queries | B | 2h |
| Implement 5-minute update cycle (Apache Airflow / cron + diff engine) | B | 2h |
| Build accuracy scorer (compare predicted hazard resolution → actual outcome) | B | 1.5h |
| Implement tree versioning (v1 → v2 → v3 with accuracy deltas) | B | 1h |
| Decision tree → API endpoint for SHELDRA consumption | B | 1h |

### 1D — Decision Tree Visualization (P0 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Interactive DAG flow chart renderer (React Flow) | C | 2h |
| Color-coded node states (safe path green, warning yellow, hazard red) | C | 1h |
| Step-by-step resolution walkthrough mode | C | 1.5h |
| Export flow chart as image/PDF | C | 0.5h |

**Milestone: SHELDRA speaks and guides; Decision Tree generates first flow chart**

---

## Phase 2: Integration + Supporting Intelligence (Day 2)

### 2A — Multi-Agent System → Feeds SHELDRA (P1 — A + B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Orchestrator Agent — routes all observations to SHELDRA context | B | 2h |
| Vision Agent — PPE/behavior detection → SHELDRA corrective feedback triggers | A | 2h |
| Monitoring Agent — time-series anomaly → Decision Tree hazard input | A | 2h |
| Compliance Agent — KG queries → SHELDRA regulatory guidance | B | 1.5h |
| RAG Agent — safety document retrieval → SHELDRA knowledge grounding | A + B | 2h |
| Explanation Agent — SHELDRA decision tracing ("SHELDRA, why did you say that?") | A | 1.5h |

### 2B — Knowledge Graph → Personalization (P1 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Worker profile nodes (experience, certs, learning speed, incident history) | B | 1h |
| Hazard taxonomy nodes + decision tree version linking | B | 1.5h |
| SHELDRA interaction history (every coaching moment → graph edge) | B | 1h |
| Temporal query: "What has this worker learned in the last shift?" | B | 1h |

### 2C — VR Training Integration (P1 — C + A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| SHELDRA in VR scene (Three.js XR / A-Frame) | C | 3h |
| Hazard simulation scenarios (gas leak, fire, equipment failure) | A | 2h |
| Worker response scoring in VR | A | 1.5h |
| VR performance → worker profile update | B | 1h |

### 2D — Computer Vision → SHELDRA's Eyes (P2 — A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| PPE detection → SHELDRA corrective feedback ("Your helmet is unstrapped") | A | 2h |
| Unsafe behavior detection → SHELDRA warning | A | 2h |
| Zone encroachment → SHELDRA redirection | A | 1.5h |
| Frame-level reasoning → structured observation for SHELDRA context | A | 1h |

### 2E — Time-Series → Decision Tree Input (P2 — A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| TimesNet anomaly detection on streaming sensor data | A | 2h |
| Anomaly → Decision Tree hazard trigger ("vibration anomaly on Machine #7 → show flow chart") | A | 1.5h |
| Multi-sensor correlation → compound hazard detection | A | 1.5h |

**Milestone: SHELDRA sees, knows, and guides; Decision Trees evolve with data**

---

## Phase 3: Polish + Accuracy Loop (Day 3)

### 3A — SHELDRA Refinement (P2 — A + C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| SHELDRA emotional range (calm coach, urgent warning, praise for compliance) | A | 2h |
| Multi-language support (top 3 industrial languages) | A | 1.5h |
| SHELDRA "memory" (recalls past interactions with this worker) | B | 1h |
| Avatar polish (animations, transitions, visual effects) | C | 2h |
| SHELDRA AR overlay wireframes (HoloLens-style HUD concept) | C | 2h |

### 3B — Decision Tree Accuracy Engine (P2 — B + A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Accuracy metrics dashboard (precision, recall for hazard resolution) | B | 1.5h |
| Automated tree pruning (remove low-accuracy branches) | A + B | 2h |
| A/B testing: old tree vs new tree recommendation | B | 1.5h |
| Feedback ingestion from SHELDRA interactions → tree improvement | B | 1h |

### 3C — Human-in-the-Loop (P2 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Supervisor override of SHELDRA recommendation | C | 1.5h |
| SHELDRA audit log (every coaching moment recorded) | B | 1h |
| Shift handover: SHELDRA briefs incoming shift on hazards + worker status | A + C | 2h |
| Incident report generation (SHELDRA's perspective + Decision Tree path taken) | B + A | 1h |

### 3D — Real-Time Update Pipeline (P2 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| 5-minute incremental update for Decision Trees | B | 1.5h |
| Worker profile real-time sync (SHELDRA interactions → graph update → profile) | B | 1h |
| Accuracy measure pipeline (every hazard resolution → scored → tree updated) | B | 1.5h |
| Kafka topic restructure: `sheldra.interactions`, `decision.trees`, `worker.profiles` | B | 1h |

### 3E — Dashboard + DEMO Readiness (P2 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Main dashboard: SHELDRA view (avatar + conversation + context panel) | C | 2h |
| Decision Tree live view (click any hazard → see current flow chart) | C | 1.5h |
| Worker profile panel (SHELDRA's view of each worker) | C | 1h |
| Accuracy dashboard (tree accuracy trends, hazard resolution rates) | C | 1h |
| Mobile-responsive SHELDRA interface | C | 1h |
| **Demo script: SHELDRA-guided hazard resolution walkthrough** | All | 2h |

### 3F — Deployment (P2 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Containerize all services | B | 2h |
| Deploy SHELDRA API + avatar to cloud | B | 2h |
| WebSocket for real-time SHELDRA streaming | B | 1h |
| Load test: 100 concurrent SHELDRA sessions | B | 1h |

**Milestone: SHELDRA fully operational — personalized coaching, real-time decision trees, accuracy feedback loop**

---

## Phase 4: Presentation Prep (Last 4 Hours)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Script: "Meet SHELDRA — the world's first holographic AI safety coach" | All | 1h |
| Live demo: SHELDRA guides worker through hazard → Decision Tree generates flow chart → accuracy loop closes | All | 2h |
| Slide deck: SHELDRA-first narrative | C | 1h |
| Backup demo recording | All | 30m |
| Judge Q&A: "How does SHELDRA personalize?" "How fast do trees update?" | All | 30m |

---

## Team Weekly Allocation Summary

| Phase | Person A (AI/ML) | Person B (Backend/Infra) | Person C (Full-Stack) |
|-------|-----------------|-------------------------|----------------------|
| Foundation | SHELDRA prompt design, worker profile model | Infra, KG schema (worker + hazard), API contracts | Avatar scaffold (Three.js), SHELDRA UI shell |
| Day 1 | SHELDRA core AI + personalization + voice I/O + feedback | Decision Tree engine + update cycle + API | SHELDRA 3D avatar + lip-sync + gestures + Decision Tree viz |
| Day 2 | Multi-agent: Vision + Monitoring for SHELDRA + DT | Multi-agent: Orchestrator + Compliance + RAG + KG personalization | VR scene + SHELDRA in VR + Decision Tree step walkthrough |
| Day 3 | SHELDRA emotion + multi-language + DT tree pruning | 5-min update pipeline + accuracy metrics + audit | SHELDRA polish + AR wireframes + accuracy dashboard |
| Presentation | SHELDRA deep dive (AI decisions) | Architecture + Decision Tree accuracy story | SHELDRA live demo lead + avatar showcase |

---

## Architecture Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                     SHELDRA (Holographic AI Coach)              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────┐ │
│  │  Avatar   │  │  Voice   │  │Personal- │  │   Emotional    │ │
│  │   (3D)    │  │ I/O (TTS │  │ ization  │  │  Awareness     │ │
│  │           │  │  / STT)  │  │  Engine  │  │ (stress/fatigue)│ │
│  └─────┬─────┘  └────┬─────┘  └────┬─────┘  └───────┬────────┘ │
│        └──────────────┴─────────────┴────────────────┘         │
│                           │                                     │
│                    Context Fusion Layer                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
   │ Multi-Agent │  │ Knowledge   │  │ Decision    │
   │ System      │  │ Graph       │  │ Tree Engine │
   │ (feeds      │  │ (worker     │  │ (generates   │
   │  awareness) │  │  profiles)  │  │  flow charts)│
   └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
          │                │                │
          ▼                ▼                ▼
   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
   │ CV + IoT    │  │ RAG (safety │  │ 5-min       │
   │ Sensors     │  │ procedures) │  │ Update Cycle│
   └─────────────┘  └─────────────┘  └─────────────┘
```

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| 3D avatar too heavy for hackathon | Medium | High | Fallback to 2D animated character (Lottie/Bodymovin) with same personality |
| Voice I/O fails in noisy demo hall | Medium | Medium | Text-chat fallback; captions always visible |
| Decision Tree too complex to auto-generate | Medium | High | Seed with 3-5 pre-built trees; real-time update demo on one tree |
| LLM latency breaks real-time illusion | High | High | Pre-generate SHELDRA responses for demo scenarios; streaming TTS |
| Personalization insufficient for demo impact | Low | Medium | Pre-create 3 worker profiles (novice, experienced, expert) with visibly different SHELDRA behavior |

---

## Judging Narrative

> "Most industrial safety systems are dashboards with AI features. We built SHELDRA — the first AI safety coach that _walks beside every worker_. It see what they see, knows what they know, adapts to how they learn, and guides them step-by-step through every hazard. Its Decision Tree engine doesn't just follow static checklists — it generates _living flow charts_ that improve with every incident, updating every 5 minutes. This is not a tool. This is a teammate."
