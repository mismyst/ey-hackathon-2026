# SHELDRA — Engineering Backlog

**Total Tasks**: 130+
**Format**: `[Status] Priority | Owner | Time | Dependencies`
**Status**: `[ ]` Pending `[~]` In Progress `[x]` Done
**Priority**: P0 (Critical) / P1 (Important) / P2 (Nice-to-Have) / P3 (Stretch)

---

## Phase 0 — Foundation

### P0-INF Infrastructure - `[x]`

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 1 | Create GitHub monorepo with branch protection | P0 | B | 30m | — | Main + dev branches; PR required for main |
| 2 | Configure GitHub Actions CI (lint, typecheck, build) | P0 | B | 1h | #1 | CI passes on PR to main |
| 3 | Write docker-compose.yml (Kafka, Neo4j, Qdrant, Redis, InfluxDB, MinIO, PostgreSQL) | P0 | B | 2h | — | `docker-compose up` starts all services |
| 4 | Configure resource limits in docker-compose | P1 | B | 30m | #3 | No container OOM during demo |
| 5 | Set up Docker network + volume persistence | P1 | B | 30m | #3 | Data survives container restart |
| 6 | Create .env.example with all configuration templates | P1 | B | 30m | — | All secrets documented, none committed |

### P0-BAC Backend - `[x]`

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 7 | FastAPI application skeleton with directory structure | P0 | B | 1h | — | `uvicorn app.main:app` starts, health endpoint returns 200 |
| 8 | Pydantic models for SHELDRA request/response schemas | P0 | B | 1.5h | #7 | Models validate: worker_id, message, context, trace_id |
| 9 | WebSocket manager for real-time streaming | P0 | B | 1.5h | #7 | Client connects to /ws, receives messages |
| 10 | Redis connection manager (singleton pool) | P0 | B | 1h | #7, Redis | `redis.ping()` succeeds |
| 11 | Kafka producer/consumer base classes | P0 | B | 1.5h | #7, Kafka | Produce + consume typed messages |
| 12 | Kafka topic setup script (sheldra.interactions, decision.trees, sensor.readings, vision.detections, worker.profiles, system.alerts) | P1 | B | 1h | #11 | All topics created with schema registry |
| 13 | OpenAPI 3.0 specification (single endpoint: /api/v1/sheldra/chat) | P0 | B+C | 1.5h | — | Spec validated; TypeScript client generated |

### P0-FE Frontend - `[x]`

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 14 | Next.js 14 scaffold with App Router + TypeScript | P0 | C | 1h | — | `npm run dev` starts; page renders |
| 15 | Tailwind CSS + shadcn/ui component library | P0 | C | 30m | #14 | Buttons, cards, inputs render correctly |
| 16 | React Three Fiber setup + basic scene | P0 | C | 1.5h | #14 | 3D cube renders with orbit controls |
| 17 | WebSocket client hook (useWebSocket.ts) | P0 | C | 1h | #14 | Connects to /ws, receives JSON messages |
| 18 | Dashboard layout shell: sidebar + main panel + context panel | P0 | C | 1.5h | #14 | Three-column layout renders |
| 19 | Dark mode theme (control room optimized) | P1 | C | 30m | #14 | Toggle works; all components support dark |

### P0-KG Knowledge Graph

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 20 | Neo4j schema script: Node labels Worker, Hazard, DecisionTree, Incident, SafetyRule, Procedure, SHELDRASession, Zone, Equipment | P0 | B | 1.5h | Neo4j | All node types creatable with properties |
| 21 | Edge types: HAS_PROFILE, GUIDED_BY, ABOUT, RESOLVED_VIA, REQUIRES, TRIGGERED_BY, LOCATED_IN, MONITORED_BY | P0 | B | 1h | #20 | All edge types creatable with properties |
| 22 | Seed script: 3 workers (novice, experienced, expert) with profiles | P0 | B | 1h | #20 | `MATCH (w:Worker) RETURN w` returns 3 |
| 23 | Seed script: 5 zones, 10 equipment, 10 safety rules | P0 | B | 1.5h | #20 | Graph has complete seed data |
| 24 | Neo4j Python driver connection manager | P0 | B | 1h | #20 | `neo4j.query("RETURN 1")` succeeds |

