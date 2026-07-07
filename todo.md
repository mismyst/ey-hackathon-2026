# SHELDRA — Industrial Safety Intelligence Platform Task Tracker

> Legend: `[ ]` Pending · `[~]` In Progress · `[x]` Done
> Priority: 🔴 P0 · 🟡 P1 · 🟢 P2 · ⚪ P3

---

## Phase 0: Foundation (Pre-Hackathon)

### SHELDRA Identity & Design (All)
- [ ] 🔴 Name/backstory: "Safety Holographic Enhanced Learning & Decision-Reality Assistant"
- [ ] 🔴 SHELDRA visual identity: color palette, avatar style (futuristic but trustworthy)
- [ ] 🟡 SHELDRA voice profile: tone (calm, authoritative, encouraging)
- [ ] 🟡 SHELDRA personality guardrails: never alarm, always explain, redirect not reprimand

### Infrastructure (B)
- [ ] 🔴 Create GitHub monorepo with branch protection
- [ ] 🔴 Set up AWS/GCP accounts, IAM roles, and credit limits
- [ ] 🔴 Write `docker-compose.yml` for local services (Kafka, Neo4j, Qdrant, Redis, MinIO)
- [ ] 🟡 Configure GitHub Actions CI (lint, typecheck, build)
- [ ] 🟢 Create `.env.example` with all config templates

### AI/ML Setup (A)
- [ ] 🔴 Research SHELDRA LLM baseline (Llama 3 8B, fine-tuning scope)
- [ ] 🔴 Set up worker profile schema (experience, learning_speed, language, certs, incident_history, interaction_history)
- [ ] 🔴 Set up synthetic worker profiles (3 levels: novice, experienced, expert)
- [ ] 🟡 Set up ONNX runtime for edge-optimized inference
- [ ] 🟡 Set up Whisper (STT) + ElevenLabs / Coqui (TTS) integration stubs
- [ ] 🟢 Collect/draft 5 safety procedure PDFs for SHELDRA's knowledge base

### Frontend Setup (C)
- [ ] 🔴 Scaffold Next.js 14 with App Router + TypeScript
- [ ] 🔴 Set up Three.js with React Three Fiber (R3F) for avatar rendering
- [ ] 🔴 Set up WebXR / A-Frame for VR scene (stretch)
- [ ] 🔴 Configure Tailwind CSS + shadcn/ui
- [ ] 🔴 Set up WebSocket client (Socket.io or native WS)
- [ ] 🟡 Set up react-speech-kit / Web Speech API for voice I/O
- [ ] 🟢 Create dashboard layout shell (SHELDRA main view, DT panel, sidebar)

### API Contracts (B + C)
- [ ] 🔴 Design SHELDRA API: `POST /api/v1/sheldra/chat` (context → response)
- [ ] 🔴 Design Decision Tree API: `GET /api/v1/decision-trees/{hazard_id}`
- [ ] 🔴 Design Worker Profile API: `GET/PUT /api/v1/workers/{id}`
- [ ] 🟡 Design Real-time update API: `WS /ws/sheldra/stream`
- [ ] 🟡 Set up FastAPI application skeleton with routers

### Knowledge Graph Schema (B)
- [ ] 🔴 Define `Worker` node (with profile properties)
- [ ] 🔴 Define `Hazard` node + `DecisionTree` node + `TreeNode` node
- [ ] 🔴 Define `SHELDRASession` node (interaction log)
- [ ] 🟡 Define edges: `HAS_PROFILE`, `EXPERIENCED`, `GUIDED_BY`, `RESOLVED_VIA`

---

## Phase 1: SHELDRA + Decision Tree Core (Day 1)

### SHELDRA Core AI (A)

#### LLM & Prompt Pipeline
- [ ] 🔴 Design SHELDRA system prompt: persona + guardrails + context injection template
- [ ] 🔴 Implement context assembly: Worker Profile + Current Observations + History + Hazard Context
- [ ] 🔴 Implement SHELDRA response pipeline: Context → Profile Augmentation → RAG Retrieval → Prompt Assembly → LLM → Response Parsing
- [ ] 🟡 Implement streaming response (SSE or WebSocket) for real-time chat feel
- [ ] 🟡 Implement "SHELDRA thinking" animation while generating (processing indicator)

#### Personalization Engine
- [ ] 🔴 Build profile → prompt augmentation: novice gets step-by-step, expert gets confirmation
- [ ] 🔴 Implement learning speed adaptation: detect if worker hesitates → simplify instructions
- [ ] 🟡 Implement language detection + response in worker's preferred language
- [ ] 🟡 Implement experience-aware feedback: adjust detail level based on certs + incident history
- [ ] 🟢 Implement personalization test: same hazard, 3 profiles → 3 different SHELDRA responses

