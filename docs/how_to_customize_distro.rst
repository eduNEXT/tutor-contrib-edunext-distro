How to customize tutor-distro plugin
====================================

Tutor distro plugin manages a set of settings:


General Settings
----------------

+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Setting                                                                                                                                                | Default value                                                                                                        |
+===============================+========================================================================================================================+======================================================================================================================+
| **DOCKER_IMAGE_OPENEDX**                                                                                                                               |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Base docker image, that contain all distro basic configuration for production and replace tutor default openedx image                                  |    docker.io/ednxops/distro-edunext-edxapp:<distro_version>                                                          |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **DOCKER_IMAGE_OPENEDX_DEV**                                                                                                                           |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Base docker image, that contain all distro basic configuration for development and replace tutor default openedx image                                 |    docker.io/ednxops/distro-edunext-edxapp-dev:<distro-version>                                                      |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| *Note: if you have different images that aren't based on these, you can have some problems.*                                                                                                                                                                                  |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **EDX_PLATFORM_REPOSITORY**                                                                                                                            |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Repository for your edx-platform base code                                                                                                             |    https://github.com/eduNEXT/edunext-platform.git                                                                   |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **EDX_PLATFORM_VERSION**                                                                                                                               |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Branch to use as main code                                                                                                                             |    ednx-release/<distro-version>.master                                                                              |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
|**DISTRO_THEMES**                                                                                                                                       |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
|Establish repository(ies) of your openedx theme(s)                                                                                                      |   - name: ednx-saas-themes                                                                                           |
|                                                                                                                                                        |     repo: ednx-saas-theme                                                                                            |
|You can add other repositories using the same estructure definition describe in default value in the config.yml file                                    |     version: edunext/<distro-version>                                                                                |
|                                                                                                                                                        |     domain: github.com                                                                                               |
|                                                                                                                                                        |     protocol: ssh                                                                                                    |
|                                                                                                                                                        |     path: eduNEXT                                                                                                    |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **DISTRO_THEMES_ROOT**                                                                                                                                 |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Directory where the themes are cloned                                                                                                                  |    /openedx/themes                                                                                                   |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **DISTRO_THEME_DIRS**                                                                                                                                  |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Path to theme directories                                                                                                                              |     - /openedx/themes/ednx-saas-themes/edx-platform/                                                                 |
|                                                                                                                                                        |     - openedx/themes/ednx-saas-themes/edx-platform/bragi-generator                                                   |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **DISTRO_THEMES_NAME**                                                                                                                                 | .. code-block:: yml                                                                                                  |
|                                                                                                                                                        |                                                                                                                      |
| Name(s) for enable theme(s)                                                                                                                            |     - bragi                                                                                                          |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **DISTRO_EXTRA_MIDDLEWARES**                                                                                                                           |.. code-block:: yml                                                                                                   |
|                                                                                                                                                        |                                                                                                                      |
| Add any middleware to openedx setting MIDDLEWARE                                                                                                       |     - middleware.test.1                                                                                              |
+-------------------------------+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+


To override these settings define it on config.yml file (``$(tutor config printroot)/config.yaml``) or use the command ``tutor config save --set GENERAL_SETTING=Value``.


Plugins or packages
-------------------

By default distro installs next plugins, in a version compatible with the distro release:


+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+
| Name                         | Description                                                                                   | More information                            |
+==============================+===============================================================================================+=============================================+
| DISTRO_EOX_TENANT_DPKG       | Multi-tenancy django app for edx-platform                                                     | https://github.com/eduNEXT/eox-tenant       |
+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+
| DISTRO_EOX_CORE_DPKG         | Adds multiple API endpoints in order to extend the functionality of the edx-platform          | https://github.com/eduNEXT/eox-core         |
+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+
| DISTRO_EOX_AUDIT_MODEL_DPKG  | Register status of any execution of a method or function                                      | https://github.com/eduNEXT/eox-audit-model  |
+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+
| DISTRO_EOX_THEMING_DPKG      | Tool to make it easy to create a openedx theme (Django)                                       | https://github.com/eduNEXT/eox-theming      |
+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+
| DISTRO_EOX_HOOKS_DPKG        | Extend edx-platform through Django configurations and Open edX Events                         | https://github.com/eduNEXT/eox-hooks/       |
+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+
| DISTRO_EOX_TAGGING_DPKG      | Tags objects in edx-platform which can be used to categorize, include extra information, etc. | https://github.com/eduNEXT/eox-tagging/     |
+------------------------------+-----------------------------------------------------------------------------------------------+---------------------------------------------+


You can disable anyone by the ``tutor config save --set DISTRO_<PLUGIN_NAME>_DPKG=None`` command, or by setting this in ``$(tutor config printroot)/config.yaml``.


.. code-block:: yml

        DISTRO_<PLUGIN_NAME>_DPKG: None


:warning: **NOTE**: From Olmo version Distro has not defaulted packages. Now it is necessary to add the packages you want in ``config.yml`` file.

If you want to override default packages or add a new one go to the corresponding section: `How to add a new package. <./how_to_add_new_packages.rst>`_