### P0-DAT Data Generators

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 25 | IoT sensor simulator (temp, vibration, gas, noise) with anomaly injection | P0 | A | 2h | — | Produces to Kafka `sensor.readings`; anomalies every 5-10 min |
| 26 | Camera frame simulator (augmented COCO images with PPE annotations) | P0 | A | 2h | — | Produces frames with bounding boxes to vision pipeline |
| 27 | Safety procedure PDFs (3-5 documents with sections, steps, citations) | P1 | B | 1h | — | PDFs readable; text extractable |

---

## Phase 1 — SHELDRA Intelligence Engine

### P1-ORC Event Orchestrator

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 28 | EventOrchestrator base class with module registry | P0 | B | 2h | #7 | Modules register with {name, capabilities, handler} |
| 29 | Request lifecycle: validate → route → execute → collect → respond | P0 | B | 1.5h | #28 | Inbound event passed through lifecycle; response returned |
| 30 | Trace ID generation and propagation | P0 | B | 1h | #28 | Every log line includes trace_id |
| 31 | Module timeout handling (default: 5s per module) | P1 | B | 1h | #28 | Module exceeding timeout returns partial result |
| 32 | Graceful degradation: module failure → log + continue | P1 | B | 1h | #28 | Engine works with degraded module set |
| 33 | Event type routing table (chat, sensor_alert, vision_detection, tree_update) | P0 | B | 1h | #28 | Each event type routes to correct modules |

### P1-LLM LLM Reasoning Core

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 34 | Ollama setup with Llama 3 8B | P0 | A | 2h | — | `ollama run llama3` responds to prompts |
| 35 | System prompt design: SHELDRA persona, guardrails, response format | P0 | A | 1.5h | #34 | Prompt produces structured JSON output |
| 36 | Context injection template: {profile, observations, history, knowledge} → prompt | P0 | A | 1.5h | #35 | All context fields appear in prompt |
| 37 | Structured output parser: extract {message, tone, gesture, confidence, citations} from LLM response | P0 | A | 1h | #36 | Parser handles edge cases; defaults on failure |
| 38 | Streaming response via async generator | P1 | A | 1.5h | #37 | Client receives incremental tokens |
| 39 | LLM fallback: timeout → cached response | P1 | A | 1h | #34 | Engine returns cached response if LLM > 5s |

### P1-MEM Memory Manager

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 40 | Short-term memory: Redis session store (TTL: 30min) | P0 | B | 1h | Redis | Worker session persists across requests |
| 41 | Conversation history buffer (last 20 exchanges per session) | P0 | B | 1h | #40 | Retrieved conversations include metadata |
| 42 | Long-term memory: KG query for worker interaction history | P1 | B | 1.5h | KG Manager | `MATCH (w:Worker)-[:GUIDED_BY]->(s:SHELDRASession)` returns ordered |
| 43 | Context window assembly: short + long → prioritized context | P1 | B | 1h | #41, #42 | Context fits token limit; recent first |
| 44 | Memory eviction policy (LRU on size, TTL on stale) | P2 | B | 1h | #40 | Memory usage bounded to configurable limit |

### P1-KGM Knowledge Graph Manager

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 45 | Cypher query builder class (parameterized, injection-safe) | P0 | B | 1.5h | Neo4j | All queries use parameters, not string interpolation |
| 46 | Worker CRUD: create, read, update worker node + profile | P0 | B | 1.5h | #20 | Worker created with all properties |
| 47 | Session CRUD: log SHELDRA interaction as graph node | P0 | B | 1h | #20 | Every SHELDRA response creates SHELDRASession node |
| 48 | Hazard queries: get hazards by zone, type, severity | P1 | B | 1h | #20 | Returns ranked hazard list |
| 49 | Temporal graph query: "state as of 10 minutes ago" | P2 | B | 1.5h | #20 | Query with timestamp filter returns correct snapshot |
| 50 | Graph query cache (Redis, TTL 30s, invalidated on write) | P2 | B | 1h | #45, Redis | Cache hit returns < 5ms; miss queries Neo4j |

