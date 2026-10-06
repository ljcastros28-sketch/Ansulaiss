# Ansulais — Contexto del proyecto

Sitio web estático de **Ansulais** (fabricante de muebles de madera y tapizados, Bogotá, Colombia). HTML/CSS/JS plano, **sin build ni frameworks**. Se despliega automático a GitHub Pages vía GitHub Actions al hacer push a `main`.

- Repo: https://github.com/ljcastros28-sketch/Ansulaiss.git
- Sitio en vivo: **https://ansulais.com** (conectado el 2026-10-05; el link viejo https://ljcastros28-sketch.github.io/Ansulaiss/ redirige solo)
- Dominio `ansulais.com`: comprado en Google Domains, hoy administrado en **Squarespace Domains** (solo registro + DNS). El sitio NO se aloja en Squarespace: sigue en GitHub Pages. El dominio se configura en GitHub → Settings → Pages → Custom domain (con deploy por Actions, un archivo `CNAME` se ignora, no hace falta). DNS en Squarespace: 4 registros A `@` → 185.199.108.153 / 109.153 / 110.153 / 111.153 y CNAME `www` → `ljcastros28-sketch.github.io`. **En ese DNS también hay registros de correo que no se deben tocar**: Google Workspace (MX `smtp.google.com`, TXT `v=spf1…`, TXT `google._domainkey`) y Brevo (CNAME `brevo1/2._domainkey`, `mail`, `img.mail`, `r.mail`; TXT `brevo-code`, `_dmarc`) y el TXT `@` `google-site-verification=…` que verifica el dominio en Google Search Console (si se borra, se pierde la verificación).
- Carpeta publicada: **`web/`** — todo lo que se ve en el sitio vive ahí.

## Regla de oro: qué se sube a git

**Solo se commitea/pushea lo que está dentro de `web/`** (más la documentación y herramientas del repo: `CLAUDE.md`, `README.md`, `tools/`, `.github/`). El resto de carpetas y archivos en la raíz del repo (`SALAS Y SOFÁS/`, `COMEDORES/`, `salas_fondoblanco/`, `comedores_fondoblanco/`, `alcobas_fondoblanco/`, `otros_fondoblanco/`, `quequiereshoy/`, `nosotros/`, fotos/videos sueltos en la raíz como `sofa123.jpe`, `imagen_hero*.png`, etc.) son **material de trabajo en progreso del usuario** — fotos originales sin procesar para catálogos futuros u otras secciones. **Nunca los toques, muevas, borres ni los incluyas en un commit** a menos que el usuario lo pida explícitamente. Cuando se necesita una foto de ahí para el sitio, se procesa con `python tools/optimizar_fotos.py <origen> web/assets/...` (genera `.webp` + miniatura `-sm.webp`) y solo esa salida entra a git.

Workflow típico de cada cambio:
1. Editar archivo(s) dentro de `web/`.
2. Abrir con `start "" "web/archivo.html"` (o el que corresponda) para revisar antes de subir.
3. `git add web/<archivos tocados>` — nunca `git add -A` ni `git add .` (para no arrastrar material WIP del usuario sin querer).
4. Commit + `git push` (el usuario normalmente pide que se suba directo, no hace falta preguntar cada vez salvo que algo se vea raro).

## Páginas del sitio (todas dentro de `web/`)

| Archivo | Qué es |
|---|---|
| `index.html` | Home: hero (foto `sofa123.jpg`/`sofa123_9-16.jpg` de fondo), franja de datos animada (marquee de vidrio sobre el hero), "¿Qué ofrecemos?" (carrusel horizontal con flechas en desktop / swipe en móvil), Nosotros, materiales (madera + espuma Espumados), Contacto |
| `catalogo.html` | Selector de categorías ("¿Qué buscas el día de hoy?") → enlaza a los tres catálogos reales (comedores, salas, alcobas); "otros" sigue "próximamente" |
| `catalogo-salas.html` | Catálogo de salas/sofás — 35 piezas, con filtros y lightbox |
| `catalogo-comedores.html` | Catálogo de comedores — 24 piezas, con filtros y lightbox |
| `catalogo-alcobas.html` | Catálogo de alcobas/camas — 13 piezas (códigos `ALC-xx`), filtros: Cabecero extendido / Clásicas / Nido y cajones, con lightbox. Faltan fotos de más piezas: se irán agregando |
| `search.html` | Buscador "directo": en vez de listar opciones, lleva a la pieza (por nombre o código `SAL-05`), al catálogo con el filtro puesto ("sofá cama", "comedor redondo", "cama nido") o a la sección ("horario" → contacto, "garantía" → reembolsos). Solo lista resultados cuando de verdad hay varias piezas posibles ("botones", "comedor 6 puestos"). Palabras clave en el array `ROUTES` |
| `privacidad.html` | Política de tratamiento de datos (Ley 1581 de 2012, Colombia) |
| `cookies.html` | Política de cookies (el sitio NO usa analítica/tracking, solo Google Fonts + una preferencia local de "ya viste el aviso") |
| `terminos.html` | Términos y condiciones (venta sobre pedido, Ley 1480 de 2011) |
| `404.html` | Página de error de GitHub Pages. Sus enlaces empiezan con `/` porque se sirve en cualquier ruta |
| `reembolsos.html` | Garantía, cambios y devoluciones (explica por qué no aplica derecho de retracto estándar al ser piezas personalizadas, pero sí la garantía legal) |

