edunext-distro plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================
What is Distro
--------------
Distro is an opinioned openedx distribution with some custom stuff to have an easy-to-use and a ready to deploy in local or in development openedx distribution. This can be watch like a tutor-plugin but is taken a little bit far away.


Installation
------------

::

    pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro

Usage
-----

::

    tutor plugins enable edunext-distro

How to add packages
-----

Open your tutordistro/plugin.py

The most important thing you have to declare into `defaults` dict is the upper case package name and set it to True, this is for enable and disable from terminal like:

::

    tutor distro --set EOX_CORE=False


Then you must to set a key with the upper case package name followed by `_DPKG` for example `"EOX_CORE_DPKG"`, the value of that key is a dictionary with the following data:

- name **# Package name**
- index **# Where download it (choices are pip or git)**
- repository **# This is optional only if you use a git repo**
- version **#This is optional only if you use a git repo**
- variables **# The variables key is the part of custom development which you need to setup a `development` or a `production` environment with whatever dava you may need**
  - development **# A dictionary: Dict[str, str] with all the settings you can need to start a deleopment environment**
  - production **# A dictionary: Dict[str, str] with all the settings you can need to start a production environment**

Example
::

    "defaults": {
        # Another `defaults` settings
        "EOX_CORE": True,
        "EOX_CORE_DPKG": {
            "name": "eox-core",
            "index": "git",
            "repository": "https://github.com/eduNEXT/eox-core.git",
            "version": "v6.0.1",
            "variables": {
                "development": {
                    # Development custom settings
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper.backends.users_m_v1",
                },
                "production": {
                    # Production custom settings
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper.backends.users_m_v1",
                },
            },
        }
    }



How to add custom themes
-----
Declare the path of your themes, by default the themes path goes here `/openedx/themes`

::

    "defaults": {
        # Another `defaults` settings
        "THEMES_ROOT": "/openedx/themes"
    }



Now setup the directories where going to be placed your themes, to allow openedx to know where can look up them

::

    "defaults": {
        # Another `defaults` settings
        "THEME_DIRS": [
            "/openedx/themes/ednx-saas-themes/edx-platform",
            "/openedx/themes/ednx-saas-themes/edx-platform/bragi-children",
            "/openedx/themes/ednx-saas-themes/edx-platform/bragi-generator",
        ]
    }



Declare the theme names of all your themes in this list `THEMES_NAME` to enable correctly them with the distro command `enable-themes`

::

    "defaults": {
        # Another `defaults` settings
        "THEMES_NAME": [
            "bragi",
        ],
    }

**Custom docker images**

You need a opinioned docker image and an opinioned edx_platform to manage the local and developmento environment. This settings need to be placed into `set` key and not in `defaults`.

- DOCKER_IMAGE_OPENEDX **# The docker image repository for the openedx-platform**
- DOCKER_IMAGE_OPENEDX_DEV **# The docker image repository for development environment to openedx-platform**
- EDX_PLATFORM_REPOSITORY **# This is the git repo to clone the edx-platform in development environment**
- EDX_PLATFORM_VERSION **# This is to select a version tag or branch from edx-platform repository**

::

    "set": {
        # Another `set` stuff
        "DOCKER_IMAGE_OPENEDX": "docker.io/ednxops/distro-edunext-edxapp:vM.mango.1.0-plugin",
        "DOCKER_IMAGE_OPENEDX_DEV": "docker.io/ednxops/distro-edunext-edxapp-dev:vM.mango.1.0-plugin",
        "EDX_PLATFORM_REPOSITORY": "https://github.com/eduNEXT/edunext-platform.git",
        "EDX_PLATFORM_VERSION": "edunext/mango.master",
    },




License
-------

This software is licensed under the terms of the AGPLv3.