### P1-PER Personalization Engine

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 51 | Profile loader: worker_id → KG query → Profile object | P0 | A | 1h | #46 | Profile object has all adaptation fields |
| 52 | Content depth computation: (experience + learning_speed + certs) → depth level 1-5 | P0 | A | 1.5h | #51 | Novice = level 5; expert = level 1 |
| 53 | Tone selection: normal, calm (stressed), urgent (high risk), praise (compliant) | P1 | A | 1h | #51 | Tone matches emotional state + risk level |
| 54 | Vocabulary adaptation: technical level matches worker expertise | P1 | A | 1h | #51 | Novice gets plain language; expert gets domain terms |
| 55 | Feedback style: gentle (first offense) → firm (repeat) → escalate (persistent) | P1 | A | 1h | #51 | Escalation triggered after 3 same-type violations |
| 56 | Profile → prompt augmentation: inject adaptation parameters into LLM context | P0 | A | 1h | #52, #53, #54, LLM Core | LLM prompt includes adaptation instructions |

### P1-RAG RAG Engine

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 57 | PDF text extraction (pdfplumber) + chunking (512 chars, 50 overlap) | P0 | B | 1h | #27 | Chunks preserve section headers; overlap handles boundary |
| 58 | Embedding service: E5-mistral-7b via ONNX Runtime | P0 | B | 2h | — | Embedding of single text returns 4096-dim vector in < 500ms |
| 59 | Qdrant collection setup with hybrid search (dense + BM25) | P0 | B | 1h | #58, Qdrant | Search returns top-3 chunks with scores |
| 60 | Document ingestion pipeline: PDF path → chunks → embed → store | P1 | B | 1h | #57, #58, #59 | 5 documents ingested; collection has 100+ chunks |
| 61 | Retrieval: query → hybrid search → re-rank (cross-encoder) → top 3 | P1 | B | 1.5h | #59 | Re-ranked results are more relevant than raw search |
| 62 | Citation tracking: source document, section, page for each chunk | P1 | B | 30m | #57 | Retrieved chunks include provenance metadata |

### P1-GRD Safety Guardrails

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 63 | Constraint rule engine: regex + keyword patterns for prohibited outputs | P1 | A | 1h | — | Rule violations trigger rejection |
| 64 | Confidence threshold: reject responses with composite confidence < 0.5 | P1 | A | 30m | Explainability Engine | Low-confidence responses replaced with escalation |
| 65 | Procedure contradiction check: LLM output vs. retrieved RAG context | P2 | A | 1.5h | RAG Engine | If output contradicts RAG context, reject + log |
| 66 | Audit log writer: every output + guardrail decision → Kafka topic + PostgreSQL | P1 | B | 1h | Kafka, PostgreSQL | Audit log queryable by trace_id, worker_id, timestamp |

### P1-XAI Explainability Engine

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 67 | Trace collector: hook into EventOrchestrator lifecycle to collect module decisions | P0 | A | 1.5h | EventOrchestrator | Trace object contains module name, input, output, latency for each step |
| 68 | Natural language explanation generator (template-based): "Vision Agent detected X. Compliance Agent identified violation of Rule Y. Decision: Z." | P1 | A | 1h | #67 | Template fills with actual trace data |
| 69 | Confidence provenance: model score * context relevance * history accuracy → composite | P1 | A | 1h | #67 | Composite confidence is explanatory, not opaque |
| 70 | SHAP integration: pre-computed feature attribution per detection class | P2 | A | 2h | Vision Intelligence | Vision decisions include pixel importance overlay |
| 71 | Trace visualization API: GET /api/v1/sheldra/trace/{trace_id} | P1 | B | 1h | #67 | Returns full trace as JSON |

