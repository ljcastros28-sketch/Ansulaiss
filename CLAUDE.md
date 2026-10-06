# Ansulais — Contexto del proyecto

Sitio web estático de **Ansulais** (fabricante de muebles de madera y tapizados, Bogotá, Colombia). HTML/CSS/JS plano, **sin build ni frameworks**. Se despliega automático a GitHub Pages vía GitHub Actions al hacer push a `main`.

- Repo: https://github.com/ljcastros28-sketch/Ansulaiss.git
- Sitio en vivo: **https://ansulais.com** (conectado el 2026-10-05; el link viejo https://ljcastros28-sketch.github.io/Ansulaiss/ redirige solo)
- Dominio `ansulais.com`: comprado en Google Domains, hoy administrado en **Squarespace Domains** (solo registro + DNS). El sitio NO se aloja en Squarespace: sigue en GitHub Pages. El dominio se configura en GitHub → Settings → Pages → Custom domain (con deploy por Actions, un archivo `CNAME` se ignora, no hace falta). DNS en Squarespace: 4 registros A `@` → 185.199.108.153 / 109.153 / 110.153 / 111.153 y CNAME `www` → `ljcastros28-sketch.github.io`. **En ese DNS también hay registros de correo que no se deben tocar**: Google Workspace (MX `smtp.google.com`, TXT `v=spf1…`, TXT `google._domainkey`) y Brevo (CNAME `brevo1/2._domainkey`, `mail`, `img.mail`, `r.mail`; TXT `brevo-code`, `_dmarc`) y el TXT `@` `google-site-verification=…` que verifica el dominio en Google Search Console (si se borra, se pierde la verificación).
- Carpeta publicada: **`web/`** — todo lo que se ve en el sitio vive ahí.

## Regla de oro: qué se sube a git

**Solo se commitea/pushea lo que está dentro de `web/`** (más la documentación y herramientas del repo: `CLAUDE.md`, `README.md`, `tools/`, `.github/`). **`web/` contiene SOLO lo que usa la página**; todo lo demás vive en **`material/`** (organizado así el 2026-10-06, a pedido del usuario):

- `material/fotos-catalogo/` — `salas_fondoblanco/`, `comedores_fondoblanco/`, `alcobas_fondoblanco/`, `otros_fondoblanco/`, `SALAS Y SOFÁS/`, `COMEDORES/` (originales para catálogos)
- `material/fotos-secciones/` — `nosotros/`, `quequiereshoy/`, `hero/` (`imagen_hero*.png`, `sofa123*.jpe`)
- `material/marca/` — logos, `manual_identidad.pdf`, `nosotrosbola.svg`, `iconos/` de redes
- `material/videos/` — `video2.mp4`, `logo_video.mp4`
- `material/originales-web/` — los `.jpg` originales de las fotos publicadas, con la misma ruta que tienen en `web/` (ej. `material/originales-web/assets/catalogo/salas/sofa_basico/sofa_de_frente.jpg`)

Es **material de trabajo del usuario**: nunca lo toques, muevas, borres ni lo incluyas en un commit a menos que el usuario lo pida explícitamente. (Unos 109 archivos de ahí ya estaban en git desde antes y siguen versionados con su nueva ruta; no agregar más.) Cuando se necesita una foto de ahí para el sitio, se procesa con `python tools/optimizar_fotos.py material/... web/assets/...` (genera `.webp` + miniatura `-sm.webp`) y solo esa salida entra a git. Si algo de `web/` deja de usarse, se mueve a `material/`.

Workflow típico de cada cambio:
1. Editar archivo(s) dentro de `web/`.
2. Abrir con `start "" "web/archivo.html"` (o el que corresponda) para revisar antes de subir.
3. `git add web/<archivos tocados>` — nunca `git add -A` ni `git add .` (para no arrastrar material WIP del usuario sin querer).
4. Commit + `git push` (el usuario normalmente pide que se suba directo, no hace falta preguntar cada vez salvo que algo se vea raro).

## Páginas del sitio (todas dentro de `web/`)

