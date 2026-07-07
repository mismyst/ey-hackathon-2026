# Industrial Safety Intelligence Platform — Task Tracker

> Legend: `[ ]` Pending · `[~]` In Progress · `[x]` Done
> Priority: 🔴 P0 · 🟡 P1 · 🟢 P2 · ⚪ P3

---

## Phase 0: Foundation (Pre-Hackathon)

### Infrastructure (B)
- [ ] 🔴 Create GitHub monorepo with branch protection
- [ ] 🔴 Set up AWS/GCP accounts, IAM roles, and credit limits
- [ ] 🔴 Write `docker-compose.yml` for local services (Kafka, Neo4j, Qdrant, Redis, MinIO)
- [ ] 🟡 Configure GitHub Actions CI (lint, typecheck, build)
- [ ] 🟡 Set up Terraform or Pulumi for cloud infra-as-code
- [ ] 🟢 Create `.env.example` with all config templates

### AI/ML Setup (A)
- [ ] 🔴 Download YOLOv8n/v8s pretrained weights (PPE + person detection)
- [ ] 🔴 Download TimesNet / PatchTST pretrained checkpoint
- [ ] 🔴 Set up synthetic data generator: COCO-style PPE images (blender or augmentation)
- [ ] 🟡 Set up ONNX runtime for edge-optimized inference
- [ ] 🟡 Create model registry structure (MLflow or local)

### Frontend Setup (C)
- [ ] 🔴 Scaffold Next.js 14 with App Router + TypeScript
- [ ] 🔴 Set up Three.js with React Three Fiber
- [ ] 🔴 Configure Tailwind CSS + shadcn/ui component library
- [ ] 🟡 Set up WebSocket client library (Socket.io or native WS)
- [ ] 🟢 Create basic layout shell (sidebar, topbar, main content)

### API Contracts (B + C)
- [ ] 🔴 Define OpenAPI 3.0 spec for all endpoints
- [ ] 🔴 Set up FastAPI application skeleton with routers
- [ ] 🟡 Generate TypeScript client from OpenAPI spec
- [ ] 🟡 Set up Pydantic models matching database schema

---

## Phase 1: Core MVP — The Differentiator (Day 1)

### Multi-Agent System (A + B)

#### Agent Framework (B)
- [x] 🔴 [DONE - DESIGN] Define Agent base class with lifecycle (init → observe → reason → act → report)
- [x] 🔴 [DONE - DESIGN] Define message protocol: `{agent_id, target_id, message_type, payload, timestamp, trace_id}`
- [ ] 🔴 Implement Orchestrator Agent with state machine
- [ ] 🔴 Implement agent registry (agents register with capabilities)
- [ ] 🔴 Implement inter-agent communication via Redis Pub/Sub
- [ ] 🟡 Implement shared context store (Redis) for cross-agent state
- [ ] 🟡 Implement trace logging for every agent decision
- [ ] 🟢 Build agent health-check endpoint

#### Vision Agent (A)
- [ ] 🔴 Implement frame ingestion from simulated RTSP stream
- [ ] 🔴 Implement YOLOv8 inference pipeline (PPE: helmet, vest, gloves, goggles)
- [ ] 🔴 Implement zone encroachment logic (polygon-based ROI)
- [ ] 🟡 Implement unsafe behavior detection (pose keypoints → rule engine)
- [ ] 🟡 Convert detection events → agent messages
- [ ] 🟡 Implement confidence threshold filtering
- [ ] 🟢 Person tracking across frames (simple IoU tracking)

#### Monitoring Agent (A)
- [ ] 🔴 Implement TimesNet inference for anomaly scoring
- [ ] 🔴 Implement sliding window (60s) on streaming sensor data
- [ ] 🟡 Implement multi-sensor correlation anomaly
- [ ] 🟡 Implement adaptive thresholding (moving baseline)
- [ ] 🟡 Convert anomaly scores → agent messages with severity

#### Compliance Agent (B)
- [ ] 🔴 Implement Cypher query builder for safety rules
- [ ] 🔴 Implement rule-matching engine (current graph state vs. violation patterns)
- [ ] 🟡 Implement regulatory reference lookup via RAG
- [ ] 🟡 Implement severity scoring based on violation type + history

