import click

from tutordistro.distro.syntax_validator.infrastructure.structure_validator import validate_extra_files_requirements, validate_extra_pip_requirements, validate_extra_settings, validate_packages, validate_theme_settings, validate_themes


class ConfigRepository:
    def validate_config(self, config_file):
        try:
            config = config_file.file_path

            validate_packages(config)
            validate_extra_pip_requirements(config)
            validate_themes(config)
            validate_theme_settings(config)
            validate_extra_files_requirements(config)
            validate_extra_settings(config)

            return True
        except Exception as error:
            click.echo(error)
            return False
