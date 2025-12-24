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
            }
        ],
    },
}