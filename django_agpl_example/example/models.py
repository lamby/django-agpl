from django_agpl.signals import project_downloaded

def project_downloaded_cb(sender, **kwargs):
    print "Project was just downloaded (via signal)"

project_downloaded.connect(project_downloaded_cb)