#### Response Agent (B)
- [ ] 🔴 Implement action template system (evacuate, alert, shutdown, log)
- [ ] 🔴 Implement action execution with confirmation step
- [ ] 🟡 Implement escalation logic (if no supervisor response in T seconds)
- [ ] 🟢 Integrate with Twilio/email for external alerts

#### Explanation Agent (A)
- [ ] 🔴 Implement decision trace collector (gathers reasoning from all agents)
- [ ] 🔴 Implement natural language explanation generator
- [ ] 🟡 Implement confidence provenance (model scores + context relevance)
- [ ] 🟡 Implement counterfactual explanation (what would change this decision?)

### Computer Vision Pipeline (A)
- [ ] 🔴 Set up video frame extractor at configurable FPS
- [ ] 🔴 Implement PPE class detection with bounding box overlay
- [ ] 🔴 Implement worker-camera calibration (mapping 2D detections → 3D zones)
- [ ] 🟡 Implement queue-based frame processing (avoid backpressure)
- [ ] 🟢 Implement alert-on-missing-PPE logic
- [ ] 🟢 Implement dashboard bounding box streaming

### Knowledge Graph (B)
- [ ] 🔴 Define Neo4j node labels: `Worker`, `Zone`, `Equipment`, `Incident`, `SafetyRule`, `Procedure`, `Sensor`
- [ ] 🔴 Define Neo4j edge types: `OPERATES_IN`, `ASSIGNED_TO`, `LOCATED_IN`, `TRIGGERED_BY`, `VIOLATES`, `MITIGATES`, `MONITORED_BY`
- [ ] 🔴 Seed graph with synthetic factory data (20 workers, 5 zones, 10 machines)
- [ ] 🔴 Implement `createIncident` mutation (event → graph node + edges)
- [ ] 🟡 Implement graph query API for Compliance Agent
- [ ] 🟡 Implement temporal graph queries (what changed in last hour?)
- [ ] 🟢 Implement GraphQL wrapper over Neo4j (optional)

### Real-Time Ingestion (B)
- [ ] 🔴 Configure Kafka topics: `sensor.readings`, `vision.events`, `agent.messages`, `system.alerts`
- [ ] 🔴 Implement IoT sensor simulator (Python: temp, vibration, gas, noise, humidity)
- [ ] 🔴 Implement Kafka producer for simulated data
- [ ] 🟡 Implement Kafka consumer → agent event bridge
- [ ] 🟡 Implement schema registry with Avro/Protobuf
- [ ] 🟢 Implement Flink/KSQL for windowed aggregates (5min avg, min, max)

---

## Phase 2: Intelligence Layer (Day 2)

### RAG Pipeline (B + A)
- [ ] 🟡 Collect 3-5 safety procedure PDFs (OSHA-style synthetic)
- [ ] 🟡 Implement PDF chunking with overlap (LangChain or custom)
- [ ] 🟡 Implement embedding pipeline with E5-mistral-7b or BGE-large
- [ ] 🟡 Set up Qdrant with hybrid search (dense + sparse BM25)
- [ ] 🟡 Connect RAG query to Compliance Agent
- [ ] 🟢 Implement citation-grounded response formatting
- [ ] 🟢 Implement "I don't know" fallback for low-confidence queries

### Time-Series Anomaly (A)
- [ ] 🟡 Train/calibrate TimesNet on synthetic normal data
- [ ] 🟡 Implement real-time inference server (Triton or custom FastAPI)
- [ ] 🟡 Implement anomaly alert suppression (debounce to avoid alert storms)
- [ ] 🟡 Implement root-cause correlation (which sensor is most anomalous?)
- [ ] 🟢 Implement time-series dashboard charts (line + anomaly highlights)

### Digital Twin (C)
- [ ] 🟡 Create 3D factory layout (floor, walls, equipment placeholders)
- [ ] 🟡 Implement real-time state sync via WebSocket (equipment on/off, worker positions)
- [ ] 🟡 Implement equipment status overlays (color-coded: normal/warning/critical)
- [ ] 🟡 Implement incident heatmap overlay (zones colored by risk score)
- [ ] 🟢 Implement camera frustum visualization (which camera covers which zone)
- [ ] 🟢 Implement zoom-to-incident animation on alert
- [ ] 🟢 Mobile-responsive 3D view (orbit controls)