#### Corrective Feedback
- [ ] 🔴 Implement feedback trigger from Vision Agent observations (e.g., "missing helmet")
- [ ] 🔴 Implement feedback templates: observation → impact → correction → confirmation
- [ ] 🟡 Implement graded feedback: gentle reminder → firm warning → escalate
- [ ] 🟢 Implement positive reinforcement: "Great job wearing your harness correctly!"

#### Emotional Awareness
- [ ] 🟡 Implement voice stress analysis (prosody features from STT)
- [ ] 🟡 Implement fatigue detection (response time, interaction patterns)
- [ ] 🟡 Adapt SHELDRA tone based on emotional state: stressed → calming, confused → clarifying
- [ ] 🟢 Log emotional state → worker profile for shift handover

### SHELDRA Holographic Avatar (C)

#### 3D Avatar
- [ ] 🔴 Implement R3F avatar scene with lighting + environment
- [ ] 🔴 Implement SHELDRA character model (Ready Player Me or custom geometric)
- [ ] 🔴 Implement idle animation loop (gentle floating/scanning)
- [ ] 🟡 Implement gesture system: pointing, nodding, warning stance, hands-free
- [ ] 🟡 Implement transition animations (appear, disappear, resize)
- [ ] 🟢 Implement responsive avatar size (full desktop, small mobile)

#### Lip-Sync & Voice
- [ ] 🔴 Integrate TTS service (ElevenLabs API or Coqui TTS local)
- [ ] 🔴 Implement lip-sync from audio waveform (viseme mapping or amplitude-based)
- [ ] 🟡 Implement voice activity indicator (subtle glow pulse)
- [ ] 🟢 Implement text captions below avatar (accessibility + noisy environment fallback)

#### UI Overlay
- [ ] 🔴 Implement SHELDRA speech bubble with streaming text
- [ ] 🔴 Implement context panel (current worker info, current hazard, environment status)
- [ ] 🟡 Implement SHELDRA "sight" visualization (what SHELDRA is currently observing)
- [ ] 🟡 Implement mini-map showing SHELDRA's position relative to factory floor
- [ ] 🟢 Implement "Ask SHELDRA" input box (text fallback for voice)

### Decision Tree Engine (B)

#### Data Model & Generation
- [ ] 🔴 Design JSON schema: `{ tree_id, hazard_type, version, nodes: [{ id, question, conditions, branches, action, accuracy }], edges, root_id }`
- [ ] 🔴 Implement tree generator: hazard type → query KG for related rules → build node graph
- [ ] 🔴 Implement tree serializer → API response
- [ ] 🟡 Implement tree versioning (v1, v2, v3 with accuracy deltas tracked)
- [ ] 🟢 Seed 3 pre-built trees for demo (gas leak, PPE violation, equipment anomaly)

#### 5-Minute Update Cycle
- [ ] 🔴 Implement incremental update daemon (cron / background worker every 300s)
- [ ] 🔴 Implement accuracy scorer: compare predicted hazard resolution → actual outcome
- [ ] 🔴 Implement branch pruning: remove branches with < 50% accuracy over last 10 evaluations
- [ ] 🟡 Implement new branch generation: detect patterns in incorrect resolutions → propose new branches
- [ ] 🟡 Implement A/B testing: serve old tree vs new tree to different workers
- [ ] 🟢 Implement update notification: "Decision Tree #7 updated — new branch added for gas leak escalation"

#### API
- [ ] 🔴 `GET /api/v1/decision-trees` — list all available trees
- [ ] 🔴 `GET /api/v1/decision-trees/{hazard_id}` — current tree for hazard
- [ ] 🔴 `GET /api/v1/decision-trees/{id}/history` — version history + accuracy deltas
- [ ] 🟡 `POST /api/v1/decision-trees/evaluate` — score a resolution path from SHELDRA interaction
- [ ] 🟢 `GET /api/v1/decision-trees/accuracy-dashboard` — aggregate accuracy metrics

### Decision Tree Visualization (C)

#### Flow Chart Renderer
- [ ] 🔴 Implement interactive DAG using React Flow
- [ ] 🔴 Implement color-coded nodes: safe (green), caution (yellow), hazard (red), resolved (blue)
- [ ] 🔴 Implement step-by-step walkthrough mode (highlight current node, animate path)
- [ ] 🟡 Implement click-to-expand nodes (show details, conditions, past resolutions)
- [ ] 🟡 Implement zoom + pan controls
- [ ] 🟢 Implement "Decision Tree updated" badge when new version available

#### Hazard Resolution Flow
- [ ] 🔴 Build demo overlay: SHELDRA guides → Decision Tree shows current position in tree
- [ ] 🟡 Implement tree comparison view: old tree vs new tree side-by-side
- [ ] 🟢 Implement export to PNG/PDF for compliance documentation

