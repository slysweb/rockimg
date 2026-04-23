# -*- coding: utf-8 -*-
"""Generate static EN blog header from view/public/header.html — run from repo root."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HEADER_TPL = ROOT / "view" / "public" / "header.html"

# en-us strings for keys used in header.html
LANG = {
    "nav.image_creation": "Image creation",
    "nav.image_editing": "Image editing",
    "nav.image_conversion": "Image conversion",
    "nav.image_color_art": "Image color & art",
    "lang.label": "Language",
    "lang.en-us": "English",
    "lang.de-de": "Deutsch",
    "lang.fr-fr": "Français",
    "lang.ja-jp": "日本語",
    "lang.zh-cn": "中文",
    "lang.ko-kr": "한국어",
    "lang.it-it": "Italiano",
    "lang.es-es": "Español",
    "lang.nl-nl": "Nederlands",
    "tool.gif_meme_maker": "GIF Meme Maker",
    "tool.meme_quotes_creator": "Meme Quotes Creator",
    "tool.note_card": "Note Card",
    "tool.speech_bubble_meme": "Speech Bubble Meme",
    "tool.svg_gradient_generator": "SVG Gradient Generator",
    "tool.add_border": "Add Border",
    "tool.add_captions": "Add Captions",
    "tool.add_text_to_gif": "Add Text to GIF",
    "tool.annotate_image": "Annotate Image",
    "tool.blur_photo": "Blur Photo",
    "tool.circle_image": "Circle Image",
    "tool.combine_gifs": "Combine GIFs",
    "tool.exif_remover": "EXIF Remover",
    "tool.gif_cropper": "GIF Cropper",
    "tool.highlight_image": "Highlight Image",
    "tool.image_authenticity_checker": "Image Authenticity Checker",
    "tool.image_compressor": "Image Compressor",
    "tool.image_file_renamer": "Image File Renamer",
    "tool.image_overlay": "Image Overlay",
    "tool.image_splitter": "Image Splitter",
    "tool.images_combine": "Images Combine",
    "tool.watermark_detector": "Invisible Watermark Checker",
    "tool.merge_two_photos": "Merge Two Photos",
    "tool.mirror_picture": "Mirror Picture",
    "tool.photo_mosaic": "Photo Mosaic",
    "tool.rounded_corners": "Rounded Corners",
    "tool.stop_gif": "Stop GIF",
    "tool.apng_to_gif": "APNG to GIF",
    "tool.avif_converter": "AVIF Converter",
    "tool.bmp_to_jpg": "BMP to JPG",
    "tool.bmp_to_png": "BMP to PNG",
    "tool.eps_to_jpg": "EPS to JPG",
    "tool.eps_to_png": "EPS to PNG",
    "tool.gif_frame_extractor": "GIF Frame Extractor",
    "tool.gif_to_apng": "GIF to APNG",
    "tool.gif_to_mp4": "GIF to MP4",
    "tool.gif_to_webp": "GIF to WebP",
    "tool.heic_converter": "HEIC Converter",
    "tool.heif_to_jpg": "HEIF to JPG",
    "tool.heif_to_png": "HEIF to PNG",
    "tool.jpg_to_bmp": "JPG to BMP",
    "tool.jpg_to_eps": "JPG to EPS",
    "tool.mov_to_gif": "MOV to GIF",
    "tool.mp4_to_gif": "MP4 to GIF",
    "tool.mp4_to_webp": "MP4 to WebP",
    "tool.png_to_bmp": "PNG to BMP",
    "tool.png_to_eps": "PNG to EPS",
    "tool.tiff_converter": "TIFF Converter",
    "tool.video_frame_extractor": "Video Frame Extractor",
    "tool.webp_converter": "WebP Converter",
    "tool.webp_frame_extractor": "WebP Frame Extractor",
    "tool.webp_to_gif": "WebP to GIF",
    "tool.webp_to_mp4": "WebP to MP4",
    "tool.add_noise": "Add Noise",
    "tool.ascii_to_picture": "ASCII to Picture",
    "tool.beauty_filter": "Beauty Filter",
    "tool.black_and_white": "Black and White",
    "tool.color_blind_test": "Color Blind Test",
    "tool.eye_test_chart": "Eye Test Chart",
    "tool.get_image_color": "Get Image Color",
    "tool.glitch_effect": "Glitch Effect",
    "tool.image_filters": "Image Filters",
    "tool.image_to_pixel_art": "Image to Pixel Art",
    "tool.invert_image": "Invert Image",
    "tool.picture_to_ascii": "Picture to ASCII",
    "tool.pictures_to_draw": "Pictures to Draw",
    "tool.vectorize_image": "Vectorize Image",
}


def main():
    text = HEADER_TPL.read_text(encoding="utf-8")
    text = re.sub(r"\s*\{assign name=\"langPrefix\" value=\":lang_prefix\(\)\" /\}\s*\n", "\n", text)
    text = text.replace('href="{$langPrefix==\'\'?\'/\':$langPrefix}"', 'href="/"')
    text = re.sub(r'href="\{\$langPrefix\}/', 'href="/', text)

    def repl_lang(m):
        key = m.group(1)
        if key not in LANG:
            raise KeyError(f"Missing LANG key: {key}")
        return LANG[key]

    text = re.sub(r"\{:lang\('([^']+)'\)\}", repl_lang, text)

    # Static EN blog: English active
    text = re.sub(
        r'<a class="location-option\{eq name="langMenuCurrent" value="en-us"\} is-active\{/eq\}" href="/"\{eq name="langMenuCurrent" value="en-us"\} aria-current="true"\{/eq\}>',
        '<a class="location-option is-active" href="/" aria-current="true">',
        text,
    )
    text = re.sub(
        r'<a class="location-option\{eq name="langMenuCurrent" value="([^"]+)"\} is-active\{/eq\}" href="([^"]+)"\{eq name="langMenuCurrent" value="\1"\} aria-current="true"\{/eq\}>',
        r'<a class="location-option" href="\2">',
        text,
    )

    text = re.sub(
        r'<a class="mobile-menu-item\{eq name="langMenuCurrent" value="en-us"\} is-active\{/eq\}" href="/"\{eq name="langMenuCurrent" value="en-us"\} aria-current="true"\{/eq\}>',
        '<a class="mobile-menu-item is-active" href="/" aria-current="true">',
        text,
    )
    text = re.sub(
        r'<a class="mobile-menu-item\{eq name="langMenuCurrent" value="([^"]+)"\} is-active\{/eq\}" href="([^"]+)"\{eq name="langMenuCurrent" value="\1"\} aria-current="true"\{/eq\}>',
        r'<a class="mobile-menu-item" href="\2">',
        text,
    )

    # Indent for blog pages (inside <div class="container">)
    lines = text.splitlines()
    indented = "\n".join("        " + line if line.strip() else "" for line in lines)
    out = ROOT / "public" / "blog" / "_blog_header_static.html"
    out.write_text(indented.rstrip() + "\n", encoding="utf-8")
    print("Wrote", out, "lines", len(lines))

    blog_dir = ROOT / "public" / "blog"
    # Consume leading whitespace before <header> so we do not double-indent on replace
    pattern = re.compile(r"\s*<header>.*?</header>", re.DOTALL)
    for path in sorted(blog_dir.glob("*.html")):
        if path.name.startswith("_"):
            continue
        body = path.read_text(encoding="utf-8")
        # Leading \n restores newline after <div class="container"> (consumed by \s*)
        new_body, n = pattern.subn("\n" + indented.rstrip() + "\n", body, count=1)
        if n != 1:
            print("SKIP (no header match):", path)
            continue
        path.write_text(new_body, encoding="utf-8")
        print("Patched", path.name)


if __name__ == "__main__":
    main()
