"""
Tutor distrto defaults settings.
"""

import os
from glob import glob

import pkg_resources
from tutor import hooks

from tutordistro.commands.cli import distro
from tutormfe.hooks import MFE_APPS

from .__about__ import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

templates = os.path.join(HERE, "templates")

config = {
    "defaults": {},
    "unique": {},
    "overrides": {},
}


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
        hooks.Filters.ENV_PATCHES.add_item((
            os.path.basename(path), patch_file.read()
        ))

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

@MFE_APPS.add()
def _add_my_mfe(mfes):
    mfes["learning"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-learning.git",
        "port": 2000,
        "version": "ednx-release/palma.master",
    }
    mfes["account"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-account.git",
        "port": 1997,
        "version": "ednx-release/palma.master",
    }
    mfes["gradebook"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-gradebook.git",
        "port": 1994,
        "version": "ednx-release/palma.master",
    }
    mfes["profile"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-profile.git",
        "port": 1995,
        "version": "ednx-release/palma.master",
    }
    mfes["authn"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-authn.git",
        "port": 1999,
        "version": "ednx-release/palma.master",
    }
    mfes["communications"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-communications.git",
        "port": 1984,
        "version": "ednx-release/palma.master",
    }
    mfes["discussions"] = {
        "repository": "https://github.com/eduNEXT/frontend-app-discussions.git",
        "port": 2002,
        "version": "ednx-release/palma.master",
    }
    mfes["ora-grading"] = {
        "repository": "https://github.com/edunext/frontend-app-ora-grading.git",
        "port": 1993,
        "version": "ednx-release/palma.master",
    }
    return mfes
