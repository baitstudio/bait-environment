import os

from conda_git_deployment import utils


root_dir = os.path.dirname(__file__)
conda_dir = os.environ["CONDA_GIT_REPOSITORY"]

environment = {}

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(conda_dir, "ftrack-template"),
    os.path.join(conda_dir, "ftrack-locations"),
    os.path.join(conda_dir, "pyblish-maya", "pyblish_maya", "pythonpath"),
    os.path.join(
        conda_dir,
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "pythonpath"
    ),
    os.path.join(conda_dir, "pyblish-hiero"),
    os.path.join(conda_dir, "maya-capture"),
    os.path.join(root_dir, "environment", "PYTHONPATH"),
]

# HIERO_PLUGIN_PATH
environment["HIERO_PLUGIN_PATH"] = [
    os.path.join(
        conda_dir,
        "pyblish-hiero",
        "pyblish_hiero",
        "hiero_plugin_path",
    ),
    os.path.join(
        conda_dir,
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "hiero_plugin_path"
    ),
]

# Add in maya plugins and shelf preferences
environment["MAYA_SCRIPT_PATH"] = [
    os.path.join(root_dir, "environment", "MAYA_SCRIPT_PATH")
]

environment["MAYA_SHELF_PATH"] = [
    os.path.join(root_dir, "environment", "MAYA_SHELF_PATH")
]

environment["XBMLANGPATH"] = [
    os.path.join(root_dir, "environment", "XBMLANGPATH")
]

# NUKE_PATH
environment["NUKE_PATH"] = [
    os.path.join(
        conda_dir,
        "pyblish-nuke",
        "pyblish_nuke",
        "nuke_path"
    ),
    os.path.join(
        conda_dir,
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "nuke_path"
    ),
]

# FTRACK_TEMPLATES_PATH
environment["FTRACK_TEMPLATES_PATH"] = [
    os.path.join(root_dir, "environment", "FTRACK_TEMPLATES_PATH")
]

# FTRACK_LOCATION_PLUGIN_PATH
environment["FTRACK_LOCATION_PLUGIN_PATH"] = [
    os.path.join(root_dir, "environment", "FTRACK_LOCATION_PLUGIN_PATH"),
]

# FTRACK_LOCATIONS_MODULE
environment["FTRACK_LOCATIONS_MODULE"] = ["ftrack_template_disk"]

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(conda_dir, "ftrack-hooks", "djv_plugin"),
    os.path.join(conda_dir, "ftrack-hooks", "pending_changes"),
    os.path.join(conda_dir, "ftrack-hooks", "status_assign"),
    os.path.join(conda_dir, "ftrack-hooks", "pipeline_plugins"),
    os.path.join(root_dir, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
]

utils.write_environment(environment)
