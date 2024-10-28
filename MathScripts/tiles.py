# tiles formula will be length *width
one_tile = (1*1)
box_of_tiles_area = (one_tile * 12)
area_of_bathroom = 60
total_boxes_needed = (area_of_bathroom / box_of_tiles_area) 

print(f'You will need {total_boxes_needed} boxes of tiles to fill the dimensions of the bathroom')

# For 10% extra, caclulate 10% and add it to total boxes
import math
additional_tiles = 60 * .1
total_area_needed = additional_tiles + area_of_bathroom
final_total_boxes_needed = round(total_area_needed / box_of_tiles_area)
print(f'You will need {final_total_boxes_needed} total boxes to have additional tiles in case of breakage')