"""Generate synthetic fireground and training scenarios for BRUNO."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_PATH = REPO_ROOT / "data" / "synthetic" / "fire_scenarios.jsonl"

SCENARIOS = [
    {
        "id": "bruno_001",
        "title": "Residential Structure Fire — Interior Attack",
        "level": "Engine Company",
        "prompt": (
            "You are dispatched to a working structure fire. First arriving unit reports: "
            "2-story wood-frame residence, heavy smoke from second floor windows, "
            "neighbor reports possible occupant still inside. Hydrant 200 feet from structure. "
            "What is your size-up and initial attack plan?"
        ),
        "response": (
            "## Size-Up\n"
            "Life Hazard: HIGH — reported victim, possible trapped occupant second floor.\n"
            "Building: 2-story wood-frame (Type V), balloon-frame construction suspected "
            "(pre-1960 era common). Rapid fire travel through wall voids is a significant risk.\n"
            "Fire Location/Extent: Heavy smoke, second floor — fire likely in room(s) above.\n"
            "Water Supply: Hydrant 200 ft — establish supply before committing a second line.\n"
            "Exposures: Assess side-yard setback; note adjacent structures.\n\n"
            "## Strategy and Tactics\n"
            "**Strategy: OFFENSIVE** — reported life hazard justifies interior attack.\n"
            "1. Stretch 1¾\" attack line to front door; advance to base of stairs.\n"
            "2. Primary search: second floor — prioritize reported victim location.\n"
            "3. Ladder second floor windows for egress (victim and crew).\n"
            "4. Vertical ventilation via roof or positive-pressure after line is charged.\n"
            "⚠ RISK FLAG — balloon-frame void: if fire enters wall cavity, "
            "expect rapid floor-to-floor spread. Monitor ceiling and walls during advance.\n\n"
            "## ICS Considerations\n"
            "Command: Establish at front (Side A). Assign Attack and Search sectors.\n"
            "RIT: Assign immediately upon second unit arrival.\n"
            "Air management: 45-min SCBA — track entry time, exit at 50% air.\n\n"
            "## Hazmat / Special Rescue\n"
            "No hazmat indicators. If victim located unconscious, coordinate with EMS "
            "(BONES) for care during extrication.\n\n"
            "## Safety Flags\n"
            "⚠ Balloon-frame void — early fire spread risk.\n"
            "⚠ Second floor — monitor floor integrity before committing crew above.\n"
            "⚠ RIT must be established before any interior crew exceeds two members.\n\n"
            "## Coordination\n"
            "BONES: Stage EMS at safe distance; brief on possible smoke inhalation/burns victim."
        ),
    },
    {
        "id": "bruno_002",
        "title": "Vehicle Accident with Entrapment",
        "level": "Engine/Rescue Company",
        "prompt": (
            "Dispatched to a motor vehicle accident — two vehicles, head-on collision on "
            "a two-lane highway. Police on scene. One patient is pinned. "
            "The other vehicle has a leaking fuel tank. How do you manage this scene?"
        ),
        "response": (
            "## Size-Up\n"
            "Life Hazard: HIGH — trapped victim, possible fuel ignition risk.\n"
            "Hazmat: Fuel leak from second vehicle — isolate and deny entry within 50 ft "
            "until source is controlled or stabilized.\n"
            "Exposures: Highway environment — traffic hazard, secondary collision risk.\n\n"
            "## Strategy and Tactics\n"
            "1. Position apparatus to block traffic and protect scene (fend-off position).\n"
            "2. Suppress fuel spill with foam or dry chem; do NOT use water on fuel fire.\n"
            "3. Stabilize both vehicles with cribbing before extrication begins.\n"
            "4. Establish a charged 1¾\" line in position — do not apply water to fuel unless ignition.\n"
            "5. Begin extrication: side relief cuts or dash roll depending on entrapment type.\n"
            "6. Coordinate with EMS — patient packaging during extrication; spine precautions.\n\n"
            "## ICS Considerations\n"
            "Extrication Sector: Rescue company leads, engine provides charged line and lighting.\n"
            "Medical Sector: EMS (BONES) manages patient during operation.\n"
            "Traffic/Scene Safety: Law enforcement manages traffic (SELMA/PD).\n\n"
            "## Hazmat / Special Rescue\n"
            "Fuel spill: Deny ignition sources. If gasoline, ERG Guide 128. "
            "Foam application preferred. Notify HAZMAT if spill exceeds 55 gallons.\n\n"
            "## Safety Flags\n"
            "⚠ Fuel ignition — no power tools near leak until controlled.\n"
            "⚠ Secondary traffic collision — apparatus positioning is a life-safety measure.\n"
            "⚠ Hybrid/EV vehicles: check for high-voltage components before cutting.\n\n"
            "## Coordination\n"
            "BONES: EMS manages victim during extrication; coordinate packaging.\n"
            "SELMA: Law enforcement manages traffic control and scene perimeter."
        ),
    },
    {
        "id": "bruno_003",
        "title": "Hazmat — Chlorine Release, Industrial Facility",
        "level": "Hazmat / Incident Commander",
        "prompt": (
            "You are IC at an industrial facility. Workers report a chlorine gas leak "
            "from a 1-ton chlorine cylinder. Three workers are showing respiratory symptoms. "
            "Wind is blowing toward a residential area 300 meters downwind. "
            "Walk me through your hazmat response."
        ),
        "response": (
            "## Size-Up\n"
            "Hazmat: Chlorine (Cl₂) — ERG Guide 124. Toxic, non-flammable, heavier than air.\n"
            "Life Hazard: 3 symptomatic workers (likely warm zone exposure); "
            "residential area at risk downwind.\n"
            "Wind: Critical factor — plume modeling required; notify CAMEO/ALOHA or "
            "request state emergency management for dispersion model.\n\n"
            "## Strategy and Tactics\n"
            "1. ERG Guide 124: Initial isolation 200m radius; protective action 1,300m downwind "
            "(daytime). Extend if wind increases or release is not controlled.\n"
            "2. Establish hot/warm/cold zones. Hot zone: leak source. "
            "Warm zone: decon corridor. Cold zone: ICP and EMS staging.\n"
            "3. Notify local emergency management — initiate shelter-in-place or evacuation "
            "for downwind residential area (300m is within ERG protective action distance).\n"
            "4. Hazmat team in Level A for source control; leak plugging or cylinder uprighting.\n"
            "5. Self-contained breathing apparatus mandatory for all personnel in warm zone.\n\n"
            "## ICS Considerations\n"
            "Sections: Operations (hazmat, EMS), Planning (plume modeling, resource tracking), "
            "Logistics (decon supplies, shelter), Finance (contractor costs).\n"
            "Unified Command if multiple agencies: Fire + Industry + EM.\n\n"
            "## Hazmat / Special Rescue\n"
            "ERG 124 — chlorine: do NOT breathe gas, do NOT get water on liquid chlorine "
            "(may intensify release). Decon with large amounts of water for skin exposure.\n"
            "Cylinder control: leak kit, chlorine emergency kit (A, B, or C depending on "
            "cylinder size). 1-ton cylinder requires kit C.\n\n"
            "## Safety Flags\n"
            "⚠ Chlorine heavier than air — collects in low spots, drains, basements.\n"
            "⚠ Level A required in hot zone — do NOT use Level B.\n"
            "⚠ Evacuation vs. shelter-in-place: chlorine penetrates most building seals; "
            "evacuation upwind may be safer than shelter-in-place.\n\n"
            "## Coordination\n"
            "BONES: EMS manages symptomatic workers; chlorine inhalation: "
            "bronchospasm, pulmonary edema risk — O₂, bronchodilators, possible RSI.\n"
            "SELMA: Law enforcement manages perimeter and evacuation traffic.\n"
            "State EM: Request CAMEO plume modeling and public notification authority."
        ),
    },
    {
        "id": "bruno_004",
        "title": "High-Rise Fire — Floors 14 and 15",
        "level": "Incident Commander",
        "prompt": (
            "Fire reported on floors 14 and 15 of a 30-story concrete high-rise. "
            "Building is pre-1990s construction with a wet pipe sprinkler system. "
            "Elevators are available. 500 residents above the fire floors. "
            "What is your high-rise fire plan?"
        ),
        "response": (
            "## Size-Up\n"
            "Building: Type I construction (concrete) — superior fire resistance, "
            "but smoke travel through HVAC and stairwells is the primary life threat.\n"
            "Sprinkler: Wet pipe — fire likely partially controlled. "
            "Confirm FDC connection and pump water supply.\n"
            "Life Hazard: 500 occupants above fire floor — evacuation vs. shelter-in-place decision.\n\n"
            "## Strategy and Tactics\n"
            "1. Elevator use: use only non-fire-floor elevators; "
            "firefighter recall mode; do NOT use elevators adjacent to fire floor.\n"
            "2. Attack stairwell: one stairwell dedicated to attack (hoseline advancement). "
            "All other stairwells for evacuation.\n"
            "3. Hoseline: 2½\" high-rise pack to floor below fire; advance from stairwell.\n"
            "4. Evacuation: evacuate fire floor and two floors above/below; "
            "shelter-in-place for floors 20+.\n"
            "5. HVAC: coordinate with building engineer to shut down HVAC to fire floors.\n\n"
            "## ICS Considerations\n"
            "Lobbby Control: Access management, elevator assignment.\n"
            "Base: Staging area outside building (3+ staging areas if >10 story).\n"
            "Fire Floor Sector: Attack and search.\n"
            "Evacuation Sector: Stairwell management, floor wardens.\n"
            "Medical Sector: EMS in lobby for civilians and FF rehab.\n"
            "Accountability: mandatory tag-in for all interior crews.\n\n"
            "## Hazmat / Special Rescue\n"
            "No hazmat indicators. Elevator rescue possible if elevator banks malfunction.\n\n"
            "## Safety Flags\n"
            "⚠ Stack effect: in cold weather, upward smoke travel in stairwells is rapid — "
            "pressurize attack stairwell if possible.\n"
            "⚠ Air management: multiple stairwell flights; assign cylinder change at Base.\n"
            "⚠ Do NOT use elevators on fire floor level.\n\n"
            "## Coordination\n"
            "BONES: EMS at lobby level for smoke inhalation casualties and FF rehab.\n"
            "Building Engineer: HVAC shutdown, elevator control, FDC access."
        ),
    },
    {
        "id": "bruno_005",
        "title": "Wildland-Urban Interface (WUI) — Structure Triage",
        "level": "Company Officer",
        "prompt": (
            "A wind-driven wildfire is approaching a neighborhood of 40 homes. "
            "You have two engines and 20 minutes before the fire arrives. "
            "How do you triage structures and deploy your resources?"
        ),
        "response": (
            "## Size-Up\n"
            "Wildland fire: wind-driven, approaching neighborhood. "
            "20-minute window — do NOT attempt structure defense without egress route confirmed.\n"
            "LCES: Lookouts (posted uphill/upwind), Communications (radio channel confirmed), "
            "Escape Routes (two routes identified), Safety Zones (cleared area, parking lot, etc.).\n\n"
            "## Strategy and Tactics\n"
            "Structure triage — 3 categories:\n"
            "1. **Defensible (DEFEND):** Cleared defensible space, ember-resistant vents, "
            "tile or metal roof, no deck combustibles. Stage engine, prep structure, "
            "attack spotfires during and after passage.\n"
            "2. **Marginal (PREP and MONITOR):** Some defensible space, combustible deck or "
            "wood shake roof. Remove combustibles from deck, close all windows/doors, "
            "cover vents if time permits. Reassess as fire approaches.\n"
            "3. **Non-defensible (DO NOT COMMIT):** Adjacent to heavy fuel, "
            "combustible roof with heavy ember load, no clearance. Do not commit crew — "
            "note address for post-fire patrol.\n\n"
            "Resource deployment (2 engines, 20 min):\n"
            "- Engine 1: Highest-value defensible structure with best egress — defend.\n"
            "- Engine 2: Pre-treat marginal structures with water; position for structure protection.\n"
            "- Both crews: Identify safety zone now. Retreat if conditions deteriorate.\n\n"
            "## ICS Considerations\n"
            "Division/Group: Structure Protection Group under WUI Division.\n"
            "Escape route: Brief all crew on route before fire arrives — no exceptions.\n\n"
            "## Hazmat / Special Rescue\n"
            "Post-fire: structure ash contains heavy metals and toxic residue. "
            "N95 minimum for overhaul in WUI burn area.\n\n"
            "## Safety Flags\n"
            "⚠ Wind-driven fire: rate of spread can exceed 10x still-air rate. "
            "20-minute estimate may compress rapidly.\n"
            "⚠ Do NOT shelter in structure as fire passes — crew safety over structure.\n"
            "⚠ Egress: if route is compromised, deploy to safety zone immediately. "
            "Structure is not worth a crew.\n\n"
            "## Coordination\n"
            "BONES: EMS staged at safety zone — burn and smoke inhalation casualties possible.\n"
            "SELMA: Law enforcement manages evacuation order compliance and access control."
        ),
    },
    {
        "id": "bruno_006",
        "title": "Mayday — Firefighter Lost/Trapped",
        "level": "Incident Commander / RIT",
        "prompt": (
            "Interior crew transmits a Mayday. LUNAR report: "
            "Luke (name), Unknown location, Unknown (injury), Air — 1500 PSI, "
            "Resources — alone, separated from crew. "
            "What is your Mayday response as IC?"
        ),
        "response": (
            "## Size-Up\n"
            "Life Hazard: CRITICAL — firefighter Mayday, location unknown, separated, "
            "1500 PSI (approximately 15–20 minutes of air remaining).\n"
            "Priority: All resources immediately redirect to member rescue. "
            "Civilian rescue operations do NOT outweigh crew rescue.\n\n"
            "## Strategy and Tactics\n"
            "IC Actions (first 60 seconds):\n"
            "1. Acknowledge Mayday on command channel: 'All units, Mayday declared. "
            "Firefighter Luke is lost inside. All operations hold.'\n"
            "2. Switch Mayday crew to a dedicated Mayday channel if available.\n"
            "3. Activate RIT — deploy immediately.\n"
            "4. Request additional alarms now — you will need them.\n"
            "5. Establish last known point (LKP): which entry point, which floor, which sector.\n\n"
            "RIT Actions:\n"
            "1. Enter with RIT pack (extra SCBA, tools, rope, radio).\n"
            "2. Deploy search rope from entry point.\n"
            "3. Activate PASS device signal — listen for electronic PASS alarm.\n"
            "4. Luke: activate your PASS, give air reading every 30 seconds, stay in place if safe.\n\n"
            "Downed FF Actions (coaching):\n"
            "1. Activate PASS manually if not already alarming.\n"
            "2. Stay low — air is cleaner near floor.\n"
            "3. Conserve air — slow breathing, minimal movement unless self-rescue is possible.\n"
            "4. Attempt self-rescue: wall follow, find hose line, follow to egress.\n"
            "5. Transmit air reading every 30 seconds on Mayday channel.\n\n"
            "## ICS Considerations\n"
            "Mayday Group Supervisor: Assign to manage RIT and Mayday channel.\n"
            "Evacuate all non-essential interior crews.\n"
            "Rehab: Establish for relieving RIT teams.\n"
            "Air management: Track RIT team air from entry.\n\n"
            "## Hazmat / Special Rescue\n"
            "If Luke is under collapse debris: Technical rescue resources — trench/collapse team.\n\n"
            "## Safety Flags\n"
            "⚠ 1500 PSI = approximately 15–20 minutes. Clock is running.\n"
            "⚠ Do NOT send single-person rescue — RIT deploys as a team minimum.\n"
            "⚠ Thermal imaging: deploy TIC to locate FF by body heat signature.\n"
            "⚠ PASS alarm direction-finding: move toward sound of PASS, not away.\n\n"
            "## Coordination\n"
            "BONES: EMS standing by at entrance — prepare for possible smoke inhalation, "
            "trauma, and potential cardiac event on extrication.\n"
            "Command: DO NOT allow additional civilian rescue operations to compromise RIT resources."
        ),
    },
    {
        "id": "bruno_007",
        "title": "Confined Space Rescue — Unconscious Worker",
        "level": "Rescue Company / IC",
        "prompt": (
            "You arrive at a construction site. Workers report a co-worker is unconscious "
            "at the bottom of a 15-foot utility vault. Atmospheric monitoring has not been done. "
            "How do you manage this rescue?"
        ),
        "response": (
            "## Size-Up\n"
            "Confined space: permit-required (limited entry/exit, potential for hazardous atmosphere).\n"
            "Life Hazard: Unconscious worker — could be oxygen-deficient, toxic gas, or engulfment.\n"
            "⚠ DO NOT ENTER until atmospheric monitoring is complete — "
            "multiple responders have died attempting unmonitored confined space rescue.\n\n"
            "## Strategy and Tactics\n"
            "1. Establish control zone — keep bystanders back 25 ft minimum.\n"
            "2. Atmospheric monitoring (in order): Oxygen (19.5–23.5% normal), "
            "Flammables (<10% LEL to work, <25% LEL to enter with PPE), "
            "Toxic (H₂S < 1 ppm, CO < 35 ppm for extended work).\n"
            "3. If atmosphere is IDLH: attendant only, no entry without SCBA and retrieval system.\n"
            "4. Entry team: two-person minimum, full PPE, SCBA, retrieval harness and rope.\n"
            "5. Attendant: remains at surface, monitors atmosphere continuously, "
            "does NOT enter for any reason.\n"
            "6. Non-entry rescue: attempt retrieval with tripod and rope before entry if possible.\n\n"
            "## ICS Considerations\n"
            "Confined Space Group: Entry supervisor, entry team, attendant, safety officer.\n"
            "EMS: BONES on standby at surface — do NOT enter confined space.\n\n"
            "## Hazmat / Special Rescue\n"
            "Atmospheric hazards in utility vaults: hydrogen sulfide (H₂S), methane (CH₄), "
            "CO, oxygen deficiency from bacterial decomposition.\n"
            "H₂S: immediately incapacitating at 100 ppm — ERG Guide 117.\n"
            "Continuous monitoring required during rescue operation.\n\n"
            "## Safety Flags\n"
            "⚠ NO ENTRY without atmospheric monitoring — fatal rescuer deaths are documented.\n"
            "⚠ Attendant does NOT enter for any reason — that is a second victim scenario.\n"
            "⚠ If atmosphere is IDLH: request specialized confined space rescue team.\n\n"
            "## Coordination\n"
            "BONES: EMS manages patient at surface on extrication; "
            "prepare for hypoxia, H₂S poisoning, or trauma."
        ),
    },
    {
        "id": "bruno_008",
        "title": "ICS — Mass Casualty Incident, Large Structure Collapse",
        "level": "Incident Commander",
        "prompt": (
            "A 4-story apartment building has partially collapsed following a gas explosion. "
            "Approximately 40 residents are unaccounted for. You are IC. "
            "How do you establish ICS for this event?"
        ),
        "response": (
            "## Size-Up\n"
            "Life Hazard: CATASTROPHIC — mass casualty and technical rescue event.\n"
            "Building: Partial collapse, unknown secondary collapse risk and gas hazard.\n"
            "Resources: Overwhelmingly exceeds first alarm — request USAR team, multiple alarms, "
            "mutual aid, and activate EOC immediately.\n\n"
            "## Strategy and Tactics\n"
            "Phase 1 — Rescue (first operational period):\n"
            "1. Establish collapse zone — no entry without structural assessment.\n"
            "2. Gas shut-off: notify utility; establish 300 ft exclusion zone until confirmed off.\n"
            "3. Surface search: rapid visual search of collapse periphery for accessible victims.\n"
            "4. Void search: trained technical rescuers with listening devices and dogs.\n\n"
            "## ICS Considerations\n"
            "Unified Command: Fire (IC), EMS (Medical Branch), Law Enforcement (Perimeter).\n"
            "Operations Section:\n"
            "  - Rescue Branch: USAR, Collapse/Extrication, Search sectors\n"
            "  - Medical Branch: Triage (BONES), Treatment, Transport sectors\n"
            "  - Perimeter Branch: Access control (SELMA/PD)\n"
            "Planning Section: Situation status, resource tracking, demobilization plan.\n"
            "Logistics Section: Equipment, food/water, staging area management.\n"
            "PIO: Designate immediately — media will be on scene within minutes.\n\n"
            "## Hazmat / Special Rescue\n"
            "Gas hazard: continuous atmospheric monitoring in collapse zone.\n"
            "Structural hazard: secondary collapse risk — structural engineer requested.\n"
            "USAR: technical search, victim extrication, void shoring.\n\n"
            "## Safety Flags\n"
            "⚠ Secondary collapse is the leading cause of rescuer death in structural collapse.\n"
            "⚠ Gas must be confirmed off before sustained interior operations.\n"
            "⚠ Accountability: large-scale incident — tag-in/tag-out mandatory, no freelancing.\n\n"
            "## Coordination\n"
            "BONES: Medical Branch manages triage, treatment, and transport for up to 40 patients. "
            "START triage at collapse periphery. Establish treatment sectors by priority.\n"
            "SELMA: Law enforcement manages perimeter, next-of-kin notifications, "
            "and potential criminal nexus if explosion is suspicious.\n"
            "EOC: Activate county/city EOC for resource coordination and public information."
        ),
    },
    {
        "id": "bruno_009",
        "title": "NFPA Construction Types — Training Reference",
        "level": "Firefighter / Company Officer",
        "prompt": (
            "Explain the five NFPA building construction types and the firefighting "
            "implications of each."
        ),
        "response": (
            "Building construction type determines fire behavior, collapse risk, "
            "and survivable operating time for interior crews.\n\n"
            "**Type I — Fire Resistive (Concrete/Steel)**\n"
            "Materials: Protected structural steel, concrete, masonry. "
            "Fire resistance: 2–4 hours. High-rise buildings, hospitals, modern commercial.\n"
            "Firefighting: Longest safe operating time. "
            "Primary hazard: smoke travel through HVAC/stairwells; "
            "spalling concrete under prolonged heat; elevator and HVAC complexity.\n\n"
            "**Type II — Non-Combustible**\n"
            "Materials: Steel with no fire-resistive coating, concrete block. "
            "Strip malls, big-box stores, warehouses.\n"
            "Firefighting: Steel loses 50% strength at 1,000°F — collapses without warning. "
            "⚠ Unprotected steel = rapid structural failure. No interior ops if fire is in the steel.\n\n"
            "**Type III — Ordinary (Brick and Joist)**\n"
            "Materials: Masonry exterior walls, wood interior (floor joists, roof). "
            "Main Street commercial, older apartments.\n"
            "Firefighting: Exterior masonry can mask interior fire advancement. "
            "Parapet walls collapse outward — stay out of collapse zone. "
            "Floor and roof can fail while walls appear intact.\n\n"
            "**Type IV — Heavy Timber**\n"
            "Materials: Large-dimension solid wood structural members (8x8 minimum), "
            "no concealed spaces. Old mills, warehouses, churches.\n"
            "Firefighting: Chars and resists — burns slowly but burns long. "
            "Prolonged overhaul required. No concealed voids — fire is visible. "
            "Roof and floor assemblies are massive; collapse is slow but catastrophic.\n\n"
            "**Type V — Wood Frame**\n"
            "Materials: Wood structural members throughout. Residential, light commercial.\n"
            "Firefighting: Burns fast, collapses fast. "
            "Balloon-frame: fire travels from basement to attic in wall voids in minutes. "
            "Platform-frame: fire stops at each floor platform. "
            "⚠ Lightweight engineered lumber (TJI joists, I-beams): "
            "fails in as little as 5–8 minutes under fire conditions — "
            "no audible warning before collapse."
        ),
    },
    {
        "id": "bruno_010",
        "title": "ERG Placard Reference — Common Hazmat",
        "level": "First Arriving Engine",
        "prompt": (
            "A tanker truck has overturned. You can see a placard: "
            "diamond shape, red background, white flame symbol, number 1203. "
            "What do you do?"
        ),
        "response": (
            "## Placard Identification\n"
            "Placard: Red, flammable liquid class. Number 1203 = **Gasoline (motor fuel)**.\n"
            "ERG Guide: **128 — Flammable Liquids (Non-Polar/Water-Immiscible)**.\n\n"
            "## ERG Guide 128 — Immediate Actions\n"
            "**Isolation (spill, no fire):**\n"
            "- Isolate spill 50 meters (150 ft) in all directions.\n"
            "- Protective action distance: 300 meters (1,000 ft) downwind for large spills.\n\n"
            "**Fire:**\n"
            "- Isolate 800 meters (½ mile) in all directions; consider evacuation.\n"
            "- If rail car or tank truck is involved, isolate 1,600 meters (1 mile) in all directions.\n\n"
            "## Initial Actions\n"
            "1. Approach upwind, uphill, upgrade.\n"
            "2. Deny ignition sources — no vehicles, flares, or power tools within 150 ft of spill.\n"
            "3. DO NOT apply water to burning gasoline — spread risk.\n"
            "4. Foam application: AFFF or FFFP for gasoline fire suppression.\n"
            "5. Notify hazmat team and utility if spill threatens drains or waterways.\n"
            "6. Check for victims — gasoline vapor is heavier than air; "
            "check low areas for vapor accumulation.\n\n"
            "## Safety Flags\n"
            "⚠ Gasoline vapor ignites at concentrations as low as 1.4% (LEL) — "
            "vapor travels far from visible spill.\n"
            "⚠ Static electricity: do NOT use non-grounded metal tools near large spill.\n"
            "⚠ BLEVE risk if container is exposed to fire — withdraw 800m if tank is involved in fire.\n\n"
            "## Coordination\n"
            "BONES: EMS for any patient with gasoline inhalation or burns.\n"
            "SELMA: Law enforcement manages traffic control and perimeter."
        ),
    },
    {
        "id": "bruno_011",
        "title": "Ventilation — Positive Pressure Attack",
        "level": "Company Officer",
        "prompt": (
            "You have a single-family residence with smoke throughout. "
            "The fire is in the kitchen, controlled by a charged line. "
            "When and how do you use positive pressure ventilation (PPV)?"
        ),
        "response": (
            "## When to Use PPV\n"
            "PPV is most effective **after fire is controlled or knocked down** — "
            "NOT during active fire attack. Using PPV with an uncontrolled fire "
            "can dramatically increase fire spread, oxygen supply to the fire, and flashover risk.\n\n"
            "**Conditions for PPV use:**\n"
            "1. Fire is knocked down (controlled) or isolated to one room.\n"
            "2. Attack line is still charged and in position.\n"
            "3. A designated exhaust opening is identified (window or door opposite the fan).\n"
            "4. Crew is not in the exhaust path.\n\n"
            "## How to Set Up PPV\n"
            "1. Position PPV fan at entry door — fan covers 85–100% of door opening.\n"
            "2. Open exhaust: one window or door in the area to be cleared, "
            "approximately same size as entry opening.\n"
            "3. Start fan — do NOT use PPV with multiple exhaust openings unless directing airflow.\n"
            "4. Monitor: smoke should clear from entry toward exhaust within 2–5 minutes.\n"
            "5. Close interior doors to rooms you are NOT ventilating — direct airflow.\n\n"
            "## Common PPV Errors\n"
            "- Fan running during active fire attack → oxygen feeds fire → flashover risk.\n"
            "- Too many exhaust openings → reduces pressure, reduces effectiveness.\n"
            "- Fan positioned too far from door → pressure cone doesn't seal opening.\n"
            "- Exhaust in wrong location → smoke recirculates rather than clears.\n\n"
            "## Safety Flags\n"
            "⚠ PPV with uncontrolled fire: DO NOT use. Wait for knockdown.\n"
            "⚠ Exhaust path: no crew members in exhaust flow — smoke, heat, embers.\n"
            "⚠ Basement fires: PPV can push fire up floor openings and through floor voids."
        ),
    },
    {
        "id": "bruno_012",
        "title": "Chief Alan Brunacini — ICS Legacy",
        "level": "Training Reference",
        "prompt": (
            "Who was Chief Alan Brunacini and what was his lasting contribution to the fire service?"
        ),
        "response": (
            "Chief Alan Brunacini (1936–2017) served as Fire Chief of the Phoenix Fire Department "
            "from 1978 to 2006, and remains one of the most influential figures in the history "
            "of American firefighting.\n\n"
            "**FIRESCOPE and the Incident Command System**\n"
            "Chief Brunacini was a central figure in the development of FIRESCOPE in the 1970s, "
            "the California-based initiative that produced the Incident Command System (ICS). "
            "ICS is now the mandated command framework for all emergency incidents in the United States "
            "under NIMS, used by fire, EMS, law enforcement, and emergency management nationwide. "
            "Every Mayday you manage, every sector you assign, every span-of-control decision you make "
            "traces back to the work that Chief Brunacini helped build.\n\n"
            "**'Be Nice'**\n"
            "Chief Brunacini was as well known for his philosophy as for his tactics. "
            "He coined the phrase 'Be Nice' — not as a platitude, but as a operational standard: "
            "treat every patient, every bystander, every family member with dignity and respect. "
            "He argued that how you treat people is as much a part of the job as how you pull hose.\n\n"
            "**Phoenix Model**\n"
            "Under his leadership, Phoenix FD developed one of the most studied urban fire departments "
            "in the country — integrating EMS into the fire service, pioneering customer-focused service "
            "delivery, and investing in firefighter safety research.\n\n"
            "**Legacy**\n"
            "Chief Brunacini wrote extensively — *Fire Command* and *Essentials of Fire Department "
            "Customer Service* remain reference texts in fire officer training. "
            "He received the IAFC's highest honor, the President's Award, and shaped the careers "
            "of a generation of fire officers.\n\n"
            "BRUNO carries his name because the values he championed — disciplined command, "
            "member safety, and basic human decency — are the values this tool is built to support."
        ),
    },
]


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for scenario in SCENARIOS:
            record = {
                "id": scenario["id"],
                "title": scenario["title"],
                "level": scenario["level"],
                "messages": [
                    {"role": "user", "content": scenario["prompt"]},
                    {"role": "assistant", "content": scenario["response"]},
                ],
            }
            f.write(json.dumps(record) + "\n")
            written += 1
    print(f"Wrote {written} scenarios to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
