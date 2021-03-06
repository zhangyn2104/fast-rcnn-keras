IMAGE_SIZE = [480, 576, 688, 864, 1200]
DEFAUTL_IMAGE_SIZE = IMAGE_SIZE[1]
# 图像缩小的倍数
FEAT_STRIDE = 16
POOL_HEIGHT, POOL_WIDTH = (7, 7)
# 每个batch_size 含有128个参与训练的样本
TRAIN_BATCH_SIZE = 128
# 正样本数127 * 0.25
TRAIN_FG_FRACTION = 0.25
# 如果iou > 0.5则为正样本
TRAIN_FG_THRESH = 0.5
TRAIN_BG_THRESH_HI = 0.5
TRAIN_BG_THRESH_LO = 0.1


TRAIN_RPN_BBOX_LAMBDA = 10.0

