"""
PST Visual Gallery -- Golden Protocol execution (Colab-ready, free T4 GPU).

Runs a REPRESENTATIVE SUBSET of portrait style-transfer (PST) methods on a
UNIFIED content portrait and a UNIFIED set of public-domain style references,
then assembles publication-ready gallery grids. This is a *pilot* execution of
the survey's proposed Golden Protocol (Section 6), not an exhaustive 90-method
leaderboard.

Design notes
------------
* Every method is isolated in try/except so a single failure never aborts the
  run; the gallery simply includes however many methods succeeded.
* Asset download has multiple fallbacks; if the unified content portrait fails
  to download, the notebook falls back to Colab `files.upload()` so the author
  can supply a rights-clear portrait.
* Output PNGs are written to ../images so they drop straight into main.tex:
    gallery_overview.png  (Fig.1: paradigm highlight strip)
    gallery_grid.png      (Fig.2: methods x styles matrix)
    gallery_failures.png  (Fig.3: failure modes / identity-style trade-off)

Run:  open PST_Gallery.ipynb on Colab (GPU runtime) and Run all.
"""

import os
import io
import sys
import urllib.request
import traceback
from PIL import Image
import numpy as np
import torch
import torch.nn.functional as F
import torchvision.transforms as T

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "images"))
os.makedirs(OUT, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}

# ---------------------------------------------------------------------------
# Unified assets (Golden Protocol: one content, one style set, for all methods)
# ---------------------------------------------------------------------------
CONTENT_URLS = [
    # public-domain portrait photographs (Wikimedia Commons, PD)
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Grace_Hopper.jpg/480px-Grace_Hopper.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/President_Barack_Obama.jpg/480px-President_Barack_Obama.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Photograph_of_Abraham_Lincoln.jpg/480px-Photograph_of_Abraham_Lincoln.jpg",
]
STYLE_URLS = {
    # public-domain paintings (Wikimedia Commons, PD) -- canonical NST styles
    "StarryNight": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/600px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
    "Scream": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg/600px-Edvard_Munch%2C_1893%2C_The_Scream%2C_oil%2C_tempera_and_pastel_on_cardboard%2C_91_x_73_cm%2C_National_Gallery_of_Norway.jpg",
    "GreatWave": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Great_Wave_off_Kanagawa2.jpg/600px-Great_Wave_off_Kanagawa2.jpg",
    "AmericanGothic": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Grant_Wood_-_American_Gothic_-_Google_Art_Project.jpg/600px-Grant_Wood_-_American_Gothic_-_Google_Art_Project.jpg",
    "WaterLilies": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Claude_Monet_-_Water_Lilies_-_1906%2C_Ryerson.jpg/600px-Claude_Monet_-_Water_Lilies_-_1906%2C_Ryerson.jpg",
    "Cubism": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Pablo_Picasso%2C_1907%2C_Les_Demoiselles_d%27Avignon.jpg/600px-Pablo_Picasso%2C_1907%2C_Les_Demoiselles_d%27Avignon.jpg",
}
SIZE = 512


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def log(*a):
    print("[gallery]", *a, flush=True)


def download(url, path, timeout=90):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
    with open(path, "wb") as f:
        f.write(data)
    return path


def fetch_first(urls, dest_dir, tag):
    os.makedirs(dest_dir, exist_ok=True)
    for i, url in enumerate(urls):
        try:
            p = os.path.join(dest_dir, f"{tag}_{i}.tmp")
            download(url, p)
            return p
        except Exception as e:  # noqa
            log(f"  fetch failed: {url} -> {e}")
    return None


def maybe_upload(tag):
    """Colab file upload fallback (no-op outside Colab)."""
    try:
        from google.colab import files  # type: ignore
        log(f"  falling back to upload for {tag}: choose a JPG/PNG")
        upl = files.upload()
        if upl:
            return os.path.join(OUT, f"{tag}_upload.png")
    except Exception:
        pass
    return None


def load_image(path, size=SIZE):
    img = Image.open(path).convert("RGB")
    return img.resize((size, size), Image.LANCZOS)


def to_tensor(img):
    t = T.Compose([T.ToTensor()])(img)
    return t.unsqueeze(0).to(DEVICE)


def to_img(t):
    t = t.detach().cpu().clamp(0, 1).squeeze(0)
    return T.ToPILImage()(t)


def save(img, name):
    p = os.path.join(OUT, name)
    img.save(p)
    log("saved", p)
    return p