### P1-DEC Decision Tree Engine

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 72 | Tree data model: JSON schema (tree_id, hazard_type, version, nodes[], edges[], root_id) | P0 | B | 1.5h | — | Schema validates all tree structures |
| 73 | Tree generator: hazard type → KG query for rules + procedures → build node graph | P0 | B | 2h | KG Manager, RAG | Generated tree has valid paths from root to leaf |
| 74 | 5 pre-built trees for demo (PPE violation, gas leak, equipment anomaly, fire, confined space) | P0 | A+B | 2h | #72 | Each tree manually verified for correctness |
| 75 | Branch accuracy scorer: outcome → node update → rolling 10-trial score | P0 | B | 1.5h | #72 | Score updates persist to KG |
| 76 | 5-minute update cycle daemon: score → prune → regenerate → version | P1 | B | 2h | #75 | Tree version increments; change log available |
| 77 | Tree versioning: new version on every update; rollback to any prior version | P1 | B | 1h | #76 | Rollback restores previous tree state |
| 78 | Tree → SHELDRA integration: tree output feeds LLM context | P1 | A+B | 1.5h | #73, LLM Core | Tree path included in SHELDRA's prompt context |

---

## Phase 2 — Perception Modules

### P2-VIS Vision Intelligence

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 79 | YOLOv8n ONNX export + inference server (FastAPI + ONNX Runtime) | P0 | A | 2h | — | Inference < 30ms per frame on CPU |
| 80 | Frame ingestion: Kafka topic → frame buffer (bounded queue, 100 frames) | P0 | A | 1.5h | Kafka | Backpressure: old frames dropped when buffer full |
| 81 | PPE detection: 6 classes (helmet, vest, gloves, goggles, harness, shoes) → structured event | P0 | A | 1.5h | #79 | Event: {worker_id, missing_items: [], confidence, timestamp} |
| 82 | Zone encroachment: polygon ROI defined per zone → IoU with person bbox | P0 | A | 1.5h | #79 | Event: {worker_id, zone, encroachment_type, timestamp} |
| 83 | Pose estimation (RTMPose) → behavior rules (reaching angle, climbing, fall detection) | P1 | A | 2h | #79 | Fall detection: velocity downward > threshold triggers event |
| 84 | Person tracking (ByteTrack): persist worker ID across frames | P1 | A | 1.5h | #79 | Same worker maintains ID for > 100 frames |
| 85 | Vision events → Kafka `vision.detections` → EventOrchestrator | P0 | A | 1h | #81, Kafka | EventOrchestrator receives detection events |

### P2-MON Monitoring Intelligence

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 86 | TimesNet ONNX export + inference server | P0 | A | 2h | — | Inference < 100ms per 60-point window |
| 87 | Sliding window buffer (60s, 1 reading/s) per sensor | P0 | A | 1h | Kafka | Buffer maintained for each sensor ID |
| 88 | Anomaly scorer: reconstruction error → normalized anomaly score (0-1) | P0 | A | 1h | #86 | Normal sensor: score < 0.3; anomaly: score > 0.7 |
| 89 | Multi-sensor correlation: joint reconstruction error across (temp + vibration + gas) | P1 | A | 1.5h | #88 | Correlated anomaly score > 0.8 triggers compound alert |
| 90 | Adaptive threshold: time-of-day baseline (shift pattern) | P2 | A | 1.5h | #88 | Night shift baseline differs from day shift |
| 91 | Anomaly event → Kafka `system.alerts` → EventOrchestrator | P0 | A | 1h | #88, Kafka | EventOrchestrator receives anomaly events |
| 92 | Alert suppression: debounce 30s per sensor to prevent storms | P2 | A | 1h | #88 | No duplicate alerts within 30s window |

---

## Phase 3 — Interface & Integration

