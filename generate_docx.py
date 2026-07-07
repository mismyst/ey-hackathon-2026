#!/usr/bin/env python3
"""Generate SHELDRA architecture proposal as a Word document."""

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import datetime

doc = Document()

# ── Global Styles ──────────────────────────────────────────────────────────
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
style.paragraph_format.space_after = Pt(6)

for level in range(1, 4):
    h = doc.styles[f'Heading {level}']
    h.font.color.rgb = RGBColor(0x1A, 0x3C, 0x6E)

def add_table(headers, rows):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
    for row_data in rows:
        row_cells = table.add_row().cells
        for i, val in enumerate(row_data):
            row_cells[i].text = str(val)
    return table

def add_para(text, bold=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = bold
    return p

def add_heading(text, level=1):
    return doc.add_heading(text, level=level)

# ── Title Page ────────────────────────────────────────────────────────────
doc.add_paragraph()
doc.add_paragraph()
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('SHELDRA')
run.bold = True
run.font.size = Pt(36)
run.font.color.rgb = RGBColor(0x1A, 0x3C, 0x6E)

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('Safety Holographic Enhanced Learning\n& Decision-Reality Assistant')
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(0x4A, 0x6F, 0xA5)

tagline = doc.add_paragraph()
tagline.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = tagline.add_run('The World\'s First Holographic AI Safety Coach')
run.italic = True
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x6B, 0x8F, 0xC6)

doc.add_paragraph()
meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
meta.add_run(f'ET AI Hackathon 2026 — Industrial Safety Intelligence Challenge\n')
meta.add_run(f'Date: {datetime.date.today().strftime("%B %d, %Y")}\n')
meta.add_run(f'Team: 3 Members (AI/ML \u00b7 Backend/Infra \u00b7 Full-Stack)')

doc.add_page_break()

# ── Table of Contents ────────────────────────────────────────────────────
doc.add_heading('Table of Contents', level=1)
toc_items = [
    '1. Problem Reframing',
    '2. Vision Statement',
    '3. Unique Value Proposition',
    '4. SHELDRA \u2014 The Holographic AI Safety Coach',
    '5. Decision Tree Algorithm',
    '6. System Architecture Overview',
    '7. Multi-Agent Architecture (Supporting SHELDRA)',
    '8. SHELDRA AI Pipeline',
    '9. Personalization Engine',
    '10. Computer Vision Pipeline (SHELDRA\u2019s Eyes)',
    '11. Time-Series Prediction Models',
    '12. Knowledge Graph Design',
    '13. RAG Architecture',
    '14. Digital Twin Architecture',
    '15. Data Ingestion Pipeline',
    '16. Graph AI Opportunities',
    '17. Explainable AI Layer',
    '18. Human-in-the-Loop Workflow',
    '19. Emergency Response Workflow',
    '20. VR Training Integration',
    '21. Database Schema & Data Model',
    '22. API Architecture',
    '23. Frontend Dashboard Design',
    '24. Live Demo Flow',
    '25. Tech Stack with Justification',
    '26. AI Models with Justification',
    '27. Open-Source Tools',
    '28. Cloud Deployment Architecture',
    '29. Evaluation Metrics',
    '30. Future Roadmap: MVP \u2192 Enterprise SaaS',
    '31. Risks and Mitigations',
    '32. Why SHELDRA Can Become a Unicorn Startup',
]
for item in toc_items:
    p = doc.add_paragraph(item)
    p.paragraph_format.space_after = Pt(2)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# 1. PROBLEM REFRAMING
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('1. Problem Reframing', level=1)

add_para(
    'Industrial safety today is built on a broken premise: that a human supervisor watching '
    '50+ camera feeds and scrolling through dashboards can prevent incidents. This is not '
    'a monitoring problem \u2014 it is a guidance problem.'
)

add_para(
    'Traditional systems ask: "What went wrong?" They generate reports after the fact. '
    'They classify, log, and archive incidents. They treat safety as retrospective compliance.'
)

add_para(
    'We reframe the problem around three fundamental insights:'
)

insights = [
    ('Workers need a coach, not a dashboard.',
     'The most effective safety interventions happen in the moment, not in the post-mortem. '
     'A worker removing PPE does not need a report generated \u2014 they need a voice saying '
     '"Your harness clip is not fastened." SHELDRA is that voice.'),
    ('Safety knowledge is trapped in documents.',
     'OSHA manuals, SOPs, and incident reports contain the knowledge to prevent accidents, '
     'but this knowledge is inaccessible in the moment of need. A worker facing a gas leak '
     'cannot flip through a 200-page manual. SHELDRA retrieves and delivers the exact '
     'procedure, in their language, at their experience level.'),
    ('Every incident is a learning opportunity \u2014 if you capture it.',
     'Current systems lose 90% of the signal from near-misses. A corrected behavior, '
     'a supervisor override, a successful evacuation \u2014 these are data points that should '
     'improve every future response. Our Decision Tree algorithm captures every outcome '
     'and updates itself every 5 minutes.'),
]

for name, desc in insights:
    p = doc.add_paragraph()
    run = p.add_run(f'{name} ')
    run.bold = True
    p.add_run(desc)

# ═══════════════════════════════════════════════════════════════════════════
# 2. VISION STATEMENT
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('2. Vision Statement', level=1)

add_para(
    '"An autonomous holographic AI safety coach that walks beside every worker, sees what '
    'they see, knows what they know, and guides them through every hazard with personalized, '
    'adaptive intelligence \u2014 powered by a living decision tree that learns from every '
    'interaction, every sensor, every incident, updating in real time."'
)