---

## Phase 3: Integration & Polish (Day 3)

### Human-in-the-Loop (C)
- [ ] 🟢 Implement alert queue with priority sorting
- [ ] 🟢 Implement acknowledge / dismiss / escalate buttons
- [ ] 🟢 Implement supervisor override mechanism (override AI decision)
- [ ] 🟢 Implement audit trail for all HITL actions
- [ ] 🟢 Implement shift handover summary
- [ ] ⚪ Implement supervisor note attachment

### Explainable AI (A + C)
- [ ] 🟢 Implement SHAP summary for vision model decisions
- [ ] 🟢 Implement agent decision trace visualizer (timeline of agent reasoning)
- [ ] 🟢 Implement confidence gauge per prediction
- [ ] 🟢 Implement "Why this alert?" panel (natural language + evidence)
- [ ] ⚪ Implement counterfactual explorer ("what if worker wore helmet?")

### Emergency Response Workflow (B + C)
- [ ] 🔴 Implement automated response triggers (pre-built action plans)
- [ ] 🟡 Implement escalation ladder: worker → supervisor → manager → director
- [ ] 🟡 Implement multi-channel alerting: WebSocket push → email (SendGrid) → SMS (Twilio)
- [ ] 🟡 Implement post-incident report generator (PDF with timeline + evidence)
- [ ] 🟢 Implement incident playback (replay timeline of events)

### Dashboard Completion (C)
- [ ] 🔴 Implement real-time safety score (0-100) with trend line
- [ ] 🔴 Implement agent activity feed (streaming log of agent actions)
- [ ] 🟡 Implement Knowledge Graph explorer (force-directed graph visualization)
- [ ] 🟡 Implement incident timeline (chronological + filterable)
- [ ] 🟡 Implement worker shift view (who is where, PPE compliance %)
- [ ] 🟢 Implement dark mode toggle
- [ ] 🟢 Implement responsive layout (mobile PWA)

### Deployment (B)
- [ ] 🟡 Write Dockerfiles for all services (optimized multi-stage)
- [ ] 🟡 Write `docker-compose.prod.yml` with resource limits
- [ ] 🟡 Deploy to AWS ECS Fargate or GCP Cloud Run
- [ ] 🟡 Set up CloudFront / CDN for frontend assets
- [ ] 🟡 Set up domain + SSL (Let's Encrypt or Cloudflare)
- [ ] 🟡 Configure logging (CloudWatch / GCP Logging)
- [ ] 🟢 Load test with k6 (1000 events/sec sustained)
- [ ] 🟢 Set up auto-scaling policies

---

## Phase 4: Presentation Prep (Last 4h)

### Demo Flow (All)
- [ ] 🔴 Script 5-min demo walkthrough (problem → solution → live demo → impact)
- [ ] 🔴 Rehearse demo 3x with timer
- [ ] 🔴 Record backup demo video (in case live fails)
- [ ] 🟡 Prepare "easter eggs" for judge questions (hard-coded impressive scenarios)
- [ ] 🟡 Prepare disaster recovery: offline demo mode without cloud

### Slides (C)
- [ ] 🟡 Finalize slide deck (10 slides max)
- [ ] 🟡 Include architecture diagram
- [ ] 🟡 Include live demo screenshots as fallback
- [ ] 🟡 Prepare Q&A cheat sheet for each team member

---

## Quick Reference: Daily Standup Questions

Each morning, answer:
1. What did I complete yesterday?
2. What am I working on today?
3. What blockers do I have?
4. What integration points need coordination?

---

## File Map

```
/
├── frontend/          # Next.js dashboard + Digital Twin (C)
├── backend/
│   ├── agents/        # Multi-agent system (A + B)
│   ├── ingestion/     # Kafka producers, consumers (B)
│   ├── models/        # CV, Time-series inference (A)
│   ├── knowledge-graph/ # Neo4j schema + queries (B)
│   └── rag/           # Document ingestion + retrieval (B)
├── infra/             # Docker, Terraform, CI/CD (B)
├── data/              # Synthetic data, sample docs
└── docs/              # Architecture, API specs
```
