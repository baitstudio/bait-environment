import os

import pyblish.api
import nuke


class BaitEnvironmentRepairWriteSettings(pyblish.api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def process(self, context, plugin):

        # Get the errored instances
        failed = []
        for result in context.data["results"]:
            if (result["error"] is not None and
               result["instance"] is not None and
               result["instance"] not in failed):
                failed.append(result["instance"])

        # Apply pyblish.logic to get the instances for the plug-in
        instances = pyblish.api.instances_by_plugin(failed, plugin)

        for instance in instances:

            # repairing alpha output
            valid_outputs = ["rgb", "rgba", "all"]
            if instance[0]["channels"].value() not in valid_outputs:
                instance[0]["channels"].setValue("all")

            # repairing proxy mode
            nuke.root()["proxy"].setValue(False)


class BaitEnvironmentValidateWriteSettings(pyblish.api.InstancePlugin):
    """ Validates the write settings. """

    order = pyblish.api.ValidatorOrder
    families = ["write"]
    label = "Write Settings"
    optional = True
    actions = [BaitEnvironmentRepairWriteSettings]

    def process(self, instance):

        # validate extension
        split = os.path.splitext(instance[0]["file"].getValue())
        msg = "Output extension needs to be \".exr\", \".png\", \".dpx\""
        msg += " or \".mov\", currently \"%s\"" % split[1]
        assert split[1] in [".exr", ".png", ".dpx", ".mov"], msg

        # validate alpha
        msg = "Output channels are wrong."
        valid_outputs = ["rgb", "rgba", "all"]
        assert instance[0]["channels"].value() in valid_outputs, msg

        # validate proxy mode
        msg = "Can't publish with proxy mode enabled."
        assert not nuke.root()["proxy"].value(), msg
