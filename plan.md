# ET AI Hackathon 2026 — Industrial Safety Intelligence Platform

## Execution Plan: Phases, Priorities & Team Split

---

## Vision Statement

> An autonomous industrial immune system that predicts, prevents, and responds to safety incidents in real-time by fusing computer vision, IoT telemetry, knowledge graphs, and multi-agent AI — replacing reactive compliance dashboards with a living, learning intelligence layer.

---

## Team Structure

| Person | Role | Primary Focus | Secondary Focus |
|--------|------|---------------|-----------------|
| **A** | AI/ML Engineer | Vision models, Time-series anomaly detection, AI pipeline | Multi-agent orchestration logic |
| **B** | Backend/Infrastructure | Ingestion pipeline, Knowledge Graph, APIs, Cloud infra | RAG pipeline, Digital Twin backend |
| **C** | Full-Stack / Frontend | Dashboard, Digital Twin 3D viz, HITL UX, Demo flow | Knowledge Graph visualization |

---

## Priority Matrix

| Priority | Category | Components | Effort | Impact |
|----------|----------|------------|--------|--------|
| P0 | Core Differentiator | Multi-Agent Orchestrator + Knowledge Graph | High | Highest |
| P0 | Core Differentiator | Computer Vision PPE/unsafe detection | Medium | Highest |
| P0 | Must-Have | Data ingestion (synthetic + real-time) | Medium | High |
| P1 | Intelligence | RAG for safety procedures | Medium | High |
| P1 | Intelligence | Time-series anomaly detection | Medium | High |
| P1 | UX | Digital Twin visualization | High | High |
| P2 | Polish | Explainable AI overlay | Medium | Medium |
| P2 | Polish | Human-in-the-loop workflows | Medium | High |
| P2 | Infrastructure | Cloud deployment, CI/CD | Medium | Medium |
| P3 | Stretch | Graph AI (GNN for root cause) | High | Medium |
| P3 | Stretch | Mobile push alerts | Low | Low |

---

## Phase 0: Foundation (Pre-Hackathon)

| Task | Owner | Duration | Dependencies |
|------|-------|----------|--------------|
| Set up monorepo (GitHub) | B | 1h | None |
| Configure cloud accounts (AWS/GCP) | B | 1h | None |
| Research & download pretrained models (YOLOv8, TimesNet, E5) | A | 2h | None |
| Set up synthetic data generators | A + B | 3h | None |
| Docker-compose for local infra (Kafka, Neo4j, Qdrant, Redis) | B | 2h | None |
| Frontend scaffold (Next.js + Three.js + Tailwind) | C | 2h | None |
| Define API contracts (OpenAPI spec) | B + C | 2h | None |
| Seed knowledge graph schema | B | 2h | Neo4j running |
| Set up CI/CD (GitHub Actions) | B | 1h | Repo ready |

**Milestone: All infrastructure runs locally via docker-compose**

---

## Phase 1: Core MVP — The Differentiator (Day 1)

### 1A — Multi-Agent System (P0 — A + B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Implement Agent base class + communication protocol | B | 2h |
| Orchestrator Agent with state management | B | 2h |
| Vision Agent wrapper (calls CV model) | A | 1.5h |
| Monitoring Agent (time-series anomaly) | A | 1.5h |
| Compliance Agent (KG queries) | B | 1.5h |
| Response Agent + action templates | B | 1h |
| Explanation Agent (reasoning traces) | A | 1.5h |
| Inter-agent message passing via Redis Pub/Sub | B | 1h |

### 1B — Computer Vision Pipeline (P0 — A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| PPE detection model (YOLOv8 fine-tune or zero-shot) | A | 3h |
| Unsafe behavior detection (pose-based) | A | 3h |
| Zone encroachment detection | A | 1.5h |
| Camera feed ingestion (simulated RTSP -> frames) | A | 1h |
| Frame-level reasoning -> agent events | A | 1h |

### 1C — Knowledge Graph (P0 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Define Cypher schema (Nodes: Worker, Zone, Equipment, Incident, Rule) | B | 1h |
| Seed with synthetic factory data | B | 1h |
| Implement real-time graph updates from events | B | 2h |
| Graph query layer for Compliance Agent | B | 1h |

### 1D — Real-Time Ingestion (P0 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Kafka topic setup + schema registry | B | 1h |
| IoT sensor simulator (temperature, vibration, gas, noise) | B | 1.5h |
| Camera event stream producer | A | 1h |
| Flink/KSQL stream processor for windowed aggregates | B | 2h |

**Milestone: End-to-end flow — sensor event → agent → alert → graph update**

---

## Phase 2: Intelligence Layer (Day 2)

### 2A — RAG Pipeline (P1 — B + A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Ingest safety manuals / SOPs (PDF chunking) | B | 1h |
| Embedding pipeline (E5 or BGE) | B | 1h |
| Hybrid search (dense + BM25 in Qdrant) | B | 1.5h |
| RAG query agent (routes to LLM + context) | A | 2h |
| Citation-grounded responses | A | 1h |

