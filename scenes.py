SCENES = {
    "menu_main": {
        "title": "Clockwork Collapse (working title)",
        "text_blocks": [
            {
                "text": "A text-based mystery RPG.\n\nChoose an option to begin."
            }
        ],
        "choices": [
            {
                "id": "menu_new_game",
                "label": "New Game",
                "next": "intro",
            },
            {
                "id": "load_game",
                "label": "Load game",
                "next": "LOAD",
            },
            {
                "id": "menu_quit",
                "label": "Quit Game",
                "next": "QUIT",
            }
        ],
    },

    "intro": {
        "title": "Clockwork Collapse",
        "text_blocks": [
            {
                "text": """CLOCKWORK COLLAPSE

The city of Chronvale runs on time.

Every clock synchronized. Every schedule precise. Every citizen on track.

The Meridian Engine ensures it.

You work near the Engine. You trust the system.

Today is routine.

(Or so you think.)"""
            }
        ],
        "choices": [
            {
                "id": "intro_begin",
                "label": "[Begin]",
                "next": "character_creation"
            }
        ]
    },

    "character_creation": {
        "title": "Sign In",
        "text_blocks": [
            {
                "text": """Before your shift begins, you sign in at the terminal.

NAME: _____________

[Enter your name when prompted]"""
            }
        ],
        "choices": [
            {
                "id": "char_continue",
                "label": "[Continue]",
                "next": "demo_01_workspace_entry",
                "effects": {
                    "flags": {"mq_01_assigned": True}
                },
                "start_quest": "mq_routine_stabilization"
            }
        ]
    },

    "demo_01_workspace_entry": {
        "title": "Administrative Annex",
        "text_blocks": [
            {
                "text": """You return to your workstation in the administrative annex.

The Meridian Engine hums beneath your feet—a deep, constant vibration that never stops. Readouts flicker on nearby terminals. Status lights blink green.

Davies is back at his desk, head down, working on something. He doesn't look up as you pass.

Your terminal still displays your task assignment: Panel 7-B, Gauges 14 through 18.""",
                "condition": {"requires_flag": "talked_to_davies"}
            },
            {
                "text": """You arrive at your workstation in the administrative annex.

The Meridian Engine hums beneath your feet—a deep, constant vibration that never stops. Readouts flicker on nearby terminals. Status lights blink green.

Everything is normal.

A coworker, Davies, waves from across the room. "Morning. Got your task assignment yet?"

You check the terminal. Today's order: routine maintenance check on the task floor instrumentation.""",
                "condition": {"requires_flag_false": "talked_to_davies"}
            }
        ],
        "choices": [
            {
                "id": "workspace_to_task_floor",
                "label": "Head to the task floor",
                "next": "demo_01_task_floor"
            },
            {
                "id": "workspace_to_break",
                "label": "Talk to Davies first",
                "next": "demo_01_break_area"
            },
            {
                "id": "workspace_to_supply",
                "label": "Check the supply cage",
                "next": "demo_01_supply_cage",
            },
        ]
    },

    "demo_01_break_area": {
        "title": "Break Area",
        "text_blocks": [
            {
                "text": """You walk over to Davies, who's pouring himself a cup of something that only barely qualifies as coffee.

"Another day, another calibration," he says with a tired grin. "You get used to it. Engine's been running smooth lately though. No major pulses this week."

He takes a sip and winces.

"Well, mostly smooth. Couple clocks in Sector 4 drifted yesterday, but that's normal tolerance. Nothing to worry about."

He pauses.

"Right?"

Before you can respond, he shakes his head. "Anyway. I've got gauges to check. See you at lunch."

He walks off, already forgetting the question he just asked.""",
                "condition": {"requires_flag_false": "talked_to_davies"}
            },
            {
                "text": """Davies is still here, refilling his coffee cup.

He glances up as you approach, then looks confused. "Hey... didn't we just talk?"

You tell him it's been a few minutes.

He frowns. "Right. Yeah. Sorry, must've spaced out." He takes another sip of coffee and returns to his work.""",
                "condition": {"requires_flag": "talked_to_davies"}
            }
        ],
        "choices": [
            {
                "id": "break_to_task_floor",
                "label": "Head to the task floor",
                "next": "demo_01_task_floor",
                "effects": {
                    "flags": {"talked_to_davies": True}
                }
            },
            {
                "id": "break_to_supply",
                "label": "Check the supply cage first",
                "next": "demo_01_supply_cage",
                "effects": {
                    "flags": {"talked_to_davies": True}
                }
            },
            {
                "id": "break_to_workspace",
                "label": "Return to your workstation",
                "next": "demo_01_workspace_entry",
                "effects": {
                    "flags": {"talked_to_davies": True}
                }
            }
        ]
    },

"demo_01_supply_cage": {
    "title": "Supply Cage",
    "text_blocks": [
        {
            "text": """The supply cage is a cramped maintenance storage area lined with wire shelving. Tools, spare parts, and dusty equipment manuals fill the space.

A work order is pinned to the bulletin board:

"MAINTENANCE REQUEST: Component retrieval needed. Storage tunnel access required. See Hendricks if available."

The request is dated three days ago. No one seems to have taken it.""",
            "condition": {"requires_flag_false": "opt_01_component_retrieved"}
        },
        {
            "text": """The supply cage is a cramped maintenance storage area lined with wire shelving. Tools, spare parts, and dusty equipment manuals fill the space.

The work order you completed is still pinned to the bulletin board, but someone has stamped it "COMPLETED" in red ink.

You don't remember doing that.""",
            "condition": {"requires_flag": "opt_01_component_retrieved"}
        }
    ],
    "choices": [
        {
            "id": "supply_take_quest",
            "label": "Take the work order (Optional Quest)",
            "next": "opt_01_hook",
            "effects": {
                "flags": {"opt_01_started": True}
            },
            "start_quest": "opt_01_component_retrieval",
            "condition": {"requires_flag_false": "opt_01_component_retrieved"}
        },
        {
            "id": "supply_to_task_floor",
            "label": "Ignore it and head to task floor",
            "next": "demo_01_task_floor"
        },
        {
            "id": "supply_to_workspace",
            "label": "Return to workspace",
            "next": "demo_01_workspace_entry"
        }
    ]
},

"demo_01_task_floor": {
    "title": "Task Floor",
    "text_blocks": [
        {
            "text": """The task floor is a maze of pressure gauges, flow regulators, and status panels. Everything is labeled with faded tags and cryptic abbreviations.

You locate your assigned instruments: Panel 7-B, Gauges 14 through 18.

You begin the inspection.

Gauge 14: Normal.
Gauge 15: Normal.
Gauge 16: Normal.
Gauge 17: Normal.
Gauge 18: ...

You blink.

Gauge 18 reads normal. But you could have sworn—just for a second—the needle was pointing somewhere else entirely.

You tap the glass. The needle stays steady.

Must have been a trick of the light."""
        }
    ],
    "choices": [
        {
            "id": "task_floor_complete",
            "label": "Mark inspection complete and move on",
            "next": "demo_02_corridor",
            "effects": {
                "flags": {
                    "mq_02_task_performed": True,
                    "noticed_first_anomaly": True
                }
            }
        },
        {
            "id": "task_floor_log_anomaly",
            "label": "Log the gauge reading as questionable",
            "next": "demo_02_corridor",
            "effects": {
                "flags": {
                    "mq_02_task_performed": True,
                    "noticed_first_anomaly": True,
                    "documented_gauge_anomaly": True
                }
            }
        }
    ]
},

"demo_02_corridor": {
    "title": "Corridor",
    "text_blocks": [
        {
            "text": """You head back through the corridor toward the administrative section.

Ahead of you, Davies is walking in the same direction.

You catch up. "Hey, finished already?"

He turns, looking slightly confused. "Finished what?"

"The gauges. You said you had gauges to check."

He frowns. "I... yeah. Right. I did say that."

There's a pause.

"When did I say that?"

You stare at him.

He laughs awkwardly. "Sorry, long shift. My head's all over the place today. Anyway, I've got gauges to check. See you at lunch."

He walks off.

You're certain he already said that exact sentence less than twenty minutes ago."""
        }
    ],
    "choices": [
        {
            "id": "corridor_follow_davies",
            "label": "Follow Davies and ask him about it",
            "next": "demo_02_corridor_followup",
            "effects": {
                "flags": {"mq_03_anomalies_noted": True}
            }
        },
        {
            "id": "corridor_let_go",
            "label": "Let it go and head back to workspace",
            "next": "demo_end_vertical_slice",
            "effects": {
                "flags": {"mq_03_anomalies_noted": True}
            }
        }
    ]
},

"demo_02_corridor_followup": {
    "title": "Corridor",
    "text_blocks": [
        {
            "text": """You call after Davies. "Wait—are you okay? You just told me that."

He stops and looks back, puzzled. "Told you what?"

"That you have gauges to check. Word for word. The exact same thing."

Davies stares at you for a moment, then shrugs. "Well... I do have gauges to check. It's my job." He seems genuinely unbothered.

"Look, if you're worried about me, I'm fine. Maybe you're the one who needs a break."

He gives you a friendly pat on the shoulder and walks away, already humming to himself.

You stand alone in the corridor.

Something is wrong."""
        }
    ],
    "choices": [
        {
            "id": "followup_continue",
            "label": "[Continue]",
            "next": "demo_end_vertical_slice",
            "effects": {
                "flags": {"confronted_davies": True}
            }
        }
    ]
},

"demo_end_vertical_slice": {
    "title": "Administrative Annex",
    "text_blocks": [
        {
            "text": """You stand in the corridor, trying to process what just happened.

Davies said the same thing twice. Word for word. And he didn't remember saying it the first time.

The Meridian Engine's hum feels different now. Oppressive. Like it's hiding something.

You need answers."""
        }
    ],
    "choices": [
        {
            "id": "vertical_to_records",
            "label": "Check the records archive",
            "next": "demo_02_records_entrance"
        },
        {
            "id": "vertical_to_city",
            "label": "Head to the city edge",
            "next": "demo_02_city_edge"
        }
    ]
},

"demo_02_records_entrance": {
    "title": "Records Archive - Entrance",
    "text_blocks": [
        {
            "text": """The Records Archive is located in a forgotten corner of the facility, down two flights of stairs and through a corridor that nobody uses anymore.

The door is unlocked. Inside, rows of filing cabinets and old terminals line the walls. Dust hangs in stale air. A single flickering light illuminates the space.

Everything here predates the digital system. Paper records. Maintenance logs. Incident reports.

If something's wrong with the Engine, there might be traces of it here.""",
            "condition": {"requires_flag_false": "visited_records"}
        },
        {
            "text": """You return to the Records Archive.

The dust-filled room is just as you left it. Files scattered across tables. The flickering light casting shadows on the walls.

After your encounter with Warden Kess, you shouldn't linger here. You've already drawn too much attention.""",
            "condition": {"requires_flag": ["visited_records", "met_warden_kess"]}
        },
        {
            "text": """You return to the Records Archive.

The dust-filled room is just as you left it. Files scattered across tables. The flickering light casting shadows on the walls.

The answers you found here raised more questions than they answered.""",
            "condition": {"requires_flag": "visited_records", "requires_flag_false": "met_warden_kess"}
        }
    ],
    "choices": [
        {
            "id": "records_search_anomalies",
            "label": "Search for anomaly reports",
            "next": "demo_02_records_anomalies",
            "effects": {
                "flags": {"visited_records": True}
            },
            "condition": {"requires_flag_false": ["found_anomaly_report", "met_warden_kess"]}
        },
        {
            "id": "records_search_maintenance",
            "label": "Check maintenance logs",
            "next": "demo_02_records_maintenance",
            "effects": {
                "flags": {"visited_records": True}
            },
            "condition": {"requires_flag_false": ["found_maintenance_log", "met_warden_kess"]}
        },
        {
            "id": "records_to_city",
            "label": "Head to the city edge instead",
            "next": "demo_02_city_edge",
            "condition": {"requires_flag_false": "visited_records"}
        },
        {
            "id": "records_leave",
            "label": "Leave the archive",
            "next": "demo_end_vertical_slice"
        }
    ]
},

"demo_02_records_anomalies": {
    "title": "Records Archive - Anomaly Reports",
    "text_blocks": [
        {
            "text": """You pull open a drawer labeled "ANOMALY REPORTS - ARCHIVED."

Most of the files are decades old. Equipment malfunctions. Sensor drift. Nothing unusual.

Then you find one dated six months ago.

"TEMPORAL ECHO EVENT - SUBLEVEL 3"

The report describes workers experiencing déjà vu. Repeated conversations. Objects appearing in places they'd already been moved from.

The conclusion: "Acceptable variance. No action required."

But someone crossed out that line in red pen and wrote: "NOT ACCEPTABLE."

The signature is illegible."""
        }
    ],
    "choices": [
        {
            "id": "anomaly_to_maintenance",
            "label": "Check the maintenance logs",
            "next": "demo_02_records_maintenance",
            "effects": {
                "flags": {"found_anomaly_report": True}
            },
            "condition": {"requires_flag_false": "found_maintenance_log"}
        },
        {
            "id": "anomaly_keep_looking",
            "label": "Keep searching for more reports",
            "next": "demo_02_records_deeper",
            "effects": {
                "flags": {"found_anomaly_report": True}
            }
        }
    ]
},

"demo_02_records_maintenance": {
    "title": "Records Archive - Maintenance Logs",
    "text_blocks": [
        {
            "text": """The maintenance logs are more recent. You recognize some of the handwriting—Davies, Hendricks, others from your shift.

Most entries are routine. Pressure adjustments. Calibration checks. Standard procedures.

But then you notice something odd.

Three weeks ago, there's an entry: "Chronometric stabilizer adjusted. Pulse frequency reduced."

Two weeks ago: "Stabilizer adjusted again. Temporal drift compensated."

One week ago: "Stabilizer requires constant recalibration. Recommend investigation."

The next entry is dated yesterday: "Investigation cancelled. Resume normal operations."

That doesn't make sense. Who cancelled it? And why?"""
        }
    ],
    "choices": [
        {
            "id": "maintenance_to_anomalies",
            "label": "Look for anomaly reports",
            "next": "demo_02_records_anomalies",
            "effects": {
                "flags": {"found_maintenance_log": True}
            },
            "condition": {"requires_flag_false": "found_anomaly_report"}
        },
        {
            "id": "maintenance_keep_looking",
            "label": "Keep searching",
            "next": "demo_02_records_deeper",
            "effects": {
                "flags": {"found_maintenance_log": True}
            }
        }
    ]
},

"demo_02_records_deeper": {
    "title": "Records Archive",
    "text_blocks": [
        {
            "text": """You dig deeper into the files.

There's a pattern here. Every few months, someone reports temporal anomalies. Equipment behaving strangely. Time seeming to skip or repeat.

And every time, the reports are marked "resolved" or "acceptable variance."

But they're not resolved. They're just... filed away.

You hear footsteps in the corridor outside.

Heavy. Deliberate.

Someone's coming."""
        }
    ],
    "choices": [
        {
            "id": "deeper_continue",
            "label": "Continue",
            "next": "demo_02_security_encounter"
        }
    ]
},

"demo_02_security_encounter": {
    "title": "Records Archive",
    "text_blocks": [
        {
            "text": """The door opens. A security officer steps inside—tall, severe, wearing the dark uniform of Engine Security.

Her badge reads: WARDEN KESS.

She looks at you. Her expression is unreadable.

"You're not authorized to be here."

Her voice is flat. Mechanical. Like she's said this exact line a thousand times before.

"This area is restricted. Return to your station immediately."

She doesn't wait for your response. She simply stands there, blocking the doorway, waiting for you to comply."""
        }
    ],
    "choices": [
        {
            "id": "security_comply",
            "label": "Apologize and leave",
            "next": "demo_02_after_security",
            "effects": {
                "flags": {"met_warden_kess": True, "complied_with_security": True}
            }
        },
        {
            "id": "security_question",
            "label": "Ask about the anomaly reports",
            "next": "demo_02_security_confrontation",
            "effects": {
                "flags": {"met_warden_kess": True, "questioned_security": True}
            }
        }
    ]
},

"demo_02_security_confrontation": {
    "title": "Records Archive",
    "text_blocks": [
        {
            "text": """You hold up the anomaly report. "What is this? Why are these reports being ignored?"

Warden Kess doesn't react. Her eyes don't even flicker to the paper.

"Those reports have been addressed. The Engine is functioning within acceptable parameters."

"Acceptable?" You gesture to the log. "People are experiencing temporal anomalies. Time is—"

"Time," she interrupts, "is not your concern. The Engine is stable. Return to your station."

Something about the way she says it makes your skin crawl. Like she's not just enforcing protocol—she's reciting it.

You notice her badge. It's not quite right. The metal is slightly warped, like it's been exposed to intense heat.

She takes a step closer. "This is your only warning."""
        }
    ],
    "choices": [
        {
            "id": "confrontation_leave",
            "label": "Leave the archive",
            "next": "demo_02_after_security"
        },
        {
            "id": "confrontation_press",
            "label": "Press her for answers",
            "next": "demo_02_security_escalation"
        }
    ]
},

"demo_02_security_escalation": {
    "title": "Records Archive",
    "text_blocks": [
        {
            "text": """"I need to know what's happening," you insist. "Davies is repeating himself. The gauges are acting strange. Something is wrong with—"

Warden Kess's hand moves to her radio.

Then everything stops.

The lights flicker.

The Engine's hum shifts—drops an octave—then surges back up.

For a fraction of a second, you see Warden Kess standing in a different position. Three feet to the left. Her expression different. Confused.

Then reality snaps back.

She's in front of you again, hand still reaching for her radio. She blinks. Looks around.

"What... what was I—"

The radio crackles. A voice: "All personnel, Code Amber. Temporal fluctuation detected. Remain at your stations."

Warden Kess stares at you. For the first time, there's something human in her eyes.

Fear.

"Get out of here," she whispers. "Now."""
        }
    ],
    "choices": [
        {
            "id": "escalation_leave",
            "label": "Leave immediately",
            "next": "demo_02_after_security"
        }
    ]
},

"demo_02_after_security": {
    "title": "Corridor",
    "text_blocks": [
        {
            "text": """You hurry through the corridors back toward the administrative section.

The Engine's hum is different now. Wrong. Like a heartbeat that's skipping.

Around you, the facility feels... unstable. Lights flicker. Shadows seem to move in ways they shouldn't.

You need to figure out what's happening before it gets worse."""
        }
    ],
    "choices": [
        {
            "id": "after_security_investigate_further",
            "label": "Investigate the Engine sector directly",
            "next": "demo_03_engine_approach"
        }
    ]
},

"demo_02_city_edge": {
    "title": "City Edge - Civilian Quarter",
    "text_blocks": [
        {
            "text": """You emerge into the civilian quarter at the city's edge—a stark contrast to the industrial zones you're used to.

Market stalls line the street. People move about their daily routines. Clocks on every corner tick in perfect synchronization.

Everything seems normal here.

But as you watch, you notice something odd. A woman walks past carrying groceries. You blink, and she's walking past again. Same groceries. Same pace. Same vacant expression.

No one else seems to notice.""",
            "condition": {"requires_flag_false": "witnessed_civilian_loop"}
        },
        {
            "text": """The civilian quarter continues its unsettling routine.

The woman with groceries still loops past. Over and over. The same path. The same vacant stare.

Market stalls remain open, but the vendors seem... automatic. Going through motions without thought.

The temporal anomalies are everywhere here.""",
            "condition": {"requires_flag": "witnessed_civilian_loop"}
        }
    ],
    "choices": [
        {
            "id": "city_investigate_civilian",
            "label": "Approach the woman",
            "next": "demo_02_city_civilian_talk",
            "condition": {"requires_flag_false": "witnessed_civilian_loop"}
        },
        {
            "id": "city_to_optional_quest",
            "label": "Check the bulletin board",
            "next": "opt_02_hook",
            "condition": {"requires_flag_false": "opt_02_started"}
        },
        {
            "id": "city_return_corridor",
            "label": "Return to the facility",
            "next": "demo_02_city_return_to_corridor"
        }
    ]
},

"demo_02_city_civilian_talk": {
    "title": "City Edge",
    "text_blocks": [
        {
            "text": """You step in front of the woman. "Excuse me, are you alright?"

She stops. Looks at you with glassy eyes.

"I'm fine. Just getting groceries." Her voice is flat. Rehearsed.

"Have we met before? I feel like I've seen you—"

"Just getting groceries," she repeats, cutting you off. The exact same intonation.

She steps around you and continues walking.

A few seconds later, you see her again at the far end of the street, walking toward you. Same groceries. Same pace.

Looping."""
        }
    ],
    "choices": [
        {
            "id": "civilian_talk_continue",
            "label": "Investigate further",
            "next": "demo_02_city_edge",
            "effects": {
                "flags": {"witnessed_civilian_loop": True}
            }
        }
    ]
},

"demo_02_city_return_to_corridor": {
    "title": "Facility Corridor",
    "text_blocks": [
        {
            "text": """You return to the facility corridors.

The civilian quarter felt wrong. People moving through routines like clockwork. Looping. Repeating.

The temporal anomalies aren't confined to the Engine facility. They're spreading into the city itself.

You need to find out what's causing this.""",
            "condition": {"requires_flag_false": "returned_from_city"}
        },
        {
            "text": """You're back in the facility corridors.

The Engine's hum feels more oppressive after witnessing what's happening in the city. The anomalies are everywhere now.

You need to decide your next move.""",
            "condition": {"requires_flag": "returned_from_city"}
        }
    ],
    "choices": [
        {
            "id": "return_corridor_to_records",
            "label": "Head to the records archive",
            "next": "demo_02_records_entrance",
            "effects": {
                "flags": {"returned_from_city": True}
            },
            "condition": {"requires_flag_false": "met_warden_kess"}
        },
        {
            "id": "return_corridor_to_city",
            "label": "Return to city edge",
            "next": "demo_02_city_edge",
            "effects": {
                "flags": {"returned_from_city": True}
            },
            "condition": {"requires_flag_false": "met_warden_kess"}
        },
        {
            "id": "return_corridor_to_engine",
            "label": "Investigate the Engine sector directly",
            "next": "demo_03_engine_approach",
            "condition": {"requires_flag": "met_warden_kess"}
        }
    ]
},

"opt_02_hook": {
    "title": "City Edge - Bulletin Board",
    "text_blocks": [
        {
            "text": """A bulletin board outside the market displays various notices and requests.

One catches your eye:

"HELP NEEDED: Strange creature in basement. Shopkeeper too scared to go down. Reward offered."

The notice is dated today, but the paper looks weeks old. Faded. Like it's been here longer than it should have been.""",
            "condition": {"requires_flag_false": "opt_02_started"}
        },
        {
            "text": """The bulletin board still displays the notice about the basement creature.

You've already dealt with that. The glitch-rat is gone, though the shopkeeper didn't seem eager to spread the word about what really happened down there.""",
            "condition": {"requires_flag": "opt_02_completed"}
        }
    ],
    "choices": [
        {
            "id": "opt_02_accept",
            "label": "Take the job (Optional Quest)",
            "next": "opt_02_investigation_site",
            "effects": {
                "flags": {"opt_02_started": True}
            },
            "start_quest": "opt_02_city_cleanup",
            "condition": {"requires_flag_false": "opt_02_started"}
        },
        {
            "id": "opt_02_decline",
            "label": "Leave the bulletin board",
            "next": "demo_02_city_edge"
        }
    ]
},

"opt_02_investigation_site": {
    "title": "Market Basement",
    "text_blocks": [
        {
            "text": """You descend into the basement beneath the market.

It's dark. Cramped. Filled with old supplies and discarded equipment.

The air feels strange here. Thick. Like you're moving through water.

Then you hear it.

Scratching. Just like in Storage Tunnel B-4.

But louder. More aggressive."""
        }
    ],
    "choices": [
        {
            "id": "opt_02_proceed",
            "label": "Move toward the sound",
            "next": "opt_02_rat_encounter_city"
        },
        {
            "id": "opt_02_retreat",
            "label": "This is too dangerous. Leave.",
            "next": "demo_02_city_edge",
            "effects": {
                "flags": {"opt_02_started": False}
            }
        }
    ]
},

"opt_02_rat_encounter_city": {
    "title": "Market Basement - Combat",
    "text_blocks": [
        {
            "text": """A rat emerges from the shadows.

No—not a rat. Not anymore.

It's larger than the one you saw in the storage tunnel. Its movements are worse—violently stuttering through space. One moment near the wall. The next, inches from your face.

It lunges.

[COMBAT PLACEHOLDER - Press to continue]

You manage to drive it back with a metal rod, but it doesn't flee. It just... stops. Frozen mid-lunge.

Then it flickers.

And vanishes.

Like it was never there.""",
            "condition": {"requires_flag_false": "fought_glitch_rat"}
        },
        {
            "text": """Another rat. Just like before.

Larger. More unstable. Its movements jagged and wrong.

But this time, you're ready.

[COMBAT PLACEHOLDER - Press to continue]

You defeat it quickly. It flickers out of existence, leaving nothing behind but a faint distortion in the air.

These creatures aren't natural. They're side effects. Temporal echoes given form.""",
            "condition": {"requires_flag": "fought_glitch_rat"}
        }
    ],
    "choices": [
        {
            "id": "opt_02_aftermath",
            "label": "Search the area",
            "next": "opt_02_cleanup"
        }
    ]
},

"opt_02_cleanup": {
    "title": "Market Basement",
    "text_blocks": [
        {
            "text": """The basement is quiet now.

You search the area and find something odd: a small chronometric device, partially buried in the corner. It's old. Broken. But it's emitting a faint temporal signature.

This must be what's attracting the glitch-rats. Unstable time pockets draw them in like carrion.

You pocket the device. Someone at the facility might know what to do with it."""
        }
    ],
    "choices": [
        {
            "id": "opt_02_complete",
            "label": "Return to the surface",
            "next": "opt_02_turn_in",
            "effects": {
                "flags": {
                    "opt_02_device_found": True,
                    "fought_city_glitch_rat": True
                }
            }
        }
    ]
},

"opt_02_turn_in": {
    "title": "City Edge",
    "text_blocks": [
        {
            "text": """You emerge from the basement. The shopkeeper approaches cautiously.

"Is it... gone?"

You nod. "It won't come back. But you should report this to Engine Security. There's something wrong with—"

The shopkeeper interrupts. "No, no. No security. Just... thank you."

He hands you a small pouch of coins and hurries away, clearly uncomfortable.

No one wants to acknowledge what's happening. They'd rather pretend everything is normal.

But it's not."""
        }
    ],
    "choices": [
        {
            "id": "opt_02_finish",
            "label": "Leave the market",
            "next": "demo_02_city_edge",
            "effects": {
                "flags": {"opt_02_completed": True}
            }
        }
    ]
},

"opt_01_hook": {
    "title": "Storage Access Request",
    "text_blocks": [
        {
            "text": """You take the work order and examine it more closely.

The component is located in Storage Tunnel B-4, beyond the maintenance access hatch. The tunnel runs beneath the Meridian Engine's primary synchronization array.

No one's volunteered to go down there in three days.

That's... unusual. It's a routine errand."""
        }
    ],
    "choices": [
        {
            "id": "opt_01_accept",
            "label": "Head to Storage Tunnel B-4",
            "next": "opt_01_storage_access"
        },
        {
            "id": "opt_01_decline",
            "label": "Put the work order back",
            "next": "demo_01_supply_cage",
            "effects": {
                "flags": {"opt_01_started": False}
            }
        }
    ]
},

"opt_01_storage_access": {
    "title": "Storage Tunnel B-4",
    "text_blocks": [
        {
            "text": """You descend the metal stairwell into Storage Tunnel B-4.

The air grows colder. The hum of the Meridian Engine is louder here—closer. You can feel it in your chest.

The tunnel is lined with wire cages filled with obsolete equipment. Dust hangs in the air.

At the far end, you spot the component bin marked on the work order.

Then you hear it.

Scratching. Rapid. Too large to be normal."""
        }
    ],
    "choices": [
        {
            "id": "opt_01_investigate",
            "label": "Investigate the sound",
            "next": "opt_01_rat_encounter"
        },
        {
            "id": "opt_01_ignore",
            "label": "Grab the component and leave quickly",
            "next": "opt_01_retrieve_item",
            "effects": {
                "flags": {"ignored_rat": True}
            }
        }
    ]
},

"opt_01_rat_encounter": {
    "title": "Storage Tunnel B-4 - Combat",
    "text_blocks": [
        {
            "text": """You move toward the sound.

A rat the size of a small dog scuttles out from behind a broken crate.

But it's wrong.

Its movements are... stuttering. Like it's skipping frames in a film. One moment it's near the crate. The next, it's three feet closer. No transition.

It lunges.

[COMBAT PLACEHOLDER - Press to continue]

You manage to drive it off with a length of pipe. It retreats into the shadows, still flickering in and out of position.

Your hands are shaking.

That wasn't natural."""
        }
    ],
    "choices": [
        {
            "id": "opt_01_after_combat",
            "label": "Retrieve the component",
            "next": "opt_01_retrieve_item",
            "effects": {
                "flags": {"fought_glitch_rat": True}
            }
        }
    ]
},

"opt_01_retrieve_item": {
    "title": "Component Retrieved",
    "text_blocks": [
        {
            "text": """You grab the component—a small chronometric calibrator—and make your way back up to the supply cage.

As you climb the stairs, you notice something odd.

There's a maintenance log on the wall. The last entry reads:

"Confirmed: secondary pulse echo detected in sublevel tunnels. Temporal drift +0.3 seconds. Acceptable variance. - Operator {player_name}"

The date is three days from now.

You didn't write that."""
        }
    ],
    "choices": [
        {
            "id": "opt_01_complete_to_task",
            "label": "Head to the task floor",
            "next": "demo_01_task_floor",
            "effects": {
                "flags": {"opt_01_component_retrieved": True}
            }
        },
        {
            "id": "opt_01_complete_to_supply",
            "label": "Return to supply cage",
            "next": "demo_01_supply_cage",
            "effects": {
                "flags": {"opt_01_component_retrieved": True}
            }
        }
    ]
},


"demo_03_engine_approach": {
    "title": "Engine Sector Access",
    "text_blocks": [
        {
            "text": """You decide to go directly to the source.

The Engine sector is deeper in the facility. Closer to the Meridian Engine itself. Most workers avoid it unless assigned—the hum is louder there, almost overwhelming.

But if answers exist, they're there.

You make your way through corridors that grow progressively older. Newer paneling gives way to exposed piping and original construction. The architecture here predates the modern facility.

The Engine's pulse is stronger. You can feel it in your bones. Rhythmic. Almost hypnotic.

A sign on the wall reads: "CHRONOMETRIC OBSERVATION STATION - AUTHORIZED PERSONNEL ONLY"

Through a reinforced window, you can see monitoring equipment. Status readouts. Pressure gauges. All showing nominal readings.

But something feels wrong."""
        }
    ],
    "choices": [
        {
            "id": "engine_enter_station",
            "label": "Enter the observation station",
            "next": "demo_03_observation_station"
        },
        {
            "id": "engine_continue_deeper",
            "label": "Continue toward the Engine core",
            "next": "demo_03_core_approach"
        }
    ]
},

"demo_03_observation_station": {
    "title": "Chronometric Observation Station",
    "text_blocks": [
        {
            "text": """The observation station is unmanned. Unusual for this hour.

Banks of monitors display real-time readings from the Meridian Engine. Temporal drift measurements. Phase synchronization indices. Chronometric stability ratios.

Most of it is beyond your training. But you can read enough to know that several values are trending toward critical thresholds.

A logbook sits open on the desk. The last entry is from this morning:

"0600 hours - Phase variance increasing. Drift now at +2.7 seconds per cycle. Supervisor Veylin notified. Awaiting instruction."

Below it, in different handwriting:

"0800 hours - No response from Veylin. Escalating to Engine Authority."

Below that:

"0900 hours - Authority declined intervention. Maintain monitoring only. Do not adjust."

The final entry, hastily scrawled:

"1200 hours - I can't watch this anymore. If anyone reads this - the cascade threshold is 5 seconds. We're approaching 4.2. Someone needs to act."

The entry is dated today. Six hours ago.""",
            "condition": {"requires_flag_false": "read_observation_log"}
        },
        {
            "text": """The observation station remains unmanned.

The monitors continue their silent warnings. Values creeping higher. Phase variance now at 4.4 seconds.

You're running out of time.""",
            "condition": {"requires_flag": "read_observation_log"}
        }
    ],
    "choices": [
        {
            "id": "station_read_log",
            "label": "Study the technical readings",
            "next": "demo_03_observation_station",
            "effects": {
                "flags": {"read_observation_log": True, "knows_cascade_threshold": True}
            },
            "condition": {"requires_flag_false": "read_observation_log"}
        },
        {
            "id": "station_to_core",
            "label": "Continue toward the Engine core",
            "next": "demo_03_core_approach"
        },
        {
            "id": "station_to_control",
            "label": "Look for the control room",
            "next": "demo_03_control_room_search"
        }
    ]
},

"demo_03_control_room_search": {
    "title": "Lower Maintenance Level",
    "text_blocks": [
        {
            "text": """You descend another level, following signs toward "ENGINE CONTROL - RESTRICTED ACCESS"

The corridors here are narrower. Older. The walls are bare metal, riveted together like a ship's hull. The Engine's hum is loud enough to feel in your teeth.

You pass through a checkpoint gate. It should be locked, but it's standing open. Someone left in a hurry.

Ahead, you see a set of heavy doors marked with hazard warnings and temporal stability notices.

That's when you hear it.

Scratching. Like claws on metal.

Not from ahead. From behind you.

Something followed you down here."""
        }
    ],
    "choices": [
        {
            "id": "control_turn_around",
            "label": "Turn around",
            "next": "demo_03_temporal_creature_encounter"
        }
    ]
},

"demo_03_temporal_creature_encounter": {
    "title": "Lower Maintenance Level",
    "text_blocks": [
        {
            "text": """At first, you think it's a rat. A large one, like the glitch-rats from the storage tunnels.

But this is different. Worse.

It's not just stuttering through space—it's fragmenting. You see three copies of it at once. Past, present, future. All overlapping. All wrong.

One version is skeletal. One is fresh. One hasn't happened yet.

And it's not alone.

Two more emerge from the shadows. Then four. A pack of temporal echoes, drawn to the Engine's instability like carrion to death.

They're not hunting you. They're hunting time itself.

But you're in the way.

The nearest one lunges—all three versions at once."""
        }
    ],
    "choices": [
        {
            "id": "creature_fight",
            "label": "Fight them off",
            "next": "demo_03_combat_resolution",
            "effects": {
                "flags": {"fought_temporal_creatures": True}
            }
        },
        {
            "id": "creature_flee_to_doors",
            "label": "Run for the control room doors",
            "next": "demo_03_combat_resolution",
            "effects": {
                "flags": {"fled_from_creatures": True}
            }
        }
    ]
},

"demo_03_combat_resolution": {
    "title": "Lower Maintenance Level",
    "text_blocks": [
        {
            "text": """You grab a broken pipe from the floor and swing hard.

The pipe passes through one echo, connects with another, misses the third entirely. The creature shrieks—a sound that echoes forward and backward through time.

The others circle. You keep swinging, hitting temporal afterimages more than flesh.

Then the lights flare. The Engine pulses. HARD.

All three creatures flicker violently and collapse into single forms—normal rats, dead on the floor.

Whatever temporal instability was sustaining them just corrected itself.

Or the Engine forced it to correct.

You're shaking, but alive.""",
            "condition": {"requires_flag": "fought_temporal_creatures"}
        },
        {
            "text": """You run.

The creatures give chase—past versions, present versions, future versions all moving at different speeds.

You slam through the control room doors and pull them shut. Heavy. Reinforced. Temporal shielding.

On the other side, the creatures shriek and claw at the metal.

Then the lights flare. The Engine pulses. HARD.

The scratching stops.

You crack the door open. The creatures are gone. Just normal dead rats lying on the floor.

Whatever temporal instability was sustaining them just corrected itself.

Or the Engine forced it to correct.""",
            "condition": {"requires_flag": "fled_from_creatures"}
        }
    ],
    "choices": [
        {
            "id": "combat_aftermath",
            "label": "Catch your breath",
            "next": "demo_03_post_combat",
            "effects": {
                "flags": {"survived_creature_encounter": True}
            }
        }
    ]
},

"demo_03_post_combat": {
    "title": "Lower Maintenance Level",
    "text_blocks": [
        {
            "text": """You lean against the wall, trying to steady your hands.

Those things were feeding on temporal anomalies. Growing stronger from the Engine's instability.

Which means they'll keep coming. Keep getting worse.

Unless someone stops this.

The control room doors are right in front of you. Heavy. Reinforced. A sign reads:

"MERIDIAN ENGINE PRIMARY CONTROL
EMERGENCY SHUTDOWN PROTOCOLS AVAILABLE
AUTHORIZATION REQUIRED"

You could try to access it. Try to shut the Engine down before things get worse.

Or you could report this. Find someone in authority who might actually listen.

Behind you, the corridor is silent. But you know more creatures will come. Eventually."""
        }
    ],
    "choices": [
        {
            "id": "post_combat_enter_control",
            "label": "Try to access the control room",
            "next": "demo_03_control_room_locked"
        },
        {
            "id": "post_combat_find_help",
            "label": "Find someone in authority",
            "next": "demo_03_find_authority"
        },
        {
            "id": "post_combat_return_surface",
            "label": "Return to the surface levels",
            "next": "demo_03_return_surface"
        }
    ]
},

"demo_03_control_room_locked": {
    "title": "Engine Control Room - Locked",
    "text_blocks": [
        {
            "text": """The control room doors are sealed. A keypad glows beside them, requesting authorization codes far above your clearance level.

Through the reinforced window, you can see the control room itself. Banks of switches and readouts. Manual override systems. Emergency shutdown levers.

All of it useless behind a locked door.

A placard on the wall lists emergency protocols:

"IN EVENT OF CASCADE FAILURE:
1. Alert Engine Authority immediately
2. Evacuate all personnel from affected sectors
3. DO NOT attempt manual intervention
4. Authority personnel will initiate controlled shutdown"

Someone circled step 3 in red marker and wrote beside it: "They won't. They never do."

You need to make a choice. Try to find someone with authority, or get back to safer areas and warn others."""
        }
    ],
    "choices": [
        {
            "id": "locked_find_authority",
            "label": "Find someone with authority",
            "next": "demo_03_find_authority"
        },
        {
            "id": "locked_return_surface",
            "label": "Return to surface levels",
            "next": "demo_03_return_surface"
        }
    ]
},

"demo_03_find_authority": {
    "title": "Search for Authority",
    "text_blocks": [
        {
            "text": """You head back up through the maintenance levels, looking for anyone in a position to help.

The corridors are strangely empty. Either shifts have changed, or people are avoiding the Engine sectors.

You find a communication terminal and try to contact Engine Authority. The line connects, but no one answers. Just a repeating message:

"Engine Authority is currently handling priority escalations. Non-emergency inquiries will be addressed in order. Current wait time: Unknown."

You hang up. This qualifies as a priority escalation by any sane definition.

But the system doesn't care.

The Engine's hum shifts. A deep, resonant pulse that makes the walls vibrate.

Alarms begin to sound. Distant. Then closer.

Something big is happening."""
        }
    ],
    "choices": [
        {
            "id": "authority_to_pulse",
            "label": "Follow the alarms",
            "next": "demo_04_pre_pulse_warning",
            "effects": {
                "flags": {"tried_to_report": True, "mq_05_escalation_response": True}
            }
        }
    ]
},

"demo_03_return_surface": {
    "title": "Maintenance Corridor",
    "text_blocks": [
        {
            "text": """You make your way back to the upper levels, away from the Engine's oppressive pulse.

The further you get, the more normal things feel. The hum quiets. The lights stabilize.

It's easy to pretend everything's fine up here.

But you know better now. You've seen what's growing in the depths. The temporal creatures. The ignored warnings. The locked control room.

You could report this. Find someone who might listen. Or you could just... return to work. Let someone else deal with it.

That's when you feel it.

A pulse. Deeper than before. Stronger.

The lights flicker in sequence down the corridor.

Alarms begin to sound.

The choice has been made for you."""
        }
    ],
    "choices": [
        {
            "id": "surface_to_pulse",
            "label": "Head toward the alarms",
            "next": "demo_04_pre_pulse_warning",
            "effects": {
                "flags": {"returned_from_depths": True, "mq_05_escalation_response": True}
            }
        }
    ]
},

"demo_03_core_approach": {
    "title": "Engine Core Access Corridor",
    "text_blocks": [
        {
            "text": """You continue deeper, following the corridors toward the Engine core itself.

Few workers ever come this close. The hum is almost unbearable. The air feels thick. Heavy with pressure you can't quite describe.

Ahead, you see a massive observation window—reinforced glass meters thick—looking into the Meridian Engine chamber.

The Engine itself is massive. A towering structure of brass and steel and something else. Something that doesn't quite look like metal. Geometric shapes that hurt to look at directly. Spinning components that seem to rotate through more dimensions than three.

It's beautiful. Terrifying. Wrong.

And it's glowing.

Not with heat. With something else. Temporal energy, maybe. Whatever keeps time moving in Chronvale.

Right now, that glow is pulsing irregularly. Like a heartbeat struggling to maintain rhythm.

You watch as one of the geometric components flickers. For just a moment, it's in two places at once.

Then it corrects. Snaps back into alignment.

The Engine is holding itself together. Barely.

You need to leave. Now."""
        }
    ],
    "choices": [
        {
            "id": "core_leave_quickly",
            "label": "Get away from the Engine",
            "next": "demo_03_return_surface"
        },
        {
            "id": "core_document_what_you_see",
            "label": "Take a moment to note what you're seeing",
            "next": "demo_03_core_witness",
            "effects": {
                "flags": {"witnessed_engine_instability": True}
            }
        }
    ]
},

"demo_03_core_witness": {
    "title": "Engine Core Observation",
    "text_blocks": [
        {
            "text": """You force yourself to watch. To document. To remember.

The Engine's central component—a massive ring of impossible geometry—rotates slowly. But not smoothly. Every few seconds, it stutters. Skips. Repeats a moment of rotation.

Around it, smaller components spin in orbits that shouldn't be possible. Some move forward through time. Others backward. All of them synchronized to a rhythm only the Engine understands.

On a status board, you see readouts:

"TEMPORAL DRIFT: 4.6 SECONDS
PHASE VARIANCE: CRITICAL
CASCADE THRESHOLD: 5.0 SECONDS
WARNING: APPROACHING SYNCHRONIZATION FAILURE"

That's when the Engine pulses.

Not a small pulse. A massive one.

The entire chamber flares with light. The geometric components all flicker at once—past, present, future overlapping in a dizzying blur.

Alarms shriek. Emergency lighting activates.

You need to move. Now."""
        }
    ],
    "choices": [
        {
            "id": "witness_to_pulse",
            "label": "Run toward the nearest exit",
            "next": "demo_04_pre_pulse_warning",
            "effects": {
                "flags": {"witnessed_major_pulse": True, "mq_05_escalation_response": True}
            }
        }
    ]
},

"demo_04_pre_pulse_warning": {
    "title": "Facility-Wide Alert",
    "text_blocks": [
        {
            "text": """The alarms are deafening now. Red emergency lights pulse in sequence down every corridor.

Over the facility-wide intercom, a mechanical voice repeats:

"ATTENTION ALL PERSONNEL. CHRONOMETRIC STABILIZATION EVENT IN PROGRESS. REPORT TO ASSIGNED EMERGENCY STATIONS. REPEAT. CHRONOMETRIC STABILIZATION EVENT IN PROGRESS."

Around you, workers emerge from offices and break rooms, looking confused. Concerned. But not panicked. This has happened before. Just another drill. Another routine malfunction.

But you know better.

You've seen the observation logs. The cascade threshold. The temporal creatures growing stronger in the depths.

This isn't routine.

The Engine's hum shifts. Drops an octave. The walls vibrate.

Then, for just a moment, everything stops.

The alarms cut out. The lights freeze mid-pulse. Workers halt mid-step.

Complete silence.

You're the only thing still moving.

Then time snaps back. The alarms resume. Workers continue walking as if nothing happened.

But you felt it. A full temporal desynchronization. A second where the Engine lost its grip on reality.

It's starting."""
        }
    ],
    "choices": [
        {
            "id": "pre_pulse_continue",
            "label": "Head toward the Engine sector",
            "next": "demo_04_pulse_event"
        }
    ]
},

"demo_04_pulse_event": {
    "title": "Meridian Engine Chamber",
    "text_blocks": [
        {
            "text": """You make your way toward the Engine sector, fighting through crowds of workers heading in the opposite direction.

The closer you get, the worse it becomes. The hum is chaotic now. Arrhythmic. Like a heartbeat in fibrillation.

You reach an observation platform overlooking the main Engine chamber.

The Meridian Engine is visible through reinforced glass—massive, impossible, beautiful, and dying.

The geometric components are flickering rapidly now. Past and future versions overlapping with the present. The central ring stutters through its rotation, skipping entire seconds of movement.

A status board shows:

"TEMPORAL DRIFT: 5.4 SECONDS
CASCADE THRESHOLD EXCEEDED
EMERGENCY CONTAINMENT FAILING
SYNCHRONIZATION COLLAPSE IMMINENT"

Engineers in protective gear scramble around manual control panels. Supervisors shout orders that get lost in the noise.

Then the Engine pulses.

Not like before. This is massive. Fundamental.

The entire chamber flares with blinding light. You feel it pass through you—a wave of temporal energy that makes your bones ache and your thoughts skip.

For a moment, you see everything at once. The chamber as it was yesterday. As it is now. As it will be tomorrow. All layered together in a dizzying blur.

When the pulse fades, half the lights are dead. Emergency systems struggle to maintain containment.

And the Engine is still running. Still breaking. Still holding the city together by sheer mechanical will.

An announcement crackles over the intercom:

"ALL PERSONNEL EVACUATE TO SECONDARY STATIONS. ENGINE AUTHORITY ASSUMING DIRECT CONTROL. REPEAT. ALL PERSONNEL EVACUATE."

You have to choose."""
        }
    ],
    "choices": [
        {
            "id": "pulse_help_stabilization",
            "label": "Help with Engine stabilization efforts",
            "next": "demo_04_stabilization_route",
            "effects": {
                "flags": {"chose_stabilization": True, "witnessed_first_pulse": True}
            }
        },
        {
            "id": "pulse_help_evacuations",
            "label": "Help with civilian evacuations",
            "next": "demo_04_evacuations_route",
            "effects": {
                "flags": {"chose_evacuations": True, "witnessed_first_pulse": True}
            }
        }
    ]
},

"demo_04_stabilization_route": {
    "title": "Engine Stabilization",
    "text_blocks": [
        {
            "text": """You push through the chaos toward the stabilization teams.

An engineer—badge reads HENDRICKS—sees you approach. "You authorized for containment work?"

"I'm maintenance. I can help."

He doesn't argue. There's no time. He shoves a toolkit into your hands and points to a panel. "Pressure regulators. Manual override. Keep them stable until we can restart the automated systems."

You get to work. Around you, the Engine continues its death throes. The hum cycles through impossible frequencies. The geometric components flicker and stutter.

You adjust pressure valves. Maintain coolant flow. Follow Hendricks' shouted instructions while trying not to think about what happens if the Engine fully fails.

Time becomes fluid. You might be working for minutes. Or hours. It's impossible to tell near the Engine.

Then Hendricks grabs your shoulder. "That's all we can do. The automated systems are handling it now. We need to clear the sector."

You follow him toward the exit.

That's when you hear the scream."""
        }
    ],
    "choices": [
        {
            "id": "stabilization_to_combat",
            "label": "Turn toward the sound",
            "next": "demo_04_combat_event"
        }
    ]
},

"demo_04_evacuations_route": {
    "title": "Civilian Evacuation",
    "text_blocks": [
        {
            "text": """You head away from the Engine sector, toward the civilian access corridors.

The hallways are packed. Workers. Residents. Families. All trying to reach the evacuation points while the facility shakes around them.

A woman clutches a child who's crying. An elderly man struggles to keep pace. People are scared now. The official calm has broken.

You help where you can. Guide people toward the exits. Catch someone who stumbles when the floor lurches. Keep them moving.

A security officer—younger, overwhelmed—sees you helping. "You maintenance?"

"Yes."

"Come on. We need to clear the lower residential levels before they seal the containment doors."

You follow her down. The corridors here are older. Less maintained. The Engine's hum is a constant pressure.

She leads you to a residential block. Families still inside, gathering belongings, moving too slowly.

"Everyone out!" she shouts. "Now! No bags, no possessions. Move!"

They comply. Slowly. Too slowly.

You help usher them toward the exits. The woman with the child. The elderly man. A young couple arguing about what to take.

The officer's radio crackles: "All units, containment doors closing in five minutes. Clear your sectors and withdraw."

Five minutes.

You do the math. There are too many people still inside.

That's when you hear the scream."""
        }
    ],
    "choices": [
        {
            "id": "evacuations_to_combat",
            "label": "Run toward the sound",
            "next": "demo_04_combat_event"
        }
    ]
},

"demo_04_combat_event": {
    "title": "Temporal Anomaly",
    "text_blocks": [
        {
            "text": """You round the corner and stop.

There's something in the corridor ahead.

Not a rat this time. Something bigger. Humanoid.

It was a person once. You can still see traces of humanity in its shape. But the pulse did something to them. Caught them in the wrong place at the wrong moment when temporal containment failed.

Now they're fragmenting. Multiple versions of themselves existing simultaneously. Past, present, future. All wrong. All in pain.

One version is screaming. One is already dead. One hasn't been born yet. All of them are reaching toward you with hands that flicker in and out of reality.

Behind the creature, you see another worker—trapped, backing against the wall. They were the one who screamed.

The creature turns toward them. All its versions moving at once. Predatory. Hungry.

Not for flesh. For time. For causality. For the temporal coherence that person still has.

You don't have time to think. Only act.""",
            "condition": {"requires_flag": "chose_stabilization"}
        },
        {
            "text": """You run toward the sound and freeze.

There's something blocking the corridor. Something that was human.

One of the evacuees. Caught in the pulse at the worst possible moment. Their timeline shattered. Now they exist in three states at once—before the pulse, during, after. All overlapping. All wrong.

The security officer beside you goes for her stunner. "What the hell—"

The creature lunges. Past-version and future-version simultaneously. She fires. The bolt passes through empty space—the creature's already moved.

It grabs her. She screams. Her timeline begins to fragment, pulled apart by contact with the anomaly.

You have to stop this. Now.""",
            "condition": {"requires_flag": "chose_evacuations"}
        }
    ],
    "choices": [
        {
            "id": "combat_attack",
            "label": "Attack the creature",
            "next": "demo_04_combat_resolution",
            "effects": {
                "flags": {"attacked_temporal_anomaly": True}
            }
        },
        {
            "id": "combat_distract",
            "label": "Try to distract it",
            "next": "demo_04_combat_resolution",
            "effects": {
                "flags": {"distracted_temporal_anomaly": True}
            }
        }
    ]
},

"demo_04_combat_resolution": {
    "title": "Temporal Combat",
    "text_blocks": [
        {
            "text": """You grab the heaviest tool from your belt and charge.

The creature turns—all three versions at once. You swing at the present-version. Connect. It shrieks.

But hitting it is like hitting water. Your blow passes through temporal afterimages, connects with something semi-solid, then continues through empty air.

The creature lashes out. You dodge one version, but another catches your arm. Cold. Burning cold. Like touching absolute zero.

Your arm goes numb. For a moment, you see your own hand fragmenting—past, present, future bleeding together.

Then you hear it. A deep, resonant tone. The Engine, reasserting control.

The creature freezes. All its versions align for just a moment. You see the person it was. Terrified. Trapped.

Then it collapses. Just a body on the floor. Normal. Dead.

Your arm tingles as feeling returns. You look at your hand. Solid. Present. Whole.

Behind you, Hendricks is staring. "What... what was that?"

You don't answer. You don't know.""",
            "condition": {"requires_flag": ["attacked_temporal_anomaly", "chose_stabilization"]}
        },
        {
            "text": """You wave your arms, shout, do anything to get its attention away from the trapped worker.

It works. Sort of.

The creature turns. All three versions fix on you at once. Past-version angry. Present-version confused. Future-version already moving to attack.

You run. It follows. The corridor blurs around you as temporal instability warps space.

Then you feel it. A deep, resonant pulse from the Engine. Reasserting order. Forcing causality back into alignment.

The creature shrieks. Its three versions slam together violently. For just a moment, you see the person it was. An engineer. Badge still visible.

Then it collapses. Just a body. Normal. Dead.

The trapped worker stares at you, then at the corpse, then runs.

You lean against the wall, shaking.""",
            "condition": {"requires_flag": ["distracted_temporal_anomaly", "chose_stabilization"]}
        },
        {
            "text": """You grab a fire extinguisher from the wall and swing it at the creature.

It connects with something—the present-version, maybe—and the creature releases the security officer. She falls, gasping, her timeline still intact.

The creature turns on you. All three versions. Hungry. Desperate.

You swing again. Miss. It grabs for you with hands that exist in multiple moments at once.

Cold. Burning cold. Your vision splits. You see yourself from outside. Past you. Future you. All bleeding together.

Then the Engine pulses. Deep. Resonant. Forceful.

Reality snaps back. The creature's three versions slam together violently, forced into alignment.

It collapses. Just a body. One of the evacuees you were helping earlier.

The security officer pulls herself up, still shaking. "What... what was that?"

You don't answer. You can't.""",
            "condition": {"requires_flag": ["attacked_temporal_anomaly", "chose_evacuations"]}
        },
        {
            "text": """You shout, wave, do anything to get its attention.

The creature turns. Releases the security officer. She scrambles backward, timeline still intact but barely.

All three versions of the creature focus on you now. You run.

The corridor blurs. Time becomes fluid around the anomaly. You see yourself running in past-tense and future-tense simultaneously.

Then the Engine pulses. Deep. Forceful.

The creature shrieks as its three versions are forced together. You see the person it was. Just an evacuee. Wrong place, wrong time.

It collapses. Normal. Dead.

You stop running. The security officer catches up, breathing hard. "We need to get out of here. Now."

You nod. Can't speak. Can only move.""",
            "condition": {"requires_flag": ["distracted_temporal_anomaly", "chose_evacuations"]}
        }
    ],
    "choices": [
        {
            "id": "combat_resolution_continue",
            "label": "Catch your breath",
            "next": "demo_04_aftermath",
            "effects": {
                "flags": {"survived_temporal_combat": True, "mq_06_pulse_witnessed": True}
            }
        }
    ]
},

"demo_04_aftermath": {
    "title": "After the Pulse",
    "text_blocks": [
        {
            "text": """The alarms have quieted. The emergency lighting has stabilized. The Engine's hum has returned to something approaching normal.

But nothing is normal.

Around you, workers move through the corridors in a daze. Some are crying. Others just stare blankly, processing what they witnessed.

The pulse broke something. Not just in the Engine. In people's ability to deny what's happening.

You see it in their faces. The realization that the anomalies aren't glitches. That time itself is breaking. That the Engine might not hold.

Hendricks finds you. "You okay?"

You nod. Not really true, but true enough.

"Good. Because Engine Authority is calling an emergency briefing. All personnel who witnessed the pulse. They want statements."

He pauses. Looks at the body on the floor.

"What are you going to tell them?"

You don't know yet.""",
            "condition": {"requires_flag": "chose_stabilization"}
        },
        {
            "text": """The alarms have quieted. The emergency lighting has stabilized. The Engine's hum has returned to something approaching normal.

But nothing is normal.

The security officer—her badge reads TORRES—sits on the floor, back against the wall, just breathing.

"That was..." She can't finish. Doesn't need to.

Around you, evacuees are being led to safe zones. Medical teams tend to injuries. Engineers assess structural damage.

But you can see it in everyone's faces. The realization that this isn't just a malfunction. That time itself is coming apart. That the Engine might not save them.

Torres pulls herself up. "Engine Authority is calling an emergency briefing. Everyone who witnessed the pulse needs to give a statement."

She looks at the body on the floor.

"What are you going to tell them?"

You don't know yet.""",
            "condition": {"requires_flag": "chose_evacuations"}
        }
    ],
    "choices": [
        {
            "id": "aftermath_help_injured",
            "label": "Help with the injured first",
            "next": "demo_04_help_npc",
            "effects": {
                "flags": {"chose_to_help": True}
            }
        },
        {
            "id": "aftermath_go_to_briefing",
            "label": "Go to the briefing immediately",
            "next": "demo_04_briefing_skip",
            "effects": {
                "flags": {"went_to_briefing": True}
            }
        },
        {
            "id": "aftermath_return_workspace",
            "label": "Return to your workspace",
            "next": "demo_05_workspace_return"
        }
    ]
},

"demo_04_help_npc": {
    "title": "Medical Station",
    "text_blocks": [
        {
            "text": """You head to the makeshift medical station set up in a break room.

It's overwhelmed. Too many injured, not enough medics. Burns from energy discharge. Fractures from structural collapse. And worse—people with temporal fragmentation symptoms. Shaking. Disoriented. Experiencing moments out of sequence.

You help where you can. Fetch supplies. Hold pressure on wounds. Guide people who can't remember which timeline they're in.

An older medic—exhausted, grateful—nods to you. "Thanks. Most people just... walk past. Pretend they don't see."

One of the injured is Davies. Your coworker from the break room. He doesn't recognize you. Keeps asking what year it is. His timeline is scrambled.

You stay with him until the medics can sedate him. Until his questions stop.

When you finally leave, the briefing has already started. You missed it.

But you helped. That counts for something."""
        }
    ],
    "choices": [
        {
            "id": "help_to_workspace",
            "label": "Return to your workspace",
            "next": "demo_05_workspace_return",
            "effects": {
                "flags": {"helped_davies": True}
            }
        }
    ]
},

"demo_04_briefing_skip": {
    "title": "Engine Authority Briefing",
    "text_blocks": [
        {
            "text": """The briefing room is packed. Workers standing shoulder to shoulder. All of them exhausted. Shaken.

At the front, an Engine Authority representative—immaculate suit, calm demeanor, completely disconnected from reality—reads from prepared notes:

"The recent synchronization event was successfully contained. Temporal drift has been corrected to acceptable parameters. All systems are stable. There is no ongoing danger to personnel or city infrastructure."

Someone in the crowd shouts: "People died!"

"Regrettable accidents during emergency procedures," the representative responds smoothly. "Full investigations will be conducted. Compensation will be provided to affected families."

"What about the creatures?" someone else asks. "The things in the corridors?"

"Isolated anomalies. Already contained. No further threat."

You feel the lie settle over the room like a weight. The official story. The acceptable narrative.

Nothing is wrong. The Engine is stable. Everything is under control.

The representative continues talking, but you're not listening anymore.

You know the truth. And the truth is worse than they're willing to admit."""
        }
    ],
    "choices": [
        {
            "id": "briefing_return_workspace",
            "label": "Leave the briefing",
            "next": "demo_05_workspace_return",
            "effects": {
                "flags": {"attended_briefing": True}
            }
        }
    ]
},

# ===== BEAT 5: Workspace Discovery & Document Ending =====

"demo_05_workspace_return": {
    "title": "Administrative Annex - Your Workspace",
    "text_blocks": [
        {
            "text": """You return to your workspace in the administrative annex.

It's quieter than it should be. Most workers are still at the briefing or helping with cleanup. The usual hum of activity—keyboards clicking, people talking, terminals beeping—is absent.

Just you and the Engine's ever-present hum.

Your desk is exactly as you left it this morning. Terminal still displaying your completed task assignment. Coffee cup half-empty. Everything normal.

Except nothing is normal anymore.

You've witnessed the pulse. Fought temporal creatures. Seen people's timelines fragment. Watched Davies forget which year he's living in.

And Engine Authority called it "successfully contained."

You sit at your desk, trying to process everything. That's when you notice something odd.

There are documents on your desk that weren't there before. Or maybe they were, and you didn't notice. Time is getting harder to trust.

One is a status report. Another looks like a maintenance log. And underneath them, partially visible, is something else. Something handwritten."""
        }
    ],
    "choices": [
        {
            "id": "workspace_search_desk",
            "label": "Search through the documents on your desk",
            "next": "demo_05_search_stacks"
        },
        {
            "id": "workspace_check_tray",
            "label": "Check your inbox tray",
            "next": "demo_05_search_tray"
        },
        {
            "id": "workspace_check_board",
            "label": "Check the assignment board on the wall",
            "next": "demo_05_search_board"
        }
    ]
},

"demo_05_search_stacks": {
    "title": "Your Desk",
    "text_blocks": [
        {
            "text": """You shuffle through the stack of documents on your desk.

Status reports. Maintenance schedules. The usual bureaucratic paperwork that accumulates during a shift.

But as you sort through them, you notice something wrong.

Several documents reference events that happened today. The gauge inspection. The records archive. Even the pulse event.

But they're dated from last week.

And they're written in your handwriting.

You pull out one report in particular. It's titled:

"CHRONOMETRIC STABILITY OBSERVATION LOG - OPERATOR {player_name}"

The date at the top is seven days ago. But the content describes today. Everything that happened. The Davies repetition. The temporal creatures. The major pulse.

All of it documented. By you. A week before it happened.

Or... a week after it happened the first time.

Your hands are shaking.

There's more. At the bottom of the stack."""
        }
    ],
    "choices": [
        {
            "id": "stacks_continue",
            "label": "Keep reading",
            "next": "demo_06_document_reveal",
            "effects": {
                "flags": {"found_document_in_stacks": True, "reached_decision_point": True}
            }
        }
    ]
},

"demo_05_search_tray": {
    "title": "Inbox Tray",
    "text_blocks": [
        {
            "text": """You pull your inbox tray closer.

It's full. More than usual. Documents you don't remember receiving.

You flip through them. Status updates. Maintenance reports. Routine inter-department memos.

Then you find something that makes you stop.

An envelope. Unmarked. No sender information. No official stamp.

Inside is a handwritten document. The paper is worn. Like it's been read and re-read many times.

The handwriting is yours.

The title reads:

"MERIDIAN ENGINE OPERATIONAL LOG - ITERATION UNKNOWN"

Below it, in smaller text:

"If you're reading this, it's happening again. You won't remember writing this. You never do. But you need to know: the Engine didn't fail. It reset. And you're the only one who notices."

Your chest tightens.

You keep reading."""
        }
    ],
    "choices": [
        {
            "id": "tray_continue",
            "label": "Keep reading",
            "next": "demo_06_document_reveal",
            "effects": {
                "flags": {"found_document_in_tray": True, "reached_decision_point": True}
            }
        }
    ]
},

"demo_05_search_board": {
    "title": "Assignment Board",
    "text_blocks": [
        {
            "text": """You walk over to the assignment board mounted on the wall.

It displays the day's task assignments for all workers in your section. Your name is listed with your completed task: "Panel 7-B, Gauges 14-18."

But as you look closer, you notice something underneath. A piece of paper that's been pushed behind the board's edge. Almost hidden.

You pull it out.

It's a report. Handwritten on standard facility paper. The handwriting is rushed. Desperate. But unmistakably yours.

At the top, it reads:

"URGENT - CHRONOMETRIC FAILURE DOCUMENTATION"

And below that:

"This is the third time. Maybe the fourth. I'm losing count. The pulse happens. The Engine 'stabilizes.' Everyone forgets. Except me. This document is the only proof. If you're reading this, you're me, and it's happening again."

The room feels colder.

You turn the page."""
        }
    ],
    "choices": [
        {
            "id": "board_continue",
            "label": "Keep reading",
            "next": "demo_06_document_reveal",
            "effects": {
                "flags": {"found_document_at_board": True, "reached_decision_point": True}
            }
        }
    ]
},

"demo_06_document_reveal": {
    "title": "The Document",
    "text_blocks": [
        {
            "text": """You read the document. Every word. Every observation. Every warning.

It describes today in detail. The gauge anomaly at Panel 7-B. Davies repeating himself. The records archive. Warden Kess glitching during the Engine pulse. The temporal creatures. The cascade failure.

Everything.

But it's not written in past tense. It's written as instructions. As a warning to yourself.

Key passages stand out:

"The gauge at Panel 7-B will flicker. It's not a malfunction. It's the first visible sign of temporal desynchronization. Document it. You'll need proof later."

"Davies will repeat himself in the corridor. He won't remember. No one ever does. Except you."

"The cascade threshold is 5 seconds. Once it's exceeded, the pulse is inevitable. You can't stop it. I've tried."

"The temporal creatures are people. Workers caught in the wrong moment during a pulse. The Engine forces them back into alignment. It doesn't save them. It just... ends them."

And at the bottom, the most chilling line:

"After the pulse, the Engine will 'stabilize.' Temporal drift will reset to zero. And everyone will forget. Except you. And then it will start again. The drift will increase. The anomalies will return. The pulse will come. And you'll write this document again, hoping the next version of you remembers."

Below that, in shaky handwriting:

"I don't know how many times this has happened. But I've learned something unsettling: the loop feels deliberate. The Engine's behavior is too consistent, too precise. This isn't random failure—it's controlled repetition. Someone or something is maintaining this pattern."

The document ends with a partial sentence:

"The question isn't whether we can break the loop. The question is whether we're meant to—"

The rest is torn off. Or never written.

You sit in silence, holding the paper.

Everything you experienced today. You've experienced it before. Maybe many times.

And you'll experience it again.

The Engine's hum continues. Steady. Rhythmic. Indifferent.

You need to decide what to do with this information.""",
            "condition": {"requires_flag": "found_document_in_stacks"}
        },
        {
            "text": """You read the document carefully.

It's addressed to you. From you. Written in your own handwriting but with the urgency of someone running out of time.

It describes today's events in precise detail:

"0800 hours - Task assignment: Panel 7-B. Gauge 18 will show temporal flutter. First warning sign."

"0930 hours - Davies repetition event in corridor. Memory desynchronization confirmed."

"1200 hours - Records archive investigation. Warden Kess will intervene. During confrontation, minor pulse will cause her timeline to briefly fragment."

"1500 hours - Major cascade event. Temporal drift exceeds 5.0 seconds. Multiple casualties. Temporal creature manifestations."

Every event you witnessed is documented here. With timestamps. With details you haven't even fully processed yet.

But the document doesn't just record what happened. It warns you about what's coming:

"After pulse stabilization: Engine Authority will declare the event 'resolved.' They're not lying. From their perspective, it IS resolved. Temporal drift resets to zero. Everyone's memories realign with the 'official' timeline. Except yours."

"Time frame until next cycle: Unknown. Previous iterations ranged from 3 days to 2 weeks. The Engine is destabilizing faster each time."

"Important: You cannot prevent the pulse. I've tried. Every action you take is already part of the pattern. But here's what troubles me: the pattern is too perfect. Too deliberate. Like it's being orchestrated. The anomalies, the pulse, the reset—they follow rules. Someone set those rules."

And at the very end:

"You're reading this because I made sure it would reach you. I hid copies throughout the workspace. One of them found you. That means the loop is real. But maybe... maybe it's not a prison. Maybe it's a design. And if someone designed it, they had a reason.

The question is: are we trying to escape? Or are we supposed to understand?

- {player_name}, Iteration [UNKNOWN]"

The signature is yours. But you don't remember writing this.

You won't remember writing the next one either.

The implications settle over you like a weight. Everything that happened today will happen again. And you're the only one who'll remember that it already did.""",
            "condition": {"requires_flag": "found_document_in_tray"}
        },
        {
            "text": """You read the document, and with each line, reality becomes less stable.

It's a report. Clinical. Procedural. Written in your handwriting but with the detached tone of someone documenting a repeating nightmare.

"CHRONOMETRIC FAILURE PATTERN - ITERATION ANALYSIS"

The document lists multiple cycles. Each one describes a sequence of events remarkably similar to today:

"Iteration 1 (suspected): Gauge anomalies observed. Investigation minimal. Pulse occurred. No documentation survived."

"Iteration 2: Pattern recognized. Records consulted. Warden Kess encountered. Pulse occurred. Documentation lost in reset."

"Iteration 3: Documentation method revised. Document hidden in workspace. Pulse occurred. Reset confirmed. Document survived."

"Current Iteration: Unknown. Likely 4th or higher. Pattern holding. Documentation protocol successful."

Each iteration includes observations:

"Temporal creatures appear approximately 2 hours before major pulse. Manifestation rate increasing with each cycle."

"Davies repetition event is consistent marker. Occurs 6-8 hours into cycle. Reliable temporal anchor."

"Cascade threshold consistently reached at 5.0 seconds drift. Engine 'reset' follows immediately. All personnel memory affected except primary observer (self)."

And then, analysis:

"Hypothesis: The Meridian Engine is not failing. It's designed to reset. The temporal anomalies are not malfunctions. They're symptoms of the Engine approaching reset threshold."

"Question: Why am I exempt from memory reset? Why do I retain continuity across iterations?"

"Hypothesis 1: Random anomaly during Engine event granted immunity."

"Hypothesis 2: The exemption is intentional. Someone needs to remember. Someone needs to observe. Why else would the loop allow documentation to persist?"

The final section is titled "DISTURBING CONCLUSION":

"The loop is not a failure. It's a system. And systems have purposes.

"Engine Authority either doesn't know (unlikely—they control the Engine) or actively maintains this state.

"The temporal 'anomalies' follow too-predictable patterns. Gauge flutter at 0800. Davies repetition at 0930. Cascade at 1500. Like clockwork.

"Like... a schedule.

"Option 1: This is containment. The loop prevents something worse.
"Option 2: This is preservation. Someone chose this over collapse.
"Option 3: This is a test. And I'm the variable."

At the bottom, scrawled quickly:

"If you're reading this, ask yourself: are we trapped in the loop, or are we maintaining it? And if someone's orchestrating this—who benefits from keeping us inside?"

The Engine's hum feels different now. Not just ambient noise. But the sound of a machine doing exactly what it was designed to do.

Looping.""",
            "condition": {"requires_flag": "found_document_at_board"}
        }
    ],
    "choices": [
        {
            "id": "document_keep_it",
            "label": "Hide the document where you'll find it next time",
            "next": "demo_end",
            "effects": {
                "flags": {"kept_document": True}
            }
        },
        {
            "id": "document_try_to_report",
            "label": "Take it to Engine Authority",
            "next": "demo_end",
            "effects": {
                "flags": {"tried_to_report_document": True}
            }
        },
        {
            "id": "document_destroy",
            "label": "Destroy it and try to forget",
            "next": "demo_end",
            "effects": {
                "flags": {"destroyed_document": True}
            }
        }
    ]
},

"demo_end": {
    "title": "End of Demo",
    "text_blocks": [
        {
            "text": """You sit at your desk, holding the document, surrounded by the quiet hum of the Meridian Engine.

You know the truth now. The loop is real. Time is broken. And you're the only one who remembers.

What happens next is up to you.

But one thing is certain: the Engine will continue. The anomalies will return. The pulse will come again.

And when it does, you'll be here. Remembering. Documenting. Trying to find a way out.

The question isn't whether the loop will repeat.

The question is: what will you do differently next time?

[END OF DEMO - CLOCKWORK COLLAPSE]

Thank you for playing.

---

This demo introduced you to the world of Clockwork Collapse, the mystery of the Meridian Engine, and your character's unique awareness of the temporal loop.

The full game will explore:
• The origin of the loop and why it exists
• Your character's immunity to the memory reset
• The other residents of Chronvale and their hidden roles
• The true purpose of the Meridian Engine
• Whether the loop can be broken—and what breaking it might cost

Your choices in this demo have been noted. They will affect the full game's story.""",
            "condition": {"requires_flag": "kept_document"}
        },
        {
            "text": """You take the document and head toward Engine Authority's offices.

The corridors are quiet. The facility is returning to normal. Or what passes for normal.

You reach the office. The same representative from the briefing is there, reviewing reports.

You show them the document. Your document. Proof of the loop.

They read it carefully. Their expression doesn't change.

When they finish, they look up at you.

"This is an impressive stress response," they say calmly. "The recent pulse event was traumatic for many workers. It's not uncommon to experience dissociation, false memories, or temporal confusion after such an incident."

"It's not false. It's real. I wrote that. I've lived through this before—"

"We have excellent mental health resources available," they interrupt. "I'll schedule you for an evaluation. In the meantime, you're relieved of duty. Go home. Rest."

They take the document. File it away. Dismiss you with professional courtesy.

You stand in the corridor, realizing: they don't believe you. Or they do believe you, and this is exactly how they handle people who remember.

Either way, the document is gone. And the loop will continue.

[END OF DEMO - CLOCKWORK COLLAPSE]

Thank you for playing.

---

This demo introduced you to the world of Clockwork Collapse, the mystery of the Meridian Engine, and your character's unique awareness of the temporal loop.

The full game will explore:
• The origin of the loop and why it exists
• Your character's immunity to the memory reset
• The other residents of Chronvale and their hidden roles
• The true purpose of the Meridian Engine
• Whether the loop can be broken—and what breaking it might cost

Your choices in this demo have been noted. They will affect the full game's story.""",
            "condition": {"requires_flag": "tried_to_report_document"}
        },
        {
            "text": """You stare at the document for a long moment.

Then you crumple it up.

If the loop is real, destroying the document won't stop it. And if it's not real, if you're just experiencing some kind of stress-induced delusion, then keeping it will only make things worse.

Better to forget. Better to move on.

You drop the crumpled paper into the recycling bin.

But even as you try to convince yourself it's the right choice, you can't shake the feeling that you've done this before.

Tried to forget.

Failed.

And next time—when the anomalies return, when Davies repeats himself, when the pulse comes again—you won't have the document to prove you're not going crazy.

You'll have to start from scratch.

Again.

The Engine hums. Steady. Indifferent. Eternal.

[END OF DEMO - CLOCKWORK COLLAPSE]

Thank you for playing.

---

This demo introduced you to the world of Clockwork Collapse, the mystery of the Meridian Engine, and your character's unique awareness of the temporal loop.

The full game will explore:
• The origin of the loop and why it exists
• Your character's immunity to the memory reset
• The other residents of Chronvale and their hidden roles
• The true purpose of the Meridian Engine
• Whether the loop can be broken—and what breaking it might cost

Your choices in this demo have been noted. They will affect the full game's story.""",
            "condition": {"requires_flag": "destroyed_document"}
        }
    ],
    "choices": [
        {
            "id": "end_to_menu",
            "label": "Return to Main Menu",
            "next": "menu_main"
        }
    ]
}
}