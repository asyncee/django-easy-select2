Quickstart
----------

In your admin.py::

    from django.contrib import admin
    from easy_select2 import select2_modelform
    from polls.models import Poll

    PollForm = select2_modelform(Poll, attrs={'width': '250px'})

    class PollAdmin(admin.ModelAdmin):
        form = PollForm


Thats all. All your choice widgets are select2 widgets 250px wide.
