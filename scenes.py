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
                "next": "demo_01_workspace_entry"
            }
        ]
    },

    "demo_01_workspace_entry": {
        "title": "Administrative Annex",
        "text_blocks": [
            {
                "text": """You return to your workstation in the administrative annex.

The Meridian Engine's hum continues, steady and constant. Your terminal still displays your task assignment: Panel 7-B, Gauges 14 through 18.

Davies is nowhere to be seen. Probably checking those gauges. Again.""",
                "condition": {"requires_flag": "mq_01_assigned"}
            },
            {
                "text": """You return to your workstation in the administrative annex.

The Meridian Engine hums beneath your feet—a deep, constant vibration that never stops. Readouts flicker on nearby terminals. Status lights blink green.

Davies is back at his desk, head down, working on something. He doesn't look up as you pass.

You check the terminal. Today's order: routine maintenance check on the task floor instrumentation.""",
                "condition": {"requires_flag": "talked_to_davies", "requires_flag_false": "mq_01_assigned"}
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
                "next": "demo_01_task_floor",
                "effects": {
                    "flags": {"mq_01_assigned": True}
                },
                "start_quest": "mq_routine_stabilization",
                "condition": {"requires_flag_false": "mq_01_assigned"}
            },
            {
                "id": "workspace_to_task_floor_assigned",
                "label": "Head to the task floor",
                "next": "demo_01_task_floor",
                "condition": {"requires_flag": "mq_01_assigned"}
            },
            {
                "id": "workspace_to_break",
                "label": "Talk to Davies first",
                "next": "demo_01_break_area",
                "condition": {"requires_flag_false": "mq_01_assigned"}
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
                    "flags": {
                        "mq_01_assigned": True,
                        "talked_to_davies": True
                    },
                },
                "start_quest": "mq_routine_stabilization",
                "condition": {"requires_flag_false": "mq_01_assigned"}
            },
            {
                "id": "break_to_task_floor_assigned",
                "label": "Head to the task floor",
                "next": "demo_01_task_floor",
                "condition": {"requires_flag": "mq_01_assigned"}
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
            "next": "demo_01_task_floor",
            "effects": {
                "flags": {"mq_01_assigned": True}
            },
            "start_quest": "mq_routine_stabilization",
            "condition": {"requires_flag_false": "mq_01_assigned"}  
        },
        {
            "id": "supply_to_task_floor_already_assigned",
            "label": "Head to task floor",
            "next": "demo_01_task_floor",
            "condition": {"requires_flag": "mq_01_assigned"}  
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
    "title": "End of Vertical Slice",
    "text_blocks": [
        {
            "text": """[END OF VERTICAL SLICE]

This is where the demo would continue into Beat 2 (Pattern Emerges).

Current progress:
- Main quest started
- First anomaly witnessed (gauge)
- Second anomaly confirmed (Davies repetition)
- Player awareness established

Next: Investigate records, encounter security, experience first pulse."""
        }
    ],
    "choices": [
        {
            "id": "end_slice_return",
            "label": "[Return to main menu]",
            "next": "menu_main"
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
                "flags": {
                    "opt_01_component_retrieved": True,
                    "mq_01_assigned": True
                }
            },
            "start_quest": "mq_routine_stabilization",
            "condition": {"requires_flag_false": "mq_01_assigned"}
        },
        {
            "id": "opt_01_complete_continue",
            "label": "Continue with your assignment",
            "next": "demo_01_task_floor",
            "effects": {
                "flags": {"opt_01_component_retrieved": True}
            },
            "condition": {"requires_flag": "mq_01_assigned"}
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