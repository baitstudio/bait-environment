import pyblish.api


class BaitEnvironmentMayaValidateImageFormat(pyblish.api.InstancePlugin):

    order = pyblish.api.ValidatorOrder
    label = "Image Format"
    families = ["renderlayer"]
    optional = True
    hosts = ["maya"]

    def process(self, instance):

        ext = instance.data["collection"].format("{tail}")
        valid_extensions = [".exr", ".png", ".jpg"]

        msg = "Output \"{0}\" image format is not valid.".format(ext)
        msg += " Select from {0}.".format(valid_extensions)
        assert ext in valid_extensions, msg
