# SHELDRA — Industrial Safety Intelligence Platform

## Project Plan

---

## Architecture in One Sentence

SHELDRA is a single AI system — the **SHELDRA Intelligence Engine** — with 11 internal modules. Everything else (dashboard, avatar, voice, VR, API) is just an interface to SHELDRA. The engine ingests heterogeneous data, reasons over it with an LLM core, maintains state via a Knowledge Graph and Memory Manager, generates hazard resolution trees that improve every 5 minutes, and delivers personalized, explainable safety guidance through any frontend channel.

---

## System Layers

```
User (Worker / Supervisor / Safety Officer)
     ↓
┌──────────────────────────────────────────┐
│  Presentation Layer                       │
│  Dashboard (Next.js) · Avatar (R3F)      │
│  Voice (STT/TTS) · VR (A-Frame)          │
└────────────────┬─────────────────────────┘
                 │ HTTPS / WebSocket
┌────────────────▼─────────────────────────┐
│  API Layer (FastAPI)                      │
│  Entry: /api/v1/sheldra/*                 │
└────────────────┬─────────────────────────┘
                 │
┌────────────────▼─────────────────────────┐
│  SHELDRA Intelligence Engine              │
│  ┌──────────────┬──────────────┬────────┐ │
│  │ Orchestrator │ LLM Core     │ DecTree│ │
│  │ Personalize  │ KG Manager   │ RAG    │ │
│  │ Vision Intel │ Monitor Intel│ Memory │ │
│  │ Explainability  │ Guardrails        │ │
│  └──────────────┴──────────────┴────────┘ │
└────────────────┬─────────────────────────┘
                 │
┌────────────────▼─────────────────────────┐
│  Infrastructure Layer                     │
│  Kafka · Redis · MinIO · Service Mesh     │
└────────────────┬─────────────────────────┘
                 │
┌────────────────▼─────────────────────────┐
│  Data Layer                               │
│  Neo4j · Qdrant · InfluxDB · PostgreSQL   │
└────────────────┬─────────────────────────┘
                 │
┌────────────────▼─────────────────────────┐
│  Cloud Layer                              │
│  AWS ECS · RDS · S3 · CloudFront          │
└──────────────────────────────────────────┘
```

**Principle**: The Intelligence Engine has zero knowledge of the frontend. The frontend never directly accesses the data layer. Every interaction passes through the engine.

---

## Team Responsibilities

| Person | Role | SHELDRA Modules Owned | Secondary |
|--------|------|----------------------|-----------|
| **A** | AI Engineer | LLM Reasoning Core, Vision Intelligence, Monitoring Intelligence, Decision Tree Engine, Personalization Engine | Explainability Engine |
| **B** | Backend Engineer | Event Orchestrator, Knowledge Graph Manager, RAG Engine, Memory Manager, Safety Guardrails, Infrastructure, Data Layer | Decision Tree Engine |
| **C** | Frontend Engineer | Dashboard, 3D Avatar, Voice I/O, VR Scene, FastAPI API Layer | Explainability Engine visualization |

---

## Phase 0: Foundation — Rationale

**Why**: Before any intelligence can be built, the communication infrastructure, data persistence, and rendering pipeline must exist. Phase 0 creates the backbone that Phase 1's engine modules will connect to.

### Tasks

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Monorepo setup (GitHub, branches, CI) | B | 1h | — |
| Docker Compose for all infra services (Kafka, Neo4j, Qdrant, Redis, InfluxDB, MinIO, PostgreSQL) | B | 2h | — |
| FastAPI application skeleton with health-check endpoint | B | 1h | — |
| Next.js scaffold with R3F, Tailwind, shadcn/ui | C | 2h | — |
| SHELDRA Intelligence Engine base class + module interface | B | 2h | — |
| Knowledge Graph schema: Worker, Hazard, DecisionTree, Incident, SafetyRule, Procedure, SHELDRASession, Zone, Equipment | B | 2h | — |
| Synthetic worker profiles (3 types: novice, experienced, expert) | A | 1h | — |
| Synthetic IoT sensor data generator | A | 1.5h | — |
| Synthetic camera frame generator (augmented COCO with PPE classes) | A | 2h | — |
| Safety procedure PDFs (3-5 documents) | B | 1h | — |
| API contract specification (OpenAPI 3.0) — single endpoint: POST /api/v1/sheldra/chat | B+C | 1.5h | — |
| WebSocket streaming setup for real-time responses | B | 1h | — |