Cada página es **standalone**: CSS y JS están inline en su propio `<style>`/`<script>`, **duplicados entre páginas a propósito** (no hay build ni archivos compartidos/includes). Si cambias algo que debe verse igual en todas (header, footer, cookie banner, nav-search, page-loader), **hay que replicar el cambio a mano en cada archivo HTML**.

Archivos de soporte en `web/`: `robots.txt`, `sitemap.xml` (agregar ahí cualquier página nueva), `apple-touch-icon.png` (ícono para celulares), `assets/og-ansulais.jpg` (imagen 1200×630 de vista previa al compartir el link; es el único `.jpg` permitido, porque WhatsApp/Facebook no siempre leen WebP).

**Cada página nueva** debe llevar en el `<head>` el mismo bloque que las demás: `description`, `canonical` (`https://ansulais.com/<archivo>`), `theme-color`, `apple-touch-icon` y las etiquetas `og:*` / `twitter:card`. `index.html` además tiene los datos del negocio en JSON-LD (`FurnitureStore`): si cambia dirección, horario, teléfono o redes, actualizarlo ahí también.

## Datos de la empresa (usar siempre estos, no inventar)

- Dirección: Crr 51 # 76-32, Bogotá D.C.
- Correo: ansulais31@gmail.com
- Teléfono / WhatsApp: +57 300 492 8400
- Razón social: **ANSULAIS S.A.S.** — NIT: 900963049-7 (aparece en el footer de las 10 páginas, en `privacidad.html`, `terminos.html` y en el JSON-LD de `index.html`)
- Dominio: ansulais.com (alojado en GitHub Pages, dominio registrado en Squarespace Domains; así está declarado en `privacidad.html` sección 5 y `cookies.html` sección 3)
- WhatsApp float / CTA: `https://wa.me/message/ISVNRLUQCE27G1`
- Número usado en el link del lightbox de catálogo: `WHATSAPP_NUMBER = "573004928400"` → `https://wa.me/573004928400?text=...`
- Horario: Lunes a sábado 11:00 a.m.–6:00 p.m., domingos 11:00 a.m.–3:00 p.m.
- Facebook: `https://www.facebook.com/share/19EzTXUeZg/?mibextid=wwXIfr`
- Instagram: `https://www.instagram.com/ansulais?igsi=dTBqdHJocHM2dnRr&utm_source=qr`
- TikTok: `https://www.tiktok.com/@ansulais?_r=1&_t=ZS-996OWQ08Us6`
- Madera principal: **flor morado**. Espuma: certificada por **Espumados** (sello CertiPUR-US; filial Espumados del Litoral con ISO 9001/14001/45001).
- **Todo se fabrica sobre pedido**: macizo, entamborado o combinado, tapizado, telas y medidas a elección del cliente. No prometer specs ni medidas fijas en ningún copy nuevo.

## Paleta / convenciones de diseño (repetidas en cada página)

```css
--beige: #f8f2de; --beige-tint: #fdfbf3; --beige-light: #fdf8ec;
--maroon: #1a1a1a; --maroon-deep: #0f0f0f; --maroon-hover: #2b2b2b;
--wood: #8a5a35; --ink: #241a12;
```
- Fondo oscuro (`--maroon-deep`) alterna con secciones beige (`--beige-light`) para dar ritmo visual entre secciones.
- Tipografía: Montserrat vía Google Fonts (único servicio externo cargado en el sitio).
- Animación de aparición al hacer scroll: clase `.reveal` + `IntersectionObserver`, repetido en cada página.
- Logo: SVG inline (el glyph "A" estilizado), no son imágenes — se repite el mismo `<path>` en header/footer de cada página.

## Catálogo: dónde vive la data

