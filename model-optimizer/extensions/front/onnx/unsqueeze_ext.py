"""
 Copyright (c) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import numpy as np

from mo.ops.unsqueeze import Unsqueeze
from mo.front.extractor import FrontExtractorOp
from mo.front.onnx.extractors.utils import onnx_attr


class UnsqueezeFrontExtractor(FrontExtractorOp):
    op = 'Unsqueeze'
    enabled = True

    @staticmethod
    def extract(node):
        axis = np.array(onnx_attr(node, 'axes', 'ints', default=[]), dtype=np.int64)

        attrs = {
            'unsqueeze_dims': axis if len(axis) != 0 else None
        }

        # update the attributes of the node
        Unsqueeze.update_node_stat(node, attrs)
        return __class__.enabled
