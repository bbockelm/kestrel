
from distutils.core import setup
setup(name='kestrel',
      version='0.2',
      scripts=['src/gfactory_entry_requests', 'src/gfactory_frontend_groups', 'src/gfactory_frontend_info', 'src/gwms_analyze_job', 'src/kestrel_config_val', 'src/kestrel_unzip_log', 'src/gwms_compare_collectors', 'src/kestrel_launch_pilot', 'src/kestrel_pilot_config''],
      data_files=[('/usr/share/kestrel', ['config/kestrel_config_global', 'src/gfactory_entry_requests.cpf', 'src/gfactory_frontend_groups.cpf']),
                  ('/etc/kestrel', ['config/kestrel_config']),
                  ('/etc/kestrel/config.d', ['config/01-osg.conf']),
                  ('/usr/share/kestrel/config.d', ['config/01-osg-defaults.conf']),
                 ]
      )

