QUESTS = {
    "mq_routine_stabilization": {
        "id": "mq_routine_stabilization",
        "name": "Routine Stabilization Order",
        "description": "Complete your assigned maintenance task.",
        "objectives": [
            {
                "id": "mq_01_assigned",
                "description": "Report to workstation",
                "type": "flag",
                "requirement": "mq_01_assigned",
                "completed": False
            },
            {
                "id": "mq_02_task_performed",
                "description": "Perform maintenance checks",
                "type": "flag",
                "requirement": "mq_02_task_performed",
                "completed": False
            },
            {
                "id": "mq_03_anomalies_noted",
                "description": "Investigate anomalies",
                "type": "flag",
                "requirement": "mq_03_anomalies_noted",
                "completed": False
            }
        ]
    },

    "opt_01_component_retrieval": {
        "id": "opt_01_component_retrieval",
        "name": "Component Retrieval",
        "description": "Retrieve the chronometric calibrator from Storage Tunnel B-4.",
        "objectives": [
            {
                "id": "opt_01_started",
                "description": "Accept the work order",
                "type": "flag",
                "requirement": "opt_01_started",
                "completed": False
            },
            {
                "id": "opt_01_component_retrieved",
                "description": "Retrieve the component",
                "type": "flag",
                "requirement": "opt_01_component_retrieved",
                "completed": False
            }
        ]
    }
}