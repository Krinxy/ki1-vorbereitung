# You do not need to modify this file!
# Diese Datei muss nicht geändert werden!

from prog_given import read_image_in_color_and_bw
from prog_own import edge_detection, blue_edges, save_final_image


colorimage, grayimage = read_image_in_color_and_bw()

try:
    print("Detecting horizontal edges ...")
    edges = edge_detection(grayimage)
except Exception as e:
    print("An error occured during edge detection: {}".format(e))
    print("If you want to code edge detection later! " +
          "You can just implement the other functions first.")
    edges = grayimage

print("The result of edge_detection is now stored as the blue color channel")
blue = blue_edges(colorimage, edges)

print("Saving the final result")
save_final_image(blue)
