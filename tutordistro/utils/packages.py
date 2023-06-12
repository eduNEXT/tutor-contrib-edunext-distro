def get_distro_packages(settings) -> dict:
    distro_packages = {key: val for key,
                       val in settings.items() if key.endswith("_DPKG") and val != 'None'}
    return distro_packages


def get_public_distro_packages(settings) -> dict:
    distro_packages = get_distro_packages(settings)
    public_packages = {key: val for key,
                        val in distro_packages.items() if not val["private"]}
    return public_packages


def get_private_distro_packages(settings) -> dict:
    distro_packages = get_distro_packages(settings)
    private_packages = {key: val for key,
                        val in distro_packages.items() if val["private"]}
    return private_packages
