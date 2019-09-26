'''
schemas.py
----------

This file allows us to select what columns we want from database models, and
save them as json output.
'''
from app import ma

class NewProjectSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('nlihc_id',
                  'latitude',
                  'longitude',
                  'census_tract',
                  'neighborhood_cluster',
                  'ward',
                  'neighborhood_cluster_desc',
                  ## Basic Project Information
                  'proj_name',
                  'proj_addre',
                  'proj_units_tot',
                  'proj_units_assist_max',
                  'proj_owner_type',
        )

new_project_schema = NewProjectSchema(many=True)
