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
        "PUBLIC_PACKAGES": [ "eox-core[sentry] >= 7.0.0", "eox-tenant >= 6.2.0", "eox-theming >= 4.0", "eox-hooks >= 3.0", "eox-audit-model >= 1.0", "eox-tagging >= 5.0"],
        "EXTRA_SETTINGS": {
            "common": {},
            "development": {},
            "produccion" : {}
        },
        "THEMES_ROOT": "/openedx/themes",
        "THEME_DIRS": [],
        "THEMES_NAME": [],
        "THEMES": [],
        "INSTALL_EDNX_REQUIREMENTS": False,
        "DISTRO_DISABLE_MFE": False
    },
    "unique": {},
    "overrides": {
        "DOCKER_IMAGE_OPENEDX": "docker.io/ednxops/distro-edunext-edxapp:nuez",
        "DOCKER_IMAGE_OPENEDX_DEV": "docker.io/ednxops/distro-edunext-edxapp-dev:nuez",
        "EDX_PLATFORM_REPOSITORY": "https://github.com/eduNEXT/edunext-platform.git",
        "EDX_PLATFORM_VERSION": "ednx-release/nuez.master",
    },
}

################# Initialization tasks
# To run the script from templates/distro/tasks/myservice/init, add:
hooks.Filters.COMMANDS_INIT.add_item(
    (
        "lms",
        ("distro", "tasks", "lms", "init"),
    )
)

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
