from glob import glob
import os
import click

from .commands import enable_theme_volumes

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "defaults": {
        "VERSION": __version__,
        "ENVIRONMENT_BASIC": False,
        "EOX_CORE": True,
        "EOX_TENANT": True,
        "EOX_THEMING": True,

        # DISTRO PACKAGES
        "EOX_CORE_DPKG": {
            "name": "eox-core",
            "index": "git",
            "repository": "https://github.com/eduNEXT/eox-core.git",
            "version": "v6.0.1",
            "variables": {
                "development": {
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper.backends.users_m_v1",
                    "EOX_CORE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper.backends.enrollment_l_v1",
                    "EOX_CORE_PRE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper.backends.pre_enrollment_l_v1"
                },
                "production": {
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper.backends.users_m_v1",
                    "EOX_CORE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper.backends.enrollment_l_v1",
                    "EOX_CORE_PRE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper.backends.pre_enrollment_l_v1"
                }
            }
        },
        "EOX_TENANT_DPKG": {
            "name": "eox-tenant",
            "index": "git",
            "version": "v6.0.0",
            "repository": "https://github.com/eduNEXT/eox-tenant.git",
            "variables": {
                "development": {
                   "EOX_TENANT_USERS_BACKEND": "eox_tenant.edxapp_wrapper.backends.users_l_v1",
                   "EOX_TENANT_LOAD_PERMISSIONS": False,
                },
                "production": {
                   "EOX_TENANT_USERS_BACKEND": "eox_tenant.edxapp_wrapper.backends.users_l_v1",
                   "EOX_TENANT_LOAD_PERMISSIONS": False,
                }
            }
        },
        "EOX_THEMING_DPKG": {
            "index": "git",
            "name": "eox-theming",
            "repository": "https://github.com/eduNEXT/eox-theming.git",
            "version": "v3.0.0",
            "variables": {
                "development": {
                   "GET_BRANDING_API": "eox_tenant.edxapp_wrapper.backends.branding_api_l_v1",
                },
                "production": {
                   "GET_BRANDING_API": "eox_tenant.edxapp_wrapper.backends.branding_api_l_v1",
                }
            }
        },
        "THEMES_ROOT": "/openedx/distro-themes",
        "THEME_DIRS": [
            "/openedx/distro-themes/ednx-saas-themes/edx-platform",
            "/openedx/distro-themes/ednx-saas-themes/edx-platform/bragi-children",
            "/openedx/distro-themes/ednx-saas-themes/edx-platform/bragi-generator",
        ],
        "THEMES_NAME": [
            "bragi",
        ],
        "THEMES": [
            {
                "repo": "ednx-saas-themes",
                "version": "edunext/mango.master",
                "domain": "github.com",
                "protocol": "https",
                "path": "eduNEXT",
            },
        ],
    },
    "set": {
        "DOCKER_IMAGE_OPENEDX": "docker.io/ednxops/distro-edunext-edxapp:vM.mango.1.0-plugin",
        "DOCKER_IMAGE_OPENEDX_DEV": "docker.io/ednxops/distro-edunext-edxapp-dev:vM.mango.1.0-plugin",
        "EDX_PLATFORM_REPOSITORY": "https://github.com/eduNEXT/edunext-platform.git",
        "EDX_PLATFORM_VERSION": "edunext/mango.master",
    }
}

hooks = {}


def patches():
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches


@click.group(help="Distro plugin", commands=(enable_theme_volumes,))
def command():
    pass
