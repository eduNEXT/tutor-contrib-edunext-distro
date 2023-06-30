How to add a new package
====================================

You can add a package directly in config.yml file (``$(tutor config printroot)/config.yaml``).

It's possible to install from a repository or by pip but take in mind, the second option couldn't install it as editable.

Follow the next structure:

+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Package Variable                                           | Description                                                                                                                                   | Example                                                                         |
+============================================================+===============================================================================================================================================+=================================================================================+
| index                                                      | Mode to install a package this could be **git** or **pip**                                                                                    | git                                                                             |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| name                                                       | Indicate the package you want to install                                                                                                      | eox-tenant                                                                      |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| version                                                    | Release, tag or branch do you want to install                                                                                                 | v6.0.0                                                                          |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Installing from a repo you have to add:*                                                                                                                                                                                                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| domain                                                     | Source code hosting system                                                                                                                    | github.com                                                                      |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| path                                                       | Web path where the repo is stored. In GitHub usually correspond to **user_name** and in GitLab usually is **user_name/folder**                | eduNEXT                                                                         |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| private                                                    | Boolean to indicate if the package is public or private                                                                                       | false                                                                           |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| protocol                                                   | Protocol used to clone the repository, you can use **HTTPS** or **ssh** (used especially in private packages)                                 | https                                                                           |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| repo                                                       | Repository name                                                                                                                               | eox-tenant                                                                      |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| *Aditional variables:*                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| variables                                                  | This is a set of additional configurations for development and production, you have to refer to official plugin documentation to configure it | .. code-block:: yml                                                             |
|                                                            |                                                                                                                                               |                                                                                 |
|                                                            |                                                                                                                                               |    variables:                                                                   |
|                                                            |                                                                                                                                               |      development:                                                               |
|                                                            |                                                                                                                                               |        EOX_TENANT_LOAD_PERMISSIONS": false                                      |
|                                                            |                                                                                                                                               |      production:                                                                |
|                                                            |                                                                                                                                               |        EOX_TENANT_LOAD_PERMISSIONS": false                                      |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+


It should look like this:

.. code-block:: yml

  DISTRO_EOX_THEMING_DPKG:
    index: git
    name: eox-theming
    private: false
    repo: eox-theming
    domain: github.com
    path: eduNEXT
    protocol: https
    version: v3.1.0
    variables:
      development:
        GET_BRANDING_API: eox_tenant.edxapp_wrapper.backends.branding_api_l_v1
        EOX_THEMING_CONFIG_SOURCES: [
          "from_eox_tenant_microsite_v2",
          "from_django_settings"
        ]
      production:
        GET_BRANDING_API: eox_tenant.edxapp_wrapper.backends.branding_api_l_v1
        EOX_THEMING_CONFIG_SOURCES: [
          "from_eox_tenant_microsite_v2",
          "from_django_settings"
        ]

Private packages
----------------

Once you define your private packages in config file you need to enable them with command:

.. code-block:: bash

  tutor distro enable-private-packages

Other Options
-------------

How to add extra files requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should set the variable **INSTALL_EXTRA_FILE_REQUIREMENTS** in your config.yml file if you need to install extra files with. The structure should be like:

.. code-block:: yaml

  INSTALL_EXTRA_FILE_REQUIREMENTS:
    path: ./requirements/extra_file/
    files: [
      /edunext/base.txt,
      /test/test.txt
    ]

It's important that ``.txt`` files are added in requirements directory, similar to EXTRA PIP REQUIREMENTS from `Tutor <https://docs.tutor.overhang.io/configuration.html#installing-extra-xblocks-and-requirements>`__.

How to enable openedx extra settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You should set the variable **OPENEDX_EXTRA_SETTINGS** in your config.yml file if you need to enable ``cms_env``, ``lms_env`` or ``pre_init_lms_task`` settings to plugins works as expected. For now the principals settings should be like this:

.. code-block:: yaml

  OPENEDX_EXTRA_SETTINGS:
    cms_env: [
      USE_EOX_TENANT: true
    ]
    lms_env: [
      USE_EOX_TENANT: true,
      ENABLE_EOX_THEMING_DERIVE_WORKAROUND: true
    ]
    pre_init_lms_tasks: [
      ./manage.py lms migrate contenttypes,
      ./manage.py lms migrate eox_core,
      ./manage.py lms migrate eox_tenant,
      ./manage.py lms migrate eox_tagging,
      ./manage.py lms migrate eox_audit_model
    ]

The list could grow according to the needs that arise at the time of configuring the plugins.

  **Note**: Other Options as ``INSTALL_EXTRA_FILE_REQUIREMENTS`` and ``OPENEDX_EXTRA_SETTINGS`` are included from Olmo version, you can use it from this release.

Use your new packages
----------------------

To use in local mode:

1. Build the docker image.
2. Run ``tutor local do init``
3. Run ``tutor local start``


To use in dev mode:

1. Run ``tutor dev do init``
2. Run ``tutor dev start``
