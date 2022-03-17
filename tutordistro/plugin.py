from glob import glob
import os

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "defaults": {
        "VERSION": __version__,
        "EOX_CORE": True,
        "EOX_TENANT": True,

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
                "production": {}
            }
        },
        "EOX_TENANT_DPKG": {
            "name": "eox-tenant",
            "index": "pip",
            "version": "6.0.0",
            "variables": {
                "development": {
                   "EOX_TENANT_USERS_BACKEND": "eox_tenant.edxapp_wrapper.backends.users_l_v1",
                   "EOX_TENANT_LOAD_PERMISSIONS": False,
                },
                "production": {}
            }
        }
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