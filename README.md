# Distro plugin for [Tutor](https://docs.tutor.overhang.io)

This plugin facilitates customizing Open edX by adding commands and settings to make your instance easy to use and deploy locally or in development environments.

## Installation

To install the latest release, run:

```bash
pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro
```

You can install a specific version by adding the tag at the end, e.g.:

```bash
pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro#v.17.0.0
```

## Usage

1. **Enable the plugin**: after installing the plugin, enable it by running:

```bash
tutor plugins enable distro
```

2. **Configure the Distro plugin**: this plugin adds a new set of settings use to further customize your Open edX installation. Refer to the following documentation to know the Distro variables:

- [How to customize distro](./docs/how_to_customize_distro.rst)
- [How to add a new package](./docs/how_to_add_new_packages.rst)

:warning: From version 15, this plugin has no default values.

3. After enabling the plugin, you'll have the following commands available to use:

```bash
# Validate the Distro settings are properly set
tutor distro syntax-validator

# Validate the repositories for packages are valid
tutor distro repository-validator

# Enable the themes
tutor distro enable-themes

# Enable the package
tutor distro enable-private-packages

# Run Tutor commands
tutor distro run-extra-commands
```
### SUGGESTION: add reference to the documentation for each command ###


4. Launch your customized instance `tutor local launch` or `tutor dev launch`.

### Using a custom edx-platform branch

If you want to use a custom edx-platform branch alongside the plugin, your branch must be compatible with the plugin's release. Please see the following table for details on compatibility.

| openedx | tutor |
| ------- | ----- |
| lilac   | v12   |
| maple   | v13   |
| nutmeg  | v14   |
| olive   | v15   |
| palm    | v16   |
| quince  | v17   |

Then, specify the docker image variables to identify the images with the new branch. Then, launch your instance or build the new images.

Example:

```yaml
DOCKER_IMAGE_OPENEDX: 'docker.io/ednxops/distro-edunext-edxapp:quince'
DOCKER_IMAGE_OPENEDX_DEV: 'docker.io/ednxops/distro-edunext-edxapp-dev:quince'
```

# Packages

### SUGGESTION: add description to each section ###

If you're not adding configuration variables to your packages or installing private packages, you can use `OPENEDX_EXTRA_PIP_REQUIREMENTS` instead.

## How to add a new package

In your ``config.yml`` you can include a package by following this structure:

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