### 2B — Time-Series Anomaly Detection (P1 — A)

| Task | Owner | Est. Time |
|------|-------|-----------|
| TimesNet / PatchTST model deployment | A | 2h |
| Real-time anomaly scoring on streaming data | A | 2h |
| Multi-sensor correlation (vibration + temp + gas) | A | 2h |
| Threshold-free anomaly detection (unsupervised) | A | 1.5h |

### 2C — Digital Twin (P1 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| 3D factory scene in Three.js / Spline | C | 4h |
| Real-time state sync via WebSocket | C | 2h |
| Equipment status overlays | C | 1.5h |
| Incident heatmap overlay | C | 1h |

**Milestone: AI agents reason over fused vision + IoT + document data**

---

## Phase 3: Integration & Polish (Day 3)

### 3A — Human-in-the-Loop (P2 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Supervisor approval queue | C | 1.5h |
| Alert acknowledge / dismiss / escalate | C | 1h |
| Explanation panel (why this alert?) | C + A | 1.5h |
| Audit trail logging | B | 1h |

### 3B — Explainable AI (P2 — A + C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| SHAP/LIME integration for vision decisions | A | 2h |
| Decision trace visualization (agent reasoning chain) | C | 1.5h |
| Confidence scoring for all predictions | A | 1h |
| Natural language explanations via explanation agent | A | 1.5h |

### 3C — Emergency Response Workflow (P2 — B + C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Automated response templates (evacuate, shutdown, alert) | B | 1h |
| Multi-channel alerting (WebSocket, email, SMS via Twilio) | B | 1.5h |
| Escalation ladder (supervisor → manager → director) | B | 1h |
| Post-incident report generator | B + A | 1h |

### 3D — Dashboard Completion (P2 — C)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Real-time safety score / KPIs | C | 1h |
| Agent activity feed | C | 1h |
| Knowledge Graph explorer (Neo4j Bloom embed or custom) | C | 2h |
| Incident timeline | C | 1h |
| Mobile-responsive layout | C | 1h |

### 3E — Deployment (P2 — B)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Containerize all services | B | 2h |
| Deploy to cloud (AWS ECS or GCP Cloud Run) | B | 2h |
| Domain + SSL setup | B | 30m |
| Load test with simulated 1000 events/sec | B | 1h |

**Milestone: Fully integrated, deployable platform**

---

## Phase 4: Presentation Prep (Last 4 Hours)

| Task | Owner | Est. Time |
|------|-------|-----------|
| Script writing (problem → solution → demo → impact) | All | 1h |
| Demo flow rehearsals | All | 2h |
| Slide deck finalization | C | 1h |
| Backup demo recording | All | 30m |
| Judge Q&A prep | All | 30m |

---

## Team Weekly Allocation Summary

| Phase | Person A | Person B | Person C |
|-------|----------|----------|----------|
| Foundation | Pretrained models + data generators | Infra setup, KG schema, API contracts | Frontend scaffold |
| Day 1 | Vision pipeline + Agent wrappers | Multi-agent infra + KG + ingestion | Digital Twin basic scene |
| Day 2 | Time-series models + RAG agent | RAG pipeline + stream processing | DT polish + KG viz |
| Day 3 | XAI + confidence scoring + report gen | Emergency workflows + deployment | HITL + dashboard + KG explorer |
| Presentation | Technical deep-dive support | Architecture slides | Demo lead + slides |

---

## Key Integration Points

```
Camera Feeds ──► Vision Agent ──┐
                                 ├──► Orchestrator ──► Knowledge Graph
IoT Sensors ──► Monitoring Agent ┘         │                  │
                                           ▼                  ▼
Safety Docs ──► RAG Agent ──► LLM ◄── Context Fusion ──► Digital Twin
                                           │
                                           ▼
                                    Explanation Agent
                                           │
                                           ▼
                                    HITL Console ◄── Dashboard
```

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Model accuracy too low for demo | Medium | High | Fallback to scripted demo with real inference overlay |
| Neo4j query latency | Low | Medium | Pre-compute common graph traversals; use Redis cache |
| Real-time 3D rendering lags | Medium | Medium | Reduce scene complexity; use sprite-based indicators |
| API integration gaps | Medium | High | Mock interfaces with clear contract testing |
| Team member drop-off | Low | High | Cross-train; each person documents their interfaces |
| Cloud credits exhausted | Low | Medium | Optimize for local demo; use free tiers |

---

## Success Criteria for Judging

| Criterion | How We Win |
|-----------|------------|
| Innovation | Multi-agent KG-native architecture (not chatbot); fused intelligence |
| Technical depth | Explainable AI chain-of-reasoning; Digital Twin state sync |
| Practical impact | Real-time emergency response; compliance automation |
| Scalability | Kafka + stream processing; microservices; cloud-native |
| Presentation | Narrative: "Industrial Immune System" — not another dashboard |
