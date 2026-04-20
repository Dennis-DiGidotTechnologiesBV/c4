## Release notes for DiGidot Controller Software v3.3.1 - Published on 20 of April 2026 ##

## Added
- **LED IC (Experimental):** Added support for UCS7604 with native 16-bit control from the input.

## Changed
- **FTP:** Improved documentation and guidance for using the FTP service.

## Improved
- **Faders:** The brightness slider on the *Scenes* page has been completely rewritten, resulting in significantly improved responsiveness, especially on desktop systems.

## Fixed

### High
- **Backup & Restore:** The *Export Backup* button was not visible on certain systems, preventing users from creating backups. This has been resolved. The option is now always available, with a warning for platforms that do not support filesystem access.

### Medium
- **Backup & Restore:** Device settings (including UDP, OSC, and HTTP) are now correctly restored.
- **Recording:** Cross-fade actions now function correctly after trimming a scene.
- **Generate:** Changes to color input fields are now correctly applied when using 5-channel LED ICs.

### Low
- **IOconfig:** The 16-bit toggle in advanced settings is now saved correctly.
- **IOconfig:** Automatic IP addressing has been fixed for grouped devices containing only a single internal device (e.g., DiGidot PowerNode 12X).
- **IOconfig:** The *Save* button on the Global Configuration page is no longer incorrectly disabled.