# ---------------------------------------------------------------------------
# Method 1 -- Gatys neural style transfer (optimization-based, no decoder)
# ---------------------------------------------------------------------------
def gatys(content_img, style_img, size=SIZE, steps=250, style_w=1e6, content_w=1.0):
    import torchvision.models as models
    vgg = models.vgg19(pretrained=True).features.to(DEVICE).eval()
    for p in vgg.parameters():
        p.requires_grad_(False)
    content_layers = ["21"]
    style_layers = ["0", "5", "10", "19", "28"]

    def get_feats(x):
        feats = {}
        for name, layer in vgg._modules.items():
            x = layer(x)
            if name in content_layers:
                feats[name] = x
            if name in style_layers:
                feats[name] = x
        return feats

    def gram(f):
        b, c, h, w = f.size()
        f = f.view(b * c, h * w)
        return torch.mm(f, f.t()) / (b * c * h * w)

    c = to_tensor(content_img)
    s = to_tensor(style_img)
    with torch.no_grad():
        c_feats = get_feats(c)
        s_grams = {k: gram(v) for k, v in get_feats(s).items()}
    x = c.clone().requires_grad_(True)
    opt = torch.optim.LBFGS([x])

    def closure():
        opt.zero_grad()
        feats = get_feats(x)
        loss_c = F.mse_loss(feats["21"], c_feats["21"])
        loss_s = sum(F.mse_loss(gram(feats[k]), s_grams[k]) for k in style_layers)
        loss = content_w * loss_c + style_w * loss_s
        loss.backward()
        return loss

    for _ in range(steps):
        opt.step(closure)
    return to_img(x)


# ---------------------------------------------------------------------------
# Method 2 -- AdaIN (feed-forward encoder; needs decoder weights, best-effort)
# ---------------------------------------------------------------------------
def adain(content_img, style_img, size=SIZE, alpha=1.0):
    import torchvision.models as models
    from collections import OrderedDict

    # --- download weights (fail -> raise so caller skips this method) ---
    wdir = os.path.join(OUT, "_weights")
    os.makedirs(wdir, exist_ok=True)
    dec_url = "https://raw.githubusercontent.com/naoto0804/pytorch-AdaIN/master/decoder.pth"
    vgg_url = "https://raw.githubusercontent.com/naoto0804/pytorch-AdaIN/master/vgg_normalised.pth"
    dec_p = os.path.join(wdir, "decoder.pth")
    vgg_p = os.path.join(wdir, "vgg_normalised.pth")
    if not os.path.exists(dec_p):
        download(dec_url, dec_p)
    if not os.path.exists(vgg_p):
        download(vgg_url, vgg_p)

    vgg = models.vgg19(pretrained=False)
    vgg.load_state_dict(torch.load(vgg_p))
    enc = vgg.features[:21].to(DEVICE).eval()
    for p in enc.parameters():
        p.requires_grad_(False)
    dec = torch.load(dec_p, map_location=DEVICE).to(DEVICE).eval()
    for p in dec.parameters():
        p.requires_grad_(False)

    def feat(x):
        return enc(to_tensor(x))

    def adain_feat(cf, sf):
        c_mean = cf.mean(dim=[2, 3], keepdim=True)
        c_std = cf.std(dim=[2, 3], keepdim=True) + 1e-5
        s_mean = sf.mean(dim=[2, 3], keepdim=True)
        s_std = sf.std(dim=[2, 3], keepdim=True) + 1e-5
        t = (cf - c_mean) / c_std * s_std + s_mean
        return alpha * t + (1 - alpha) * cf

    with torch.no_grad():
        cf, sf = feat(content_img), feat(style_img)
        tf = adain_feat(cf, sf)
        out = dec(tf)
    return to_img(out)


# ---------------------------------------------------------------------------
# Method 3 -- IP-Adapter (diffusion-based, best-effort; downloads ~few GB)
# ---------------------------------------------------------------------------
def ip_adapter(content_img, style_img, size=SIZE, steps=30, scale=0.8, seed=0):
    from diffusers import DiffusionPipeline, StableDiffusionImg2ImgPipeline
    from diffusers.utils import make_image_grid
    import ip_adapter  # pip install ip_adapter

    base = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        base, torch_dtype=torch.float16, safety_checker=None
    ).to(DEVICE)
    # attach IP-Adapter
    from ip_adapter import IPAdapter
    image_encoder = pipe.image_encoder if hasattr(pipe, "image_encoder") else None
    # simpler: use IPAdapterPlus/Standard from huggingface h94/IP-Adapter
    from ip_adapter import IPAdapter as _IP
    ip = _IP(pipe, "h94/IP-Adapter", subfolder="models",
             weight_name="ip-adapter_sd15.bin", device=DEVICE)
    gen = torch.Generator(device=DEVICE).manual_seed(seed)
    # use the style image as the IP reference; prompt guides portrait semantics
    out = ip.generate(
        pil_image=style_img,
        prompt="a portrait photo, highly detailed face, preserving identity",
        negative_prompt="deformed, ugly, bad anatomy",
        num_inference_steps=steps,
        guidance_scale=scale,
        ip_adapter_scale=0.7,
        generator=gen,
        num_images_per_prompt=1,
    )
    return out[0].resize((size, size))


