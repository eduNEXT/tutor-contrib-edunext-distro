How to override or add a new package
====================================

You can add or override a package directly in config.yml file (``$(tutor config printroot)/config.yaml``).

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


Override packages
-----------------

To override a default package identify its name and set it like ``DISTRO_<PACKAGE_NAME>_DPKG:``, and add the package variables. You can check all default plugins name `here <./how_to_customize_distro.rst#plugins-or-packages>`_ 

An example of override eox-theming plugin:

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
    


Use your new packages
----------------------

To use in local mode:

1. Build the docker image.
2. Run ``tutor local init``
3. Run ``tutor local start``


To use in dev mode:

1. Run ``tutor dev init``
2. Run ``tutor dev start``