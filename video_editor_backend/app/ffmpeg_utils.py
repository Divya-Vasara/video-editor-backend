import subprocess

def trim_video(input_path, output_path, start_time, end_time):
    command = [
        "ffmpeg", "-i", input_path,
        "-ss", str(start_time), "-to", str(end_time),
        "-c:v", "libx264", "-c:a", "aac", output_path
    ]
    subprocess.run(command, check=True)

def overlay_subtitles(input_path, output_path, text, start_time, end_time):
    drawtext_filter = (
        f"drawtext=text='{text}':fontcolor=white:fontsize=24:"
        f"x=(w-text_w)/2:y=h-40:enable='between(t,{start_time},{end_time})'"
    )
    command = [
        "ffmpeg", "-i", input_path, "-vf", drawtext_filter,
        "-codec:a", "copy", output_path
    ]
    subprocess.run(command, check=True)

def merge_video_parts(input_path, trimmed_path, subtitle_path, output_path):
    # For now assume the subtitle_path is same as trimmed_path
    command = [
        "ffmpeg", "-i", subtitle_path, "-c:v", "libx264", "-c:a", "aac", output_path
    ]
    subprocess.run(command, check=True)
