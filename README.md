# Distro plugin for [Tutor](https://docs.tutor.overhang.io)

## What is distro
Distro is an opinioned openedx distribution with some custom stuff to have an easy-to-use
and a ready to deploy in local or in development openedx distribution.
This can be watch like a tutor-plugin but is taken a little bit far away.

## Installation
`pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro@v2.0.0`

## Usage
```bash
tutor plugins enable distro
tutor distro enable-themes
````
# Required tutor settings
This plugin works with some docker images. These are defined by default
if you have different images that aren't based on these, you can have some problems.

```yaml
DOCKER_IMAGE_OPENEDX: "docker.io/ednxops/distro-edunext-edxapp:nuez"
DOCKER_IMAGE_OPENEDX_DEV: "docker.io/ednxops/distro-edunext-edxapp-dev:nuez"
```

Also, you need an edx-platform version distro compatible.

| openedx  |  distro  |  tutor  |
|----------|----------|---------|
|  lilac   | limonero |   v12   |
|  maple   |   mango  |   v13   |
|  nutmeg  |   nuez   |   v14   |

You can find distro releases on https://github.com/edunext/edunext-platform.

```yaml
EDX_PLATFORM_REPOSITORY: "https://github.com/eduNEXT/edunext-platform.git"
EDX_PLATFORM_VERSION: "ednx-release/nuez.master"
```

# Packages

## Default packages
These packages will be installed in a default installation.

- eox-theming (DISTRO_EOX_THEMING_DPKG)
- eox-tenant (DISTRO_EOX_TENANT_DPKG)
- eox-core (DISTRO_EOX_CORE_DPKG)
- eox-hooks (DISTRO_EOX_HOOKS_DPKG)
- eox-audit-model (DISTRO_EOX_AUDIT_MODEL_DPKG)
- eox-tagging (DISTRO_EOX_TAGGING_DPKG)

**NOTE**: Currently nuez only install eox-tenant by default.

## How to add a new package
In your config.yml you can set any package following this structure:

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

# If you want to install a package from pip
# you must set the index to pip and remove repository but this
# won't be installed as editable.
````

Package's variables will be used on cms and lms settings.

In the dev environment your package will be cloned on **/openedx/extra_deps/MY-PLUGIN-NAME**
if you want to edit it you can
[mount a volume](https://docs.tutor.overhang.io/dev.html?highlight=bind#manual-bind-mount-to-any-directory) to that path.

### Private package
In your new package you can set the setting **private** on true, It's mean that this won't be cloned
from a public repository, for it works you should run the command to clone private packages:

```bash
tutor distro enable-private-packages
```

- **local**: It will be necessary to build a new image and run the command tutor local init && tutor local start again.
- **dev**: you must run the command tutor dev init && tutor dev start again.

## How to override a default package
You can use the same steps that in **How to add a new package** just set the variable with the same name:

- DISTRO_EOX_CORE_DPKG
- DISTRO_EOX_TENANT_DPKG
- DISTRO_EOX_THEMING_DPKG
- DISTRO_EOX_HOOKS_DPKG
- DISTRO_EOX_AUDIT_MODEL_DPKG
- DISTRO_EOX_TAGGING_DPKG

## Disable packages
You can disable any default package following this structure in your config.yml:

```yaml
DISTRO_MY_PACKAGE_NAME_DPKG: None
```

Development environment take this changes with _tutor config save_ and restart, the local environment needs to rebuild the image to take it.

> **Warning:** Default packages can have dependencies with other default packages or base application and disable it would break some features.

# Themes
Declare the path of your themes using `tutor config save --set DISTRO_THEMES_ROOT="your_path"`,
by default the themes path goes here **/openedx/themes**

## Default themes
These themes will be installed in a default installation.

- [bragi](https://github.com/eduNEXT/ednx-saas-themes/tree/edunext/mango.master)

**NOTE**: Currently nuez doesn't have a default theme.

## How to add a theme
You can override the default themes on the config.yml but
this will remove them if you don't define them again.

Set the themes to clone:
```yaml
DISTRO_THEMES:
- domain: github.com
  name: ednx-saas-themes
  path: eduNEXT
  protocol: ssh
  repo: ednx-saas-themes
  version: edunext/mango.master
```

Set themes dir:
```yaml
DISTRO_THEME_DIRS:
- /openedx/themes/ednx-saas-themes/edx-platform
- /openedx/themes/ednx-saas-themes/edx-platform/bragi-children
- /openedx/themes/ednx-saas-themes/edx-platform/bragi-generator
```

Set themes name:
```yaml
DISTRO_THEMES_NAME:
- bragi
```

Run the command to clone the themes:
```bash
tutor distro enable-themes
```

- **local**: you must build a new image to add the new themes and
compile statics and run the command `tutor local init && tutor local start` again.
- **dev**: you must run the command `tutor dev init && tutor dev start` again.
  - **since tutor 13.0.0** you should recompile statics in the container, you could run the next command to do it:
  ```bash
  openedx-assets themes --theme-dirs THEME_DIRS --themes THEME_NAMES
  ```

# Build a new image
**requirements:** you should have enabled the distro plugin, also you had have run the commands `tutor distro enable-themes` and `tutor distro enable-private-packages`.

1. You should change 2 variables in your config.yml to define the new DOCKER_IMAGE_OPENEDX and DOCKER_IMAGE_OPENEDX_DEV to use.

2. You should run the next command:
```bash
export DOCKER_BUILDKIT=1
tutor images build -a BUILDKIT_INLINE_CACHE=1 --docker-arg="--cache-from" --docker-arg="ednxops/distro-edunext-edxapp:mango" -a EDX_PLATFORM_REPOSITORY=https://github.com/eduNEXT/edunext-platform.git -a EDX_PLATFORM_VERSION=ednx-release/mango.master openedx
```
If you are using another edx-platform you should change it in the commando.

3. That command will create a new image with the tag defined in your DOCKER_IMAGE_OPENEDX, now, you should run the next command:

```bash
tutor images push openedx
```

# Other Options

## How to add custom middlewares
You should set the variable **DISTRO_EXTRA_MIDDLEWARES** in your config.yml to add a new
middleware to **settings.MIDDLEWARE**

```yaml
DISTRO_EXTRA_MIDDLEWARES:
- middleware.test.1
- middleware.test.2
```

# License
This software is licensed under the terms of the AGPLv3.