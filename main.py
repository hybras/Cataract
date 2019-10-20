#!/usr/bin/python3

"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2

# from networktables import NetworkTables
from cataract import CataractPipeline


def extra_processing(pipeline):
    """
	Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
	:param pipeline: the pipeline that just processed an image
	:return: None
	"""
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []



    for keypoint in pipeline.find_blobs_output:
        print(keypoint.pt)



def main():

    print("Creating video capture")
    cap = cv2.VideoCapture(0)

    print("Creating pipeline")
    pipeline = CataractPipeline()

    print("Running pipeline")
    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            extra_processing(pipeline)

    print("Capture closed")


if __name__ == "__main__":
    main()
