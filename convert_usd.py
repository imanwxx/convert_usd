#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pxr import Usd

input_file = "cw2.usd"  # 替换为您的 USD 文件路径
output_file = "cw2.usda"
    
stage = Usd.Stage.Open(input_file)
stage.Export(output_file)
print(f"已转换: {input_file} to {output_file}")
