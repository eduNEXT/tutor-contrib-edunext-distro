# Distro plugin for [Tutor](https://docs.tutor.overhang.io)

This plugin is a tool to facilitate the customization of an Open edX instance, adding commands and settings to have an easy-to-use
and a ready-to-deploy in a local or development environment.

## Installation

To install the latest release, run:

```bash
pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro
```

You can install a specific version by adding the tag at the end, e.g, `@v17.0.0`

## Usage

1. **Enable the plugin**: after installing the plugin, enable it by running:

```bash
tutor plugins enable distro
```

2. **Configure the Distro plugin**: this plugin adds a new set of settings used to further customize your Open edX installation. Refer to the following documentation to know the Distro variables:

- [How to customize distro](./docs/how_to_customize_distro.rst)
- [How to add a new package](./docs/how_to_add_new_packages.rst)

> [!NOTE]
> From version 15, this plugin has no default values.

3.  After enabling the plugin, you'll have the following [commands](#commands) available to use:

```bash
# Validate the Distro settings are properly set
tutor distro syntax-validator

# Validate the repositories for packages are valid
tutor distro repository-validator

# Enable themes
tutor distro enable-themes

# Enable private packages
tutor distro enable-private-packages

# Run Tutor commands
tutor distro run-extra-commands
```

4. Launch your customized instance `tutor local launch` or `tutor dev launch`.

### Using a custom edx-platform branch

If you want to use a custom edx-platform branch alongside the plugin, your branch must be compatible with the plugin's release. Refer to the [How to customize distro](./docs/how_to_customize_distro.rst) document to set up the repository.

Please see the following table for details on compatibility.

| openedx | tutor |
| ------- | ----- |
| lilac   | v12   |
| maple   | v13   |
| nutmeg  | v14   |
| olive   | v15   |
| palm    | v16   |
| quince  | v17   |

Then, specify the docker image variables to identify your custom images, like the example:

```yaml
DOCKER_IMAGE_OPENEDX: 'docker.io/ednxops/distro-edunext-edxapp:quince'
DOCKER_IMAGE_OPENEDX_DEV: 'docker.io/ednxops/distro-edunext-edxapp-dev:quince'
```

Finally, launch your instance or build a new image to reflect the changes.