# ---------------------------------------------------------------------------
# grid assembly
# ---------------------------------------------------------------------------
def build_grids(content_img, styles, results):
    """results: dict[method_name] -> dict[style_name] -> PIL.Image"""
    methods = list(results.keys())
    style_names = list(styles.keys())
    ncol = len(style_names) + 1  # +1 for content column
    nrow = len(methods) + 1       # +1 for style-reference row

    cell = SIZE
    pad = 6
    W = ncol * (cell + pad) + pad
    H = nrow * (cell + pad) + pad

    def new_canvas():
        return Image.new("RGB", (W, H), (255, 255, 255))

    # Fig.2 -- full matrix
    grid2 = new_canvas()
    # top-left empty, then style references
    for j, sn in enumerate(style_names):
        grid2.paste(styles[sn].resize((cell, cell)),
                    (pad + (j + 1) * (cell + pad), pad))
    # content column + method rows
    for i, m in enumerate(methods):
        y = pad + (i + 1) * (cell + pad)
        grid2.paste(content_img.resize((cell, cell)), (pad, y))
        for j, sn in enumerate(style_names):
            im = results[m].get(sn)
            if im is not None:
                grid2.paste(im.resize((cell, cell)),
                            (pad + (j + 1) * (cell + pad), y))
    save(grid2, "gallery_grid.png")

    # Fig.1 -- paradigm highlight: content + one rep per paradigm on StarryNight
    rep_styles = {m: results[m].get("StarryNight") for m in methods}
    present = [m for m in methods if rep_styles[m] is not None]
    strip = Image.new("RGB", ((len(present) + 1) * (cell + pad) + pad, cell + 2 * pad),
                      (255, 255, 255))
    strip.paste(content_img.resize((cell, cell)), (pad, pad))
    for k, m in enumerate(present):
        strip.paste(rep_styles[m].resize((cell, cell)),
                    (pad + (k + 1) * (cell + pad), pad))
    save(strip, "gallery_overview.png")

    # Fig.3 -- failure modes: Gatys drift vs IP-Adapter control on a hard style
    hard = "Cubism" if "Cubism" in style_names else style_names[-1]
    a = results.get("Gatys", {}).get(hard)
    b = results.get("IP-Adapter", {}).get(hard)
    pair = Image.new("RGB", (2 * (cell + pad) + pad, cell + 2 * pad), (255, 255, 255))
    if a is not None:
        pair.paste(a.resize((cell, cell)), (pad, pad))
    if b is not None:
        pair.paste(b.resize((cell, cell)), (pad + (cell + pad), pad))
    save(pair, "gallery_failures.png")

    log(f"grids built: methods={methods}, styles={style_names}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    log(f"device={DEVICE}")
    adir = os.path.join(OUT, "_assets")
    # unified content
    cpath = fetch_first(CONTENT_URLS, adir, "content") or maybe_upload("content")
    if cpath is None:
        raise RuntimeError("No content portrait available; please upload one.")
    content_img = load_image(cpath)
    save(content_img, "_content.png")

    # unified styles
    styles = {}
    for name, url in STYLE_URLS.items():
        try:
            p = download(url, os.path.join(adir, f"style_{name}.jpg"))
            styles[name] = load_image(p)
        except Exception as e:  # noqa
            log(f"style {name} failed: {e}")
    if not styles:
        raise RuntimeError("No style references downloaded.")
    log(f"loaded {len(styles)} styles: {list(styles)}")

    methods = {
        "Gatys (optimization)": gatys,
        "AdaIN (feed-forward)": adain,
        "IP-Adapter (diffusion)": ip_adapter,
    }
    results = {}
    for mname, mfn in methods.items():
        log(f"running {mname} ...")
        try:
            per = {}
            for sname, simg in styles.items():
                per[sname] = mfn(content_img, simg)
                log(f"  {mname} x {sname} done")
            results[mname] = per
        except Exception as e:  # noqa
            log(f"METHOD {mname} FAILED:\n{traceback.format_exc()}")

    if not results:
        raise RuntimeError("All methods failed; see log above.")
    build_grids(content_img, styles, results)
    log("DONE. PNGs in", OUT)


if __name__ == "__main__":
    main()