---

## Phase 2: Integration + Supporting Intelligence (Day 2)

### Multi-Agent System → Feeds SHELDRA (A + B)

#### Agent Framework (B)
- [ ] 🟡 Implement Agent base class + message protocol
- [ ] 🟡 Orchestrator Agent: routes all observations → SHELDRA context assembly
- [ ] 🟡 Implement agent-to-SHELDRA bridge (agent messages → SHELDRA awareness state)
- [ ] 🟢 Implement shared context store (Redis) for SHELDRA's world model

#### Vision Agent → SHELDRA Corrective Feedback (A)
- [ ] 🟡 PPE detection (YOLOv8) → SHELDRA: "Your safety glasses are on top of your helmet"
- [ ] 🟡 Zone encroachment → SHELDRA: "Please step back, this area requires confined space certification"
- [ ] 🟡 Unsafe behavior (pose) → SHELDRA: "Bend your knees, not your back, when lifting"
- [ ] 🟢 Frame capture → SHELDRA context (what SHELDRA "sees")

#### Monitoring Agent → Decision Tree Input (A)
- [ ] 🟡 TimesNet anomaly detection → Decision Tree trigger
- [ ] 🟡 Multi-sensor correlation → compound hazard detection → tree selection
- [ ] 🟢 Anomaly severity scoring → tree path weighting

#### Compliance Agent (B)
- [ ] 🟡 KG query: relevant safety rules for current context → SHELDRA guidance
- [ ] 🟡 Regulatory reference → Decision Tree branch condition

#### RAG Agent (A + B)
- [ ] 🟡 Embed safety procedure PDFs (E5-mistral-7b)
- [ ] 🟡 RAG retrieval → SHELDRA response grounding (citation-anchored)
- [ ] 🟡 "SHELDRA, show me the regulation" → citation display

#### Explanation Agent (A)
- [ ] 🟡 SHELDRA decision trace: "Why did you suggest evacuation?"
- [ ] 🟡 Collect evidence chain: observation → rule → recommendation
- [ ] 🟢 Display trace in SHELDRA UI panel

### Knowledge Graph → Personalization (B)
- [ ] 🟡 Worker profile: experience, certs, learning_speed, incident_history, language
- [ ] 🟡 SHELDRA interaction history: every coaching moment → `(Worker)-[:GUIDED_BY]->(SHELDRA)-[:ABOUT]->(Hazard)`
- [ ] 🟡 Hazard taxonomy: types, severity, frequency, related trees
- [ ] 🟢 Temporal query: "What has this worker learned in the last shift?"

### VR Training Integration (C + A)
- [ ] 🟡 SHELDRA avatar rendered in A-Frame / Three.js XR scene
- [ ] 🟡 Hazard simulation: visual + audio cues for gas leak, fire, equipment failure
- [ ] 🟡 SHELDRA guides worker through VR hazard scenario
- [ ] 🟡 Worker response scoring: reaction time, decision accuracy, procedure adherence
- [ ] 🟢 VR performance data → worker profile update
- [ ] 🟢 VR scene switching: normal operation → hazard → resolution

### Digital Twin (C)
- [ ] 🟢 Basic 3D factory layout
- [ ] 🟢 SHELDRA position indicator in Digital Twin (floating avatar marker)
- [ ] 🟢 Hazard highlight overlay (pulsing red for active hazard)
- [ ] 🟢 Camera feed thumbnail integration (what SHELDRA "sees")

---

## Phase 3: Polish + Accuracy Loop (Day 3)

### SHELDRA Refinement (A + C)

#### Emotion & Personality
- [ ] 🟢 Tone modulation: coaching mode (calm), warning mode (urgent), praise mode (warm)
- [ ] 🟢 Stress detection: adapt speech rate + simplicity based on worker stress
- [ ] 🟢 SHELDRA "memory": recalls past interactions with specific worker
- [ ] ⚪ Joke/icebreaker capability for high-stress de-escalation

#### Multi-Language (A)
- [ ] 🟢 SHELDRA in top 3 languages (English, Spanish, Mandarin)
- [ ] 🟢 Detect worker language from profile → switch automatically
- [ ] ⚪ Real-time translation for multilingual teams

#### Avatar Polish (C)
- [ ] 🟢 SHELDRA holographic shader effects (scan lines, glow, translucency)
- [ ] 🟢 Gesture-to-speech synchronization
- [ ] 🟢 Environmental responsiveness (avatar lighting matches scene)
- [ ] ⚪ AR wireframe overlays (HoloLens-style HUD concept)

### Decision Tree Accuracy Engine (B + A)

