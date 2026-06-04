# Changelog

## 2026.06.04

### What Changed
Revived the dormant arc-theme build and added a parametric **accent color** and
**theme name** to the build system, so recolored/renamed Arc variants (e.g.
Arc-Dali, Arc-Dawn, Arc-Tory) can be produced without sed-hacking the source.

### Technical Details
- Added two meson options: `accent` (default `#5294e2`) and `theme_name`
  (default `Arc`). Defaults reproduce the stock build exactly.
- `accent` flows into gtk3/gtk4 via `gtk.scss.in` (`$accent: @accent@;`) →
  `_colors.scss` (`$selected_bg_color`/`$suggested_color` now reference `$accent`,
  with a `$accent: #5294e2 !default;` guard). Rendered SVG assets are recolored at
  build time by a new helper `meson/recolor-svg.py` invoked from each
  `assets/meson.build` as a `custom_target` (replaces the `#5294e2` gradient stop).
- `theme_name` parametrizes `variant_name` in the top `meson.build`; the existing
  `index.theme.in` `@variant_name@` template then renames dirs and `index.theme`
  fields automatically.
- Build gotcha documented: Inkscape 1.x collides over D-Bus under parallel ninja;
  build with `dbus-run-session -- ninja -j1`.

### Files Modified
- meson_options.txt
- meson.build
- meson/recolor-svg.py (new)
- common/gtk-3.0/sass/gtk.scss.in, common/gtk-4.0/sass/gtk.scss.in
- common/gtk-3.0/sass/_colors.scss, common/gtk-4.0/sass/_colors.scss
- common/gtk-3.0/meson.build, common/gtk-4.0/meson.build
- common/gtk-3.0/assets/meson.build, common/gtk-4.0/assets/meson.build
- INSTALL.md, CHANGELOG.md (new)
