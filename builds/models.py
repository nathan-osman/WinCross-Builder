from django.db import models

from packages.models import Version

class Build(models.Model):
    '''Represents a build of a particular package version.'''
    
    models.ForeignKey(Version, help_text='The package version that this build belongs to')