from setuptools import setup, find_packages

#
# Package information
#
setup(
	name		= 'noct',
	version		= '0.1.1.1',
	description	= 'Notification CLI Tool',
	author		= 'tuntunkun.org',
	author_email	= 'naoya@tuntunkun.com',
    	packages	= find_packages(),
	package_dir     = { 'noct' : 'noct' },
	install_requires= [
		'click',
		'requests',
	],
	entry_points	= {
		'console_scripts'	: [
			'noct = noct.cli:cmd',
		]
	},
)