**Milestone**: `docker-compose up` starts all services. Health-check passes. API accepts requests and forwards to SHELDRA stub.

---

## Phase 1: SHELDRA Intelligence Engine — Rationale

**Why**: The core differentiator is SHELDRA itself — a unified reasoning system. Phase 1 builds the 11 internal modules so that by Day 1 end, SHELDRA can accept a context, reason over it with an LLM, retrieve knowledge, and return a personalized response.

### 1A — Event Orchestrator

**Why**: Every input (API call, sensor reading, vision detection) must enter through a single gateway that routes to the correct module, manages the request lifecycle, and collects traces.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Implement EventOrchestrator class with module registry | B | 2h | Engine base class |
| Request lifecycle: validate → route → execute → collect → respond | B | 1.5h | — |
| Module registry: modules register with capabilities | B | 1h | — |
| Trace ID propagation across all modules | B | 1h | — |
| Error handling: module failure → graceful degradation | B | 1h | — |

### 1B — LLM Reasoning Core

**Why**: Central inference. All modules feed context into this core, which generates SHELDRA's responses.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Llama 3 8B setup via Ollama (local) | A | 2h | — |
| Prompt template system: system prompt + context injection | A | 1.5h | — |
| Structured output parsing: { message, tone, gesture, confidence, citations } | A | 1h | — |
| Streaming response via Server-Sent Events | A+B | 1.5h | WebSocket |
| Guardrail integration (output validation before returning) | A | 1h | Safety Guardrails stub |

### 1C — Memory Manager

**Why**: SHELDRA must remember what happened in the current session (short-term) and what happened with this worker historically (long-term).

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Short-term memory: Redis-based conversation context (TTL: session) | B | 1h | Redis |
| Long-term memory: Knowledge Graph queries for worker interaction history | B | 1.5h | KG schema |
| Session state management (worker ID, current hazard, active tree) | B | 1h | — |
| Context window assembly: short + long → LLM prompt context | B | 1h | — |

### 1D — Knowledge Graph Manager

**Why**: All entity relationships (workers, zones, equipment, hazards, incidents) live in one queryable graph.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Cypher query builder: parameterized, safe | B | 1.5h | Neo4j |
| Node CRUD: Worker, Hazard, DecisionTree, Incident, SafetyRule, SHELDRASession, Zone, Equipment | B | 2h | KG schema |
| Edge CRUD: HAS_PROFILE, GUIDED_BY, ABOUT, RESOLVED_VIA, REQUIRES, TRIGGERED_BY, LOCATED_IN | B | 1.5h | — |
| Temporal query support: "state as of timestamp X" | B | 1.5h | — |
| Graph query cache (Redis) for frequent access patterns | B | 1h | Redis |

### 1E — Personalization Engine

**Why**: SHELDRA must respond differently to a novice vs. an expert. This module computes adaptation parameters.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Worker profile loader: query KG → build profile object | A | 1h | KG Manager |
| Adaptation dimension computation (content depth, speech rate, tone, vocabulary, feedback style) | A | 2h | — |
| Learning speed inference from interaction patterns | A | 1.5h | Memory Manager |
| Profile → prompt augmentation (inject profile into LLM context) | A | 1h | LLM Core |

### 1F — RAG Engine

**Why**: SHELDRA's knowledge must be grounded in actual safety documentation.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| PDF chunking pipeline (512 chars, 50 overlap) | B | 1h | — |
| Embedding service (E5-mistral-7b via ONNX) | B | 2h | — |
| Qdrant hybrid search (dense + BM25) | B | 1.5h | Qdrant |
| Context assembly: top-3 chunks → LLM context | B | 1h | LLM Core |
| Citation tracking: which document, section, page | B | 0.5h | — |

### 1G — Safety Guardrails

**Why**: SHELDRA must never give unsafe advice. This module validates every output before delivery.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Constraint rules: never contradict procedure, always cite sources, escalate uncertainty | A | 1h | — |
| Output validation pipeline: structured response → rule check → pass/fail | A | 1h | LLM Core |
| Confidence threshold enforcement: if < 0.5, trigger escalation | A | 0.5h | — |
| Audit log writer: every output → immutable log (Kafka + PostgreSQL) | B | 1h | Kafka |

### 1H — Explainability Engine

