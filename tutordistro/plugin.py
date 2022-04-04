from glob import glob
import os
import click
from tutor.commands.context import Context

from tutordistro.commands.enable_themes import enable_themes

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "defaults": {
        "VERSION": __version__,
        # DISTRO PACKAGES
        "EOX_CORE_DPKG": {
            "name": "eox-core",
            "index": "git",
            "repository": "https://github.com/eduNEXT/eox-core.git",
            "version": "v5.1.1",
            "variables": {
                "development": {
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper"
                                              ".backends.users_l_v1",
                    "EOX_CORE_ENROLLMENT_BACKEND": "eox_core.edxapp_wrapper"
                                                   ".backends.enrollment_l_v1",
                    "EOX_CORE_PRE_ENROLLMENT_BACKEND": "eox_core"
                                                       ".edxapp_wrapper"
                                                       ".backends"
                                                       ".pre_enrollment_l_v1",
                },
                "production": {
                    "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper"
                                              ".backends.users_l_v1",
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
            "name": "eox-tenant",
            "index": "git",
            "version": "v5.1.3",
            "repository": "https://github.com/eduNEXT/eox-tenant.git",
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
            "repository": "https://github.com/eduNEXT/eox-theming.git",
            "version": "v2.0.0",
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
            "repository": "https://github.com/eduNEXT/eox-audit-model.git",
            "version": "v0.7.0",
            "variables": {
                "development": {
                },
                "production": {
                },
            },
            "private": False,
        },
        "EOX_HOOKS_DPKG": {
            "index": "git",
            "name": "eox-hooks",
            "repository": "https://github.com/eduNEXT/eox-hooks.git",
            "version": "v2.0.0",
            "variables": {
                "development": {
                    "EOX_HOOKS_ENROLLMENTS_BACKEND": "eox_hooks.edxapp_wrapper.backends.enrollments_l_v1",
                    "EOX_HOOKS_COURSES_BACKEND": "eox_hooks.edxapp_wrapper.backends.courses_l_v1",
                    "EOX_HOOKS_COURSE_MODES_BACKEND": "eox_hooks.edxapp_wrapper.backends.course_modes_l_v1",
                    "EOX_HOOKS_MODELS_BACKEND": "eox_hooks.edxapp_wrapper.backends.models_l_v1",
                },
                "production": {
                    "EOX_HOOKS_ENROLLMENTS_BACKEND": "eox_hooks.edxapp_wrapper.backends.enrollments_l_v1",
                    "EOX_HOOKS_COURSES_BACKEND": "eox_hooks.edxapp_wrapper.backends.courses_l_v1",
                    "EOX_HOOKS_COURSE_MODES_BACKEND": "eox_hooks.edxapp_wrapper.backends.course_modes_l_v1",
                    "EOX_HOOKS_MODELS_BACKEND": "eox_hooks.edxapp_wrapper.backends.models_l_v1",
                },
            },
            "private": False,
        },
        "EOX_TAGGING_DPKG": {
            "index": "git",
            "name": "eox-tagging",
            "repository": "https://github.com/eduNEXT/eox-tagging.git",
            "version": "v3.0.0",
            "variables": {
                "development": {
                    "EOX_TAGGING_GET_ENROLLMENT_OBJECT": "eox_tagging.edxapp_wrappers.backends.enrollment_l_v1",
                },
                "production": {
                    "EOX_TAGGING_GET_ENROLLMENT_OBJECT": "eox_tagging.edxapp_wrappers.backends.enrollment_l_v1",
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
                "version": "edunext/limonero.master",
                "domain": "github.com",
                "protocol": "ssh",
                "path": "eduNEXT",
            },
        ],
        "INSTALL_EDNX_REQUIREMENTS": True,
    },
    "set": {
        "DOCKER_IMAGE_OPENEDX": "docker.io/ednxops/distro-edunext-edxapp:vL"
                                ".limonero.1.0-plugin",
        "DOCKER_IMAGE_OPENEDX_DEV": "docker.io/ednxops/distro-edunext-edxapp"
                                    "-dev:vL.limonero.1.0-plugin",
        "EDX_PLATFORM_REPOSITORY": "https://github.com/eduNEXT/edunext-platform.git",
        "EDX_PLATFORM_VERSION": "limonero.5.1",
    },
}

hooks = {}


def patches():  # pylint: disable=missing-function-docstring
    all_patches = {}
    for path in glob(os.path.join(HERE, "patches", "*")):
        with open(path, 'r', encoding="utf8") as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches


@click.group(help="Distro plugin", commands=(enable_themes,))
@click.pass_obj
def command(context: Context) -> None:  # pylint: disable=unused-argument,missing-function-docstring
    pass


command.add_command(enable_themes)
