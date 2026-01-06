QUESTS = {
    "reach_the_end": {
        "id": "reach_the_end",
        "name": "Reach the end",
        "description": "Reach the end of the test to complete this quest.",
        "objectives": [
            {
                "id": "obj_find_key",
                "description": "Find the key",
                "type": "flag",
                "requirement": "has_key",
                "completed": False
            },
            {
                "id": "obj_use_key",
                "description": "Unlock the door",
                "condition": "has_key",
                "type": "flag",
                "requirement": "door_unlocked",
                "completed": False
            }
        ]
    }
}