**Why**: Every SHELDRA decision must be traceable for trust and compliance.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Trace collector: gather all module decisions during request lifecycle | A | 1.5h | Event Orchestrator |
| Natural language explanation generator (template-based) | A | 1h | — |
| Confidence provenance: model + context + history → composite score | A | 1h | — |
| SHAP integration: vision model feature attribution (cached per class) | A | 2h | Vision Intel |

**Phase 1 Milestone**: `POST /api/v1/sheldra/chat` with `{ worker_id, message, context }` returns `{ response, avatar_command, confidence, trace_id }` in < 3 seconds.

---

## Phase 2: Perception Modules — Rationale

**Why**: SHELDRA needs eyes (Vision) and senses (Monitoring) to perceive the environment. Phase 2 adds these perception modules so SHELDRA can respond to real-world events without waiting for human input.

### 2A — Vision Intelligence

**Why**: Camera feeds are the richest real-time data source. This module processes frames and produces structured observations for the Event Orchestrator.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| YOLOv8n inference server (ONNX Runtime) | A | 2h | — |
| Frame ingestion from simulated RTSP streams | A | 1.5h | Kafka |
| PPE detection (6 classes) → structured event | A | 1.5h | — |
| Zone encroachment (polygon ROI) → structured event | A | 1.5h | — |
| Pose estimation (RTMPose) → behavior analysis | A | 2h | — |
| Person tracking (ByteTrack) → persistent worker IDs | A | 1.5h | — |
| Event producer → Kafka topic `vision.detections` | A | 1h | Kafka |

### 2B — Monitoring Intelligence

**Why**: IoT sensors provide continuous quantitative data. This module detects anomalies and produces hazard triggers for the Decision Tree Engine.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| TimesNet inference server (ONNX Runtime) | A | 2h | — |
| Sliding window (60s) anomaly scorer | A | 1.5h | — |
| Multi-sensor correlation (temp + vibration + gas) | A | 2h | — |
| Anomaly → hazard trigger → Event Orchestrator | A | 1h | Event Orchestrator |
| Adaptive thresholding (time-of-day baseline) | A | 1.5h | — |

### 2C — Decision Tree Engine

**Why**: Hazard resolution must be dynamic, not static. This module generates, updates, and scores decision trees. It is the learning loop of the platform.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Tree data model: JSON schema with nodes, branches, conditions, actions, scores | B | 1.5h | — |
| Tree generator: hazard type → KG query → node graph | B | 2h | KG Manager |
| 5-minute update cycle daemon (background worker) | B | 2h | — |
| Branch accuracy scorer: outcome → score → branch update | B | 1.5h | — |
| Tree versioning + rollback support | B | 1h | — |
| Decision Tree → API (for frontend flow chart viz) | B | 1h | FastAPI |
| Integration: Vision/Monitoring events → tree selection → SHELDRA guidance | A+B | 2h | Vision + Monitoring |

**Phase 2 Milestone**: Vision detects missing PPE → Event Orchestrator → SHELDRA generates corrective feedback. Sensor anomaly → Decision Tree loads hazard resolution → SHELDRA guides worker.

---

## Phase 3: Interface & Integration — Rationale

**Why**: The engine is built. Phase 3 connects it to users through the dashboard, avatar, voice, and VR, and adds the supervisor HITL layer.

### 3A — SHELDRA Dashboard

**Why**: The primary interface for supervisors and safety officers to monitor SHELDRA's activity.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Main layout: SHELDRA panel + context sidebar + DT panel | C | 2h | Phase 1 API |
| Real-time interaction feed (WebSocket) | C | 1.5h | WebSocket |
| SHELDRA avatar component (R3F) | C | 3h | R3F scaffold |
| Conversation panel with streaming text | C | 1h | — |
| Context panel: current worker, hazard, environment | C | 1h | KG Manager |
| Decision Tree flow chart (React Flow) | C | 2.5h | Decision Tree API |
| Worker profile viewer | C | 1.5h | KG Manager |
| Accuracy dashboard | C | 2h | Decision Tree API |
| Supervisor console: alert queue, override controls, audit log | C | 2h | — |
| Dark mode (control room optimized) | C | 0.5h | — |

### 3B — Voice I/O

