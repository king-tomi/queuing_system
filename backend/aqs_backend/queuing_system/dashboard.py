# queuing_system/dashboard.py

from admin_tools.dashboard import modules, Dashboard

class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        self.children.append(modules.AppList(
            title='Applications',
            exclude=('django.contrib.*',),
        ))

        self.children.append(modules.ModelList(
            title='Queuing System Models',
            models=('queuing_system.models.QueueEntry', 'queuing_system.models.Customer', 'queuing_system.models.Staff'),
        ))

        self.children.append(modules.LinkList(
            title='Useful Links',
            children=[
                {
                    'title': 'Queue Overview',
                    'url': '/admin/dashboard/overview/',
                    'external': False,
                },
                {
                    'title': 'Queue List',
                    'url': '/admin/queues/',
                    'external': False,
                },
                {
                    'title': 'Staff Queue Load',
                    'url': '/admin/staff-load/',
                    'external': False,
                },
            ]
        ))