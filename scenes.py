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

You need to figure out what's happening before it gets worse.

[END OF BEAT 2 - PATTERN EMERGES]

Next: Deeper investigation, critical choices, and the first major pulse event."""
        }
    ],
    "choices": [
        {
            "id": "after_security_to_city",
            "label": "Head to the city edge",
            "next": "demo_02_city_edge"
        },
        {
            "id": "after_security_return",
            "label": "[End demo - Return to main menu]",
            "next": "menu_main"
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
            }
        },
        {
            "id": "return_corridor_to_city",
            "label": "Return to city edge",
            "next": "demo_02_city_edge",
            "effects": {
                "flags": {"returned_from_city": True}
            }
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
}
}