### P3-DSH Dashboard

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 93 | Main layout: SHELDRA panel (40%) + conversation (40%) + context sidebar (20%) | P0 | C | 2h | #18 | Three flexible panels resize correctly |
| 94 | SHELDRA 3D avatar component (R3F) with idle animation | P0 | C | 3h | #16 | Avatar renders with floating animation |
| 95 | Conversation panel: streaming text display + message history | P1 | C | 1.5h | #17, API | Messages appear in real-time; scroll follows latest |
| 96 | Context panel: current worker card, active hazard, environment status | P1 | C | 1h | API | All fields populate from API response |
| 97 | Decision Tree flow chart (React Flow): DAG with color-coded nodes | P1 | C | 2.5h | API, React Flow | Nodes: green (safe), yellow (caution), red (hazard), blue (resolved) |
| 98 | Accuracy dashboard: tree accuracy trend line, branch breakdown, version history | P2 | C | 2h | API | Chart updates every 5 min; interactive filter |
| 99 | SHELDRA interaction feed: scrolling log of all coaching moments | P2 | C | 1h | #17 | Feed shows timestamp, worker, hazard, action, outcome |

### P3-SUP Supervisor Console

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 100 | Alert queue: severity-sorted list with acknowledge/dismiss/escalate | P1 | C | 1.5h | API | Queue updates in real-time via WebSocket |
| 101 | Override panel: modify or cancel SHELDRA recommendation | P1 | C | 1.5h | #100 | Override logged with reason + supervisor ID |
| 102 | Audit log viewer: search by worker, hazard, time range | P2 | C | 1h | API | Results paginated; exportable to CSV |
| 103 | Shift handover summary: active hazards, unresolved alerts, worker status | P2 | C | 1.5h | API | Summary generated on demand |

### P3-AVT Avatar

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 104 | Gesture system: pointing, nodding, warning stance, hands-free | P1 | C | 2h | #94 | Gestures trigger from LLM response field `gesture` |
| 105 | Lip-sync: audio waveform → viseme animation | P1 | C | 1.5h | #94, Voice TTS | Lip movement matches spoken audio |
| 106 | Emotion expression: calm/warm/urgent facial expressions | P2 | C | 1.5h | #94 | Expression changes with LLM response field `tone` |
| 107 | Holographic shader: scan lines, glow, translucency | P2 | C | 2h | #94 | Visual effect suggests holographic projection |
| 108 | Mobile responsive: avatar adapts to screen size (full → thumbnail) | P2 | C | 1h | #94 | Avatar visible on mobile without layout break |
| 109 | 2D fallback (Lottie animation) if 3D performance insufficient | P2 | C | 1h | — | Identical behavior; same gesture/voice system |

### P3-VCE Voice I/O

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 110 | Speech-to-text: browser microphone → Whisper API → text | P1 | C | 2h | — | Speech recognized with < 2s latency |
| 111 | Text-to-speech: SHELDRA response → ElevenLabs/Coqui → audio playback | P1 | C | 1.5h | LLM Core | Audio plays; voice matches SHELDRA persona |
| 112 | Voice activity detection (VAD): detect when user stops speaking | P2 | C | 1h | #110 | Recording stops automatically on silence |
| 113 | Caption overlay: text displayed during audio playback | P2 | C | 30m | #111 | Captions synchronized with audio |
| 114 | Push-to-talk button (voice chat fallback) | P2 | C | 30m | #110 | Button toggles recording |

### P3-VR VR Training

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 115 | A-Frame / Three.js XR scene: factory floor with equipment | P2 | C | 3h | — | Scene loads; user navigates with keyboard/mouse |
| 116 | SHELDRA avatar in VR scene | P2 | C | 1.5h | #115, Avatar | Avatar renders in VR; gestures work |
| 117 | Hazard simulation: gas leak visual + audio cues | P2 | C | 1.5h | #115 | Hazard triggers on schedule or button |
| 118 | VR training flow: SHELDRA introduces → hazard triggers → worker responds → SHELDRA scores | P2 | C | 2h | #116, #117 | Score calculated: reaction time + decision accuracy + procedure adherence |
| 119 | Score → worker profile update (KG) | P2 | C | 1h | #118, KG Manager | Profile reflects latest training score |

