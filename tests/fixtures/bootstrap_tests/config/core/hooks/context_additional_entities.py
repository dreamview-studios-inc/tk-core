# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook which provides advanced customization of context creation.
Returns a dict with two keys:

    entity_types_in_path: a list of Shotgun entity types (ie. CustomNonProjectEntity05) that
        context_from_path should recognize and use to fill its additional_entities list.
    
    entity_fields_on_task: a list of Shotgun fields (ie. sg_extra_link) on the Task entity
        that context_from_entity should query Shotgun for and insert the resulting entities
        into its additional_entities_list.

"""

from tank import Hook


class ContextAdditionalEntities(Hook):

    def execute(self):
        val = {
            "entity_types_in_path": [],
            "entity_fields_on_task": ["additional_field"]
        }
        
        return val
