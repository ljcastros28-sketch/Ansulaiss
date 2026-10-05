# Ansulais — Contexto del proyecto

Sitio web estático de **Ansulais** (fabricante de muebles de madera y tapizados, Bogotá, Colombia). HTML/CSS/JS plano, **sin build ni frameworks**. Se despliega automático a GitHub Pages vía GitHub Actions al hacer push a `main`.

- Repo: https://github.com/ljcastros28-sketch/Ansulaiss.git
- Sitio en vivo: https://ljcastros28-sketch.github.io/Ansulaiss/
- Carpeta publicada: **`web/`** — todo lo que se ve en el sitio vive ahí.

## Regla de oro: qué se sube a git

**Solo se commitea/pushea lo que está dentro de `web/`.** El resto de carpetas y archivos en la raíz del repo (`SALAS Y SOFÁS/`, `COMEDORES/`, `salas_fondoblanco/`, `comedores_fondoblanco/`, `alcobas_fondoblanco/`, `otros_fondoblanco/`, `quequiereshoy/`, `nosotros/`, fotos/videos sueltos en la raíz como `sofa123.jpe`, `imagen_hero*.png`, etc.) son **material de trabajo en progreso del usuario** — fotos originales sin procesar para catálogos futuros u otras secciones. **Nunca los toques, muevas, borres ni los incluyas en un commit** a menos que el usuario lo pida explícitamente. Cuando se necesita una foto de ahí para el sitio, se copia/procesa hacia `web/assets/` y solo esa copia entra a git.

Workflow típico de cada cambio:
1. Editar archivo(s) dentro de `web/`.
2. Abrir con `start "" "web/archivo.html"` (o el que corresponda) para revisar antes de subir.
3. `git add web/<archivos tocados>` — nunca `git add -A` ni `git add .` (para no arrastrar material WIP del usuario sin querer).
4. Commit + `git push` (el usuario normalmente pide que se suba directo, no hace falta preguntar cada vez salvo que algo se vea raro).

## Páginas del sitio (todas dentro de `web/`)

| Archivo | Qué es |
|---|---|
| `index.html` | Home: hero (foto `sofa123.jpg`/`sofa123_9-16.jpg` de fondo), franja de datos animada (marquee de vidrio sobre el hero), "¿Qué ofrecemos?" (carrusel horizontal con flechas en desktop / swipe en móvil), Nosotros, materiales (madera + espuma Espumados), Contacto |
| `catalogo.html` | Selector de categorías ("¿Qué buscas el día de hoy?") → enlaza a los dos catálogos reales; alcobas/otros siguen "próximamente" |
| `catalogo-salas.html` | Catálogo de salas/sofás — 35 piezas, con filtros y lightbox |
| `catalogo-comedores.html` | Catálogo de comedores — 24 piezas, con filtros y lightbox |
| `search.html` | Buscador funcional sobre las 59 piezas combinadas (salas + comedores), con filtros por categoría |
| `privacidad.html` | Política de tratamiento de datos (Ley 1581 de 2012, Colombia) |
| `cookies.html` | Política de cookies (el sitio NO usa analítica/tracking, solo Google Fonts + una preferencia local de "ya viste el aviso") |
| `terminos.html` | Términos y condiciones (venta sobre pedido, Ley 1480 de 2011) |
| `reembolsos.html` | Garantía, cambios y devoluciones (explica por qué no aplica derecho de retracto estándar al ser piezas personalizadas, pero sí la garantía legal) |

Cada página es **standalone**: CSS y JS están inline en su propio `<style>`/`<script>`, **duplicados entre páginas a propósito** (no hay build ni archivos compartidos/includes). Si cambias algo que debe verse igual en todas (header, footer, cookie banner, nav-search, page-loader), **hay que replicar el cambio a mano en cada archivo HTML**.

## Datos de la empresa (usar siempre estos, no inventar)

- Dirección: Crr 51 # 76-32, Bogotá D.C.
- Correo: ansulais31@gmail.com
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
- `index.html` → array `offerPool` (las mismas 59 piezas combinadas, solo nombre/href/img, para el carrusel "¿Qué ofrecemos?")
- `search.html` → array `catalog` (las mismas 59, con `cat` para los filtros)

**Si se agrega o quita una pieza del catálogo, hay que actualizar los 3-4 lugares donde está duplicada la lista** (no hay una sola fuente de verdad, es intencional por ser sitio estático sin build).

Fotos de catálogo en: `web/assets/catalogo/salas/<carpeta>/<foto>.jpg` y `web/assets/catalogo/comedores/<carpeta>/<foto>.jpg`.

## Cosas ya implementadas (no reinventar)

- Page loader (logo + 3 puntos) en las 9 páginas — se oculta solo al cargar o a los 4s.
- Banner de cookies (aceptar/rechazar) con `localStorage` key `ansulais_cookie_choice`, en las 9 páginas.
- Nav-search: en móvil el input estaba `display:none` — se arregló para que se expanda al tocar el ícono (clase `.is-open` en `#navSearchForm`).
- Skip-link de accesibilidad ("Saltar al contenido") en las 9 páginas.
- Footer con links legales (Términos, Privacidad, Cookies, Cambios y devoluciones) en las 9 páginas.

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
