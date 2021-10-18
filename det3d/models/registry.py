from det3d.utils import Registry

READERS = Registry("reader")
BACKBONES = Registry("backbone")
ENCODERS = Registry("encoder2d")
DECODERS = Registry("decoder2d")
CFE = Registry("cfe")
NECKS = Registry("neck")
HEADS = Registry("head")
LOSSES = Registry("loss")
DETECTORS = Registry("detector")
SECOND_STAGE = Registry("second_stage")
ROI_HEAD = Registry("roi_head")
FUSION = Registry("fusion_layer")