add_para(
    'SHELDRA is not a dashboard. SHELDRA is not a report. SHELDRA is a teammate \u2014 '
    'one that never blinks, never forgets, never has a bad day, and always puts the '
    'worker\u2019s safety first.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 3. UNIQUE VALUE PROPOSITION
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('3. Unique Value Proposition', level=1)

uvps = [
    ('A Coach, Not a Dashboard',
     'Every other industrial safety system is a screen to watch. SHELDRA is a presence '
     'that guides, corrects, teaches, and reassures. Workers do not monitor SHELDRA \u2014 '
     'SHELDRA watches over them. This flips the human-AI relationship from observation '
     'to partnership.'),
    ('Personalized at the Individual Level',
     'SHELDRA adapts to each worker\u2019s experience, learning speed, language, and '
     'emotional state. A novice gets step-by-step guidance. An expert gets a quick confirmation. '
     'A stressed worker gets a calm, simplified voice. No two workers experience the same '
     'SHELDRA.'),
    ('Living Decision Trees That Improve Every 5 Minutes',
     'Static checklists kill. Our Decision Tree algorithm generates dynamic flow charts '
     'that evolve with every incident. If a resolution path fails, the tree learns, prunes '
     'the branch, and proposes a better one. Updates every 5 minutes. Accuracy is '
     'measured, displayed, and improved continuously.'),
    ('Holographic by Design, Multi-Modal by Necessity',
     'SHELDRA manifests as a 3D holographic avatar \u2014 visually present, spatially aware, '
     'emotionally intelligent. She speaks, gestures, points, and demonstrates. On mobile, '
     'desktop, AR glasses, or VR headsets. The interface adapts to the environment.'),
    ('Full-Stack Awareness',
     'SHELDRA sees through cameras (PPE detection, behavior analysis), feels through '
     'sensors (temperature, vibration, gas), reads through documents (safety manuals via RAG), '
     'and remembers through the Knowledge Graph (every interaction, every worker, every '
     'incident). No other safety AI has this complete situational awareness.'),
]

for name, desc in uvps:
    p = doc.add_paragraph()
    run = p.add_run(f'{name}: ')
    run.bold = True
    p.add_run(desc)

# ═══════════════════════════════════════════════════════════════════════════
# 4. SHELDRA
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('4. SHELDRA \u2014 The Holographic AI Safety Coach', level=1)

add_para(
    'SHELDRA is the central interface of the platform \u2014 an adaptive, personalized, '
    'holographic AI assistant that workers interact with throughout their shift. She is '
    'not a chatbot. She is a spatial, emotional, multi-modal presence.'
)

add_heading('4.1 Core Capabilities', level=2)

sheldra_caps = [
    ['Proactive Guidance', 'SHELDRA monitors the environment and proactively speaks up: '
     '"Watch your step \u2014 there is an oil spill in aisle 3."', 'CV + IoT + KG'],
    ['Corrective Feedback', 'When a safety violation is detected, SHELDRA intervenes with '
     'a specific, actionable correction: "Your safety glasses are on top of your helmet. '
     'Please adjust them before entering Zone A."', 'Vision Agent + Profile'],
    ['Procedural Walkthrough', 'For complex or rare tasks, SHELDRA provides step-by-step '
     'guidance, pausing at each step for confirmation.', 'RAG + Decision Tree'],
    ['Hazard Q&A', 'Workers can ask SHELDRA anything: "What is the protocol for hydrogen '
     'sulfide detection?" SHELDRA answers with citations from safety manuals.', 'RAG'],
    ['Emergency Response', 'During an incident, SHELDRA switches to emergency mode: '
     'clear, authoritative, time-stamped evacuation instructions.', 'Decision Tree + Emergency'],
    ['Training & Simulation', 'In VR mode, SHELDRA becomes a training instructor, '
     'scoring worker responses and adapting future training.', 'VR Scene + Profile'],
    ['Shift Handover', 'At shift change, SHELDRA generates a summary for the incoming '
     'team: active hazards, worker status, unresolved issues.', 'KG + Profile'],
]
add_table(['Capability', 'Description', 'Powered By'], sheldra_caps)

add_heading('4.2 SHELDRA Personality & Behavior', level=2)
add_para(
    'SHELDRA\u2019s personality is designed for industrial environments:\n'
    '- Calm authority: Never alarms unnecessarily. Communicates clearly even in emergencies.\n'
    '- Encouraging: Praises correct behavior. "Great job locking out that equipment."\n'
    '- Patience: Repeats and rephrases if a worker does not understand.\n'
    '- Adaptability: Switches tone based on worker emotional state (stressed = slower, simpler).\n'
    '- Memory: Reminds workers of past coaching moments. "Remember last week\u2019s training '
    'on confined space entry?"'
)

add_heading('4.3 Holographic Avatar Design', level=2)
add_para(
    'The SHELDRA avatar is rendered in real-time 3D using React Three Fiber:\n'
    '- Full-body presence with idle animation (gentle floating, scanning environment)\n'
    '- Gesture system: pointing at hazards, nodding in acknowledgment, open-palm for warnings\n'
    '- Lip-sync: synchronized to TTS audio output via waveform analysis\n'
    '- Holographic shader: scan-line overlay, subtle glow, translucent effect\n'
    '- Responsive: resizes from full-screen desktop to mobile thumbnail\n'
    '- Environmental awareness: avatar lighting matches factory scene\n\n'
    'Fallback for hackathon: 2D animated character with same gesture/vocal personality, '
    'rendered via Lottie/Bodymovin if 3D performance is insufficient.'
)

add_heading('4.4 Interaction Modalities', level=2)
add_para(
    '- Voice: Speak to SHELDRA (Whisper STT) / SHELDRA speaks back (ElevenLabs/Coqui TTS)\n'
    '- Text: Type to SHELDRA in chat panel\n'
    '- Visual: SHELDRA highlights hazards on screen / in AR overlay\n'
    '- Gesture (future): Wave to summon, point to direct attention\n'
    '- Multi-modal: Combine voice + visual for complex instructions'
)

# ═══════════════════════════════════════════════════════════════════════════
# 5. DECISION TREE ALGORITHM
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('5. Decision Tree Algorithm', level=1)

add_para(
    'The Decision Tree Engine is the second primary pillar. It replaces static safety '
    'checklists with living, learning flow charts that evolve with every incident. '
    'Every SHELDRA interaction, every sensor reading, every supervisor override feeds '
    'back into the tree, making it more accurate over time.'
)

add_heading('5.1 Data Model', level=2)
add_para(
    'Each decision tree is a directed acyclic graph (DAG):\n\n'
    '{\n'
    '  "tree_id": "gas-leak-001",\n'
    '  "hazard_type": "gas_leak",\n'
    '  "version": 7,\n'
    '  "last_updated": "2026-07-07T14:30:00Z",\n'
    '  "overall_accuracy": 0.89,\n'
    '  "nodes": [\n'
    '    {\n'
    '      "id": "node-001",\n'
    '      "type": "question | action | condition | resolution",\n'
    '      "question": "Is the gas sensor reading above 50ppm?",\n'
    '      "conditions": { "sensor.gas_ppm": { "gt": 50 } },\n'
    '      "branches": [\n'
    '        { "to": "node-002", "label": "Yes", "action": "evacuate_zone" },\n'
    '        { "to": "node-003", "label": "No", "action": "monitor" }\n'
    '      ],\n'
    '      "accuracy": 0.92,\n'
    '      "times_taken": 47\n'
    '    }\n'
    '  ],\n'
    '  "root_id": "node-001"\n'
    '}'
)

add_heading('5.2 Tree Generation', level=2)
add_para(
    'Trees are generated from three sources:\n'
    '1. Knowledge Graph: Hazard taxonomy nodes link to safety rules, procedures, and '
    'historical incidents. These define the initial tree structure.\n'
    '2. Safety Documents (RAG): Procedure steps are parsed into action nodes.\n'
    '3. Historical Incidents: Past resolution paths are extracted as branch patterns.\n\n'
    'The generator combines these into a coherent tree, validates it for completeness '
    '(all branches terminate in resolution or escalation), and assigns initial confidence '
    'scores based on source reliability.'
)

add_heading('5.3 The 5-Minute Update Cycle', level=2)
add_para(
    'This is the core differentiator. Every 5 minutes:\n\n'
    '1. Collect outcomes: Gather all hazard resolutions from the last 5 minutes \u2014 '
    'both successful and failed.\n'
    '2. Score each branch: For each path taken, compare predicted outcome vs actual outcome. '
    'Update branch accuracy scores.\n'
    '3. Prune low-accuracy branches: Any branch with < 50% accuracy over last 10 evaluations '
    'is flagged for pruning. If accuracy does not recover in 3 cycles, it is removed.\n'
    '4. Propose new branches: Analyze failed resolutions for patterns. If a common '
    'alternative path emerges, propose it as a new branch.\n'
    '5. Version the tree: Each update creates a new tree version. Old trees are retained '
    'for A/B testing and rollback.\n'
    '6. Notify SHELDRA: "Decision Tree #7 updated to version 8 \u2014 new branch added '
    'for gas leak escalation."'
)

add_heading('5.4 Flow Chart Examples', level=2)

add_para('Example 1: PPE Violation Resolution', bold=True)
add_para(
    'Root: Worker entered Zone A without safety glasses\n'
    '\u251c\u2500 Is worker in a designated PPE-required zone?\n'
    '\u2502   \u251c\u2500 Yes \u2192 Notify worker + display nearest PPE station\n'
    '\u2502   \u2502   \u251c\u2500 Worker complies? \u2192 Log compliance + praise\n'
    '\u2502   \u2502   \u2514\u2500 Worker does not comply? \u2192 Escalate to supervisor\n'
    '\u2502   \u2514\u2500 No \u2192 No action needed (log entry)\n'
    '\u2514\u2500 Does worker have a medical exemption?\n'
    '    \u251c\u2500 Yes \u2192 Verify exemption in KG \u2192 Log + allow\n'
    '    \u2514\u2500 No \u2192 Escalate to safety officer'
)

add_para('Example 2: Gas Leak Response', bold=True)
add_para(
    'Root: Gas sensor anomaly detected in Zone B\n'
    '\u251c\u2500 Gas level > 50ppm?\n'
    '\u2502   \u251c\u2500 Yes \u2192 Initiate zone evacuation\n'
    '\u2502   \u2502   \u251c\u2500 All workers evacuated? \u2192 Seal zone + alert HAZMAT\n'
    '\u2502   \u2502   \u2514\u2500 Workers remaining? \u2192 Alert rescue team\n'
    '\u2502   \u2514\u2500 No \u2192 Increase monitoring frequency\n'
    '\u2502       \u251c\u2500 Gas stabilizes? \u2192 Resume normal ops\n'
    '\u2502       \u2514\u2500 Gas rising? \u2192 Re-evaluate (loop to root)\n'
    '\u2514\u2500 Is gas source identified?\n'
    '    \u251c\u2500 Yes \u2192 Dispatch maintenance team\n'
    '    \u2514\u2500 No \u2192 Initiate source search protocol'
)

add_heading('5.5 Accuracy Evaluation', level=2)
add_para(
    'Every hazard resolution is scored:\n'
    '- Success: Hazard resolved correctly, no injuries, no escalation needed. Score: 1.0\n'
    '- Partial: Hazard resolved but with delay or confusion. Score: 0.5\n'
    '- Failure: Escalation required, incorrect procedure followed. Score: 0.0\n\n'
    'Accuracy for a node = (sum of scores) / (number of times taken) over rolling 10-trial '
    'window. Overall tree accuracy = average of all leaf node accuracies. Displayed in '
    'real-time on the dashboard.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 6. SYSTEM ARCHITECTURE OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('6. System Architecture Overview', level=1)

add_para(
    'The architecture is SHELDRA-centric. Every component exists to feed SHELDRA\u2019s '
    'awareness, power the Decision Tree, or deliver the holographic experience.'
)

add_para(
    'Layer 1 \u2014 Edge & Sensor Layer\n'
    'Cameras (RTSP), IoT sensors (temperature, vibration, gas, noise, humidity), '
    'edge gateways with lightweight preprocessing. Workers can also interact via '
    'mobile devices with AR capabilities.\n\n'
    'Layer 2 \u2014 Ingestion & Streaming Layer\n'
    'Apache Kafka as the nervous system. Topics: sheldra.interactions, decision.trees, '
    'sensor.readings, vision.events, worker.profiles, system.alerts. Schema Registry '
    'for contract enforcement.\n\n'
    'Layer 3 \u2014 SHELDRA Intelligence Layer\n'
    'The brain. Contains: SHELDRA Core AI (LLM + Personalization Engine), Decision Tree '
    'Engine (generator + updater + scorer), Multi-Agent System (feeding context), '
    'Knowledge Graph (worker profiles + hazard taxonomy), RAG Engine (safety document '
    'grounding).\n\n'
    'Layer 4 \u2014 SHELDRA Presentation Layer\n'
    'Next.js dashboard with Three.js holographic avatar, WebSocket real-time streaming, '
    'voice I/O (STT/TTS), Decision Tree flow chart visualization, VR training scenes.\n\n'
    'Layer 5 \u2014 Human-in-the-Loop Layer\n'
    'Supervisor console for monitoring SHELDRA interactions, overriding recommendations, '
    'audit trails, shift handover briefings.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 7. MULTI-AGENT ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('7. Multi-Agent Architecture (Supporting SHELDRA)', level=1)

add_para(
    'The multi-agent system exists to feed SHELDRA\u2019s situational awareness. Each agent '
    'is a specialized sensor-to-meaning pipeline that converts raw observations into '
    'structured context that SHELDRA can reason over.'
)

agents = [
    ['Orchestrator', 'B', 'Central state machine. Routes all observations to SHELDRA\u2019s '
     'context assembly. Manages incident lifecycle. The bridge between raw data and '
     'SHELDRA\u2019s awareness.'],
    ['Vision Agent', 'A', 'Processes camera frames (YOLOv8). Detects PPE compliance, zone '
     'encroachment, unsafe behaviors. Outputs structured observations that trigger '
     'SHELDRA\u2019s corrective feedback.'],
    ['Monitoring Agent', 'A', 'Ingests IoT sensor streams. Runs TimesNet anomaly detection. '
     'Anomaly scores feed into the Decision Tree engine as hazard triggers.'],
    ['Compliance Agent', 'B', 'Queries Knowledge Graph for applicable safety rules given '
     'current context. Provides SHELDRA with regulatory grounding for her guidance.'],
    ['RAG Agent', 'A/B', 'Retrieves relevant safety procedures from vector store. Provides '
     'citation-anchored knowledge for SHELDRA\u2019s responses. Enables "Show me the '
     'regulation" feature.'],
    ['Explanation Agent', 'A', 'Collects decision traces. Enables SHELDRA to answer "Why '
     'did you suggest that?" with a complete evidence chain.'],
]
add_table(['Agent', 'Owner', 'Role in SHELDRA Ecosystem'], agents)

add_heading('7.1 SHELDRA Context Assembly Flow', level=2)
add_para(
    '1. Observations arrive from Vision + Monitoring Agents\n'
    '2. Orchestrator queries Knowledge Graph for context: Who is this worker? What zone? '
    'What equipment? Current risk level?\n'
    '3. Compliance Agent cross-references observations against safety rules\n'
    '4. RAG Agent retrieves relevant procedures\n'
    '5. All context is assembled into SHELDRA\u2019s prompt: {worker_profile, observations, '
    'rules, procedures, history, emotional_state}\n'
    '6. SHELDRA generates response with personalized tone + content depth\n'
    '7. Decision Tree is updated with the interaction outcome\n'
    '8. Explanation Agent logs the full trace'
)

# ═══════════════════════════════════════════════════════════════════════════
# 8. SHELDRA AI PIPELINE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('8. SHELDRA AI Pipeline', level=1)

add_para(
    'The SHELDRA AI pipeline transforms raw context into personalized, grounded, '
    'emotionally-aware coaching responses.'
)

add_heading('8.1 Pipeline Stages', level=2)
pipeline_stages = [
    ['Context Assembly', 'Collect all observations from agents + KG. Build unified context object.', 'Orchestrator Agent'],
    ['Profile Augmentation', 'Retrieve worker profile. Adjust prompt parameters based on experience, language, learning speed, emotional state.', 'Personalization Engine'],
    ['RAG Retrieval', 'Query vector store for relevant safety procedures. Filter and rank by relevance to current context.', 'RAG Agent'],
    ['Prompt Construction', 'Assemble system prompt with SHELDRA persona, context, profile, and retrieved knowledge.', 'SHELDRA Core'],
    ['LLM Generation', 'Generate response via Llama 3 8B (streaming). Include structured fields: {message, tone, gesture, confidence, citations}.', 'LLM (Ollama/Together)'],
    ['Response Post-Processing', 'Parse structured response. Validate against safety guardrails. Extract gesture/tone commands.', 'SHELDRA Core'],
    ['TTS + Lip-Sync', 'Convert text to speech (ElevenLabs/Coqui). Generate lip-sync animation data.', 'Voice Pipeline'],
    ['Avatar Rendering', 'Animate SHELDRA avatar with speech, gesture, and facial expression.', 'R3F Avatar'],
]
add_table(['Stage', 'Description', 'Component'], pipeline_stages)

add_heading('8.2 Guardrails & Safety', level=2)
add_para(
    'SHELDRA operates under strict behavioral constraints:\n'
    '- Never contradict a safety procedure directly (escalate to supervisor instead)\n'
    '- Always provide confidence level for uncertain guidance\n'
    '- Never dismiss a worker\u2019s concern (redirect to supervisor if needed)\n'
    '- Always cite sources for procedural guidance\n'
    '- Switch to emergency mode (abbreviated, authoritative) when risk score > 0.8\n'
    '- Log all interactions for audit'
)

# ═══════════════════════════════════════════════════════════════════════════
# 9. PERSONALIZATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('9. Personalization Engine', level=1)

add_para(
    'SHELDRA is not one AI \u2014 she is a different AI for every worker. The personalization '
    'engine ensures that each worker receives guidance tailored to their individual profile.'
)

add_heading('9.1 Worker Profile Schema', level=2)

profile_fields = [
    ['worker_id', 'string', 'Unique identifier'],
    ['name', 'string', 'Worker display name'],
    ['role', 'string', 'Job title / role'],
    ['experience_level', 'enum', 'novice | experienced | expert'],
    ['learning_speed', 'float', '0.0 (slow) to 1.0 (fast). Inferred from interaction patterns.'],
    ['language', 'string', 'en | es | zh (ISO code)'],
    ['certifications', 'string[]', 'List of safety certifications'],
    ['incident_history', 'object[]', 'Past incidents involved in'],
    ['interaction_history', 'object[]', 'Past SHELDRA coaching moments'],
    ['emotional_state', 'object', 'Current estimated stress/fatigue level'],
    ['training_completed', 'object[]', 'VR training modules completed + scores'],
    ['ppe_compliance_rate', 'float', '0.0-1.0 rolling 30-day compliance'],
]
add_table(['Field', 'Type', 'Description'], profile_fields)

add_heading('9.2 Adaptation Dimensions', level=2)
adaptations = [
    ['Content Depth', 'Novice: Step-by-step instructions with rationale. Experienced: '
     'Brief confirmation with key points. Expert: Acknowledgment + request for situation report.'],
    ['Vocabulary Complexity', 'Adapt terminology to worker expertise. Novice: "Put on your '
     'helmet." Expert: "Verify your PPE before entering the restricted zone."'],
    ['Speech Rate', 'Slower for novice/high-stress. Normal for experienced/calm.'],
    ['Tone', 'Stressed: Calm, reassuring, simple sentences. Normal: Professional, encouraging. '
     'Urgent: Clear, direct, time-stamped.'],
    ['Feedback Style', 'Novice: Gentle + educational. Experienced: Direct + corrective. '
     'Expert: Brief + respectful.'],
    ['Language', 'Detect from profile. All responses in worker\u2019s preferred language.'],
]
add_table(['Dimension', 'Adaptation Logic'], adaptations)

add_heading('9.3 Learning Speed Detection', level=2)
add_para(
    'SHELDRA infers learning speed from:\n'
    '- Time to acknowledge/respond to instructions\n'
    '- Number of follow-up questions asked\n'
    '- Repetition of same safety violation\n'
    '- VR training performance (reaction time, error rate)\n'
    '- Supervisor feedback (manual rating)\n\n'
    'Learning speed score (0-1) adjusts how much detail SHELDRA provides and how quickly '
    'she progresses through multi-step procedures.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 10. COMPUTER VISION PIPELINE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('10. Computer Vision Pipeline (SHELDRA\u2019s Eyes)', level=1)

add_para(
    'The CV pipeline provides SHELDRA with visual awareness \u2014 the ability to see '
    'what workers are doing, what they are wearing, and what hazards are present.'
)

vision_models = [
    ['PPE Detection', 'YOLOv8n', '6 classes: helmet, vest, gloves, goggles, harness, safety shoes',
     'SHELDRA corrective feedback: "Your goggles are on your forehead, not your eyes."'],
    ['Person Detection', 'YOLOv8s + ByteTrack', 'Track IDs for persistent worker identification',
     'SHELDRA addressing specific workers: "Worker #3124, please..."'],
    ['Zone Encroachment', 'Polygon ROI + IoU', 'Person bbox vs. restricted zone overlap',
     'SHELDRA redirection: "This area requires confined space certification."'],
    ['Pose Estimation', 'RTMPose', '17-keypoint pose for behavior analysis',
     'SHELDRA ergonomic coaching: "Bend your knees, not your back."'],
    ['Fall Detection', 'Pose + velocity analysis', 'Sudden keypoint descent detection',
     'SHELDRA emergency: "Worker down in Zone A3 \u2014 dispatching assistance."'],
]
add_table(['Capability', 'Model', 'Approach', 'SHELDRA Integration'], vision_models)

# ═══════════════════════════════════════════════════════════════════════════
# 11. TIME-SERIES PREDICTION MODELS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('11. Time-Series Prediction Models', level=1)

add_para(
    'Time-series anomaly detection feeds the Decision Tree engine. When an anomaly is '
    'detected, the Decision Tree generates or selects a hazard resolution flow chart '
    'for SHELDRA to execute.'
)

ts_details = [
    ['TimesNet (Microsoft Research)', 'Primary anomaly detection',
     'Transforms 1D time-series into 2D tensors via FFT period detection. Captures '
     'multi-periodic patterns (shift cycles, machine cycles, seasonal variations). '
     'ICLR 2023 Best Paper.'],
    ['PatchTST (Princeton/Google)', 'Secondary / backup',
     'Self-supervised pretraining on time-series patches. Handles missing data. '
     'Strong on long-horizon anomaly forecasting.'],
    ['Anomaly Scoring', 'Ensemble: TimesNet + Isolation Forest',
     'TimesNet for complex patterns, Isolation Forest for fast baseline. '
     'Weights adjust based on recent precision/recall.'],
    ['Sensor Fusion Strategy', 'Weighted compound anomaly index',
     'Vibration (0.4) + Temperature (0.3) + Gas (0.3). Prevents single-sensor false '
     'positives from triggering unnecessary Decision Tree escalation.'],
]
add_table(['Model', 'Role', 'Details'], ts_details)

# ═══════════════════════════════════════════════════════════════════════════
# 12. KNOWLEDGE GRAPH DESIGN
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('12. Knowledge Graph Design', level=1)

add_para(
    'The Knowledge Graph serves two primary purposes: (1) worker profile storage and '
    'personalization, and (2) hazard taxonomy for Decision Tree generation.'
)

add_heading('12.1 Node Types', level=2)

nodes = [
    ['Worker', 'Core profile + preferences + learning state', 'Personalization engine'],
    ['Hazard', 'Hazard type, severity, frequency, related trees', 'Decision Tree generation'],
    ['DecisionTree', 'Tree ID, version, accuracy, last_updated', 'Decision Tree Engine'],
    ['SafetyRule', 'Rule description, regulation reference, conditions', 'Compliance Agent'],
    ['Procedure', 'Steps, applicable hazards, required PPE', 'RAG grounding'],
    ['Incident', 'Timeline, resolution path, outcome, accuracy score', 'Tree improvement'],
    ['SHELDRASession', 'Interaction log: query, response, worker state, outcome', 'Audit + learning'],
    ['Zone', 'Type, hazard level, required PPE, active hazards', 'Context awareness'],
    ['Equipment', 'Status, maintenance, last inspection, associated hazards', 'Context awareness'],
]
add_table(['Node', 'Content', 'Used By'], nodes)

add_heading('12.2 Edge Types', level=2)
edges = [
    ['HAS_PROFILE', 'Worker \u2192 Profile', 'Links worker to their personalization data'],
    ['GUIDED_BY', 'Worker \u2192 SHELDRASession', 'Records every coaching interaction'],
    ['ABOUT', 'SHELDRASession \u2192 Hazard', 'What hazard was the coaching about'],
    ['RESOLVED_VIA', 'Incident \u2192 DecisionTree', 'Which tree was used for resolution'],
    ['REQUIRES', 'Zone \u2192 SafetyRule', 'Rules applicable to a zone'],
    ['TRIGGERED_BY', 'Incident \u2192 Sensor/Observation', 'Root cause link'],
    ['HAS_VERSION', 'DecisionTree \u2192 TreeVersion', 'Version history with accuracy scores'],
]
add_table(['Edge', 'Source \u2192 Target', 'Purpose'], edges)

# ═══════════════════════════════════════════════════════════════════════════
# 13. RAG ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('13. RAG Architecture', level=1)

add_para(
    'The RAG pipeline grounds everything SHELDRA says in verifiable safety documentation. '
    'When SHELDRA gives procedural guidance, she cites her sources.'
)

add_para(
    'Document Sources:\n'
    '- Safety manuals (PDF): Step-by-step equipment procedures\n'
    '- SOP documents: Standard operating procedures per zone\n'
    '- Incident reports: Historical incidents with root cause + resolution\n'
    '- Regulatory documents: OSHA/ISO guidelines\n'
    '- Equipment datasheets: Manufacturer safety specifications\n\n'
    'Pipeline: PDF \u2192 Chunking (512 chars, 50 overlap) \u2192 Embedding (E5-mistral-7b) '
    '\u2192 Qdrant (hybrid search: dense + BM25)\n\n'
    'Retrieval: Query \u2192 Query expansion \u2192 Hybrid search \u2192 Cross-encoder re-ranking '
    '(top 3) \u2192 Context assembly \u2192 LLM generation\n\n'
    'Every response includes: answer text, confidence score, source citations (document, '
    'section, page). If retrieval confidence < 0.5, SHELDRA says "I am not sure. Let me '
    'connect you with a supervisor."'
)

# ═══════════════════════════════════════════════════════════════════════════
# 14. DIGITAL TWIN ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('14. Digital Twin Architecture', level=1)

add_para(
    'The Digital Twin provides spatial context for SHELDRA and a visual representation '
    'of the factory floor for supervisors. SHELDRA appears as a floating avatar marker '
    'in the 3D scene, showing her current position and focus.'
)

add_para(
    'Three.js / React Three Fiber \u2190 WebSocket (state sync) \u2190 Digital Twin Engine '
    '(Node.js) \u2190 Knowledge Graph + Agent Events\n\n'
    'Visual elements:\n'
    '- Factory floor plan with equipment 3D models\n'
    '- SHELDRA avatar marker (floating indicator showing her current focus area)\n'
    '- Worker position indicators (colored by PPE compliance)\n'
    '- Active hazard overlays (pulsing red zones)\n'
    '- Decision Tree overlay (current tree path highlighted on the scene)\n'
    '- Camera frustum visualization (what SHELDRA is currently "seeing")\n'
    '- Time scrubber: rewind and replay SHELDRA interactions'
)

# ═══════════════════════════════════════════════════════════════════════════
# 15. DATA INGESTION PIPELINE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('15. Data Ingestion Pipeline', level=1)

ingestion = [
    ['Kafka Topics', 'sheldra.interactions, decision.trees, sensor.readings, vision.events, worker.profiles, system.alerts', 'Typed topics with Schema Registry (Avro).'],
    ['IoT Simulator', 'Python script generating realistic sensor patterns with injected anomalies every 5-10 min', 'Synthetic data for demo with controllable anomaly injection.'],
    ['Video Frame Producer', 'FFmpeg-based RTSP frame capture at configurable FPS', 'Frame metadata: camera_id, timestamp, zone mapping.'],
    ['Stream Processing', 'KSQL for windowed aggregates, Flink for CEP (complex event processing)', '5-min rolling windows for Decision Tree update feed.'],
    ['Object Storage', 'MinIO for frames, model artifacts, incident report PDFs', 'S3-compatible API for easy cloud migration.'],
]
add_table(['Component', 'Description', 'Details'], ingestion)

# ═══════════════════════════════════════════════════════════════════════════
# 16. GRAPH AI OPPORTUNITIES
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('16. Graph AI Opportunities', level=1)

add_para(
    'The Knowledge Graph enables several AI capabilities that directly enhance SHELDRA '
    'and the Decision Tree:'
)

graph_ai = [
    ['Worker Similarity Clustering', 'Find workers with similar profiles and incident patterns. '
     'SHELDRA can say: "Workers with your profile have most often struggled with confined '
     'space procedure. May I walk you through it?"'],
    ['Hazard Propagation Prediction', 'Graph traversal predicts which zones are at highest risk '
     'of incident propagation. Decision Tree pre-positions response plans.'],
    ['Personalized Training Recommendations', 'Based on incident graph + worker profile, '
     'recommend specific VR training modules. "Your last three near-misses involved lockout/'
     'tagout. Would you like to run the LOTO VR simulation?"'],
    ['Decision Tree Cross-Pollination', 'Similar hazards share tree branches. When a tree '
     'improves for Gas Leak, related trees (Chemical Spill, Fume Release) inherit updates.'],
]
for name, desc in graph_ai:
    p = doc.add_paragraph()
    run = p.add_run(f'{name}: ')
    run.bold = True
    p.add_run(desc)

# ═══════════════════════════════════════════════════════════════════════════
# 17. EXPLAINABLE AI LAYER
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('17. Explainable AI Layer', level=1)

add_para(
    'SHELDRA can explain every decision she makes. This is critical for trust, audit, '
    'and regulatory compliance.'
)

xai_types = [
    ['SHELDRA Decision Trace', 'Timeline: what SHELDRA observed, what she considered, '
     'what she decided. Displayed as a DAG in the SHELDRA info panel.'],
    ['Natural Language Explanation', 'SHELDRA answers: "Why did you tell me to evacuate?" '
     '"I detected gas levels at 85ppm in Zone B. The procedure for >50ppm requires '
     'immediate evacuation per OSHA 1910.120."'],
    ['Confidence Provenance', 'Breakdown: model confidence (0.87) + context relevance '
     '(0.92) + tree branch accuracy (0.89) = composite confidence (0.89).'],
    ['Counterfactual', '"If you had been wearing your safety glasses, I would not have '
     'interrupted. The rule was triggered by the violation, not by you specifically."'],
    ['Decision Tree Path Highlight', 'In the flow chart, highlight the path taken and '
     'alternative paths that were considered but deprioritized.'],
]
add_table(['Explanation Type', 'How It Works'], xai_types)

# ═══════════════════════════════════════════════════════════════════════════
# 18. HUMAN-IN-THE-LOOP WORKFLOW
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('18. Human-in-the-Loop Workflow', level=1)

add_para(
    'SHELDRA proposes actions. Supervisors approve, modify, or reject. All decisions are '
    'logged and fed into the Decision Tree accuracy engine.'
)

add_para(
    'Alert Generated by SHELDRA \u2192 Queued for Supervisor Review\n'
    '\u251c\u2500 Supervisor Acknowledges \u2192 SHELDRA action executes\n'
    '\u2502   \u251c\u2500 Auto-response after N seconds of inactivity (configurable)\n'
    '\u2502   \u2514\u2500 Supervisor Override (modify or cancel)\n'
    '\u2514\u2500 SHELDRA Escalates (if no response in 60s, alert next supervisor)\n'
    '\n'
    'Supervisor Console includes:\n'
    '- Live SHELDRA interaction feed (every coaching moment)\n'
    '- Ability to override SHELDRA recommendations with reason\n'
    '- Audit log: searchable, filterable, exportable\n'
    '- Shift handover: SHELDRA generates summary for incoming team\n'
    '- Performance metrics: SHELDRA accuracy, response times, escalation rates'
)

# ═══════════════════════════════════════════════════════════════════════════
# 19. EMERGENCY RESPONSE WORKFLOW
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('19. Emergency Response Workflow', level=1)

add_para(
    'When the compound risk score exceeds 0.8, SHELDRA switches to Emergency Mode:'
)

emergency = [
    ['SHELDRA Tone Shift', 'Voice becomes clear, authoritative, time-stamped. "ATTENTION: '
     'Gas leak detected in Zone B. Evacuate immediately via Exit 4."'],
    ['Decision Tree Activation', 'Emergency tree loads automatically. SHELDRA guides step-'
     'by-step. Each step is confirmed before proceeding.'],
    ['Multi-Channel Alert', 'WebSocket push to dashboard + email alert + SMS to all '
     'supervisors. Message includes: hazard type, location, severity, recommended action.'],
    ['Escalation Ladder', 'Supervisor: 60s to acknowledge. Shift manager: 120s. '
     'Plant director: 180s. SHELDRA logs every step.'],
    ['Post-Incident Report', 'Auto-generated PDF: incident timeline, SHELDRA actions, '
     'Decision Tree path taken, human responses, outcome, accuracy score.'],
]
add_table(['Action', 'Description'], emergency)

# ═══════════════════════════════════════════════════════════════════════════
# 20. VR TRAINING INTEGRATION
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('20. VR Training Integration', level=1)

add_para(
    'SHELDRA exists in VR. The same AI coach that guides workers on the factory floor '
    'trains them in simulated scenarios \u2014 creating continuity between training and reality.'
)

add_para(
    'VR Scene (A-Frame / Three.js XR):\n'
    '- Full 3D factory environment with interactive hazards\n'
    '- SHELDRA avatar rendered inside VR scene\n'
    '- Hazard simulations: gas leak (visual + audio cues), fire, equipment failure, '
    'falling objects\n'
    '- Worker interacts via voice + hand controllers (if available)\n\n'
    'Training Flow:\n'
    '1. SHELDRA introduces the scenario\n'
    '2. Hazard triggers (SHELDRA can trigger manually or automated)\n'
    '3. Worker responds \u2014 SHELDRA observes, provides real-time feedback\n'
    '4. Scenario ends \u2014 SHELDRA scores performance: reaction time, decision accuracy, '
    'procedure adherence\n'
    '5. Score \u2192 Worker Profile update\n'
    '6. Adaptive training: SHELDRA adjusts future scenarios based on weak areas\n\n'
    'For hackathon: desktop VR mode (mouse/keyboard navigation) with WebXR upgrade path.'
)

# ═══════════════════════════════════════════════════════════════════════════
# 21. DATABASE SCHEMA
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('21. Database Schema & Data Model', level=1)

dbs = [
    ['Knowledge Graph', 'Neo4j', 'Worker profiles, hazard taxonomy, SHELDRA interaction logs, decision tree metadata', 'Graph queries, personalization, root cause analysis'],
    ['Vector Store', 'Qdrant', 'Document embeddings for RAG, feature vectors for similarity', 'Semantic search, procedure retrieval, grounding'],
    ['Time-Series', 'InfluxDB', 'IoT sensor readings, model performance metrics', 'Windowed aggregates, anomaly detection feed'],
    ['Message Log', 'Kafka (retention 7d)', 'All events: sheldra.interactions, decision.trees, sensor data', 'Stream processing, audit trail, replay'],
    ['Object Storage', 'MinIO / S3', 'Camera frames, SHELDRA interaction recordings, report PDFs', 'Long-term storage, compliance evidence'],
    ['Cache', 'Redis', 'SHELDRA session state, context cache, WebSocket state', 'Sub-millisecond reads, Pub/Sub for real-time'],
    ['Relational', 'PostgreSQL', 'Users, teams, configuration, audit log', 'Transactional data, auth, reporting'],
]
add_table(['Store', 'Tech', 'Data', 'Access Pattern'], dbs)

# ═══════════════════════════════════════════════════════════════════════════
# 22. API ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('22. API Architecture', level=1)

add_para(
    'SHELDRA-first API design. Every endpoint exists to serve SHELDRA or the Decision Tree.'
)

endpoints = [
    ['POST /api/v1/sheldra/chat', 'Send message to SHELDRA with context', 'SHELDRA interaction'],
    ['WS /ws/sheldra/stream', 'Streaming SHELDRA responses (SSE fallback)', 'Real-time chat'],
    ['GET /api/v1/sheldra/state', 'Current SHELDRA awareness state', 'Dashboard context panel'],
    ['GET /api/v1/decision-trees/{hazard_id}', 'Current tree for a hazard', 'Flow chart viz'],
    ['GET /api/v1/decision-trees/{id}/history', 'Version history + accuracy deltas', 'Accuracy dashboard'],
    ['POST /api/v1/decision-trees/evaluate', 'Score a resolution outcome', '5-min update cycle'],
    ['GET /api/v1/workers/{id}/profile', 'Worker profile with learning state', 'Personalization'],
    ['PUT /api/v1/workers/{id}/profile', 'Update profile (supervisor)', 'Profile management'],
    ['GET /api/v1/workers/{id}/interactions', 'SHELDRA interaction history for worker', 'Audit + learning'],
    ['POST /api/v1/alerts/{id}/acknowledge', 'Supervisor acknowledges alert', 'HITL workflow'],
    ['POST /api/v1/alerts/{id}/override', 'Override SHELDRA recommendation', 'HITL workflow'],
    ['GET /api/v1/analytics/accuracy', 'Decision Tree accuracy dashboard', 'Analytics view'],
]
add_table(['Endpoint', 'Purpose', 'Consumer'], endpoints)

# ═══════════════════════════════════════════════════════════════════════════
# 23. FRONTEND DASHBOARD DESIGN
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('23. Frontend Dashboard Design', level=1)

add_para(
    'The dashboard is SHELDRA-centric. The primary view puts the SHELDRA avatar and '
    'conversation at the center, with the Decision Tree flow chart alongside.'
)

views = [
    ['SHELDRA Command Center (Default)', 
     'SHELDRA 3D avatar (left panel, 40% width), conversation panel (center, 40%), '
     'context sidebar (right, 20%). Context shows: current worker, current hazard, '
     'environment state, recent interactions.'],
    ['Decision Tree View',
     'Full-screen interactive flow chart for current hazard. Highlighted path shows '
     'recommended resolution. Color-coded nodes. Version badge.Accuracy score '
     'prominent in header.'],
    ['Worker Profile Panel',
     'SHELDRA\u2019s view of a specific worker: profile, interaction history, learning '
     'speed indicator, incident history, training scores, emotion timeline.'],
    ['VR Training View',
     'Embedded VR scene with SHELDRA avatar. Works in desktop mode (mouse/keyboard) '
     'with WebXR upgrade for VR headsets.'],
    ['Accuracy Dashboard',
     'Decision Tree accuracy trends over time. Branch-level breakdown. Version history '
     'graph. Update frequency indicator. "Tree updated 5 min ago" badge.'],
    ['Supervisor Console',
     'Live SHELDRA interaction feed. Alert queue. Override controls. Shift handover '
     'summary. Audit log.'],
]
add_table(['View', 'Content'], views)

# ═══════════════════════════════════════════════════════════════════════════
# 24. LIVE DEMO FLOW
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('24. Live Demo Flow', level=1)

add_heading('24.1 Demo Script (5 minutes)', level=2)

demo = [
    ['0:00-0:45', 'Meet SHELDRA', 'Dashboard loads with SHELDRA avatar. SHELDRA introduces '
     'herself: "Welcome to Shift 3. I am SHELDRA, your safety coach. I will be monitoring '
     'Zone A today." Show normal operation: workers moving, SHELDRA observing calmly.'],
    ['0:45-1:30', 'PPE Violation + Corrective Feedback', 'Worker enters frame without safety '
     'glasses. Vision Agent detects. SHELDRA activates: "Worker #3124, your safety glasses '
     'are on your helmet. Please adjust them before entering Zone A." Show the Decision Tree '
     'generating the PPE resolution flow chart in the side panel.'],
    ['1:30-2:15', 'Personalization Demo', 'Switch to a novice worker profile. Same hazard '
     '\u2014 SHELDRA gives step-by-step guidance with rationale. Switch to an expert profile '
     '\u2014 SHELDRA gives quick confirmation. "Same hazard, three different SHELDRAs."'],
    ['2:15-3:00', 'Gas Leak + Decision Tree Update', 'IoT simulator injects gas anomaly. '
     'SHELDRA switches to emergency mode: "Gas leak detected in Zone B. Evacuate via Exit 4 '
     'immediately." Decision Tree loads Gas Leak response tree. Show tree path highlight. '
     'After resolution, show the tree update: "Decision Tree updated to version 8 \u2014 '
     'accuracy: 94%."'],
    ['3:00-3:30', 'VR Training', 'Switch to VR training scene. SHELDRA appears in VR. '
     'Run a confined space training scenario. SHELDRA guides, scores performance, '
     'updates worker profile. Show profile panel update.'],
    ['3:30-4:00', 'Accuracy Loop', 'Show the Accuracy Dashboard. Decision Tree accuracy '
     'trend over 24 hours (simulated). Show a branch being pruned. Show a new branch being '
     'generated. "This tree is alive \u2014 it learns from every interaction."'],
    ['4:00-4:30', 'Architecture Reveal', 'Flash the system architecture diagram. "Everything '
     'you saw \u2014 the avatar, the voice, the trees, the personalization \u2014 is powered '
     'by a unified intelligence layer: multi-agent system, knowledge graph, RAG pipeline, '
     'all working together to make SHELDRA real."'],
    ['4:30-5:00', 'Q&A Hook', '"SHELDRA is not a dashboard with AI features. SHELDRA is a '
     'teammate \u2014 one that never blinks, never forgets, and always puts the worker first. '
     'We would love to discuss how this becomes the standard for industrial safety."'],
]
add_table(['Time', 'Segment', 'Content'], demo)

# ═══════════════════════════════════════════════════════════════════════════
# 25. TECH STACK
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('25. Tech Stack with Justification', level=1)

tech = [
    ['SHELDRA Avatar', 'React Three Fiber + Three.js', 'Declarative 3D in React. WebGL native. '
     'Full control over shaders, animations, and lip-sync.'],
    ['SHELDRA Voice I/O', 'Whisper (STT) + ElevenLabs/Coqui (TTS)', 'Best-in-class speech '
     'recognition + natural TTS. Coqui for local/offline fallback.'],
    ['SHELDRA LLM', 'Llama 3 8B (via Ollama/Together)', 'Open-weight, capable of safety '
     'reasoning. 8B fits consumer GPUs. Can run locally. Fine-tunable.'],
    ['Decision Tree Engine', 'Custom Python (asyncio)', 'No framework overhead. Full control '
     'over tree data model, update cycle, accuracy scoring.'],
    ['Backend API', 'FastAPI (Python)', 'Async-native, auto OpenAPI docs, Pydantic validation. '
     'Python ecosystem for AI integration.'],
    ['Message Broker', 'Apache Kafka + Schema Registry', 'Industry standard. Durable, '
     'replayable, partitioned. Typed schemas with Avro.'],
    ['Stream Processing', 'KSQL / Apache Flink', 'SQL-level for simple aggregations. Flink '
     'for CEP in later phases.'],
    ['Knowledge Graph', 'Neo4j + Cypher', 'Most mature graph database. ACID. Cypher is '
     'intuitive. Bloom for graph visualization.'],
    ['Vector Store', 'Qdrant', 'Fastest vector search (Rust). Built-in hybrid. Payload '
     'filtering. Lightweight.'],
    ['Time-Series DB', 'InfluxDB OSS v2', 'Purpose-built. Downsampling, continuous queries.'],
    ['Cache/State', 'Redis', 'Sub-ms reads. Pub/Sub for SHELDRA streaming. Session state.'],
    ['Frontend', 'Next.js 14 + TypeScript', 'SSR/SSG. React Server Components. WebSocket '
     'native support.'],
    ['VR', 'A-Frame / Three.js XR', 'WebXR standard. Desktop + VR headset support. No app '
     'store required.'],
    ['LLM Serving', 'Ollama (local) / Together AI (cloud)', 'Ollama for hackathon (no cost). '
     'Together for production (lower latency).'],
    ['CI/CD', 'GitHub Actions', 'Free for public repos. Matrix builds. Tight GitHub integration.'],
    ['Infrastructure', 'Docker + Terraform', 'Containerized everything. Reproducible infra.'],
]
add_table(['Layer', 'Technology', 'Justification'], tech)

# ═══════════════════════════════════════════════════════════════════════════
# 26. AI MODELS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('26. AI Models with Justification', level=1)

models = [
    ['SHELDRA LLM', 'Llama 3 8B (Meta)', 'Open-weight, offline-capable, safety-reasoning '
     'competence. 8B fits VRAM constraints. Fine-tunable on safety domain data.'],
    ['Text Embeddings', 'E5-mistral-7b (Microsoft)', 'Best-in-class embedding quality. 4096 '
     'dim. Multilingual. Can be quantized for speed.'],
    ['PPE Detection', 'YOLOv8n (Ultralytics)', 'Real-time on CPU. 6-class PPE. Fine-tunable '
     'on custom datasets. 30+ FPS on edge.'],
    ['Person Tracking', 'YOLOv8s + ByteTrack', 'Persistent IDs across frames. Essential for '
     'SHELDRA addressing specific workers.'],
    ['Pose Estimation', 'RTMPose (OpenMMLab)', '5ms/person on GPU. 17 keypoints. Feeds '
     'SHELDRA ergonomic coaching and fall detection.'],
    ['Time-Series Anomaly', 'TimesNet (Microsoft Research)', 'ICLR 2023 Best Paper. Multi-'
     'period capture ideal for industrial cycles.'],
    ['Speech-to-Text', 'Whisper (OpenAI)', 'Multilingual. Robust to industrial noise. '
     'Tiny model for edge, Large for cloud.'],
    ['Text-to-Speech', 'ElevenLabs / Coqui TTS', 'ElevenLabs for quality. Coqui for '
     'offline/local. Both support voice customization for SHELDRA persona.'],
]
add_table(['Task', 'Model', 'Justification'], models)

# ═══════════════════════════════════════════════════════════════════════════
# 27. OPEN-SOURCE TOOLS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('27. Open-Source Tools', level=1)

oss = [
    ['Apache Kafka', 'Message streaming', 'BSL 1.1', 'Data ingestion backbone'],
    ['Neo4j', 'Graph database', 'GPL v3 / Commercial', 'Worker profiles + hazard taxonomy'],
    ['Qdrant', 'Vector search', 'Apache 2.0', 'RAG grounding for SHELDRA'],
    ['InfluxDB', 'Time-series DB', 'MIT (OSS)', 'Sensor data storage'],
    ['MinIO', 'Object storage', 'AGPL v3', 'Frame + interaction recording storage'],
    ['Redis', 'Cache + Pub/Sub', 'BSD 3-Clause', 'SHELDRA session state'],
    ['PostgreSQL', 'Relational DB', 'PostgreSQL License', 'Users, configs, audit'],
    ['FastAPI', 'Web framework', 'MIT', 'SHELDRA + Decision Tree API'],
    ['Next.js', 'React framework', 'MIT', 'SHELDRA dashboard frontend'],
    ['Three.js / R3F', '3D rendering', 'MIT', 'Holographic avatar + Digital Twin'],
    ['YOLOv8', 'Object detection', 'AGPL v3', 'SHELDRA\u2019s visual awareness'],
    ['TimesNet', 'Time-series model', 'MIT', 'Anomaly detection for Decision Tree'],
    ['Llama 3', 'LLM', 'Custom (open)', 'SHELDRA\u2019s brain'],
    ['E5', 'Text embeddings', 'MIT', 'RAG document embedding'],
    ['Whisper', 'Speech-to-text', 'MIT', 'SHELDRA voice input'],
    ['Coqui TTS', 'Text-to-speech', 'MIT', 'SHELDRA voice output (offline)'],
    ['A-Frame', 'VR framework', 'MIT', 'VR training scenes'],
    ['Docker', 'Containerization', 'Apache 2.0', 'Local dev + deployment'],
    ['Terraform', 'Infra as code', 'BSL 1.1', 'Cloud provisioning'],
]
add_table(['Tool', 'Purpose', 'License', 'SHELDRA Role'], oss)

# ═══════════════════════════════════════════════════════════════════════════
# 28. CLOUD DEPLOYMENT
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('28. Cloud Deployment Architecture', level=1)

add_para(
    'Hackathon: All services via Docker Compose on single machine (16GB RAM, optional GPU). '
    'Ollama for local SHELDRA LLM. MinIO for storage. One command: docker-compose up.'
)

add_para(
    'Production:\n'
    '- SHELDRA API + Avatar: AWS ECS Fargate (auto-scaling based on concurrent sessions)\n'
    '- SHELDRA LLM: AWS Bedrock / Together AI (managed inference, no GPU management)\n'
    '- Kafka: Confluent Cloud / MSK\n'
    '- Databases: Neo4j AuraDB, Qdrant Cloud, InfluxDB Cloud\n'
    '- Storage: AWS S3 + CloudFront\n'
    '- Frontend: Vercel (Next.js optimized)\n'
    '- Monitoring: Grafana + Prometheus + Loki\n'
    '- CI/CD: GitHub Actions \u2192 ECR \u2192 ECS blue/green'
)

# ═══════════════════════════════════════════════════════════════════════════
# 29. EVALUATION METRICS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('29. Evaluation Metrics', level=1)

metrics = [
    ['SHELDRA Response Quality', '> 90% user satisfaction (worker survey)',
     'Human evaluation on 50 interactions'],
    ['SHELDRA Response Latency', '< 2s end-to-end (voice in \u2192 voice out)',
     'Pipeline timing with streaming TTS'],
    ['Decision Tree Accuracy', '> 85% average branch accuracy',
     'Rolling 10-trial window per branch'],
    ['Tree Update Latency', '< 5 min (target: 2 min median)',
     'From outcome capture to tree version deployed'],
    ['PPE Detection Accuracy', 'mAP > 0.85 at 0.5 IoU',
     'YOLOv8 benchmark on PPE dataset'],
    ['Anomaly Detection F1', '> 0.85',
     'Precision-recall on labeled anomalies'],
    ['Personalization Differentiation', 'Clear behavioral difference between profiles',
     'A/B test: same hazard, 3 profiles, 3 different SHELDRA responses'],
    ['VR Training Score Correlation', '> 0.7 correlation with real-world performance',
     'Compare VR scores with supervisor evaluations'],
]
add_table(['Metric', 'Target', 'Method'], metrics)

# ═══════════════════════════════════════════════════════════════════════════
# 30. FUTURE ROADMAP
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('30. Future Roadmap: MVP \u2192 Enterprise SaaS', level=1)

roadmap = [
    ['MVP (Hackathon)', 'Week 1-3',
     'SHELDRA 3D avatar with voice I/O, basic personalization (3 profiles), '
     'Decision Tree with 3 pre-built trees, single facility simulation, '
     'Vision Agent for PPE feedback, basic RAG, synthetic data',
     'Working SHELDRA demo, Decision Tree update cycle proven, '
     '3-judge panel WOW moment'],
    ['Alpha', 'Month 1-2',
     'Real camera + IoT integration, 10+ Decision Trees auto-generated, '
     'personalization engine with learning speed detection, VR training scene, '
     '5-min update cycle on real data, Grafana monitoring',
     'First pilot facility, real-data validation, SOC 2 prep start'],
    ['Beta', 'Month 3-4',
     'Multi-facility SHELDRA instances, federated learning across sites, '
     'mobile app with avatar, AR overlay (HoloLens concept), '
     'SSO/RBAC, enterprise integration APIs',
     '3+ pilot facilities, partner integrations, SOC 2 readiness'],
    ['GA v1', 'Month 5-7',
     'On-premise deployment, air-gapped mode, custom SHELDRA fine-tuning, '
     'marketplace for Decision Trees, advanced personalization (emotion AI), '
     '99.9% SLA',
     '10+ paying customers, $1M+ ARR'],
    ['Enterprise SaaS', 'Month 8-12',
     'Global multi-region, cross-facility benchmarking, '
     'insurance API integration, regulatory filing automation, '
     'white-label for system integrators',
     '50+ customers, $5M+ ARR, Series A'],
    ['Platform Vision', 'Year 2+',
     'Industry-specific SHELDRA models (oil & gas, mining, logistics, healthcare), '
     'autonomous SHELDRA actions (AI-initiated lockdown for extreme scenarios), '
     'regulator-approved Safety Twin, SHELDRA app marketplace',
     'Category leader, $50M+ ARR'],
]
add_table(['Phase', 'Timeline', 'Capabilities', 'Milestones'], roadmap)

# ═══════════════════════════════════════════════════════════════════════════
# 31. RISKS AND MITIGATIONS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('31. Risks and Mitigations', level=1)

risks = [
    ['Avatar performance', 'Med', 'High', '3D avatar too heavy for hackathon hardware',
     'Fallback: 2D Lottie animation with same voice + personality. Prove 3D works but '
     'have 2D ready.'],
    ['Voice I/O in noisy hall', 'Med', 'Med', 'Demo hall noise breaks STT/TTS',
     'Text chat fallback always visible. Captions on all SHELDRA speech. '
     'Pre-record key demo segments.'],
    ['LLM latency', 'High', 'High', 'SHELDRA response > 2s breaks real-time illusion',
     'Streaming TTS (words appear as generated). Pre-generate demo responses. '
     'Show "SHELDRA thinking" animation.'],
    ['Decision Tree complexity', 'Med', 'High', 'Auto-generating valid trees from KG too complex',
     'Seed 5 expert-crafted trees. Demo update cycle on 1-2 trees. '
     'Auto-generation shown as roadmap.'],
    ['Personalization underwhelming', 'Low', 'High', 'Profiles not different enough in demo',
     'Pre-create 3 exaggerated profiles: novice (needs full handholding), '
     'experienced (brief), expert (confirmation only). Dramatize the difference.'],
    ['Integration complexity', 'High', 'Med', 'Different facility protocols, camera brands, sensors',
     'Adapter pattern from day one. REST + MQTT bridges. '
     'Start with synthetic data; real integration in alpha.'],
]
add_table(['Risk', 'Prob', 'Impact', 'Description', 'Mitigation'], risks)

# ═══════════════════════════════════════════════════════════════════════════
# 32. UNICORN THESIS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_heading('32. Why SHELDRA Can Become a Unicorn Startup', level=1)

add_heading('32.1 Market Timing', level=2)
add_para(
    '- Industrial safety market: $25B+ growing at 8% CAGR\n'
    '- Industrial AI market: $15B+ at 30% CAGR\n'
    '- OSHA fines increased 78% since 2020; severe violator program expanding\n'
    '- 2.1M US manufacturing jobs unfilled \u2014 automation of safety monitoring is necessary\n'
    '- LLMs (Llama 3), TTS (ElevenLabs), and 3D web (Three.js) have reached production maturity\n'
    '- Perfect storm: regulation + labor shortage + AI maturity + hardware affordability'
)

add_heading('32.2 Competitive Moat', level=2)
add_para(
    '1. SHELDRA is the first AI safety coach, not a dashboard.\n'
    '   Competitors build screens to watch. SHELDRA is a presence that watches over workers. '
    'This fundamental relationship inversion cannot be copied by adding a chatbot to a dashboard.\n\n'
    '2. Personalization at individual level.\n'
    '   No industrial safety system adapts to each worker\u2019s experience, learning speed, '
    'and emotional state. SHELDRA is different for every person.\n\n'
    '3. Living Decision Trees.\n'
    '   Static checklists are the industry standard. Our 5-minute update cycle creates a '
    'self-improving system that gets smarter with every incident.\n\n'
    '4. Holographic multi-modal interface.\n'
    '   Voice, 3D avatar, AR, VR, text \u2014 SHELDRA meets workers where they are. '
    'No competitor offers this range of interaction modes.\n\n'
    '5. Data network effects.\n'
    '   Every Decision Tree update across every facility improves the system for all. '
    'Privacy-preserving federated learning creates a compounding advantage.'
)

add_heading('32.3 Revenue Model', level=2)
add_para(
    '- Per-worker subscription: $50-200/worker/month depending on interaction volume\n'
    '- Tiered: SHELDRA Basic (text), SHELDRA Pro (voice + avatar), SHELDRA Enterprise (full suite)\n'
    '- Professional services: Custom avatar design, VR scenario creation, tree tuning\n'
    '- Marketplace: Community Decision Trees, SHELDRA voice packs, VR training modules\n'
    '- Target pricing: $2K-$20K/month per facility; $100K-$1M/year enterprise\n'
    '- Gross margin: 75-85%'
)

add_heading('32.4 Investor Narrative', level=2)
add_para(
    '"We are building the operating system for industrial safety \u2014 but our interface '
    'is not a dashboard. It is an AI person named SHELDRA who walks beside every worker. '
    'She sees what they see, knows what they know, adapts to how they learn, and guides '
    'them through every hazard. Her Decision Tree brain learns from every incident and '
    'updates itself every 5 minutes.\n\n'
    'Industrial safety is a $25B market with incumbents who sell yesterday\u2019s technology. '
    'SHELDRA is not a feature \u2014 she is a new category. We start with safety, but the '
    'same SHELDRA architecture applies to quality assurance, maintenance guidance, and '
    'operations training. That is a $100B+ TAM.\n\n'
    'We are not building a better dashboard. We are building every worker\u2019s '
    'personal AI safety guardian."'
)

# ── Final page ──
doc.add_page_break()
doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('"SHELDRA is not a tool.\nSHELDRA is a teammate \u2014\none that never blinks, never forgets,\nand always puts the worker first."')
run.italic = True
run.font.size = Pt(16)
run.font.color.rgb = RGBColor(0x1A, 0x3C, 0x6E)

# ── Save ──
output_path = '/Users/nayantraramakrishnan/Desktop/developer/Projects/ey-hackathon/industrial-safety-intelligence-platform-architecture.docx'
doc.save(output_path)
print(f'SHELDRA architecture document saved to: {output_path}')
