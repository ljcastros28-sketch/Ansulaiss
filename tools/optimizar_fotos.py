"""
Optimiza fotos para el sitio web de Ansulais (convierte a WebP y genera miniaturas).

Requisito: Python 3 + Pillow  ->  pip install pillow

USO

  1) Una carpeta de catálogo completa (cada subcarpeta = una pieza):

       python tools/optimizar_fotos.py material/fotos-catalogo/alcobas_fondoblanco web/assets/catalogo/alcobas

     Por cada foto (jpg, jpeg, jpe, png, webp) genera, respetando las subcarpetas:
       <nombre>.webp     -> tamaño completo (lado mayor máx. 1024 px), se usa en el lightbox
       <nombre>-sm.webp  -> miniatura (lado mayor máx. 600 px), se usa en tarjetas,
                            carrusel del home y buscador

  2) Una foto suelta (hero, portadas de categoría, etc.), sin miniatura:

       python tools/optimizar_fotos.py material/fotos-secciones/hero/imagen_hero.png web/assets --max 1600 --sin-miniatura

     -> web/assets/imagen_hero.webp

Los archivos originales NUNCA se modifican ni se borran. Si el origen y el destino
son la misma carpeta, los .webp quedan junto a los originales y tú decides si borrarlos.
"""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageOps

EXTENSIONES = {".jpg", ".jpeg", ".jpe", ".png", ".webp"}

MAX_COMPLETA = 1024   # px, lado mayor de la foto del lightbox
MAX_MINIATURA = 600   # px, lado mayor de la miniatura de tarjeta
CALIDAD_COMPLETA = 80
CALIDAD_MINIATURA = 75


def guardar_webp(img, destino, lado_max, calidad):
    copia = img.copy()
    copia.thumbnail((lado_max, lado_max), Image.LANCZOS)  # solo reduce, nunca agranda
    destino.parent.mkdir(parents=True, exist_ok=True)
    copia.save(destino, "WEBP", quality=calidad, method=6)
    return destino.stat().st_size


def procesar(origen, destino, lado_max, con_miniatura):
    with Image.open(origen) as img:
        img = ImageOps.exif_transpose(img)  # respeta la rotación de fotos de celular
        img = img.convert("RGB")
        peso = guardar_webp(img, destino.with_suffix(".webp"), lado_max, CALIDAD_COMPLETA)
        if con_miniatura:
            mini = destino.with_name(destino.stem + "-sm.webp")
            peso += guardar_webp(img, mini, MAX_MINIATURA, CALIDAD_MINIATURA)
    return peso


def main():
    parser = argparse.ArgumentParser(description="Convierte fotos a WebP optimizado para el sitio.")
    parser.add_argument("origen", type=Path, help="carpeta (o foto suelta) de origen")
    parser.add_argument("destino", type=Path, help="carpeta de destino dentro de web/assets/")
    parser.add_argument("--max", type=int, default=MAX_COMPLETA, help="lado mayor de la foto completa en px")
    parser.add_argument("--sin-miniatura", action="store_true", help="no generar la versión -sm")
    args = parser.parse_args()

    if args.origen.is_file():
        fotos = [args.origen]
        base = args.origen.parent
    else:
        fotos = sorted(
            p for p in args.origen.rglob("*")
            if p.suffix.lower() in EXTENSIONES and not p.stem.endswith("-sm")
        )
        base = args.origen

    if not fotos:
        sys.exit("No se encontraron fotos en " + str(args.origen))

    antes = despues = 0
    for foto in fotos:
        destino = args.destino / foto.relative_to(base)
        antes += foto.stat().st_size
        despues += procesar(foto, destino, args.max, not args.sin_miniatura)
        print("ok ", destino.with_suffix(".webp"))

    print("\n%d fotos | %.1f MB -> %.1f MB" % (len(fotos), antes / 1e6, despues / 1e6))


if __name__ == "__main__":
    main()