Los productos (nombre inventado + descripción + tag + carpeta de fotos) están **hardcodeados como arrays JS**, duplicados en:
- `catalogo-salas.html` (35 piezas, con `desc` completo para el lightbox)
- `catalogo-comedores.html` (24 piezas, con `desc` completo para el lightbox)
- `catalogo-alcobas.html` (13 piezas, con `desc` completo para el lightbox)
- `index.html` → array `offerPool` (las mismas 72 piezas combinadas, solo nombre/href/img, para el carrusel "¿Qué ofrecemos?")
- `search.html` → array `catalog` (las mismas 72, con `cat`, `filtro` = `tag` del catálogo y `desc` copiada del catálogo, porque el buscador también busca en la descripción)

**Si se agrega o quita una pieza del catálogo, hay que actualizar los 3 lugares donde está duplicada la lista** (no hay una sola fuente de verdad, es intencional por ser sitio estático sin build).

Fotos de catálogo en: `web/assets/catalogo/{salas,comedores,alcobas}/<carpeta>/<foto>.webp` (1024 px, lightbox) y `<foto>-sm.webp` (600 px, tarjetas/carrusel/buscador). Se generan con `tools/optimizar_fotos.py`, que **graba la "A" del logo, sutil, en el centro** de cada foto (forma en `tools/marca_agua.png`; tamaño y opacidad en las constantes `MARCA_*` del script). Las fotos de producto SIEMPRE deben pasar por ahí con marca; solo fotos decorativas (hero, portadas) usan `--sin-marca`. Los originales sin marca son los `.jpg` locales junto a cada `.webp` (ignorados por git): no borrarlos, son la fuente para regenerar. **Nunca referenciar `.jpg` en el código**: los `.jpg` que puedan quedar en `web/assets/` son restos viejos sin uso. En `index.html` (`offerPool`) y `search.html` (`catalog`) se usa siempre la versión `-sm.webp`. Las piezas nuevas van **al final** del array `products`, porque el código de artículo sale de la posición.

## Cosas ya implementadas (no reinventar)

- Page loader (logo + 3 puntos) en las 10 páginas — se oculta solo al cargar o a los 4s.
- Banner de cookies (aceptar/rechazar) con `localStorage` key `ansulais_cookie_choice`, en las 10 páginas.
- Nav-search: en móvil el input estaba `display:none` — se arregló para que se expanda al tocar el ícono (clase `.is-open` en `#navSearchForm`).
- Skip-link de accesibilidad ("Saltar al contenido") en las 10 páginas.
- Footer con links legales (Términos, Privacidad, Cookies, Cambios y devoluciones) en las 10 páginas.
- Enlaces directos en los 3 catálogos: `?filtro=<data-filter>` activa el filtro y `?pieza=<código o nombre-en-slug>` abre la pieza en el lightbox (ej. `catalogo-salas.html?pieza=SAL-05` o `?pieza=sofa-cedro`). Los usa el buscador y sirven para compartir una pieza por WhatsApp.

## Lecciones aprendidas (para no repetir bugs ya resueltos)

1. **Orden del CSS en cascada**: si una regla de media query (`@media (min-width:901px) { .algo {...} }`) está definida ANTES que una regla base sin condición para el mismo selector `.algo`, la regla base gana en el breakpoint grande también (ambas aplican; gana la que está más abajo en el archivo). **Los overrides de breakpoint deben ir SIEMPRE después de la regla base del mismo componente** en el `<style>`.
2. **`overflow-x: auto` sin `overflow-y` explícito**: el navegador computa `overflow-y` como `auto` también, lo que puede atrapar el scroll vertical/táctil dentro de un carrusel horizontal. Usar `overflow-y: hidden` + `touch-action: pan-x` para scroll horizontal puro.
3. **`aspect-ratio` + `max-height` en el mismo elemento**: compiten entre sí y fuerzan recortes raros con `object-fit: cover`. Usar solo uno de los dos.
4. **`box-shadow` cortado por `overflow: hidden`** del contenedor que oculta el scroll horizontal de un carrusel: si no hay suficiente padding vertical, se corta la sombra de las tarjetas. Más robusto: quitar el `overflow:hidden` de ese contenedor puntual y dejar que lo maneje un ancestro más grande (ej. `.hero` completo) que no necesita recortar verticalmente.
5. Antes de dar por "arreglado" un cambio visual reportado por el usuario, recordar que puede ser **caché del navegador/GitHub Pages** mostrando la versión anterior — pedir refresh forzado si el código ya se ve correcto en el archivo.

## Historial de cambios