> [!NOTE]  
> Check the [Tutor Documentation](https://docs.tutor.edly.io/configuration.html#custom-open-edx-docker-image) for more information on working with custom repositories and images.

# Packages

A package is used to modify or extend the platform's functionality, this includes plugins and xblocks.

If you are not adding configuration variables to your packages or installing private packages, you can use
[**OPENEDX_EXTRA_PIP_REQUIREMENTS**](https://docs.tutor.edly.io/configuration.html#installing-extra-xblocks-and-requirements).
instead.

## How to add a new package

In your `config.yml` you can include a package by following this structure:

```yaml
DISTRO_MY_PACKAGE_NAME_DPKG:
  index: git
  name: eox-package # directory name
  # ---- git package variables
  repo: eox-package # git repository name
  domain: github.com
  path: eduNEXT
  protocol: ssh
  # ---- end git package variables
  version: master
  private: true
  variables:
    development: {}
    production: {}
# If you want to install a package from pip,
# you must set the index to pip and remove the repository but this
# won't be installed as editable.
```

The package's variables will be loaded as LMS and CMS settings.

In case you want to make your package
editable, then you can [mount it as a volume](https://docs.tutor.overhang.io/dev.html?highlight=bind#manual-bind-mount-to-any-directory) using that path.

### Private packages

Setting the value **private** to `true` in your package configuration allows you to install a package from
a private repository. For it to work, enable it by running this command:

```bash
tutor distro enable-private-packages
```

> [!IMPORTANT]
> After adding public or private packages in a **local** environment, you should run:
>
> ```bash
> tutor images build openedx
> tutor local do init
> tutor local start
> ```
>
> or
>
> ```bash
> tutor local launch
> ```

> [!IMPORTANT]
> After adding public or private packages in a **dev** environment, you should run:
>
> ```bash
> tutor images build openedx-dev
> tutor dev do init
> tutor dev start
> ```
>
> or
>
> ```bash
> tutor dev launch
> ```

# Themes

We use a [theme](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/changing_appearance/theming/)
for changing the appearance across the Open edX platform.

Declare the path where your themes will be located with `tutor config save --set DISTRO_THEMES_ROOT="your_path"`, we recommend using **/openedx/themes**

When you set the `DISTRO_THEMES_ROOT`, the theme will be in your `<tutor_root>/env/build<distro_themes_root>`.

```yaml
DISTRO_THEMES_ROOT: /openedx/themes
```

In the previous example, the theme will be in `env/build/openedx/themes` when you execute the `enable-themes` command.

## How to add a theme

1. Set a list of themes to clone by adding `DISTRO_THEMES` configuration to your `config.yml` file, each of them should follow the structure:

```yaml
DISTRO_THEMES:
  - domain: github.com
    name: my-theme
    path: my-account
    protocol: ssh
    repo: my-openedx-theme
    version: release-compatible
```

Where:

- **Domain** corresponds to the hosting service where the theme is stored.
- **Name** is the folder where the theme will be located inside Tutor.
- **Path** is used for the URL. For GitHub repositories correspond to the username.
- **Protocol** used for cloning the theme, `ssh` for private repos, and `https` for public ones.
- **Repo** is the name of the remote repository.
- **Version** designates the branch to be cloned.

2. Set 1 or more theme directories:

```yaml
DISTRO_THEME_DIRS:
  - /openedx/themes/my-openedx-theme
```

3. Set a list of the theme names that will be enabled in your instance:

```yaml
DISTRO_THEMES_NAME:
  - my-theme
```

> [!TIP]
> If you have more than 1 theme installed, you can use `DISTRO_DEFAULT_SITE_THEME` to set the default one, otherwise, the first one in the list name will be used.

4. Run the command to clone and enable the themes:

```bash
tutor distro enable-themes
```

> [!IMPORTANT]
> After adding themes in a **local** environment, you should run:
>
> ```bash
> tutor images build openedx
> tutor local do init
> tutor local start
> ```
>
> or
>
> ```bash
> tutor local launch
> ```

> [!IMPORTANT]
> After adding themes in a **dev** environment, you should run:
>
> ```bash
> tutor images build openedx-dev
> tutor dev do init
> tutor dev start
> tutor dev run lms openedx-assets themes --theme-dirs [THEME_DIRS] --themes [THEME_NAMES]
> ```
>
> or
>
> ```bash
> tutor dev launch
> tutor dev run lms openedx-assets themes --theme-dirs [THEME_DIRS] --themes [THEME_NAMES]
> ```

# Commands

## Validators

Helpers for ensuring the correct setting definition.

### Repository validator

If you want to make sure that the git repository urls in the config.yml file are valid, run the following command:

```bash
tutor distro repository-validator
```

The command will check the git URLs of the `OPENEDX_EXTRA_PIP_REQUIREMENTS` element, for example, git+https://github.com/openedx/DoneXBlock@2.0.1#egg=done-xblock

It will also check all elements that end in DPKG and have the parameter private: false, for example:

```yml
DISTRO_EOX_HOOKS_DPKG:
  index: git
  name: eox-hooks
  repo: eox-hooks
  domain: github.com
  path: eduNEXT
  protocol: https
  private: false
  variables:
    development: {}
    production: {}
  version: master
```

### Syntax validator

If you want to validate the syntax of the config.yml file, run the following command:

```bash
tutor distro syntax-validator
```

The command will check the configuration for:

- Packages, ending with \_DPKG
- OPENEDX_EXTRA_PIP_REQUIREMENTS
- DISTRO_THEMES
- Theme settings like DISTRO_THEMES_NAME, DISTRO_THEME_DIRS and DISTRO_THEMES_ROOT
- INSTALL_EXTRA_FILE_REQUIREMENTS
- OPENEDX_EXTRA_SETTINGS

## Enablers

Commands for clone and set up themes and private packages in your instance.

Visit [Themes](#how-to-add-a-theme) and [Packages](#private-package) sections for better understanding.

## Tutor extra commands

This feature is useful for creating build pipelines or replicating instances with the same Tutor configuration with fewer steps.
You can run different tutor commands at once by adding them into the **config.yml** in the `DISTRO_EXTRA_COMMANDS` attribute, like this:

```yaml
DISTRO_EXTRA_COMMANDS:
  - tutor plugins install mfe && tutor plugins enable mfe
  - tutor plugins index add https://overhang.io/tutor/main
```

> [!NOTE]
> You can only insert commands enabled by the [Tutor CLI](https://docs.tutor.edly.io/reference/cli/index.html).

Once you have added the commands you want to execute, you will need to run the following command:

```bash
tutor distro run-extra-commands
```

# Other configurations available

Useful for extending the edx-platform configuration.

## How to add custom middleware

You should set the variable **DISTRO_EXTRA_MIDDLEWARES** in your config.yml to add a new middleware in `settings.MIDDLEWARE`

```yaml
DISTRO_EXTRA_MIDDLEWARES:
  - middleware.test.1
  - middleware.test.2
```

## How to add extra file requirements

You should set the variable **INSTALL_EXTRA_FILE_REQUIREMENTS** in your config.yml file if you need to install extra files. The structure should be like:

```yaml
INSTALL_EXTRA_FILE_REQUIREMENTS:
  path: ./requirements/extra_file/
  files: [/edunext/base.txt, /test/test.txt]
```

It's important that `.txt` files are added in the requirements directory, similar to EXTRA PIP REQUIREMENTS from
[Tutor](https://docs.tutor.overhang.io/configuration.html#installing-extra-xblocks-and-requirements).

## How to enable openedx extra settings

You should set the variable **OPENEDX_EXTRA_SETTINGS** in your config.yml file if you need to enable `cms_env`, `lms_env`, or `pre_init_lms_task` settings to make
plugins work as expected. For now, the principal settings should be like this:

```yaml
OPENEDX_EXTRA_SETTINGS:
  cms_env: [USE_EOX_TENANT: true]
  lms_env: [USE_EOX_TENANT: true, ENABLE_EOX_THEMING_DERIVE_WORKAROUND: true]
  pre_init_lms_tasks:
    [
      ./manage.py lms migrate contenttypes,
      ./manage.py lms migrate eox_core,
      ./manage.py lms migrate eox_tenant,
      ./manage.py lms migrate eox_tagging,
      ./manage.py lms migrate eox_audit_model,
    ]
```

The list could grow according to the needs that arise at the time of configuring plugins.

> [!IMPORTANT]
> **INSTALL_EXTRA_FILE_REQUIREMENTS** and **OPENEDX_EXTRA_SETTINGS** are included from version 15.

# License

This software is licensed under the terms of the AGPLv3.
