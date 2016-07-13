#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random
from jinja2 import Environment, FileSystemLoader

# 引数：x,y,z軸方向それぞれ置く数，xyzの始点，xyzのシフトする量
def create_group(x_num, y_num, z_num, x_start, y_start, z_start, x_scale, y_scale, z_scale):
  chip_star_list = []
  for x in range(x_num):
    for y in range(y_num):
      for z in range(z_num):
        temp_x = x_start+x_scale*x
        temp_y = y_start+y_scale*y
        temp_z = z_start+z_scale*z
        temp_yaw = random.uniform(0, 2*math.pi)
        ob_name = "chip_star_" + str(temp_x) + "_" + str(temp_y) + "_" + str(temp_z)
        chip_star_list.append({'name': ob_name, 'x': str(temp_x), 'y': str(temp_y), 'z': str(temp_z), 'yaw': str(temp_yaw)})
  return chip_star_list

# テンプレートファイルを指定
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('template.world')

# 棚に収納
chip_star_list = create_group(5, 5, 2, 0.06, -0.34, 0.40, 0.07, 0.07, 0.14)

chip_star_list.extend(create_group(5, 5, 2, -0.34, -0.34, 0.40, 0.07, 0.07, 0.14))

# テンプレートへの挿入
world_file = tpl.render({'chip_star_list':chip_star_list})

# ファイルへの書き込み
tmpfile = open("chip_star.world", 'w') #書き込みモードで開く
tmpfile.write(world_file.encode('utf-8'))
tmpfile.close()