| Archivo | Qué es |
|---|---|
| `index.html` | Home: hero (foto `sofa123.webp`/`sofa123_9-16.webp` de fondo), franja de datos animada (marquee de vidrio sobre el hero), "Descubre nuestra colección" (antes "¿Qué ofrecemos?"; carrusel `.quequieres` horizontal con flechas en desktop / swipe en móvil), Nosotros, materiales (madera + espuma Espumados), Contacto |
| `catalogo.html` | Selector de categorías ("¿Qué buscas el día de hoy?") → comedores, salas, alcobas y "otros" (→ `catalogo-otros.html`) |
| `catalogo-otros.html` | Selector "¿Qué otro mueble buscas?": 3 tarjetas con foto (muebles de TV, mesas de noche, mesas de centro) + 3 recuadros "próximamente" (bifés, cajoneros & perfumeros, poltronas) que abren WhatsApp con un mensaje listo. Cuando haya fotos de uno de esos 3, se le hace su catálogo y su recuadro pasa a tarjeta con foto |
| `catalogo-salas.html` | Catálogo de salas/sofás — 39 piezas, con filtros y lightbox |
| `catalogo-comedores.html` | Catálogo de comedores — 25 piezas, con filtros y lightbox |
| `catalogo-alcobas.html` | Catálogo de alcobas/camas — 25 piezas (códigos `ALC-xx`), filtros: Cabecero extendido / Clásicas / Nido y cajones, con lightbox. Faltan fotos de más piezas: se irán agregando |
| `catalogo-muebles-tv.html` | Muebles de TV — 7 piezas (códigos `TV-xx`), filtros: Flotantes / De piso |
| `catalogo-mesas-noche.html` | Mesas de noche — 17 piezas (códigos `MN-xx`), filtros: Flotantes / Con patas / Sobre base. Casi todas con 1 foto |
| `catalogo-mesas-centro.html` | Mesas de centro — 11 piezas (códigos `MC-xx`), filtros: Rectangulares / Redondas y ovaladas |
| `search.html` | Buscador "directo": en vez de listar opciones, lleva a la pieza (por nombre o código `SAL-05`), al catálogo con el filtro puesto ("sofá cama", "comedor redondo", "cama nido") o a la sección ("horario" → contacto, "garantía" → reembolsos). Solo lista resultados cuando de verdad hay varias piezas posibles ("botones", "comedor 6 puestos"). Palabras clave en el array `ROUTES` |
| `privacidad.html` | Política de tratamiento de datos (Ley 1581 de 2012, Colombia) |
| `cookies.html` | Política de cookies (el sitio NO usa analítica/tracking, solo Google Fonts + una preferencia local de "ya viste el aviso") |
| `terminos.html` | Términos y condiciones (venta sobre pedido, Ley 1480 de 2011) |
| `404.html` | Página de error de GitHub Pages. Sus enlaces empiezan con `/` porque se sirve en cualquier ruta |
| `reembolsos.html` | Garantía, cambios y devoluciones (explica por qué no aplica derecho de retracto estándar al ser piezas personalizadas, pero sí la garantía legal) |

Cada página es **standalone**: CSS y JS están inline en su propio `<style>`/`<script>`, **duplicados entre páginas a propósito** (no hay build ni archivos compartidos/includes). Si cambias algo que debe verse igual en todas (header, footer, cookie banner, nav-search, page-loader), **hay que replicar el cambio a mano en cada archivo HTML**.

Archivos de soporte en `web/`: `robots.txt`, `sitemap.xml` (agregar ahí cualquier página nueva, y poner la fecha del día en `<lastmod>` de las páginas que cambien, para que Google las vuelva a leer), `apple-touch-icon.png` (ícono para celulares), `favicon.ico` (16/32/48) + `favicon.svg` + `favicon-192.png` (ícono de pestaña y el que muestra Google en los resultados: **debe ser cuadrado**, por eso el SVG viejo de la "A" sola, de 340×440, no salía en Google), `assets/og-ansulais.jpg` (imagen 1200×630 de vista previa al compartir el link; es el único `.jpg` permitido, porque WhatsApp/Facebook no siempre leen WebP).

**Cada página nueva** debe llevar en el `<head>` el mismo bloque que las demás: `description`, `canonical` (`https://ansulais.com/<archivo>`), `theme-color`, `apple-touch-icon`, los 3 `<link rel="icon">` (favicon.ico, favicon.svg, favicon-192.png) y las etiquetas `og:*` / `twitter:card`. `index.html` además tiene los datos del negocio en JSON-LD (`FurnitureStore`): si cambia dirección, horario, teléfono o redes, actualizarlo ahí también.

## Datos de la empresa (usar siempre estos, no inventar)

