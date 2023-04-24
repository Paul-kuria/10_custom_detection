import argparse

def parse_video():
    parser = argparse.ArgumentParser(
        description="Inputs the selected video source for object detection"
    )
    parser.add_argument(
        "video",
        type=str,
        help="Enter your video source."
        "formats: .mp4, .ffmpeg",
    )
    args = parser.parse_args()
    return args.video