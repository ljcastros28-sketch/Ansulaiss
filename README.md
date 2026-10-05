# Ansulais — sitio web

Sitio estático de Ansulais (muebles de madera y tapizados, Bogotá). HTML, CSS y JavaScript plano: **no hay build, frameworks ni dependencias**. Para verlo en local basta con abrir cualquier `.html` de `web/` en el navegador.

- En vivo: https://ansulais.com (dominio en Squarespace Domains apuntando a GitHub Pages; el link viejo de github.io redirige solo)
- Despliegue: automático a GitHub Pages en cada push a `main` (`.github/workflows/deploy-pages.yml`). Solo se publica la carpeta `web/`.

## Estructura

```
web/                      ← todo lo que se publica
  index.html              Home (hero, carrusel "¿Qué ofrecemos?", nosotros, materiales, contacto)
  catalogo.html           Selector de categorías
  catalogo-salas.html     Catálogo de salas y sofás   (códigos SAL-xx)
  catalogo-comedores.html Catálogo de comedores       (códigos COM-xx)
  catalogo-alcobas.html   Catálogo de alcobas         (códigos ALC-xx)
  search.html             Buscador: lleva directo a la pieza, al filtro o a la sección (ver ROUTES)
  privacidad.html, cookies.html, terminos.html, reembolsos.html   Páginas legales
  404.html                Página de error (enlaces con "/" inicial, se sirve en cualquier ruta)
  robots.txt, sitemap.xml Para buscadores. Agrega al sitemap cualquier página nueva
  apple-touch-icon.png    Ícono al guardar el sitio en el celular
  assets/
    catalogo/<categoria>/<pieza>/<foto>.webp      foto completa (lightbox)
    catalogo/<categoria>/<pieza>/<foto>-sm.webp   miniatura (tarjetas, carrusel, buscador)
    og-ansulais.jpg       Vista previa al compartir el link (1200×630)
tools/optimizar_fotos.py  Convierte fotos a WebP optimizado (ver abajo)
```

Las demás carpetas de la raíz (`salas_fondoblanco/`, `alcobas_fondoblanco/`, `COMEDORES/`, etc.) son fotos originales de trabajo. **No forman parte del sitio y no se deben subir ni modificar.**

## Cómo está organizado el código

Cada página es independiente: su CSS va en un `<style>` y su JS en un `<script>` dentro del mismo archivo. El header, el footer, el banner de cookies, el buscador del menú y la pantalla de carga están **duplicados a propósito** en todas las páginas, porque sin build no hay includes. Si cambias uno de esos bloques, replica el cambio en todos los `.html`.

Convenciones que se repiten en todas las páginas:
- Colores como variables CSS en `:root` (`--beige-light`, `--maroon-deep`, `--wood`, etc.).
- Tipografía Montserrat desde Google Fonts. Es el único servicio externo del sitio.
- Animación al hacer scroll: clase `.reveal` + `IntersectionObserver`.
- Las media queries van **después** de la regla base del mismo componente. Si quedan antes, la regla base las pisa.

## Agregar una pieza al catálogo

1. Optimiza las fotos (necesitas Python 3 y `pip install pillow`):
   ```
   python tools/optimizar_fotos.py <carpeta_con_fotos_originales> web/assets/catalogo/<categoria>
   ```
   Cada subcarpeta del origen se trata como una pieza. Por cada foto se generan `<nombre>.webp` y `<nombre>-sm.webp`.
2. Agrega la pieza **al final** del array `products` del `catalogo-<categoria>.html` correspondiente. El código de artículo (ALC-01, ALC-02…) sale de la posición en la lista; si insertas en medio, cambias los códigos que los clientes ya conocen. El comentario encima del array explica cada campo.
3. Agrega la misma pieza en `index.html` (array `offerPool`) y en `search.html` (array `catalog`, con la misma `desc` y su `filtro` = el `tag` del catálogo), usando la miniatura `-sm.webp`.

Las piezas están en tres lugares porque el sitio no tiene una base de datos ni un build. Si quitas una pieza, quítala también de los tres.

## Agregar una categoría nueva

Copia uno de los `catalogo-*.html` y cambia el `<title>`, las etiquetas `description`/`canonical`/`og:*` del `<head>`, los botones de filtro, `products`, `tagLabels`, `basePath` y el prefijo de `articleCode`. Después enlázala desde `catalogo.html`, agrégala a `sitemap.xml` y, en `search.html`, agrega su botón de filtro y una entrada en `ROUTES` con sus palabras clave y filtros.

## Rendimiento

- Las fotos de catálogo se sirven en WebP. Las tarjetas cargan la miniatura de 600 px con `srcset`, y la foto completa de 1024 px solo se pide al abrir el lightbox. Las fotos vecinas del lightbox se precargan.
- Todas las imágenes, excepto la del hero, usan `loading="lazy"`. El hero usa `fetchpriority="high"` porque es lo primero que se ve.
- El video de "Nosotros" (`preload="none"`) solo se descarga y reproduce cuando su sección se acerca a la pantalla.
- Cualquier foto nueva debe pasar por `tools/optimizar_fotos.py`. No subas JPG/PNG originales: pesan entre 10 y 30 veces más.

## Datos de la empresa

Dirección, correo, WhatsApp, horarios y redes están en `CLAUDE.md`. Usa siempre esos datos y no inventes otros.