- Dirección: Crr 51 # 76-32, Bogotá D.C.
- Correo: ansulais31@gmail.com
- Teléfono / WhatsApp: +57 300 492 8400
- Razón social: **ANSULAIS S.A.S.** — NIT: 900963049, **sin dígito de verificación** (así lo pidió el usuario) (aparece en el footer de las 10 páginas, en `privacidad.html`, `terminos.html` y en el JSON-LD de `index.html`)
- Dominio: ansulais.com (alojado en GitHub Pages, dominio registrado en Squarespace Domains; así está declarado en `privacidad.html` sección 5 y `cookies.html` sección 3)
- WhatsApp float / CTA: `https://wa.me/message/ISVNRLUQCE27G1`
- Número usado en el link del lightbox de catálogo: `WHATSAPP_NUMBER = "573004928400"` → `https://wa.me/573004928400?text=...`
- Horario: Lunes a sábado 11:00 a.m.–6:00 p.m., domingos 11:00 a.m.–3:00 p.m.
- Facebook: `https://www.facebook.com/share/19EzTXUeZg/?mibextid=wwXIfr`
- Instagram: `https://www.instagram.com/ansulais?igsi=dTBqdHJocHM2dnRr&utm_source=qr`
- TikTok: `https://www.tiktok.com/@ansulais?_r=1&_t=ZS-996OWQ08Us6`
- Madera principal: **flor morado**. Espuma: certificada por **Espumados** (sello CertiPUR-US; filial Espumados del Litoral con ISO 9001/14001/45001).
- Garantía: **1 año** contra defectos de fabricación, desde la entrega (no cubre desgaste normal ni mal uso). Está en `terminos.html` §6 y `reembolsos.html` §4.
- Transporte: gratis **dentro de Bogotá con compras desde $2.600.000 COP**; fuera de Bogotá o compras menores lo paga el cliente (se le da el contacto de nuestro transportador; a veces se le da una cortesía). La **instalación va incluida siempre que se use nuestro transportador**, lo pague quien lo pague. Está en `terminos.html` §5.
- Anticipo: **mínimo 30 %**, normalmente 50 %. Entrega: **20 días calendario** (más en piezas complejas, especiales o 100 % macizas). Bodegaje: el cliente tiene **5 días hábiles** desde la fecha acordada para recibir; después se cobra bodega. Materiales que trae el cliente (ej. tela) no tienen garantía. "Dentro de Bogotá" = solo Bogotá D.C. (Chía, Mosquera, Soacha… son fuera). No mencionar IVA ni factura electrónica en el sitio (el usuario lo va a revisar con un abogado). Todo esto en `terminos.html` §3–§6; cuidados del mueble en `reembolsos.html` §6.
- **Tono del sitio: humano, no "hecho por IA"** (lo pidió el usuario). Evitar etiquetas pequeñas en mayúsculas sobre los títulos ("NOSOTROS", "NUESTROS MODELOS": se quitaron), frases de agencia ("desde el concepto hasta el último detalle", "nuestro compromiso no termina…", "sin sacrificar…") y fórmulas con dos puntos. Escribir como hablaría alguien del almacén: frases cortas y concretas.
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

## Puntos de quiebre (responsive)

- **≤ 900 px**: diseño de celular (menú hamburguesa). En catálogos, **≤ 560 px** baja a 2 columnas.
- **601–900 px (tablet vertical / iPad parado)**: bloque `@media (min-width: 601px) and (max-width: 900px)` que va DESPUÉS del de celular y recupera columnas (home: Nosotros/madera/contacto lado a lado, stats en fila, footer 2 columnas; catálogo de categorías 2×2; catálogos y buscador 3 columnas).
- **901–1279 px (tablet horizontal / laptop pequeño)**: solo en `index.html`, hero más alto (16:11) y logo al 66 % para que no tape el sofá ni el botón choque con la franja.
- **≥ 1280 px**: diseño de computador original.
- Para revisar se usan capturas con Edge headless a 820×1180, 1024×768 y 1180×820 (tamaños de iPad), además de 390 (celular) y 1920 (computador).

## Catálogo: dónde vive la data

Los productos (nombre inventado + descripción + tag + carpeta de fotos) están **hardcodeados como arrays JS**, duplicados en:
- `catalogo-salas.html` (39 piezas, con `desc` completo para el lightbox)
- `catalogo-comedores.html` (25 piezas, con `desc` completo para el lightbox)
- `catalogo-alcobas.html` (25 piezas, con `desc` completo para el lightbox)
- `catalogo-muebles-tv.html` (7), `catalogo-mesas-noche.html` (17) y `catalogo-mesas-centro.html` (11), generados copiando `catalogo-alcobas.html`
- `index.html` → array `offerPool` (las mismas 124 piezas combinadas, solo nombre/href/img, para el carrusel "Descubre nuestra colección")
- `search.html` → array `catalog` (las mismas 124, con `cat`, `filtro` = `tag` del catálogo y `desc` copiada del catálogo, porque el buscador también busca en la descripción)