Your package will be cloned in a **dev** environment on **/openedx/extra_deps/MY-PLUGIN-NAME**. In case you want to make your package
editable, then you can [mount it as a volume](https://docs.tutor.overhang.io/dev.html?highlight=bind#manual-bind-mount-to-any-directory) using that path.

### Private packages

Setting the value **private** to ``true`` in your package configuration allows you to install a package from
a private repository. For it to work, enable it by running this command:

```bash
tutor distro enable-private-packages
```

ℹ️ After enabling in a **local** environment, you should run:
```bash
tutor images build openedx
tutor local do init
tutor local start
```
or
```bash
tutor local launch
```

ℹ️ After enabling in a **dev** environment, you should run:
```bash
tutor images build openedx
tutor dev do init
tutor dev start
```
or
```bash
tutor dev launch
```

# Themes

We use [themes](https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/changing_appearance/theming/)
for changing the appearance across the Open edX platform.

Declare the path where your themes will be located with `tutor config save --set DISTRO_THEMES_ROOT="your_path"`, we recommend using **/openedx/themes**

When you set the `DISTRO_THEMES_ROOT`, the theme will be in your `<tutor_root>/env/build<distro_themes_root>`.

```yaml
DISTRO_THEMES_ROOT: /openedx/themes
```

In the previous example, the theme will be in `env/build/openedx/themes` when you execute the `enable-themes` command.

## How to add a theme

1. Set the themes to clone by adding this configuration to your ``config.yml`` file:

```yaml
DISTRO_THEMES:
  - domain: github.com # where the theme is stored
    name: my-theme #  folder for cloning the repo inside Tutor
    path: my-account # used for the URL; for GitHub repositories correspond to the username
    protocol: ssh # use ssh for private repos and https for public ones
    repo: my-openedx-theme # name of the repository
    version: release-compatible # branch to be cloned
```

Where:
... explain each value instead of in the snippet, so people can copy paste the configuration.

2. Set the theme directory:

```yaml
DISTRO_THEME_DIRS:
  - /openedx/themes/my-openedx-theme
```

3. Set themes name:

```yaml
DISTRO_THEMES_NAME:
  - my-theme
```

If you have more than 1 theme installed, you can use `DISTRO_DEFAULT_SITE_THEME` to set the default one.

Run the command to clone and enable the theme(s):

```bash
tutor distro enable-themes
```

### SUGGESTION: same suggestion here about using the information icons ###

- **local**: you must build a new image to add the new themes and
  compile statics and run the command `tutor local do init && tutor local start` again.
- **dev**: you must run the command `tutor dev do init && tutor dev start` again.
  - **Since tutor 13.0.0** you should recompile statics in the container, you could run the next command to do it:
  ```bash
  openedx-assets themes --theme-dirs THEME_DIRS --themes THEME_NAMES
  ```

# Build a new image

### SUGGESTION: why is a section for building a new image needed? Shouldn't tutor images build be enough?  ###

**Requirements:** You should have enabled the distro plugin, also you should have run the commands `tutor distro enable-themes` and `tutor distro enable-private-packages`.

1. You should change 2 variables in your config.yml to define the new DOCKER_IMAGE_OPENEDX and DOCKER_IMAGE_OPENEDX_DEV to use.

2. You should run the next command:

```bash
export DOCKER_BUILDKIT=1
tutor images build -a BUILDKIT_INLINE_CACHE=1 --docker-arg="--cache-from" --docker-arg="<docker-user>/<docker-repository>:<image-tag>" -a EDX_PLATFORM_REPOSITORY=<your-edx-repo> -a EDX_PLATFORM_VERSION=<branch> openedx
```

### SUGGESTION: why is this needed? instead of using tutor images build ###

3. That command will create a new image with the tag defined in your DOCKER_IMAGE_OPENEDX, now, you should run the next command:

```bash
tutor images push openedx
```

# Extra commands

## Validators

### Check the git repository URL

If you want to make sure that the git repository urls in the config.yml file are valid, run the following command:

```bash
tutor distro repository-validator
```

The command will check the git URLs of the OPENEDX_EXTRA_PIP_REQUIREMENTS element, for example, git+https://github.com/openedx/DoneXBlock@2.0.1#egg=done-xblock

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

### Check syntax in the configuration file

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

## Run tutor extra commands

### SUGGESTION: can we include why would I need this? Something like: this is useful when... ###

You can run tutor extra commands by adding them into the **config.yml** in an attribute `DISTRO_EXTRA_COMMANDS` like this:

```yaml
DISTRO_EXTRA_COMMANDS:
  - tutor plugins install mfe && tutor plugins enable mfe
  - tutor plugins index add https://overhang.io/tutor/main
```

You can only insert commands enabled by the [Tutor CLI](https://docs.tutor.edly.io/reference/cli/index.html). Once you have added the commands you want to execute, you will need to run the following command:

```bash
tutor distro run-extra-commands
```


### SUGGESTION: can we include why would I need these other configurations? Something like: this is useful when... ###

# Other configurations available

## How to add custom middleware

You should set the variable **DISTRO_EXTRA_MIDDLEWARES** in your config.yml to add a new
middleware to **settings.MIDDLEWARE**

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

It's important that `.txt` files are added in the requirements directory, similar to EXTRA PIP REQUIREMENTS from [Tutor](https://docs.tutor.overhang.io/configuration.html#installing-extra-xblocks-and-requirements).

## How to enable openedx extra settings

You should set the variable **OPENEDX_EXTRA_SETTINGS** in your config.yml file if you need to enable `cms_env`, `lms_env` or `pre_init_lms_task` settings to plugins work as expected. For now, the principal settings should be like this:

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

The list could grow according to the needs that arise at the time of configuring the plugins.

:warning: **Note**: Other Options such as `INSTALL_EXTRA_FILE_REQUIREMENTS` and `OPENEDX_EXTRA_SETTINGS` are included in the v15 version, you can use them from this release.

# License

This software is licensed under the terms of the AGPLv3.
