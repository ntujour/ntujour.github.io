# Generated Website Output

This directory is generated output. Do not edit any file here directly, including HTML, CSS, JavaScript, JSON, images, or this instruction file.

For website changes:

1. Read `/Users/jirlong/Library/CloudStorage/Dropbox/Programming/ntujour/COWORK_WEBSITE_WORKFLOW.md`.
2. Modify the corresponding source under `local_generator_app/`.
3. Build and inspect `local_generator_app/preview_output/` first.
4. Generate `public_html/` only after preview verification.
5. Publish through the Local CMS FTP deployment flow.

The FTP publisher verifies `.generated-output-manifest.json`. If anything in `public_html` changes after generation, publishing stops and reports the source location that should be edited.