**Si se agrega o quita una pieza del catálogo, hay que actualizar los 3 lugares donde está duplicada la lista** (no hay una sola fuente de verdad, es intencional por ser sitio estático sin build).

Fotos de catálogo en: `web/assets/catalogo/{salas,comedores,alcobas,otros/muebles-tv,otros/mesas-noche,otros/mesas-centro}/<carpeta>/<foto>.webp` (1024 px, lightbox) y `<foto>-sm.webp` (600 px, tarjetas/carrusel/buscador). Se generan con `tools/optimizar_fotos.py`. **Las fotos NO llevan marca de agua grabada** (el usuario notó pérdida de calidad y lo pidió así): la "A" del logo se pone ENCIMA con CSS (`::after` en `.product-card-media`, `.lightbox-media`, `.quequieres-item`, `.search-card-media`), sin tocar los archivos. Los `.jpg` originales de cada foto están en `material/originales-web/` (misma ruta que en `web/`): no borrarlos. **Nunca referenciar `.jpg` en el código** (salvo `og-ansulais.jpg`). En `index.html` (`offerPool`) y `search.html` (`catalog`) se usa siempre la versión `-sm.webp`. Las piezas nuevas van **al final** del array `products`, porque el código de artículo sale de la posición.

## Cosas ya implementadas (no reinventar)

- Page loader (logo + 3 puntos) en todas las páginas — se oculta solo al cargar o a los 4s.
- Banner de cookies (aceptar/rechazar) con `localStorage` key `ansulais_cookie_choice`, en todas las páginas.
- Nav-search: en móvil el input estaba `display:none` — se arregló para que se expanda al tocar el ícono (clase `.is-open` en `#navSearchForm`).
- Skip-link de accesibilidad ("Saltar al contenido") en todas las páginas.
- Footer con links legales (Términos, Privacidad, Cookies, Cambios y devoluciones) en todas las páginas.
- Enlaces directos en los 6 catálogos: `?filtro=<data-filter>` activa el filtro y `?pieza=<código o nombre-en-slug>` abre la pieza en el lightbox (ej. `catalogo-salas.html?pieza=SAL-05` o `?pieza=sofa-cedro`). Los usa el buscador y sirven para compartir una pieza por WhatsApp.

## Lecciones aprendidas (para no repetir bugs ya resueltos)

