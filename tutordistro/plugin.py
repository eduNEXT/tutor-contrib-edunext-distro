from glob import glob
import os
import pkg_resources

from tutor import hooks

from tutordistro.commands.cli import distro

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "defaults": {
        "VERSION": __version__,
        "EXTRA_MIDDLEWARES": [],
        # DISTRO PACKAGES
        "EOX_CORE_DPKG": {
            "index": "git",
            "name": "eox-core",
            "repo": "eox-core",
            "version": "v6.1.0",
            "domain": "github.com",
            "protocol": "https",
            "path": "eduNEXT",
            "variables": {
                "development": {
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper"
                                              ".backends.users_m_v1",
                    "EOX_CORE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper"
                                                   ".backends.enrollment_l_v1",
                    "EOX_CORE_PRE_ENROLLMENT_BACKEND": "eox_core"
                                                       ".edxapp_wrapper"
                                                       ".backends"
                                                       ".pre_enrollment_l_v1",
                },
                "production": {
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper"
                                              ".backends.users_m_v1",
                    "EOX_CORE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper"
                                                   ".backends.enrollment_l_v1",
                    "EOX_CORE_PRE_ENROLLMENT_BACKEND": "eox_core"
                                                       ".edxapp_wrapper"
                                                       ".backends"
                                                       ".pre_enrollment_l_v1",
                },
            },
            "private": False,
        },
        "EOX_TENANT_DPKG": {
            "index": "git",
            "name": "eox-tenant",
            "repo": "eox-tenant",
            "version": "v6.0.0",
            "domain": "github.com",
            "protocol": "https",
            "path": "eduNEXT",
            "variables": {
                "development": {
                    "EOX_TENANT_USERS_BACKEND": "eox_tenant.edxapp_wrapper"
                                                ".backends.users_l_v1",
                    "EOX_TENANT_LOAD_PERMISSIONS": False,
                },
                "production": {
                    "EOX_TENANT_USERS_BACKEND": "eox_tenant.edxapp_wrapper"
                                                ".backends.users_l_v1",
                    "EOX_TENANT_LOAD_PERMISSIONS": False,
                },
            },
            "private": False,
        },
        "EOX_THEMING_DPKG": {
            "index": "git",
            "name": "eox-theming",
            "repo": "eox-theming",
            "version": "v3.0.0",
            "domain": "github.com",
            "protocol": "https",
            "path": "eduNEXT",
            "variables": {
                "development": {
                    "GET_BRANDING_API": "eox_tenant.edxapp_wrapper.backends"
                                        ".branding_api_l_v1",
                },
                "production": {
                    "GET_BRANDING_API": "eox_tenant.edxapp_wrapper.backends"
                                        ".branding_api_l_v1",
                },
            },
            "private": False,
        },
        "EOX_AUDIT_MODEL_DPKG": {
            "index": "git",
            "name": "eox-audit-model",
            "repo": "eox-audit-model",
            "version": "v0.7.3",
            "domain": "github.com",
            "protocol": "https",
            "path": "eduNEXT",
            "variables": {
                "development": {
                },
                "production": {
                },
            },
            "private": False,
        },
        "EOX_TAGGING_DPKG": {
            "index": "git",
            "name": "eox-tagging",
            "repo": "eox-tagging",
            "version": "v4.0.0",
            "domain": "github.com",
            "protocol": "https",
            "path": "eduNEXT",
            "variables": {
                "development": {
                    "EOX_TAGGING_GET_ENROLLMENT_OBJECT": "eox_tagging"
                                                         ".edxapp_wrappers"
                                                         ".backends.enrollment_l_v1",
                },
                "production": {
                    "EOX_TAGGING_GET_ENROLLMENT_OBJECT": "eox_tagging"
                                                         ".edxapp_wrappers"
                                                         ".backends.enrollment_l_v1",
                },
            },
            "private": False,
        },
        "THEMES_ROOT": "/openedx/themes",
        "THEME_DIRS": [
            "/openedx/themes/ednx-saas-themes/edx-platform",
            "/openedx/themes/ednx-saas-themes/edx-platform/bragi-children",
            "/openedx/themes/ednx-saas-themes/edx-platform/bragi-generator",
        ],
        "THEMES_NAME": [
            "bragi",
        ],
        "THEMES": [
            {
                "name": "ednx-saas-themes",
                "repo": "ednx-saas-themes",
                "version": "edunext/mango.master",
                "domain": "github.com",
                "protocol": "ssh",
                "path": "eduNEXT",
            },
        ],
        "INSTALL_EDNX_REQUIREMENTS": False,
    },
    "unique": {},
    "overrides": {
        "DOCKER_IMAGE_OPENEDX": "docker.io/ednxops/distro-edunext-edxapp:vM.mango.1.0",
        "DOCKER_IMAGE_OPENEDX_DEV": "docker.io/ednxops/distro-edunext-edxapp-dev:vM.mango.1.0",
        "EDX_PLATFORM_REPOSITORY": "https://github.com/eduNEXT/edunext-platform.git",
        "EDX_PLATFORM_VERSION": "ednx-release/mango.master",
    },
}

################# Initialization tasks
# To run the script from templates/distro/tasks/myservice/init, add:


# Plugin templates
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    pkg_resources.resource_filename("tutordistro", "templates")
)
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("distro/build", "plugins"),
        ("distro/apps", "plugins"), 
    ],
)
# Load all patches from the "patches" folder
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutordistro", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

# Load all configuration entries
hooks.Filters.CLI_COMMANDS.add_items(
    [
        distro,
    ]
)

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"DISTRO_{key}", value)
        for key, value in config["defaults"].items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"DISTRO_{key}", value)
        for key, value in config["unique"].items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(list(config["overrides"].items()))
