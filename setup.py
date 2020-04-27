from setuptools import setup

setup(
    name='projectPhase2New',
    version='',
    packages=['venv.Lib.distutils', 'venv.Lib.encodings', 'venv.Lib.importlib', 'venv.Lib.collections',
              'venv.Lib.site-packages.pip', 'venv.Lib.site-packages.pip._vendor',
              'venv.Lib.site-packages.pip._vendor.idna', 'venv.Lib.site-packages.pip._vendor.pep517',
              'venv.Lib.site-packages.pip._vendor.pytoml', 'venv.Lib.site-packages.pip._vendor.certifi',
              'venv.Lib.site-packages.pip._vendor.chardet', 'venv.Lib.site-packages.pip._vendor.chardet.cli',
              'venv.Lib.site-packages.pip._vendor.distlib', 'venv.Lib.site-packages.pip._vendor.distlib._backport',
              'venv.Lib.site-packages.pip._vendor.msgpack', 'venv.Lib.site-packages.pip._vendor.urllib3',
              'venv.Lib.site-packages.pip._vendor.urllib3.util', 'venv.Lib.site-packages.pip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pip._vendor.colorama', 'venv.Lib.site-packages.pip._vendor.html5lib',
              'venv.Lib.site-packages.pip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pip._vendor.html5lib.treebuilders', 'venv.Lib.site-packages.pip._vendor.progress',
              'venv.Lib.site-packages.pip._vendor.requests', 'venv.Lib.site-packages.pip._vendor.packaging',
              'venv.Lib.site-packages.pip._vendor.cachecontrol',
              'venv.Lib.site-packages.pip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pip._vendor.webencodings', 'venv.Lib.site-packages.pip._vendor.pkg_resources',
              'venv.Lib.site-packages.pip._internal', 'venv.Lib.site-packages.pip._internal.cli',
              'venv.Lib.site-packages.pip._internal.req', 'venv.Lib.site-packages.pip._internal.vcs',
              'venv.Lib.site-packages.pip._internal.index', 'venv.Lib.site-packages.pip._internal.utils',
              'venv.Lib.site-packages.pip._internal.models', 'venv.Lib.site-packages.pip._internal.network',
              'venv.Lib.site-packages.pip._internal.commands', 'venv.Lib.site-packages.pip._internal.operations',
              'venv.Lib.site-packages.pip._internal.operations.build',
              'venv.Lib.site-packages.pip._internal.operations.install',
              'venv.Lib.site-packages.pip._internal.distributions', 'venv.Lib.site-packages.pytz',
              'venv.Lib.site-packages.tqdm', 'venv.Lib.site-packages.tqdm.contrib', 'venv.Lib.site-packages.wheel',
              'venv.Lib.site-packages.wheel.cli', 'venv.Lib.site-packages.django', 'venv.Lib.site-packages.django.db',
              'venv.Lib.site-packages.django.db.models', 'venv.Lib.site-packages.django.db.models.sql',
              'venv.Lib.site-packages.django.db.models.fields', 'venv.Lib.site-packages.django.db.models.functions',
              'venv.Lib.site-packages.django.db.backends', 'venv.Lib.site-packages.django.db.backends.base',
              'venv.Lib.site-packages.django.db.backends.dummy', 'venv.Lib.site-packages.django.db.backends.mysql',
              'venv.Lib.site-packages.django.db.backends.oracle', 'venv.Lib.site-packages.django.db.backends.sqlite3',
              'venv.Lib.site-packages.django.db.backends.postgresql', 'venv.Lib.site-packages.django.db.migrations',
              'venv.Lib.site-packages.django.db.migrations.operations', 'venv.Lib.site-packages.django.apps',
              'venv.Lib.site-packages.django.conf', 'venv.Lib.site-packages.django.conf.urls',
              'venv.Lib.site-packages.django.conf.locale', 'venv.Lib.site-packages.django.conf.locale.ar',
              'venv.Lib.site-packages.django.conf.locale.az', 'venv.Lib.site-packages.django.conf.locale.bg',
              'venv.Lib.site-packages.django.conf.locale.bn', 'venv.Lib.site-packages.django.conf.locale.bs',
              'venv.Lib.site-packages.django.conf.locale.ca', 'venv.Lib.site-packages.django.conf.locale.cs',
              'venv.Lib.site-packages.django.conf.locale.cy', 'venv.Lib.site-packages.django.conf.locale.da',
              'venv.Lib.site-packages.django.conf.locale.de', 'venv.Lib.site-packages.django.conf.locale.el',
              'venv.Lib.site-packages.django.conf.locale.en', 'venv.Lib.site-packages.django.conf.locale.eo',
              'venv.Lib.site-packages.django.conf.locale.es', 'venv.Lib.site-packages.django.conf.locale.et',
              'venv.Lib.site-packages.django.conf.locale.eu', 'venv.Lib.site-packages.django.conf.locale.fa',
              'venv.Lib.site-packages.django.conf.locale.fi', 'venv.Lib.site-packages.django.conf.locale.fr',
              'venv.Lib.site-packages.django.conf.locale.fy', 'venv.Lib.site-packages.django.conf.locale.ga',
              'venv.Lib.site-packages.django.conf.locale.gd', 'venv.Lib.site-packages.django.conf.locale.gl',
              'venv.Lib.site-packages.django.conf.locale.he', 'venv.Lib.site-packages.django.conf.locale.hi',
              'venv.Lib.site-packages.django.conf.locale.hr', 'venv.Lib.site-packages.django.conf.locale.hu',
              'venv.Lib.site-packages.django.conf.locale.id', 'venv.Lib.site-packages.django.conf.locale.is',
              'venv.Lib.site-packages.django.conf.locale.it', 'venv.Lib.site-packages.django.conf.locale.ja',
              'venv.Lib.site-packages.django.conf.locale.ka', 'venv.Lib.site-packages.django.conf.locale.km',
              'venv.Lib.site-packages.django.conf.locale.kn', 'venv.Lib.site-packages.django.conf.locale.ko',
              'venv.Lib.site-packages.django.conf.locale.lt', 'venv.Lib.site-packages.django.conf.locale.lv',
              'venv.Lib.site-packages.django.conf.locale.mk', 'venv.Lib.site-packages.django.conf.locale.ml',
              'venv.Lib.site-packages.django.conf.locale.mn', 'venv.Lib.site-packages.django.conf.locale.nb',
              'venv.Lib.site-packages.django.conf.locale.nl', 'venv.Lib.site-packages.django.conf.locale.nn',
              'venv.Lib.site-packages.django.conf.locale.pl', 'venv.Lib.site-packages.django.conf.locale.pt',
              'venv.Lib.site-packages.django.conf.locale.ro', 'venv.Lib.site-packages.django.conf.locale.ru',
              'venv.Lib.site-packages.django.conf.locale.sk', 'venv.Lib.site-packages.django.conf.locale.sl',
              'venv.Lib.site-packages.django.conf.locale.sq', 'venv.Lib.site-packages.django.conf.locale.sr',
              'venv.Lib.site-packages.django.conf.locale.sv', 'venv.Lib.site-packages.django.conf.locale.ta',
              'venv.Lib.site-packages.django.conf.locale.te', 'venv.Lib.site-packages.django.conf.locale.th',
              'venv.Lib.site-packages.django.conf.locale.tr', 'venv.Lib.site-packages.django.conf.locale.uk',
              'venv.Lib.site-packages.django.conf.locale.uz', 'venv.Lib.site-packages.django.conf.locale.vi',
              'venv.Lib.site-packages.django.conf.locale.de_CH', 'venv.Lib.site-packages.django.conf.locale.en_AU',
              'venv.Lib.site-packages.django.conf.locale.en_GB', 'venv.Lib.site-packages.django.conf.locale.es_AR',
              'venv.Lib.site-packages.django.conf.locale.es_CO', 'venv.Lib.site-packages.django.conf.locale.es_MX',
              'venv.Lib.site-packages.django.conf.locale.es_NI', 'venv.Lib.site-packages.django.conf.locale.es_PR',
              'venv.Lib.site-packages.django.conf.locale.pt_BR', 'venv.Lib.site-packages.django.conf.locale.sr_Latn',
              'venv.Lib.site-packages.django.conf.locale.zh_Hans', 'venv.Lib.site-packages.django.conf.locale.zh_Hant',
              'venv.Lib.site-packages.django.core', 'venv.Lib.site-packages.django.core.mail',
              'venv.Lib.site-packages.django.core.mail.backends', 'venv.Lib.site-packages.django.core.cache',
              'venv.Lib.site-packages.django.core.cache.backends', 'venv.Lib.site-packages.django.core.files',
              'venv.Lib.site-packages.django.core.checks', 'venv.Lib.site-packages.django.core.checks.security',
              'venv.Lib.site-packages.django.core.checks.compatibility', 'venv.Lib.site-packages.django.core.servers',
              'venv.Lib.site-packages.django.core.handlers', 'venv.Lib.site-packages.django.core.management',
              'venv.Lib.site-packages.django.core.serializers', 'venv.Lib.site-packages.django.http',
              'venv.Lib.site-packages.django.test', 'venv.Lib.site-packages.django.urls',
              'venv.Lib.site-packages.django.forms', 'venv.Lib.site-packages.django.utils',
              'venv.Lib.site-packages.django.utils.translation', 'venv.Lib.site-packages.django.views',
              'venv.Lib.site-packages.django.views.generic', 'venv.Lib.site-packages.django.views.decorators',
              'venv.Lib.site-packages.django.contrib', 'venv.Lib.site-packages.django.contrib.gis',
              'venv.Lib.site-packages.django.contrib.gis.db', 'venv.Lib.site-packages.django.contrib.gis.db.models',
              'venv.Lib.site-packages.django.contrib.gis.db.models.sql',
              'venv.Lib.site-packages.django.contrib.gis.db.backends',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.base',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.mysql',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.oracle',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.postgis',
              'venv.Lib.site-packages.django.contrib.gis.db.backends.spatialite',
              'venv.Lib.site-packages.django.contrib.gis.gdal', 'venv.Lib.site-packages.django.contrib.gis.gdal.raster',
              'venv.Lib.site-packages.django.contrib.gis.gdal.prototypes',
              'venv.Lib.site-packages.django.contrib.gis.geos',
              'venv.Lib.site-packages.django.contrib.gis.geos.prototypes',
              'venv.Lib.site-packages.django.contrib.gis.admin', 'venv.Lib.site-packages.django.contrib.gis.forms',
              'venv.Lib.site-packages.django.contrib.gis.utils', 'venv.Lib.site-packages.django.contrib.gis.geoip2',
              'venv.Lib.site-packages.django.contrib.gis.sitemaps',
              'venv.Lib.site-packages.django.contrib.gis.serializers', 'venv.Lib.site-packages.django.contrib.auth',
              'venv.Lib.site-packages.django.contrib.auth.handlers',
              'venv.Lib.site-packages.django.contrib.auth.management',
              'venv.Lib.site-packages.django.contrib.auth.migrations', 'venv.Lib.site-packages.django.contrib.admin',
              'venv.Lib.site-packages.django.contrib.admin.views',
              'venv.Lib.site-packages.django.contrib.admin.migrations',
              'venv.Lib.site-packages.django.contrib.admin.templatetags', 'venv.Lib.site-packages.django.contrib.sites',
              'venv.Lib.site-packages.django.contrib.sites.migrations',
              'venv.Lib.site-packages.django.contrib.humanize',
              'venv.Lib.site-packages.django.contrib.humanize.templatetags',
              'venv.Lib.site-packages.django.contrib.messages',
              'venv.Lib.site-packages.django.contrib.messages.storage',
              'venv.Lib.site-packages.django.contrib.postgres', 'venv.Lib.site-packages.django.contrib.postgres.forms',
              'venv.Lib.site-packages.django.contrib.postgres.fields',
              'venv.Lib.site-packages.django.contrib.postgres.aggregates',
              'venv.Lib.site-packages.django.contrib.sessions',
              'venv.Lib.site-packages.django.contrib.sessions.backends',
              'venv.Lib.site-packages.django.contrib.sessions.migrations',
              'venv.Lib.site-packages.django.contrib.sitemaps', 'venv.Lib.site-packages.django.contrib.admindocs',
              'venv.Lib.site-packages.django.contrib.flatpages',
              'venv.Lib.site-packages.django.contrib.flatpages.migrations',
              'venv.Lib.site-packages.django.contrib.flatpages.templatetags',
              'venv.Lib.site-packages.django.contrib.redirects',
              'venv.Lib.site-packages.django.contrib.redirects.migrations',
              'venv.Lib.site-packages.django.contrib.staticfiles', 'venv.Lib.site-packages.django.contrib.syndication',
              'venv.Lib.site-packages.django.contrib.contenttypes',
              'venv.Lib.site-packages.django.contrib.contenttypes.management',
              'venv.Lib.site-packages.django.contrib.contenttypes.migrations', 'venv.Lib.site-packages.django.dispatch',
              'venv.Lib.site-packages.django.template', 'venv.Lib.site-packages.django.template.loaders',
              'venv.Lib.site-packages.django.template.backends', 'venv.Lib.site-packages.django.middleware',
              'venv.Lib.site-packages.django.templatetags', 'venv.Lib.site-packages.pipenv',
              'venv.Lib.site-packages.pipenv.cli', 'venv.Lib.site-packages.pipenv.vendor',
              'venv.Lib.site-packages.pipenv.vendor.attr', 'venv.Lib.site-packages.pipenv.vendor.idna',
              'venv.Lib.site-packages.pipenv.vendor.toml', 'venv.Lib.site-packages.pipenv.vendor.yarg',
              'venv.Lib.site-packages.pipenv.vendor.click', 'venv.Lib.site-packages.pipenv.vendor.passa',
              'venv.Lib.site-packages.pipenv.vendor.passa.cli', 'venv.Lib.site-packages.pipenv.vendor.passa.models',
              'venv.Lib.site-packages.pipenv.vendor.passa.actions',
              'venv.Lib.site-packages.pipenv.vendor.passa.internals',
              'venv.Lib.site-packages.pipenv.vendor.passa.operations', 'venv.Lib.site-packages.pipenv.vendor.cursor',
              'venv.Lib.site-packages.pipenv.vendor.dotenv', 'venv.Lib.site-packages.pipenv.vendor.jinja2',
              'venv.Lib.site-packages.pipenv.vendor.plette', 'venv.Lib.site-packages.pipenv.vendor.plette.models',
              'venv.Lib.site-packages.pipenv.vendor.vistir', 'venv.Lib.site-packages.pipenv.vendor.vistir.backports',
              'venv.Lib.site-packages.pipenv.vendor.yaspin', 'venv.Lib.site-packages.pipenv.vendor.certifi',
              'venv.Lib.site-packages.pipenv.vendor.chardet', 'venv.Lib.site-packages.pipenv.vendor.chardet.cli',
              'venv.Lib.site-packages.pipenv.vendor.distlib', 'venv.Lib.site-packages.pipenv.vendor.distlib._backport',
              'venv.Lib.site-packages.pipenv.vendor.iso8601', 'venv.Lib.site-packages.pipenv.vendor.pexpect',
              'venv.Lib.site-packages.pipenv.vendor.pipreqs', 'venv.Lib.site-packages.pipenv.vendor.tomlkit',
              'venv.Lib.site-packages.pipenv.vendor.urllib3', 'venv.Lib.site-packages.pipenv.vendor.urllib3.util',
              'venv.Lib.site-packages.pipenv.vendor.urllib3.contrib',
              'venv.Lib.site-packages.pipenv.vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pipenv.vendor.urllib3.packages',
              'venv.Lib.site-packages.pipenv.vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pipenv.vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pipenv.vendor.cerberus', 'venv.Lib.site-packages.pipenv.vendor.cerberus.tests',
              'venv.Lib.site-packages.pipenv.vendor.colorama', 'venv.Lib.site-packages.pipenv.vendor.pathlib2',
              'venv.Lib.site-packages.pipenv.vendor.requests', 'venv.Lib.site-packages.pipenv.vendor.backports',
              'venv.Lib.site-packages.pipenv.vendor.backports.enum',
              'venv.Lib.site-packages.pipenv.vendor.backports.shutil_get_terminal_size',
              'venv.Lib.site-packages.pipenv.vendor.blindspin', 'venv.Lib.site-packages.pipenv.vendor.packaging',
              'venv.Lib.site-packages.pipenv.vendor.pip_shims', 'venv.Lib.site-packages.pipenv.vendor.markupsafe',
              'venv.Lib.site-packages.pipenv.vendor.ptyprocess', 'venv.Lib.site-packages.pipenv.vendor.resolvelib',
              'venv.Lib.site-packages.pipenv.vendor.shellingham',
              'venv.Lib.site-packages.pipenv.vendor.shellingham.posix',
              'venv.Lib.site-packages.pipenv.vendor.shutilwhich', 'venv.Lib.site-packages.pipenv.vendor.pythonfinder',
              'venv.Lib.site-packages.pipenv.vendor.pythonfinder.models',
              'venv.Lib.site-packages.pipenv.vendor.pythonfinder._vendor',
              'venv.Lib.site-packages.pipenv.vendor.pythonfinder._vendor.pep514tools',
              'venv.Lib.site-packages.pipenv.vendor.requirementslib',
              'venv.Lib.site-packages.pipenv.vendor.requirementslib.models',
              'venv.Lib.site-packages.pipenv.vendor.click_completion',
              'venv.Lib.site-packages.pipenv.vendor.click_didyoumean', 'venv.Lib.site-packages.pipenv.patched',
              'venv.Lib.site-packages.pipenv.patched.notpip', 'venv.Lib.site-packages.pipenv.patched.notpip._vendor',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.idna',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.pep517',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.pytoml',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.certifi',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.chardet',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.chardet.cli',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.distlib',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.distlib._backport',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.msgpack',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3.util',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3.contrib',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3.contrib._securetransport',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3.packages',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3.packages.backports',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.colorama',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.html5lib',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.html5lib._trie',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.html5lib.filters',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.html5lib.treewalkers',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.html5lib.treeadapters',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.html5lib.treebuilders',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.lockfile',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.progress',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.requests',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.packaging',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.cachecontrol',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.cachecontrol.caches',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.webencodings',
              'venv.Lib.site-packages.pipenv.patched.notpip._vendor.pkg_resources',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.cli',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.req',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.vcs',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.utils',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.models',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.commands',
              'venv.Lib.site-packages.pipenv.patched.notpip._internal.operations',
              'venv.Lib.site-packages.pipenv.patched.safety', 'venv.Lib.site-packages.pipenv.patched.pipfile',
              'venv.Lib.site-packages.pipenv.patched.piptools',
              'venv.Lib.site-packages.pipenv.patched.piptools._compat',
              'venv.Lib.site-packages.pipenv.patched.piptools.scripts',
              'venv.Lib.site-packages.pipenv.patched.piptools.repositories', 'venv.Lib.site-packages.asgiref',
              'venv.Lib.site-packages.certifi', 'venv.Lib.site-packages.distlib',
              'venv.Lib.site-packages.distlib._backport', 'venv.Lib.site-packages.sqlparse',
              'venv.Lib.site-packages.sqlparse.engine', 'venv.Lib.site-packages.sqlparse.filters',
              'venv.Lib.site-packages.setuptools', 'venv.Lib.site-packages.setuptools.extern',
              'venv.Lib.site-packages.setuptools._vendor', 'venv.Lib.site-packages.setuptools._vendor.packaging',
              'venv.Lib.site-packages.setuptools.command', 'venv.Lib.site-packages.virtualenv',
              'venv.Lib.site-packages.virtualenv.run', 'venv.Lib.site-packages.virtualenv.run.plugin',
              'venv.Lib.site-packages.virtualenv.seed', 'venv.Lib.site-packages.virtualenv.seed.embed',
              'venv.Lib.site-packages.virtualenv.seed.embed.wheels',
              'venv.Lib.site-packages.virtualenv.seed.via_app_data',
              'venv.Lib.site-packages.virtualenv.seed.via_app_data.pip_install',
              'venv.Lib.site-packages.virtualenv.util', 'venv.Lib.site-packages.virtualenv.util.path',
              'venv.Lib.site-packages.virtualenv.util.path._pathlib',
              'venv.Lib.site-packages.virtualenv.util.subprocess', 'venv.Lib.site-packages.virtualenv.config',
              'venv.Lib.site-packages.virtualenv.config.cli', 'venv.Lib.site-packages.virtualenv.create',
              'venv.Lib.site-packages.virtualenv.create.via_global_ref',
              'venv.Lib.site-packages.virtualenv.create.via_global_ref.builtin',
              'venv.Lib.site-packages.virtualenv.create.via_global_ref.builtin.pypy',
              'venv.Lib.site-packages.virtualenv.create.via_global_ref.builtin.cpython',
              'venv.Lib.site-packages.virtualenv.create.via_global_ref.builtin.python2',
              'venv.Lib.site-packages.virtualenv.discovery', 'venv.Lib.site-packages.virtualenv.discovery.windows',
              'venv.Lib.site-packages.virtualenv.activation', 'venv.Lib.site-packages.virtualenv.activation.bash',
              'venv.Lib.site-packages.virtualenv.activation.fish', 'venv.Lib.site-packages.virtualenv.activation.batch',
              'venv.Lib.site-packages.virtualenv.activation.xonsh',
              'venv.Lib.site-packages.virtualenv.activation.cshell',
              'venv.Lib.site-packages.virtualenv.activation.python',
              'venv.Lib.site-packages.virtualenv.activation.powershell', 'venv.Lib.site-packages.pkg_resources',
              'venv.Lib.site-packages.pkg_resources.extern', 'venv.Lib.site-packages.pkg_resources._vendor',
              'venv.Lib.site-packages.pkg_resources._vendor.packaging', 'venv.Lib.site-packages.importlib_metadata',
              'venv.Lib.site-packages.importlib_metadata.docs', 'venv.Lib.site-packages.importlib_metadata.tests',
              'venv.Lib.site-packages.importlib_metadata.tests.data', 'venv.Lib.site-packages.importlib_resources',
              'venv.Lib.site-packages.importlib_resources.tests',
              'venv.Lib.site-packages.importlib_resources.tests.data01',
              'venv.Lib.site-packages.importlib_resources.tests.data01.subdirectory',
              'venv.Lib.site-packages.importlib_resources.tests.data02',
              'venv.Lib.site-packages.importlib_resources.tests.data02.one',
              'venv.Lib.site-packages.importlib_resources.tests.data02.two',
              'venv.Lib.site-packages.importlib_resources.tests.data03',
              'venv.Lib.site-packages.importlib_resources.tests.zipdata01',
              'venv.Lib.site-packages.importlib_resources.tests.zipdata02', 'ntnyPth', 'ntnyPth.migrations',
              'projectPhase2New'],
    url='',
    license='',
    author='Matthew Li',
    author_email='',
    description=''
)
