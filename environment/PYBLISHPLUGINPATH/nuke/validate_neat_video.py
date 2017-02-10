import pyblish.api
import nuke


class BaitEnvironmentNukeValidateNeatVideo(pyblish.api.ContextPlugin):
    """ Fails publish if Neat Video node is present in scene. """

    order = pyblish.api.ValidatorOrder
    families = ["deadline"]
    label = "Neat Video"
    optional = True

    def process(self, context):

        for node in nuke.allNodes():
            if node.Class().lower().startswith("ofxcom.absoft.neatvideo"):
                msg = "Neat Video is in file: \"{0}\"".format(node.name())
                raise ValueError(msg)
