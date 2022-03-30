edunext-distro plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

Installation
------------

::

    pip install git+https://github.com/eduNEXT/tutor-contrib-edunext-distro

Usage
-----

::

    tutor plugins enable edunext-distro

How to add packages
-----

The most important thing you have to declare into `defaults` dict is the upper case package name and set it to True, this is for enable and disable from terminal like:

::
```bash
tutor distro --set EOX_CORE=False
```

Before this you must to set a key with the upper case package name followed by `_DPKG` for example `"EOX_CORE_DPKG"`, the value of that key is a dictionary with the following data:

- name **# Package name**
- index **# Where download it (choices are pip or git)**
- repository **# This is optional only if you use a git repo**
- version **#This is optional only if you use a git repo**
- variables **# The variables key is the part of custom development which you need to setup a `development` or a `production` environment with whatever dava you may need**
  - development **# A dictionary: Dict[str, str] with all the settings you can need to start a deleopment environment**
  - production **# A dictionary: Dict[str, str] with all the settings you can need to start a production environment**

## Example

::
```python
"defaults": {
    # Another default section settings
    "EOX_CORE": True,
    "EOX_CORE_DPKG": {
        "name": "eox-core",
        "index": "git",
        "repository": "https://github.com/eduNEXT/eox-core.git",
        "version": "v6.0.1",
        "variables": {
            "development": {
                # Development custom settings
                "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper.backends.users_m_v1",
            },
            "production": {
                # Production custom settings
                "EOX_CORE_USERS_BACKEND": "eox_core.edxapp_wrapper.backends.users_m_v1",
            },
        },
    }
}
```
License
-------

This software is licensed under the terms of the AGPLv3.