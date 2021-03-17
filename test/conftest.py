import os
import torch

torch.manual_seed(int(os.environ.get('SPLINE_MANUAL_SEED', 7)))