### P3-DPL Deployment

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 120 | Multi-stage Dockerfiles: FastAPI, Next.js, ONNX servers, RAG, Decision Tree | P0 | B | 2h | Phase 1 artifacts | Images build; sizes < 2GB each |
| 121 | docker-compose.prod.yml: resource limits, restart policies, health checks | P1 | B | 1h | #120 | `docker-compose -f prod.yml up` starts all services |
| 122 | Cloud deployment (AWS ECS Fargate): backend services | P1 | B | 2h | #121 | All services healthy; load balancer configured |
| 123 | Cloud deployment (Vercel): frontend | P1 | C | 1h | #14 | Dashboard accessible at custom domain |
| 124 | SSL certificate + domain configuration | P2 | B | 30m | #122 | HTTPS enforced; auto-renew configured |
| 125 | Load test (k6): 100 concurrent sessions, 10 req/s each | P2 | B | 1h | #121 | p95 latency < 5s; no errors |

### P3-TST Testing

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 126 | Unit tests: EventOrchestrator module routing | P1 | B | 1.5h | #28, #29, #30 | 90%+ coverage on routing logic |
| 127 | Unit tests: Decision Tree accuracy scorer | P1 | B | 1h | #75 | Scorer handles success, failure, partial outcomes |
| 128 | Unit tests: Personalization Engine adaptation dimensions | P1 | A | 1h | #51-55 | All 3 profiles produce different adaptation output |
| 129 | Integration test: vision detection → SHELDRA response (end-to-end) | P1 | A+B | 1.5h | Phase 2 complete | Detection event triggers SHELDRA feedback |
| 130 | Integration test: anomaly → Decision Tree update → tree version increment | P1 | B | 1.5h | Phase 2 complete | Tree version increases after anomaly resolution |
| 131 | Integration test: WebSocket streaming response | P1 | B+C | 1h | #38, #17 | Client receives streaming tokens with < 500ms first token |

### P3-DMO Demo

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 132 | Demo script: 5-minute walkthrough (8 segments) | P0 | All | 2h | All complete | Script covers all judging criteria |
| 133 | Demo recording (OBS): backup in case of live failure | P0 | All | 1h | #132 | 1080p recording with clear audio |
| 134 | Rehearsal #1: dry run with timer | P0 | All | 1h | #132 | Each segment within time allocation |
| 135 | Rehearsal #2: full run with QA simulation | P1 | All | 1h | #134 | Team answers prepared for likely judge questions |
| 136 | Rehearsal #3: disaster recovery (kill switch, reset state) | P1 | All | 1h | #122 | Full system reset in < 60s; demo restarts clean |

### P3-DOC Documentation

| # | Task | Pri | Owner | Time | Deps | Acceptance Criteria |
|---|------|-----|-------|------|------|-------------------|
| 137 | Architecture document (Word): 26 sections | P0 | All | 4h | — | All sections complete; diagrams included |
| 138 | API documentation (auto-generated from OpenAPI spec) | P1 | B | 30m | #13 | Swagger UI at /docs |
| 139 | README.md: project overview, setup instructions, architecture one-pager | P1 | B | 1h | — | Clear enough for new developer to set up in 15 min |

---

## Summary

| Phase | Tasks | P0 | P1 | P2 | P3 | Total Hours |
|-------|-------|----|----|----|----|-------------|
| Phase 0 | 1-27 | 16 | 8 | 3 | 0 | ~34h |
| Phase 1 | 28-78 | 22 | 22 | 7 | 0 | ~62h |
| Phase 2 | 79-92 | 8 | 4 | 2 | 0 | ~20h |
| Phase 3 | 93-139 | 8 | 18 | 16 | 5 | ~62h |
| **Total** | **139** | **54** | **52** | **28** | **5** | **~178h** |
