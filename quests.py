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
            },
            {
                "id": "mq_04_records_consulted",
                "description": "Consult the records archive",
                "type": "flag",
                "requirement": "visited_records",
                "completed": False
            },
            {
                "id": "mq_05_escalation_response",
                "description": "Respond to escalation",
                "type": "flag",
                "requirement": "met_warden_kess",
                "completed": False
            },
            {
                "id": "mq_06_pulse_witnessed",
                "description": "Witness the first pulse event",
                "type": "flag",
                "requirement": "witnessed_first_pulse",
                "completed": False
            },
            {
                "id": "mq_07_decision_point",
                "description": "Reach the critical decision point",
                "type": "flag",
                "requirement": "reached_decision_point",
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
    },

    "opt_02_city_cleanup": {
        "id": "opt_02_city_cleanup",
        "name": "City Edge Cleanup",
        "description": "Deal with the strange creature in the market basement.",
        "objectives": [
            {
                "id": "opt_02_started",
                "description": "Accept the cleanup job",
                "type": "flag",
                "requirement": "opt_02_started",
                "completed": False
            },
            {
                "id": "opt_02_device_found",
                "description": "Investigate the basement and find the chronometric device",
                "type": "flag",
                "requirement": "opt_02_device_found",
                "completed": False
            },
            {
                "id": "opt_02_completed",
                "description": "Report back to the shopkeeper",
                "type": "flag",
                "requirement": "opt_02_completed",
                "completed": False
            }
        ]
    }
}