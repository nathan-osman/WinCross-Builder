from django.db import models

class Package(models.Model):
    '''Represents a package available for building.'''
    
    name        = models.CharField(max_length=40, help_text='The name of the package')
    website     = models.URLField(help_text='A website where more information about the package can be found.')
    description = models.TextField(help_text='Information about the package')
    
    def __unicode__(self):
        '''Returns a string representation of the package.'''
        return self.name

class Version(models.Model):
    '''Represents a particular version of a package.'''
    
    package      = models.ForeignKey(Package, related_name='', help_text='The package represented by the version')
    version      = models.CharField(max_length=20, help_text='The version string of the package')
    release_date = models.DateField(help_text='The date that the version was released')
    
    def __unicode__(self):
        '''Returns a string representation of the version.'''
        return self.version