1. **Orden del CSS en cascada**: si una regla de media query (`@media (min-width:901px) { .algo {...} }`) está definida ANTES que una regla base sin condición para el mismo selector `.algo`, la regla base gana en el breakpoint grande también (ambas aplican; gana la que está más abajo en el archivo). **Los overrides de breakpoint deben ir SIEMPRE después de la regla base del mismo componente** en el `<style>`.
2. **`overflow-x: auto` sin `overflow-y` explícito**: el navegador computa `overflow-y` como `auto` también, lo que puede atrapar el scroll vertical/táctil dentro de un carrusel horizontal. Usar `overflow-y: hidden` para scroll horizontal puro, con `touch-action: pan-x pan-y` (NO solo `pan-x`: en celular impide bajar la página si el dedo empieza sobre el carrusel) y **nunca** `overscroll-behavior-y: contain` (atrapa la rueda del mouse y la página no baja con el cursor encima). Para que el gesto lateral no cambie de página, usar `overscroll-behavior-x: contain`.
3. **`aspect-ratio` + `max-height` en el mismo elemento**: compiten entre sí y fuerzan recortes raros con `object-fit: cover`. Usar solo uno de los dos.
4. **`box-shadow` cortado por `overflow: hidden`** del contenedor que oculta el scroll horizontal de un carrusel: si no hay suficiente padding vertical, se corta la sombra de las tarjetas. Más robusto: quitar el `overflow:hidden` de ese contenedor puntual y dejar que lo maneje un ancestro más grande (ej. `.hero` completo) que no necesita recortar verticalmente.
5. **Nunca usar el atajo `padding: 0 Xpx` en `.wrap` dentro de un media query**: `.wrap` comparte elemento con otras clases (`wrap legal-hero`, `wrap footer-bottom`, `wrap hero-inner`…) y el atajo borra su padding vertical (así quedaban títulos pegados al menú). Usar `padding-left` / `padding-right`.
6. Antes de dar por "arreglado" un cambio visual reportado por el usuario, recordar que puede ser **caché del navegador/GitHub Pages** mostrando la versión anterior — pedir refresh forzado si el código ya se ve correcto en el archivo.
7. **Al agregar piezas en `offerPool` (index) y `catalog` (search), la última sala y el último comedor NO son el final del array** (después vienen comedores y alcobas). Si se inserta después de esa línea hay que cuidar las comas: la línea anterior ya termina en `},` y la última pieza nueva necesita su propia `,`. Después de cada cambio, abrir `search.html` e `index.html` y revisar la consola (un `Unexpected token '{'` deja el buscador vacío).

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
- **2026-10-05** — Revertida la marca grabada: las 440 imágenes del catálogo vuelven a ser idénticas (byte a byte) a las de antes, y `tools/optimizar_fotos.py` volvió a su versión sin marca. La "A" del logo ahora es una capa CSS encima de las fotos (fichas, lightbox, carrusel del home, buscador), 16 % del ancho, muy suave. Se mantiene el bloqueo de "guardar imagen"/arrastrar.
- **2026-10-05** — Responsive para iPad: nuevo punto de quiebre de tablet vertical (601–900 px) en home, catálogo, los 3 catálogos y buscador, y de tablet horizontal (901–1279 px) en el hero del home. Corregido en las 10 páginas el `.wrap { padding: 0 24px }` de celular que borraba el espacio superior de los títulos legales y del pie de página.
- **2026-10-05** — 8 alcobas nuevas (ALC-14 a ALC-21: Cama Nido Trigo, Alcoba Arcilla, Nácar, Prisma, Marco, Marfil, Canela, Junco) desde `alcobas_fondoblanco/`, agregadas a los 3 lugares (catálogo, `offerPool`, `catalog` de search). La carpeta `espaldargeométrico` se publicó sin tilde (`espaldargeometrico`). Las tarjetas dicen "1 foto" en singular y el lightbox oculta las flechas si la pieza tiene una sola foto.
- **2026-10-06** — NIT sin dígito de verificación (900963049) en las 10 páginas y el JSON-LD. Garantía de 1 año en Términos y Cambios y devoluciones; nueva sección de transporte e instalación en Términos. Páginas legales en celular: el menú (Inicio/Catálogo/Contacto) ya no se oculta, texto y títulos más cómodos, tabla de Cookies como tarjeta y los links del pie de página, que salían negros sobre negro, ahora se ven (también en computador).
- **2026-10-06** — Términos: anticipo mínimo 30 %, entrega en 20 días calendario, bodegaje tras 5 días hábiles, Bogotá = solo Bogotá D.C. Cambios y devoluciones: sin garantía sobre materiales del cliente, nueva sección 6 de cuidados del mueble (secciones siguientes renumeradas a 7–9).
- **2026-10-06** — Home: el carrusel "¿Qué ofrecemos?" pasa a "Nuestros modelos / Descubre nuestra colección" con una frase debajo, y "Nosotros" pasa a etiqueta pequeña con el título "Tradición familiar, hecha a mano" (el ancla `#nosotros` y los links del menú siguen igual). Nueva clase `.section-eyebrow` para esas etiquetas.
- **2026-10-06** — Arreglado el carrusel del home: con el mouse o el dedo encima de las fotos la página no bajaba (`overscroll-behavior-y: contain` + `touch-action: pan-x`). Ahora baja normal y el carrusel sigue moviéndose de lado con flechas, trackpad o deslizando.
- **2026-10-06** — Home, sección Nosotros: la tarjeta blanca con la línea divisoria se reemplazó por una cuadrícula "bento" (`.nosotros-bento`, 4×3 en escritorio, 2 columnas en ≤900 px) con fotos (`nosotros_silla.webp` —referencia de internet de una silla que el usuario ya fabricó—, `nosotros_almacen.webp` desde `nosotros/almacen1.jpeg`, y `nosotros_lijado.webp`), texto de empresa familiar y las cifras +30 / +1000 / 100 %. Se quitaron las etiquetas "NOSOTROS" y "NUESTROS MODELOS". Textos del home reescritos en tono más natural; la franja y el video ya no prometen instalación siempre ("Instalación en tu casa" / "cuando el mueble va con nuestro transporte, la instalación está incluida"), acorde con Términos §5.
- **2026-10-06** — Limpieza y orden: la raíz del repo queda solo con `web/` (lo que usa la página), `material/` (todo lo demás: 512 archivos, ~1 GB, incluidos los 229 `.jpg` originales que estaban dentro de `web/assets/`), `tools/` y la documentación. Código: quitada la variable `--navy` sin uso de las 10 páginas, estilos muertos (`.menu-toggle` en privacidad, `a.is-featured` en search, `.reveal-delay-3` en index) y la cursiva de Montserrat que se pedía a Google Fonts sin usarse. `quercus-petraeaarbol.webp` de 194 a 123 KB (880 px, que es el doble de lo que se muestra).
- **2026-10-06** — 4 alcobas nuevas desde `material/fotos-catalogo/alcobas_fondoblanco/`: ALC-22 Alcoba Abedul (`camacajones_lineaspintadas`), ALC-23 Cama Cuna Nogal (`camacuna`, cat "Cama cuna" en search), ALC-24 Alcoba Coral (`camacurvasesquinas_cajones`), ALC-25 Alcoba Serena (`clasicaclasica`), en los 3 lugares. Alcoba Prisma (ALC-17) pasa de 1 a 3 fotos y su foto principal se cambió por la nueva del usuario (fondo beige). Buscador: en texto libre una palabra exacta o de la misma raíz vale 1 y un error de tipeo 0.8, para que "cuna" no empate con "Duna"/"Luna" (se comprobó que otras 29 búsquedas dan lo mismo que antes).
- **2026-10-06** — Resultados de Google: los títulos de las 11 páginas pasan de "X — Ansulais" a "X | Ansulais" (la raya larga se veía "de IA"); quitadas también las rayas largas del texto de Privacidad y Cambios y devoluciones. Ícono nuevo cuadrado (fondo beige + "A" oscura, igual que apple-touch-icon) en `favicon.ico`, `favicon.svg` y `favicon-192.png`; el SVG viejo pasó a `material/marca/logosimplificado_favicon-viejo.svg`. **No usar "—" en textos nuevos del sitio.** El usuario activó "Enforce HTTPS" en GitHub → Settings → Pages: `http://` y `www` redirigen (301) a `https://ansulais.com/`.
- **2026-10-06** — Título del home (y `og:title`) cambiado a "Ansulais | Muebles de madera y tapizados en Bogotá" para que Google lo relacione con búsquedas de muebles en Bogotá. "Comodidad para tu hogar" sigue como lema en el hero.
- **2026-10-06** — `sitemap.xml`: `lastmod` de las 9 páginas actualizado a 2026-10-06 (cambiaron títulos, textos y catálogo).
- **2026-10-06** — 4 sofás nuevos (SAL-36 Sofá Ceiba `sofaestructuramadera1`, SAL-37 Sofá Raíz `sofamadera2`, SAL-38 Sofá Arrayán `sofamadera3_brazoscurvos`, SAL-39 Sofá Samán `sofamaderacurvo`, todos filtro Sofás) y 1 comedor (COM-25 Comedor Pilar `comedoresquinascurvas`, filtro Clásicos; la foto `comedor 1` se publicó como `comedor1` sin espacio), en los 3 lugares. Total: 89 piezas.
- **2026-10-06** — Sección "Otros": nueva `catalogo-otros.html` (selector) y 3 catálogos nuevos desde `material/fotos-catalogo/otros_fondoblanco/`: `catalogo-muebles-tv.html` (7, TV-01..07), `catalogo-mesas-noche.html` (17, MN-01..17) y `catalogo-mesas-centro.html` (11, MC-01..11; la carpeta `mesasdecentro/mesaduotono` estaba vacía y no se publicó). Bifés, cajoneros & perfumeros y poltronas quedan "próximamente" con enlace a WhatsApp. En `catalogo.html` la tarjeta "otros" ya enlaza. Portadas `assets/qh_muebles_tv.webp` y `assets/qh_mesas_centro.webp` (mesas de noche reutiliza `qh_otros.webp`). Buscador: códigos TV/MN/MC (con guion o pegados al número, para que "mueble tv 2 metros" no se tome como TV-02), filtro "Otros" en resultados (`OTROS_PAGES`), rutas nuevas para mueble de TV / mesa de noche / mesa de centro / bifé-cajonero-perfumero-poltrona-aparador (→ `catalogo-otros.html`); "mesa de noche" y "nochero" dejaron de llevar a alcobas y "poltrona" a salas. 35 piezas agregadas también a `offerPool` (124 en total). 4 páginas nuevas en `sitemap.xml`.
