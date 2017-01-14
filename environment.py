import os

from conda_git_deployment import utils


root = os.path.dirname(__file__)
environment = {}

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-template"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-locations"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "pythonpath"
    ),
]

# PYBLISHPLUGINPATH
environment["PYBLISHPLUGINPATH"] = [
    os.path.join(root, "environment", "PYBLISHPLUGINPATH", "maya"),
    os.path.join(root, "environment", "PYBLISHPLUGINPATH", "ftrack"),
]

# NUKE_PATH
environment["NUKE_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nuke",
        "pyblish_nuke",
        "nuke_path"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "nuke_path"
    ),
]

# FTRACK_TEMPLATES_PATH
environment["FTRACK_TEMPLATES_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_TEMPLATES_PATH"
    )
]

# FTRACK_LOCATION_PLUGIN_PATH
environment["FTRACK_LOCATION_PLUGIN_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_LOCATION_PLUGIN_PATH"
    ),
]

# FTRACK_LOCATIONS_MODULE
environment["FTRACK_LOCATIONS_MODULE"] = ["ftrack_template_disk"]

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
]

utils.write_environment(environment)