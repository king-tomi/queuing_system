# queuing_system/menu.py

from admin_tools.menu import items, Menu

class CustomMenu(Menu):
    def init_with_context(self, context):
        self.children.append(items.MenuItem(
            title='Home',
            url='/admin/',
        ))

        self.children.append(items.AppList(
            title='Applications',
            exclude=('django.contrib.*',),
        ))

        self.children.append(items.ModelList(
            title='Queuing System Models',
            models=('queuing_system.models.QueueEntry', 'queuing_system.models.Customer', 'queuing_system.models.Staff'),
        ))

        self.children.append(items.Link(
            title='Queue Overview',
            url='/admin/dashboard/overview/',
        ))

        self.children.append(items.Link(
            title='Queue List',
            url='/admin/queues/',
        ))

        self.children.append(items.Link(
            title='Staff Queue Load',
            url='/admin/staff-load/',
        ))