#### Metrics & Dashboard (B)
- [ ] 🟢 Accuracy dashboard: precision, recall, F1 per tree
- [ ] 🟢 Resolution success rate: how many hazards resolved correctly vs escalated
- [ ] 🟢 Update frequency tracking: how many trees updated in last 24h
- [ ] 🟢 Branch effectiveness ranking

#### Automated Improvement (A + B)
- [ ] 🟢 Tree pruning: remove <50% accuracy branches after 10 evaluations
- [ ] 🟢 New branch generation: analyze incorrect resolutions → propose new conditions
- [ ] 🟢 A/B test results visualization
- [ ] ⚪ Reinforcement learning from SHELDRA interaction outcomes

### Human-in-the-Loop (B + C)
- [ ] 🟢 Supervisor dashboard: monitor all SHELDRA interactions
- [ ] 🟢 Override SHELDRA recommendation (with reason logged)
- [ ] 🟢 SHELDRA audit log: searchable, filterable
- [ ] 🟢 Shift handover: SHELDRA generates shift summary
- [ ] ⚪ Supervisor note attachment to worker profile

### Real-Time Update Pipeline (B)
- [ ] 🔴 Kafka topics: `sheldra.interactions`, `decision.trees`, `worker.profiles`, `system.alerts`
- [ ] 🔴 5-minute Decision Tree refresh (Airflow DAG or cron)
- [ ] 🟡 Worker profile real-time sync (interaction → graph update → profile refresh)
- [ ] 🟡 Accuracy evaluation pipeline: hazard resolution → score → tree feedback
- [ ] 🟢 Schema registry for all topics

### Demo Dashboard (C)
- [ ] 🔴 Main view: SHELDRA avatar + conversation panel + context sidebar
- [ ] 🔴 Decision Tree panel side-by-side with SHELDRA (see coaching + tree simultaneously)
- [ ] 🔴 Worker profile selector (switch between novice/expert to show personalization)
- [ ] 🟡 "SHELDRA's View" panel (what SHELDRA is currently observing)
- [ ] 🟡 Accuracy real-time ticker (tree updated, accuracy improved)
- [ ] 🟢 Dark mode (control room optimized)
- [ ] 🟢 Mobile-responsive

### Deployment (B)
- [ ] 🟡 Dockerfiles for all services
- [ ] 🟡 Deploy SHELDRA API + avatar to cloud
- [ ] 🟡 WebSocket for real-time SHELDRA streaming
- [ ] 🟡 SSL + domain
- [ ] 🟢 k6 load test: 100 concurrent SHELDRA sessions

---

## Phase 4: Presentation Prep (Last 4h)

### Demo Script (All)
- [ ] 🔴 "Meet SHELDRA" — 30s intro (problem → SHELDRA appears)
- [ ] 🔴 Scenario 1: PPE violation → SHELDRA corrective feedback → Decision Tree generates flow
- [ ] 🔴 Scenario 2: Gas leak → Decision Tree updates within 5 min → SHELDRA guides evacuation
- [ ] 🔴 Scenario 3: Personalization — switch worker profiles, same hazard, different SHELDRA response
- [ ] 🟡 "Behind the scenes" — Decision Tree accuracy metrics, 5-min update cycle visualization
- [ ] 🟡 Record backup demo video

### Slides (C)
- [ ] 🟡 10-slide deck: SHELDRA-first narrative
- [ ] 🟡 Architecture slide: SHELDRA at center, everything feeds her
- [ ] 🟡 Personalization comparison slide (3 worker profiles, 3 responses)
- [ ] 🟡 Decision Tree evolution slide (tree v1 vs v3, accuracy improvement)
- [ ] 🟡 Q&A cheat sheet per team member

---

## File Map

```
/
├── frontend/
│   ├── components/sheldra/     # Avatar, speech bubble, gestures (C)
│   ├── components/decision-tree/ # Flow chart viz, walkthrough (C)
│   ├── components/dashboard/   # Layout, panels, context (C)
│   ├── scenes/                 # VR training scenes (C)
│   └── pages/                  # Next.js routes (C)
├── backend/
│   ├── sheldra/                # Core AI, personalization engine, voice I/O (A)
│   ├── decision-tree/          # Tree generator, update cycle, scorer (B)
│   ├── agents/                 # Multi-agent system (A + B)
│   ├── knowledge-graph/        # Worker profiles, hazard taxonomy (B)
│   └── rag/                    # Safety document retrieval (A + B)
├── infra/                      # Docker, CI/CD (B)
├── data/
│   ├── worker-profiles/        # 3 synthetic profiles (All)
│   ├── safety-docs/            # Procedure PDFs (All)
│   └── hazard-scenarios/       # Demo scenario definitions (All)
└── docs/                       # Architecture, API specs
```
