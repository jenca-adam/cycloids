from .circledraw import create_canvas
from cv2 import VideoWriter, VideoWriter_fourcc
import tqdm
import colorsys
from numpy import arange
MP4_FOURCC = VideoWriter_fourcc(*"mp4v")
MAX_COLORS = 1
def changev(col,to):
    h,s,_=colorsys.rgb_to_hsv(*col)
    return colorsys.hsv_to_rgb(h,s,to)
def record(spins, filename, color, size, fps, nframes, speed):
    tratio=1/fps*speed
    ohue,osat,oval = colorsys.rgb_to_hsv(*color)
    hues = [colorsys.hsv_to_rgb(ohue+hdiff,osat,oval-hdiff*50) for hdiff in arange(0,1,1/MAX_COLORS)]
    frm=create_canvas(*size)
    writer = VideoWriter(filename, MP4_FOURCC, fps, size)
    for t in tqdm.tqdm(range(nframes)):
        spin=spins
        h = 0
        while hasattr(spin,"get_dpos"):
            [q.plot(frm,hues[h%len(hues)]) for q in spin.get_dpos((t)*tratio,tratio)]
            spin=spin.parent
            h+=1
            break
        writer.write(frm)

    writer.release()
