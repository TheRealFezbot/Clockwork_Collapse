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
                "next": "test_01",
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

    "test_01": {
        "title": "Test Scene One",
        "text_blocks": [
            {
                "text": "This is the first test scene.\n\nIf you can read this and see buttons below, your UI is working"
            }
        ],
        "choices": [
            {
                "id": "to_scene_02",
                "label": "Go to Scene Two",
                "next": "test_02",
            },
            {
                "id": "stay_here",
                "label": "Stay Here",
                "next": "test_01",
            },
        ],
    },
    
    "test_02": {
        "title": "Test Scene Two",
        "text_blocks": [
            {
                "text": "You are now in the second test scene.\n\nThe buttons should still be centered and horizontal."
            }
        ],
        "choices": [
            {
                "id": "back_to_scene_01",
                "label": "Go Back",
                "next": "test_01",
            },
            {
                "id": "to_scene_03",
                "label": "Go to Scene Three",
                "next": "test_03",
                "start_quest": "reach_the_end"
            },
        ],
    },

    "test_03": {
        "title": "Test Scene With Effects",
        "text_blocks": [
            {
                "text": "This is a test scene with effects.",
                "condition": {"requires_flag": "has_key"},
                "text_if_true": "There is nothing more to grab",
                "text_if_false": "There is a key you probably want to grab for this test"
            },
        ],
        "choices": [
            {
                "id": "choice_a",
                "label": "Pick up the Key",
                "next": "test_04",
                "condition": {
                    "requires_flag_false": "has_key",
                }, 
                "effects": {
                    "flags": {"has_key": True},
                    "counters": {"items_collected": +1},
                },
            },
            {
                "id": "choice_b",
                "label": "Leave it",
                "next": "test_04"
            },
        ],
    },

    "test_04": {
        "title": "Test Scene After Effects",
        "text_blocks": [
            {
                "text": "You approach a locked door.",
                "condition": {"requires_flag": "forced_door"},
                "text_if_true": "The door doesn't budge, even when using force",
            }
        ],
        "choices": [
            {
                "id": "use_key",
                "label": "Use the key",
                "next": "end_of_test",
                "condition": {"requires_flag": "has_key"},
                "effects": {"flags": {"door_unlocked": True}}
            },
            {
                "id": "try_force",
                "label": "Try to force it open",
                "next": "test_04",
                "effects": {"flags": {"forced_door": True}},
            },
            {
                "id": "go_back",
                "label": "Go Back",
                "next": "test_03",
                "condition": {"requires_flag_false": "has_key"}
            }
        ]
    },

    "end_of_test": {
        "title": "End of test",
        "text_blocks": [
            {
                "text": "This is the end of the test"
            },
        ],
        "choices": [
            {
                "id": "menu_quit",
                "label": "Quit Game",
                "next": "QUIT",
            }
        ]
    }
}