**Why**: Voice is the most natural interaction mode for workers wearing PPE.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Speech-to-text (Whisper): browser mic → text | C | 2h | — |
| Text-to-speech (ElevenLabs/Coqui): SHELDRA response → audio | C | 1.5h | — |
| Lip-sync animation from audio waveform | A+C | 2h | Avatar |
| Voice activity indicator | C | 0.5h | — |
| Caption overlay (noise fallback) | C | 0.5h | — |

### 3C — VR Training Scene

**Why**: SHELDRA should train workers in VR using the same AI that guides them on the floor.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| A-Frame / Three.js XR scene with factory environment | C | 3h | — |
| SHELDRA avatar in VR | C | 1.5h | Avatar |
| Hazard simulation: gas leak, fire, equipment failure | C | 2h | — |
| Worker response scoring | C | 1h | — |
| Score → profile update | C | 1h | KG Manager |

### 3D — Deployment & Testing

**Why**: The platform must run reliably for judging.

| Task | Owner | Time | Deps |
|------|-------|------|------|
| Dockerfiles for all services (multi-stage) | B | 2h | — |
| docker-compose.prod.yml with resource limits | B | 1h | — |
| Cloud deployment (AWS ECS or GCP Cloud Run) | B | 2h | — |
| SSL + domain setup | B | 0.5h | — |
| Load test: 100 concurrent sessions (k6) | B | 1h | — |
| Backup demo recording (OBS) | All | 1h | — |
| Demo script rehearsal (3x) | All | 2h | — |

**Phase 3 Milestone**: Full end-to-end flow: worker speaks → SHELDRA hears → engine reasons → avatar speaks back → Decision Tree updates → supervisor monitors.

---

## Demo Flow (5 Minutes)

| Time | Segment | What Judges See |
|------|---------|-----------------|
| 0:00 | SHELDRA intro | Dashboard loads. SHELDRA avatar appears. "Welcome to Shift 3. I'm SHELDRA, your safety coach." |
| 0:30 | PPE correction | Vision detects missing glasses. SHELDRA: "Worker #3124, your glasses are on your helmet." Decision Tree opens beside avatar. |
| 1:15 | Personalization switch | Same scenario, 3 profiles. Novice gets step-by-step. Expert gets brief confirmation. "One SHELDRA, adapted to each worker." |
| 2:00 | Gas leak + tree update | Anomaly detected. SHELDRA switches to emergency mode. Tree loads gas response. After resolution: "Tree updated to v8 — accuracy 94%." |
| 2:45 | Accuracy dashboard | Show tree accuracy trend, branch effectiveness, update frequency. "This tree learns every 5 minutes." |
| 3:15 | VR training | SHELDRA in VR. Guides worker through confined space scenario. Score updates profile. |
| 3:45 | Architecture reveal | One-slide: SHELDRA Intelligence Engine with 11 modules. "Everything you saw is one AI system." |
| 4:15 | Q&A hook | "We built SHELDRA in 72 hours. The architecture scales to any facility. We'd love to discuss how this redefines industrial safety." |

---

## Risk Register

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| 3D avatar performance | Demo quality | Medium | 2D fallback with identical behavior |
| LLM latency > 3s | Demo feel | High | Streaming TTS; pre-generated demo paths; "thinking" animation |
| Voice I/O fails in noisy hall | Demo segment | Medium | Text chat always visible; captions on all speech |
| Decision Tree auto-generation incomplete | Technical depth | Medium | 5 pre-built trees; show update cycle on 1 tree; auto-generation as roadmap |
| Integration gaps between modules | End-to-end fail | Medium | Contract testing; mock interfaces; orchestrated demo script |
| Cloud dependency fails (no internet) | Demo fail | Low | Local-only docker-compose mode; all services on single laptop |

---

## Deliverables Summary

| Artifact | Format | Content |
|----------|--------|---------|
| SHELDRA Intelligence Engine | Python package | 11 modules with defined interfaces |
| FastAPI Application | Python | Single entry point: /api/v1/sheldra/* |
| Next.js Dashboard | TypeScript | SHELDRA avatar, conversation, DT viz, supervisor console |
| Decision Trees | JSON | 5 pre-built trees + update cycle engine |
| Worker Profiles | Cypher | 3 synthetic profiles in Neo4j |
| VR Training Scene | A-Frame/Three.js | Factory environment + SHELDRA avatar |
| Docker Compose | YAML | All services, single command startup |
| Architecture Document | DOCX | 26-section enterprise architecture proposal |