*(agregar una línea nueva aquí cada vez que se haga un cambio relevante, con fecha)*

- **2026-10-05** — Creación de este archivo de contexto.
- **2026-10-05** — Buscador funcional (`search.html`) + páginas legales (`privacidad.html`, `cookies.html`, `terminos.html`, `reembolsos.html`) + page loader + cookie banner + skip-links en las 9 páginas + limpieza de 15 assets sin usar + fix de redes sociales/correo en footer de `catalogo.html`.
- **2026-10-05** — Correo de contacto cambiado a `ansulais31@gmail.com` en las 9 páginas (reemplaza `ansulais@ansulais.com`); se agregó el link de correo que le faltaba al footer de `catalogo-salas.html`; se agregó sección 6 en `reembolsos.html` sobre elementos decorativos/deslizantes de cortesía (sin garantía, no se reponen, no admiten reclamo, por ser obsequio).
- **2026-10-05** — Nueva sección de alcobas: `catalogo-alcobas.html` con 13 piezas (fotos de `alcobas_fondoblanco/` copiadas a `web/assets/catalogo/alcobas/`); tarjeta de alcobas en `catalogo.html` ya enlaza (sin "próximamente"); piezas agregadas a `offerPool` (index) y a `catalog` + filtro "Alcobas" (search).
- **2026-10-05** — Optimización de carga: todas las fotos del sitio pasan a WebP (catálogo: de ~110 MB a ~9.5 MB, con miniaturas `-sm.webp` para tarjetas y `srcset`); el hero usa `fetchpriority="high"`; el video de Nosotros pasa a `preload="none"` y se reproduce/pausa con `IntersectionObserver`; el lightbox precarga la foto anterior y la siguiente. Nuevo `tools/optimizar_fotos.py`, `README.md` para ingenieros y comentarios que documentan el array `products` en cada catálogo.
- **2026-10-05** — Buscador reescrito para ir directo al destino: código de artículo / nombre de pieza → abre la pieza; tipo de mueble → catálogo con filtro; palabras como horario, garantía, madera → la sección correspondiente. Tolera tildes, plurales y errores de tipeo. Los 3 catálogos aceptan `?filtro=` y `?pieza=`. `search.html` (`catalog`) ahora incluye `desc` y `filtro`.
- **2026-10-05** — Preparación para el dominio `ansulais.com`: etiquetas SEO y de vista previa al compartir (descripción, canonical, Open Graph) en las 10 páginas, JSON-LD del negocio en index, `robots.txt`, `sitemap.xml`, `404.html`, ícono para celulares y favicon con modo oscuro. Políticas: dominio ansulais.com, proveedores (GitHub Pages, Squarespace Domains, Google Fonts) y transferencia internacional; se corrigieron los plazos de la Ley 1581 (consultas 10 días hábiles, reclamos 15) que estaban invertidos. Se sacaron de git 189 `.jpg` sin uso (86 MB) vía `.gitignore`; siguen en el disco.
- **2026-10-05** — NIT 900963049-7 agregado al footer de las 10 páginas, a Privacidad (responsable del tratamiento), a Términos (identificación del vendedor) y al JSON-LD.
- **2026-10-05** — Razón social ANSULAIS S.A.S. junto al NIT en footer, Privacidad, Términos y JSON-LD (`legalName`). La marca visible sigue siendo "Ansulais".
- **2026-10-05** — Dominio conectado: `ansulais.com` en vivo con HTTPS (DNS en Squarespace → GitHub Pages), `www` y el link viejo de github.io redirigen al dominio.
- **2026-10-05** — Dominio verificado en Google Search Console (propiedad tipo Domain, por registro TXT en Squarespace); sitemap enviado desde Search Console.
- **2026-10-05** — Marca de agua anti-copia: las 220 fotos del catálogo (completas y miniaturas) regeneradas desde los originales con la marca "A + ANSULAIS + ansulais.com" grabada en el centro. `tools/optimizar_fotos.py` la pone por defecto. En index, catálogo, los 3 catálogos y search se desactivó el menú "guardar imagen", arrastrar fotos y el guardado por presión larga en iPhone. (Los pantallazos no se pueden bloquear desde una web; por eso la marca va dentro de la imagen.)
- **2026-10-05** — La marca de agua grande (A + ANSULAIS + ansulais.com) se veía fea: se cambió por solo la "A" del logo, pequeña (16 % del ancho) y suave (13 % de opacidad), en el centro. Las 220 fotos regeneradas. Al usuario NO le gustan marcas grandes/visibles; ajustar solo con su visto bueno.
