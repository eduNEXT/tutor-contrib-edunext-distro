# distro plugin for [Tutor](https://docs.tutor.overhang.io)

## What is distro
Distro is an opinioned openedx distribution with some custom stuff to have an easy-to-use
and a ready to deploy in local or in development openedx distribution.
This can be watch like a tutor-plugin but is taken a little bit far away.

## Installation
`pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro`

## Usage
```bash
tutor plugins enable distro
tutor distro enable-themes
````
# Required tutor settings
This plugin works with some docker images. These are defined by default
if you have different images that aren't based on these, you can have some problems.

```yaml
DOCKER_IMAGE_OPENEDX: "docker.io/ednxops/distro-edunext-edxapp:vM.mango.2.0-plugin"
DOCKER_IMAGE_OPENEDX_DEV: "docker.io/ednxops/distro-edunext-edxapp-dev:vM.mango.2.0-plugin"
```

Also, you need an edx-platform version distro compatible.

| openedx |  distro  |
|---------|----------|
|  lilac  | limonero |
|  maple  |   mango  |

You can find distro releases on https://github.com/edunext/edunext-platform.

```yaml
EDX_PLATFORM_REPOSITORY: "https://github.com/eduNEXT/edunext-platform.git"
EDX_PLATFORM_VERSION: "edunext/mango.master"
```

# Packages

## Default packages
These packages will be installed in a default installation.

- eox-theming (DISTRO_EOX_THEMING_DPKG)
    - eox-tenant (DISTRO_EOX_TENANT_DPKG)
      - eox-core (DISTRO_EOX_CORE_DPKG)

## Disable default packages
It's necessary to know that each eox-package has dependencies, which that means that if you
enable **DISTRO_EOX_THEMING** this will enable **eox-tenant & eox-core** too, so ,
if you want just use eox-core you must desable eox-theming and eox-tenant.

```bash
tutor config save --set DISTRO_EOX_THEMING=false --set DISTRO_EOX_TENAT=false --set DISTRO_EOX_CORE=true
```

## How to add a new package
In your config.yml you can set any package following this structure:

```yaml
DISTSRO_MY_PACKAGE_NAME_DPKG:
  index: git
  name: my-plugin-name
  repository: https://github.com/eduNEXT/my-plugin-name.git
  variables:
    development:
      MY_PLUGIN_DEV_SETTING: "VALUE"
    production:
      MY_PLUGIN_DEV_PROD_SETTING: "VALUE"
  version: my-plugin-branch

# If you want to install a package from pip
# you must set the index to pip and remove repository but this
# won't be installed as editable.
````

Package's variables will be used on cms and lms settings.

In the dev environment your package will be cloned on **/openedx/extra_deps/MY-PLUGIN-NAME**
if you want to edit it you can
[mount a volume](https://docs.tutor.overhang.io/dev.html?highlight=bind#manual-bind-mount-to-any-directory) to that path.

## How to override a default package
You can use the same steps that in **How to add a new package** just set the variable with the same name:

- DISTRO_EOX_CORE_DPKG
- DISTRO_EOX_TENANT_DPKG
- DISTRO_EOX_THEMING_DPKG

# Themes
Declare the path of your themes using `tutor config save --set DISTRO_THEMES_ROOT="your_path"`,
by default the themes path goes here **/openedx/themes**

## Default themes
These themes will be installed in a default installation.

- bragi

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

- **local**: you must to build a new image to add the new themes and
compile statics and run the command `tutor local init && tutor local start` again.
- **dev**: you must run the command `tutor dev init && tutor dev start` again.

# License
This software is licensed under the terms of the AGPLv3.